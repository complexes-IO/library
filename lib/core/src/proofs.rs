//! Kani proofs: each property for every input within the stated bounds (`cargo kani`, Linux or WSL2). The same properties run as
//! dense samples under `cargo test` (joint.rs, safety.rs tests), so a failure shows up on any machine first.
//!
//! Bounds: positions within ±50 mm, gaps 0 to 20 mm, nut turns 0 to 30, key errors within ±45°, torque 0 to 2 N m, every
//! condition each pole can take. Loops are over at most 5 poles and 20 condition variants (unwind 24).
use crate::joint::*;
use crate::generated::*;
use crate::safety;

fn any_cond(kind: Kind) -> Cond {
    let i: u8 = kani::any();
    match kind {
        Kind::Pin => { kani::assume(i < 5); [Cond::Ok, Cond::Bent, Cond::PushedBack, Cond::Broken, Cond::Corroded][i as usize] }
        Kind::Socket => { kani::assume(i < 4); [Cond::Ok, Cond::Spread, Cond::Corroded, Cond::Missing][i as usize] }
    }
}

fn any_conds(h: &HalfDef) -> [Cond; MAX_POLES] {
    let mut c = ALL_OK;
    let mut i = 0;
    while i < h.contacts.len() { let k = h.contacts[i]; c[(k.pole - 1) as usize] = any_cond(k.kind); i += 1; }
    c
}

fn any_joint() -> (&'static HalfDef, &'static HalfDef) {
    let j: usize = kani::any(); kani::assume(j < JOINTS.len()); JOINTS[j]
}

fn any_contact(kind: Kind) -> ContactDef {
    let c = ContactDef { pole: 1, kind, cond: any_cond(kind), origin: [kani::any(), kani::any(), kani::any()], dir: if kani::any() { 1 } else { -1 },
                         parallel: kani::any(), range: (kani::any(), kani::any()), wipe: kani::any(), face: kani::any(), r_mohm: 5 };
    for v in c.origin { kani::assume(v > -50_000 && v < 50_000); }
    // what the validation suite checks every element for: a zone that runs forward, a positive wipe, a face in front of the mouth
    kani::assume(c.range.0 >= 0 && c.range.0 < c.range.1 && c.range.1 <= 20_000);
    kani::assume(c.wipe > 0 && c.wipe <= 2_000 && c.face >= 0 && c.face <= 2_000);
    kani::assume(c.cond != Cond::Bent || !c.parallel);               // a bent pin's axis leans 12°: never parallel
    c
}

/// a pin and a socket anywhere: the state always agrees with the overlap and the offset that produced it
#[kani::proof]
#[kani::unwind(5)]
fn pair_states_agree_with_the_geometry() {
    let pin = any_contact(Kind::Pin); let sock = any_contact(Kind::Socket);
    let t = [pin.origin[0] as i64, pin.origin[1] as i64, pin.origin[2] as i64];
    let m = [sock.origin[0] as i64, sock.origin[1] as i64, sock.origin[2] as i64];
    let r = pair(&pin, t, pin.dir, &sock, m, sock.dir);
    let lat2 = (t[0] - m[0]) * (t[0] - m[0]) + (t[2] - m[2]) * (t[2] - m[2]);
    if r.state.conducts() {
        assert!(r.overlap >= core::cmp::max(pin.wipe, sock.wipe));
        assert!(lat2 <= LATERAL * LATERAL && pin.parallel && sock.parallel);
        assert!(pin.cond != Cond::Broken && sock.cond != Cond::Missing && sock.cond != Cond::Spread);
    }
    if r.state == State::Made { assert!(pin.cond != Cond::Corroded && sock.cond != Cond::Corroded); }
    if r.state == State::Marginal { assert!(r.overlap > 0); }
    if pin.cond == Cond::Bent || !pin.parallel { assert!(!r.state.touching()); }
}

/// at the seat with the nut home and torqued, every pole is made, for any key error the keyway allows
#[kani::proof]
#[kani::unwind(24)]
fn seated_nut_makes_every_pole() {
    let (a, b) = any_joint(); let (catch, _) = threads(a, b);
    let extra: i32 = kani::any(); kani::assume(extra >= 0 && extra <= 30_000);
    let key: i32 = kani::any(); kani::assume(key.unsigned_abs() <= a.key_tol_mdeg.unsigned_abs());
    let tq: i32 = kani::any(); kani::assume(tq >= a.torque_mnm.0 && tq <= a.torque_mnm.1);
    let r = mate(a, &ALL_OK, b, &ALL_OK, Approach::Turns(catch + extra), key, Some(tq));
    assert!(r.seated && r.sealed && !r.over_torque);
    for p in r.poles.iter().flatten() { assert!(p.state == State::Made); }
}

/// a wrong coding, a key past the keyway or two halves of one gender never make a pole, whatever else is done
#[kani::proof]
#[kani::unwind(24)]
fn a_plug_that_does_not_fit_never_makes() {
    let i: usize = kani::any(); let j: usize = kani::any(); kani::assume(i < HALVES.len() && j < HALVES.len());
    let (a, b) = (HALVES[i], HALVES[j]);
    let key: i32 = kani::any(); kani::assume(key.unsigned_abs() <= 45_000);
    kani::assume(a.coding != b.coding || a.gender == b.gender || key.unsigned_abs() > a.key_tol_mdeg.unsigned_abs());
    let g: i32 = kani::any(); kani::assume(g >= 0 && g <= 20_000);
    let r = mate(a, &any_conds(a), b, &any_conds(b), Approach::Gap(g), key, None);
    assert!(!r.seated);
    for p in r.poles.iter().flatten() { assert!(!p.state.touching()); }
}

/// a bent pin on the plug never makes and never lets the plug seat
#[kani::proof]
#[kani::unwind(24)]
fn a_bent_pin_never_makes_or_seats() {
    let (a, b) = any_joint();
    let k: usize = kani::any(); kani::assume(k < b.contacts.len() && b.contacts[k].kind == Kind::Pin);
    let pole = b.contacts[k].pole; let mut c = ALL_OK; c[(pole - 1) as usize] = Cond::Bent;
    let t: i32 = kani::any(); kani::assume(t >= 0 && t <= 30_000);
    let r = mate(a, &ALL_OK, b, &c, Approach::Turns(t), 0, None);
    assert!(!r.seated);
    assert!(!r.poles[(pole - 1) as usize].unwrap().state.touching());
}

/// L-coded FE makes before every power pin and breaks after it: at no gap does a power pin conduct without FE
#[kani::proof]
#[kani::unwind(24)]
fn fe_makes_first_breaks_last() {
    let (a, b) = any_joint(); kani::assume(a.coding == Coding::L);
    let g: i32 = kani::any(); kani::assume(g >= 0 && g <= 20_000);
    let r = mate(a, &ALL_OK, b, &ALL_OK, Approach::Gap(g), 0, None);
    let power = r.poles[0].unwrap().state.conducts() || r.poles[1].unwrap().state.conducts()
        || r.poles[2].unwrap().state.conducts() || r.poles[3].unwrap().state.conducts();
    if power { assert!(r.poles[4].unwrap().state.conducts()); }
}

/// a pushed-back A-coded pin, any of the five: made up to 4.45 mm back, marginal to 4.95, open beyond, at the seat (from the element data:
/// 6.9 protrusion, 0.45 tip, socket mouth 1.0 below the face, springs from 0.5, 0.5 wipe). Changing that data fails this proof
/// on purpose, so the new window gets looked at.
#[kani::proof]
#[kani::unwind(24)]
fn pushed_back_pin_window() {
    let (a, b) = (&DEV_F_A, &CORD_M_A);
    let pole: usize = kani::any(); kani::assume(pole < 5);
    let recess: i32 = kani::any(); kani::assume(recess >= 0 && recess <= 6_900);
    let mut q = b.with(&ALL_OK); let mut c = q[pole].unwrap(); c.origin[1] += recess; q[pole] = Some(c);
    let r = mate_contacts(a, &a.with(&ALL_OK), b, &q, Approach::Gap(0), 0, None);
    let s = r.poles[pole].unwrap().state;
    assert!((s == State::Made) == (recess <= 4_450));
    assert!((s == State::Marginal) == (recess > 4_450 && recess < 4_950));
    assert!((s == State::Open) == (recess >= 4_950));
}

/// sealed exactly when seated at or above the minimum torque; over the maximum is flagged
#[kani::proof]
#[kani::unwind(24)]
fn sealed_only_seated_and_torqued() {
    let (a, b) = any_joint();
    let t: i32 = kani::any(); kani::assume(t >= 0 && t <= 30_000);
    let tq: i32 = kani::any(); kani::assume(tq >= 0 && tq <= 2_000);
    let r = mate(a, &ALL_OK, b, &ALL_OK, Approach::Turns(t), 0, Some(tq));
    assert!(r.sealed == (r.seated && tq >= a.torque_mnm.0));
    assert!(r.over_torque == (tq > a.torque_mnm.1));
}

/// nothing in mate() can panic or overflow, for any joint, any conditions on both halves, any approach, key error and torque
#[kani::proof]
#[kani::unwind(24)]
fn mate_never_panics() {
    let (a, b) = any_joint();
    let g: i32 = kani::any(); kani::assume(g >= -1_000 && g <= 50_000);
    let key: i32 = kani::any(); kani::assume(key.unsigned_abs() <= 180_000);
    let tq: i32 = kani::any(); kani::assume(tq >= 0 && tq <= 10_000);
    let approach = if kani::any() { Approach::Gap(g) } else { Approach::Turns(g) };
    let _ = mate(a, &any_conds(a), b, &any_conds(b), approach, key, if kani::any() { Some(tq) } else { None });
}

/// the safety channel, from any state and any inputs (stop category 0, manual reset, monitored reset)
#[kani::proof]
fn safety_channel() {
    let s = safety::SafetyState { latched: kani::any(), reset_prev: kani::any() };
    let i = safety::SafetyIn { ch_a: kani::any(), ch_b: kani::any(), reset: kani::any(), k1_aux_nc: kani::any(), plc_run: kani::any() };
    let (s2, o) = safety::step(s, i);
    if !(i.ch_a && i.ch_b) { assert!(!o.relay_out && !o.k1_coil && !s2.latched); }
    if !s.latched && !(i.reset && !s.reset_prev) { assert!(!s2.latched && !o.k1_coil); }
    if !s.latched && !i.k1_aux_nc { assert!(!s2.latched); }
    if o.k1_coil { assert!(i.plc_run && i.ch_a && i.ch_b); }
}
