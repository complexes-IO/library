# ETIM classes for machine building

Source: ETIM International, **ETIM 10.0**, all sectors, English master, metric (ETIM-10.0-ALL-SECTORS-CSV-METRIC-EI-2024-12-05),
downloaded by EM on 2026-11-07 from https://www.etim-international.com/downloads/. The ETIM classification model is licensed under
the **Open Data Commons Attribution Licence (ODC-BY 1.0)**: https://opendatacommons.org/licenses/by/1-0/ . Any public use of this
data must attribute ETIM International, and these notices stay with it. The files here are a subset; the full download is not
kept in the repo.

Why it is here (EM, 2026-11-07: "the goal is to be able to build any machine from elements up"): ETIM names every product class
vendor-neutrally, with the features that define it (rated current, poles, thread size...). It is the list of what the library
needs, and each class's features are what an element of that class must state. Catalogues (McMaster-Carr, Uline, MonotaRO,
MISUMI) forbid building from their content; ETIM is open.

- `classes.csv`: the 2,245 device classes in the 66 ETIM groups machine building uses (accessory and spare-part classes left
  out). `tier` 1 is the machine core (27 groups: control, switchgear, sensors, terminals, enclosures, connectors, signalling,
  machine elements, fasteners, profiles, grippers, valves, fluid distribution, measurement, cable carrying, cables); 2 the rest
  (process, HVAC, wiring installation, handling). `inventory` names our lib/inventory.csv rows of that class; empty = a class
  we don't have yet. `features` counts the class's ETIM features.
- `class-features.csv`: the features of every tier-1 class and every class our inventory uses, in ETIM's order, with type
  (A alphanumeric choice, L logical, N numeric, R range) and unit. Feature values (the enumerations) are not copied yet.
- lib/inventory.csv `etim`: the class of each row, chosen by hand (core chat 2026-11-07); 66 rows have no ETIM 10 class. ETIM is
  thin on motion and machine mechanics (servo and stepper drives and motors, gearboxes, couplings, linear guides, timing belts,
  T-slot profiles, keys, screws by ISO type, enabling devices): those need a second list.
