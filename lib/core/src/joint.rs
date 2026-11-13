//! An M12 joint from its two halves: a port of lib/toolkit/contact.py `mate()` and `pair()` into whole micrometres.
//!
//! Every half is built in its mating frame (lib/toolkit/m12.py): mating plane y = 0, the counterpart toward -y, the key toward +z.
//! The plug turns 180° about z to face the port and stands `gap` off the seat, so a plug point (x, y, z) lands on the port at
//! (-x, -y - gap, z), turned by the key error about the axis. A contact's `origin` is a pin's tip or a socket's mouth; `dir` (+1 or
//! -1, along y) is the way it travels to engage; `range` is its contact zone measured from the origin into the part.
use crate::units::*;

#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum Gender { Male, Female }
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum Coding { A, D, L }
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum Kind { Pin, Socket }
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum Cond { Ok, Bent, PushedBack, Broken, Corroded, Spread, Missing }
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum State { Open, Marginal, Made, HighR, Blocked }

impl State {
    /// carries current (made, or made with a high resistance)
    pub fn conducts(self) -> bool { matches!(self, State::Made | State::HighR) }
    /// touching at all: what a technician sees as intermittent
    pub fn touching(self) -> bool { matches!(self, State::Made | State::HighR | State::Marginal) }
}

#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub struct ContactDef {
    pub pole: u8,
    pub kind: Kind,
    pub cond: Cond,
    pub origin: [Um; 3],
    pub dir: i8,
    pub parallel: bool,
    pub range: (Um, Um),
    pub wipe: Um,
    pub face: Um,
    pub r_mohm: MilliOhm,
}

pub struct HalfDef {
    pub name: &'static str,
    pub gender: Gender,
    pub coding: Coding,
    pub key_gap: Um,
    pub key_tol_mdeg: MilliDeg,
    pub thread_span: (Um, Um),
    pub pitch: Um,
    pub torque_mnm: (MilliNm, MilliNm),
    pub contacts: &'static [ContactDef],
    pub variants: &'static [ContactDef],
}

pub const MAX_POLES: usize = 5;
/// a pin further than this off its socket's axis does not enter it (toolkit/contact.py LATERAL: 0.15 mm)
pub const LATERAL: i64 = 150;
/// within this of the seat the joint is seated (0.05 mm)
pub const SEAT: Um = 50;

impl HalfDef {
    /// the contact at a pole in a condition: the half as built for Ok, else the variant the element builds for that condition
    pub fn contact(&self, pole: u8, cond: Cond) -> Option<ContactDef> {
        let list = if cond == Cond::Ok { self.contacts } else { self.variants };
        let mut i = 0;
        while i < list.len() {
            if list[i].pole == pole && list[i].cond == cond { return Some(list[i]); }
            i += 1;
        }
        None
    }
    /// the half's contacts with a condition per pole (index pole - 1); a condition the pole cannot take leaves it as built
    pub fn with(&self, conds: &[Cond; MAX_POLES]) -> [Option<ContactDef>; MAX_POLES] {
        let mut out = [None; MAX_POLES];
        let mut p = 1u8;
        while (p as usize) <= MAX_POLES {
            let c = conds[(p - 1) as usize];
            out[(p - 1) as usize] = self.contact(p, c).or_else(|| self.contact(p, Cond::Ok));
            p += 1;
        }
        out
    }
}

#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub struct Pair { pub state: State, pub overlap: Um, pub depth: Um, pub stop: Um }

/// how the plug comes onto the port
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum Approach {
    /// held this far off the seat (µm)
    Gap(Um),
    /// pushed on by hand to where the thread catches, then the nut turned this many thousandths of a turn
    Turns(i32),
}

#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub struct Mate {
    pub gap: Um,
    pub seated: bool,
    pub sealed: bool,
    pub gender_ok: bool,
    pub coding_ok: bool,
    pub key_ok: bool,
    pub poles: [Option<Pair>; MAX_POLES],
    /// the gap at which the threads first catch, and the length engaged at the seat (from both halves' thread spans)
    pub thread_catch: Um,
    pub thread_engaged: Um,
    /// touching off the seat: held by the contacts' friction only, not sealed (it works loose under vibration)
    pub friction_only: bool,
    pub over_torque: bool,
}

/// (catch gap, engaged length) from the male's and the female's thread spans, both measured ahead of their own mating planes
pub fn threads(port: &HalfDef, plug: &HalfDef) -> (Um, Um) {
    let (m, f) = if port.gender == Gender::Male { (port.thread_span, plug.thread_span) } else { (plug.thread_span, port.thread_span) };
    let catch = f.1 + m.1;
    let engaged = core::cmp::min(-m.0, f.1) - core::cmp::max(-m.1, f.0);
    (catch, engaged)
}

/// (cos, sin) of a small angle, scaled by 1e6, without floating point: sin θ ≈ θ - θ³/6, cos θ ≈ 1 - θ²/2. Exact to well under a
/// micrometre at 5 mm for |θ| ≤ 10°; mate() only turns the plug when the key fits (|θ| ≤ the key tolerance, under 1°).
pub fn small_angle(mdeg: MilliDeg) -> (i64, i64) {
    let t = (mdeg as i64) * 17_453 / 1_000;                    // micro-radians (π/180 = 0.0174533)
    let t2 = t * t / 1_000_000;
    (1_000_000 - t2 / 2, t - t2 * t / 6_000_000)
}

fn placed(c: &ContactDef, moved: bool, gap: Um, cs: (i64, i64)) -> ([i64; 3], i8) {
    let o = [c.origin[0] as i64, c.origin[1] as i64, c.origin[2] as i64];
    if !moved { return (o, c.dir); }
    let (x, z) = (-o[0], o[2]);                                // turned 180° about z to face the port
    let (co, si) = cs;                                         // then by the key error about the axis
    let xr = (x * co - z * si) / 1_000_000;
    let zr = (z * co + x * si) / 1_000_000;
    ([xr, -o[1] - gap as i64, zr], -c.dir)
}

/// the state of one pin in one socket, both placed (toolkit/contact.py pair())
pub fn pair(pin: &ContactDef, t: [i64; 3], pdir: i8, sock: &ContactDef, m: [i64; 3], sdir: i8) -> Pair {
    let d = (t[1] - m[1]) * sdir as i64;
    let (dx, dz) = (t[0] - m[0], t[2] - m[2]);
    let lat2 = dx * dx + dz * dz;
    let depth = d as Um;
    let open = Pair { state: State::Open, overlap: 0, depth, stop: 0 };
    if sock.cond == Cond::Missing || pin.cond == Cond::Broken { return open; }
    let face = sock.face as i64;
    if !(pin.parallel && sock.parallel && pdir == sdir) || lat2 > LATERAL * LATERAL {
        // off its socket: it meets the insert face around it
        // resting on the face counts as blocked: the plug stops there (>=, so the stop position itself stays blocked)
        return if d >= -face - SEAT as i64 { Pair { state: State::Blocked, overlap: 0, depth, stop: (d + face) as Um } } else { open };
    }
    let (s0p, s1p) = (pin.range.0 as i64, pin.range.1 as i64);
    let (s0s, s1s) = (sock.range.0 as i64, sock.range.1 as i64);
    let ov = core::cmp::min(d - s0p, s1s) - core::cmp::max(d - s1p, s0s);
    let overlap = core::cmp::max(0, ov) as Um;
    let wipe = core::cmp::max(pin.wipe, sock.wipe) as i64;
    if d > s1s { return Pair { state: State::Blocked, overlap, depth, stop: (d - s1s) as Um }; }   // on the bottom of the bore
    if ov <= 0 { return Pair { overlap, ..open }; }
    if sock.cond == Cond::Spread || ov < wipe { return Pair { state: State::Marginal, overlap, depth, stop: 0 }; }
    if pin.cond == Cond::Corroded || sock.cond == Cond::Corroded { return Pair { state: State::HighR, overlap, depth, stop: 0 }; }
    Pair { state: State::Made, overlap, depth, stop: 0 }
}

fn evaluate(pc: &[Option<ContactDef>; MAX_POLES], qc: &[Option<ContactDef>; MAX_POLES], gap: Um, key: MilliDeg) -> [Option<Pair>; MAX_POLES] {
    let cs = small_angle(key);
    let mut out = [None; MAX_POLES];
    let mut i = 0;
    while i < MAX_POLES {
        if let (Some(a), Some(b)) = (pc[i], qc[i]) {
            // the pin and the socket of this pole, whichever half each is in (an L-coded FE pin sits in the female)
            let (pin, pin_moved, sock, sock_moved) = if a.kind == Kind::Pin { (a, false, b, true) } else { (b, true, a, false) };
            if pin.kind == Kind::Pin && sock.kind == Kind::Socket {
                let (t, pd) = placed(&pin, pin_moved, gap, cs);
                let (m, sd) = placed(&sock, sock_moved, gap, cs);
                out[i] = Some(pair(&pin, t, pd, &sock, m, sd));
            } else {
                out[i] = Some(Pair { state: State::Open, overlap: 0, depth: 0, stop: 0 });   // two pins or two sockets: no counterpart
            }
        } else if pc[i].is_some() || qc[i].is_some() {
            out[i] = Some(Pair { state: State::Open, overlap: 0, depth: 0, stop: 0 });
        }
        i += 1;
    }
    out
}

/// what a technician gets when the plug (plug, its contacts qc) comes onto the port (port, pc) (toolkit/contact.py mate())
pub fn mate_contacts(port: &HalfDef, pc: &[Option<ContactDef>; MAX_POLES], plug: &HalfDef, qc: &[Option<ContactDef>; MAX_POLES],
                     approach: Approach, key_err: MilliDeg, torque: Option<MilliNm>) -> Mate {
    let gender_ok = port.gender != plug.gender;
    let coding_ok = port.coding == plug.coding;
    let key_ok = coding_ok && key_err.unsigned_abs() <= port.key_tol_mdeg.unsigned_abs();
    let (catch, engaged) = threads(port, plug);
    let mut gap = match approach {
        Approach::Gap(g) => core::cmp::max(g, 0),
        Approach::Turns(t) => core::cmp::max(0, catch - ((port.pitch as i64) * (core::cmp::max(t, 0) as i64) / 1_000).min(catch as i64) as Um),
    };
    if !gender_ok { gap = core::cmp::max(gap, port.key_gap + 5_000); }             // both male or both female: they do not mate
    else if !key_ok { gap = core::cmp::max(gap, port.key_gap); }                   // the key stops the plug short
    let key = if key_ok { key_err } else { 0 };
    let mut poles = evaluate(pc, qc, gap, key);
    // a blocked pin stops the plug where it meets the insert face (or the bottom of its bore): everything is evaluated there
    let mut rounds = 0;
    while gender_ok && key_ok && rounds < 3 {
        let mut worst: i64 = i64::MIN; let mut any = false;
        let mut i = 0;
        while i < MAX_POLES {
            if let Some(p) = poles[i] { if p.state == State::Blocked { any = true; if (p.stop as i64) > worst { worst = p.stop as i64; } } }
            i += 1;
        }
        if !any { break; }
        let g2 = gap as i64 + core::cmp::max(0, worst + SEAT as i64);
        if g2 <= gap as i64 { break; }
        gap = g2 as Um; poles = evaluate(pc, qc, gap, key); rounds += 1;
    }
    let seated = gap <= SEAT && gender_ok && key_ok;
    let tq = match torque { Some(t) => t, None => if seated { port.torque_mnm.0 } else { 0 } };
    let sealed = seated && tq >= port.torque_mnm.0;
    let over_torque = torque.map_or(false, |t| t > port.torque_mnm.1);
    let mut touching = false;
    let mut i = 0;
    while i < MAX_POLES { if let Some(p) = poles[i] { if p.state.touching() { touching = true; } } i += 1; }
    Mate { gap, seated, sealed, gender_ok, coding_ok, key_ok, poles, thread_catch: catch, thread_engaged: engaged,
           friction_only: touching && !seated && gender_ok && key_ok, over_torque }
}

/// mate() with a condition per pole on each half (Cond::Ok for a half as built)
pub fn mate(port: &HalfDef, port_conds: &[Cond; MAX_POLES], plug: &HalfDef, plug_conds: &[Cond; MAX_POLES],
            approach: Approach, key_err: MilliDeg, torque: Option<MilliNm>) -> Mate {
    mate_contacts(port, &port.with(port_conds), plug, &plug.with(plug_conds), approach, key_err, torque)
}

pub const ALL_OK: [Cond; MAX_POLES] = [Cond::Ok; MAX_POLES];

/// a case toolkit/contact.py answered (generated): the Rust rules must give the same answer
pub struct Golden {
    pub port: &'static HalfDef,
    pub plug: &'static HalfDef,
    pub plug_pole: u8,
    pub plug_cond: Cond,
    pub gap: Um,
    pub seated: bool,
    pub gap_after: Um,
    pub poles: &'static [(u8, State)],
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::generated::*;

    fn conds(pole: u8, c: Cond) -> [Cond; MAX_POLES] { let mut a = ALL_OK; if pole >= 1 { a[(pole - 1) as usize] = c; } a }

    #[test]
    fn golden_agrees_with_contact_py() {
        let mut bad = 0;
        for g in GOLDEN.iter() {
            let r = mate(g.port, &ALL_OK, g.plug, &conds(g.plug_pole, g.plug_cond), Approach::Gap(g.gap), 0, None);
            let mut ok = r.seated == g.seated && (r.gap - g.gap_after).abs() <= 2;
            for &(p, s) in g.poles.iter() { if r.poles[(p - 1) as usize].map(|x| x.state) != Some(s) { ok = false; } }
            if !ok { bad += 1; eprintln!("MISMATCH {} + {} pole {} {:?} gap {}: rust gap {} seated {} {:?}", g.port.name, g.plug.name, g.plug_pole, g.plug_cond, g.gap, r.gap, r.seated, r.poles.map(|p| p.map(|x| x.state))); }
        }
        assert_eq!(bad, 0, "{} of {} golden cases disagree", bad, GOLDEN.len());
    }

    /// the properties of src/proofs.rs, sampled densely here (Kani proves them for every value)
    #[test]
    fn seat_makes_every_pole_sampled() {
        for &(a, b) in JOINTS.iter() {
            let (catch, _) = threads(a, b);
            for k in (-a.key_tol_mdeg..=a.key_tol_mdeg).step_by(7) {
                let r = mate(a, &ALL_OK, b, &ALL_OK, Approach::Turns(catch + 1), k, Some(a.torque_mnm.0));
                assert!(r.seated && r.sealed, "{} + {} key {}", a.name, b.name, k);
                for p in r.poles.iter().flatten() { assert_eq!(p.state, State::Made, "{} + {} key {}", a.name, b.name, k); }
            }
        }
    }

    #[test]
    fn key_past_the_keyway_stops_the_plug_sampled() {
        for &(a, b) in JOINTS.iter() {
            for k in [a.key_tol_mdeg + 1, 2_000, 5_000, 45_000].into_iter().filter(|&k| k > a.key_tol_mdeg) {   // each port's own keyway (L X04: 2.452°)
                let r = mate(a, &ALL_OK, b, &ALL_OK, Approach::Turns(99_000), k, None);
                assert!(!r.key_ok && !r.seated && r.gap >= a.key_gap);
                for p in r.poles.iter().flatten() { assert!(!p.state.touching(), "{} + {} key {}", a.name, b.name, k); }
            }
        }
    }

    #[test]
    fn fe_makes_first_sampled() {
        for &(a, b) in JOINTS.iter().filter(|(a, _)| a.coding == Coding::L) {
            for g in (0..12_000).step_by(10) {
                let r = mate(a, &ALL_OK, b, &ALL_OK, Approach::Gap(g), 0, None);
                let power = (0..4).any(|i| r.poles[i].map_or(false, |p| p.state.conducts()));
                if power { assert!(r.poles[4].unwrap().state.conducts(), "{} + {} gap {}", a.name, b.name, g); }
            }
        }
    }

    #[test]
    fn pushed_back_window_sampled() {
        let (a, b) = (&DEV_F_A, &CORD_M_A);
        let base = b.with(&ALL_OK);
        for recess in (0..=6_900).step_by(10) {
            let mut q = base; let mut c = q[3].unwrap(); c.origin[1] += recess; q[3] = Some(c);
            let r = mate_contacts(a, &a.with(&ALL_OK), b, &q, Approach::Gap(0), 0, None);
            let s = r.poles[3].unwrap().state;
            let want = if recess <= 4_450 { State::Made } else if recess < 4_950 { State::Marginal } else { State::Open };
            assert_eq!(s, want, "recess {}", recess);
        }
    }

    #[test]
    fn small_angle_is_close() {
        // against the float functions, for the test only
        for mdeg in (-10_000..=10_000).step_by(250) {
            let (c, s) = small_angle(mdeg); let t = (mdeg as f64 / 1000.0).to_radians();
            // under a micrometre of error at 5 mm from the axis
            assert!(((c as f64) / 1e6 - t.cos()).abs() * 5000.0 < 1.0 && ((s as f64) / 1e6 - t.sin()).abs() * 5000.0 < 1.0, "{}", mdeg);
        }
    }
}
