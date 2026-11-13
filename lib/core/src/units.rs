//! Units as plain integers with their unit in the name: the core never mixes them silently.
//! Lengths are whole micrometres (i32: ±2 km), angles millidegrees, torque milli-newton-metres, resistance milliohms.
//! Products are taken in i64. 0.01 mm, the finest figure on file, is 10 µm, so nothing measured is lost.
pub type Um = i32;
pub type MilliDeg = i32;
pub type MilliNm = i32;
pub type MilliOhm = i32;

/// micrometres from millimetres, for tests and literals only (the core itself never sees floats)
pub const fn mm(whole: i32, thousandths: i32) -> Um { whole * 1000 + thousandths }
