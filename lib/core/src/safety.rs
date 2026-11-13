//! The motor-starter cell's emergency-stop channel, one scan at a time: the station's E-stop (two N.C. channels) into the safety
//! relay k-safe (relay-safety-2ch-2no1nc: S11/S12 and S21/S22, reset S34), whose output enables K1's coil together with the PLC's run output.
//!
//! The rules, from IEC 60204-1 (emergency stop):
//! - stop category 0: with either channel open, the relay's output and K1's coil are off in the same scan;
//! - resetting is manual and deliberate: closing the channels again does not by itself re-enable anything; only a reset
//!   press (a rising edge) with both channels closed does;
//! - the reset is monitored: it is refused while K1's auxiliary N.C. contact reports K1 still in (a welded contactor).
//! Assumptions (NOT ON FILE in this library: confirm against the 440R manual's reset and EDM sections): the reset acts on the press,
//! not the release; no cross-fault (channel discrepancy) lock-out is modelled.

#[derive(Clone, Copy, PartialEq, Eq, Debug, Default)]
pub struct SafetyState {
    /// the relay's outputs are latched on (it has been reset since the last trip)
    pub latched: bool,
    /// the reset input in the previous scan (to see the press)
    pub reset_prev: bool,
}

#[derive(Clone, Copy, PartialEq, Eq, Debug, Default)]
pub struct SafetyIn {
    pub ch_a: bool,
    pub ch_b: bool,
    pub reset: bool,
    /// K1's auxiliary N.C. contact: closed when K1 is out (dropped)
    pub k1_aux_nc: bool,
    /// the PLC's run output to K1 (the program's start / stop logic)
    pub plc_run: bool,
}

#[derive(Clone, Copy, PartialEq, Eq, Debug, Default)]
pub struct SafetyOut {
    pub relay_out: bool,
    pub k1_coil: bool,
}

pub fn step(s: SafetyState, i: SafetyIn) -> (SafetyState, SafetyOut) {
    let both = i.ch_a && i.ch_b;
    let pressed = i.reset && !s.reset_prev;
    let latched = if !both { false } else if s.latched { true } else { pressed && i.k1_aux_nc };
    let relay_out = latched && both;
    (SafetyState { latched, reset_prev: i.reset }, SafetyOut { relay_out, k1_coil: relay_out && i.plc_run })
}

#[cfg(test)]
mod tests {
    use super::*;

    /// five inputs and two state bits: 128 cases, all of them. For a model this small the test is itself a full proof;
    /// src/proofs.rs states the same properties for Kani, ready for when the model grows.
    #[test]
    fn every_state_every_input() {
        for sbits in 0..4u8 {
            let s = SafetyState { latched: sbits & 1 != 0, reset_prev: sbits & 2 != 0 };
            for ibits in 0..32u8 {
                let i = SafetyIn { ch_a: ibits & 1 != 0, ch_b: ibits & 2 != 0, reset: ibits & 4 != 0, k1_aux_nc: ibits & 8 != 0, plc_run: ibits & 16 != 0 };
                let (s2, o) = step(s, i);
                if !(i.ch_a && i.ch_b) { assert!(!o.relay_out && !o.k1_coil && !s2.latched); }
                if !s.latched && !(i.reset && !s.reset_prev) { assert!(!s2.latched && !o.k1_coil); }
                if !s.latched && !i.k1_aux_nc { assert!(!s2.latched); }
                if o.k1_coil { assert!(i.plc_run && i.ch_a && i.ch_b); }
            }
        }
    }
}
