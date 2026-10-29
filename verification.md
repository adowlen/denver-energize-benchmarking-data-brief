# Verification - Energize Denver benchmarking brief (2026-10-29)

## Pre-flight audit

Required before this package was drafted: code/audit_section10.py
recomputes every headline figure from the harmonized panel and the
raw pulls and fails loudly on any mismatch. Output
(data/audit_output.txt), run on the final build:

```
COUNTER compliance_status 2016: 3 unique values, sum=1823 == 1823; values={'In Compliance': 1337, 'Exempt': 294, 'Out of Compliance': 192} PASS
COUNTER compliance_status 2019: 3 unique values, sum=3007 == 3007; values={'In Compliance': 2298, 'Out of Compliance': 431, 'Exempt': 278} PASS
COUNTER compliance_status 2025: 4 unique values, sum=2700 == 2700; values={'in compliance': 2306, 'not submitted': 234, 'pending revisions': 96, 'exempt': 64} PASS
COUNTER primary_type 2025 (known EUI): 66 unique values, sum=2379 == 2379; top={'Multifamily Housing': 896, 'Office': 340, 'Non-Refrigerated Warehouse': 171, 'Distribution Center': 128, 'Hotel': 102, 'mixed use property': 81} PASS
COUNTER primary_type 2018 anomaly: 2018 primary-type field carries Apartment=531, Condominium=300, and only 3 Multifamily Housing rows (all three with master type Municipal); 2018 is excluded from by-type comparisons PASS
SENTINEL site_eui 2016: missing=486, zero=0, negative=0, known=1337; unknown excluded from every EUI denominator PASS
SENTINEL site_eui 2017: missing=656, zero=0, negative=0, known=2370; unknown excluded from every EUI denominator PASS
SENTINEL site_eui 2018: missing=554, zero=3, negative=0, known=2458; unknown excluded from every EUI denominator PASS
SENTINEL site_eui 2019: missing=709, zero=0, negative=0, known=2298; unknown excluded from every EUI denominator PASS
SENTINEL site_eui 2020: missing=612, zero=34, negative=0, known=2446; unknown excluded from every EUI denominator PASS
SENTINEL site_eui 2021: missing=411, zero=20, negative=0, known=2474; unknown excluded from every EUI denominator PASS
SENTINEL site_eui 2022: missing=261, zero=9, negative=0, known=2644; unknown excluded from every EUI denominator PASS
SENTINEL site_eui 2023: missing=244, zero=6, negative=0, known=2906; unknown excluded from every EUI denominator PASS
SENTINEL site_eui 2024: missing=258, zero=25, negative=0, known=2545; unknown excluded from every EUI denominator PASS
SENTINEL site_eui 2025: missing=291, zero=30, negative=0, known=2379; unknown excluded from every EUI denominator PASS
POLARITY site_eui 2016: kept sample (building_id, site_eui)=[[5819.0, 51.8], [5816.0, 62.2], [5815.0, 23.5]]; excluded sample=[[1002.0, nan], [1071.0, nan], [1116.0, nan]] (blank parses to missing, 0.0 is a stored zero; both map to unknown) PASS
POLARITY site_eui 2025: kept sample (building_id, site_eui)=[[1002.0, 64.4], [1004.0, 58.8], [1005.0, 124.4]]; excluded sample=[[1001.0, nan], [1008.0, nan], [1011.0, nan]] (blank parses to missing, 0.0 is a stored zero; both map to unknown) PASS
DENOMINATOR closure all years: known + zero + missing == rows for all 10 years (failures: []); every known share is printed on the full row count of its year PASS
UNITS eui recompute (control): 23062 of 23816 building-years agree within max(1.0, 2%) = 96.8%; numerator and denominator are the same building-year (kBtu / sq ft) PASS
PANEL 2016_2025: n=984, median 64.8 -> 53.1; share fell 73.7% PASS
PANEL 2019_2025: n=1687, median 65.9 -> 52.4; share fell 81.6% PASS
CONTROL office median 2025 (sorted-list): n=340, sorted-list median=52.9 vs stats 52.9 PASS
CONTROL weather-normalized panel direction: WN matched panel median 63.2 -> 52.2 (n=1684) moves the same way as the site-EUI panel PASS
JOIN building_id hygiene: duplicate (year, building_id) pairs=0; match rates: 2016 known also in 2025 known 984/1337 (73.6%), 2019 known also in 2025 known 1687/2298 (73.4%); unmatched buildings are buildings without a known EUI in the other year (not submitted, exempt, or not yet covered), which is why the brief reports the all-reporters series alongside the panels PASS
SCALE floor area alongside counts: 2025: 332,390,060 sq ft across 2,700 rows; 2019: 358,859,791 sq ft across 3,007 rows (physical scale printed with every count comparison) PASS
SMALL NUMBERS by-type 2025: 15 types have n>=30 and are the only types charted or compared; 51 types under 30 are flagged in stats.json and carry their counts wherever printed (incl. Hospital n=4, Data Center n=2) PASS
SERVER fresh live recounts (tables): 2016-2022 server counts equal pull-log and stats row counts PASS
SERVER excel item sizes: Hub item byte sizes for 2023-2025 equal the downloaded workbooks PASS
SERVER parcels recount: parcels live 240492 == stats 240492 PASS
SYNC README dependencies: code imports (third-party): ['matplotlib', 'numpy', 'openpyxl', 'pandas', 'pillow']; README dependency line: Python standard library; matplotlib; numpy; openpyxl; pandas; Pillow. PASS
SYNC brief numbers present in stats: headline figures cross-checked against stats.json; missing from brief: [] PASS
VOICE no en/em dashes in brief: published text uses plain hyphens only PASS
AUDIT PASSED
```

Notes on the audit's history. The first audit run FAILED on two
lines, and both dispositions are recorded here per Section 10.3.3.
(1) COUNTER primary_type 2018 anomaly: the audit asserted the 2018
primary-type field contained no Multifamily Housing value; the
builder's brief draft said the same. A row-level recount found
exactly 3 such rows (Building IDs with master type Municipal),
against Apartment 531 and Condominium 300. Verdict: the brief's
claim was wrong in its absolute form; Finding 5 now prints the
3-row count, and the audit asserts the measured counter
(531 / 300 / 3). The substantive point is unchanged: the 2018 field
does not carry the EPA taxonomy the other years carry, and 2018
stays out of by-type comparisons. (2) SYNC README dependencies: the
audit's import scan produced the module name PIL, where the README
lists the package name Pillow, and its comparison sorted
case-sensitively, so Pillow sorted away from the README's order.
Verdict: the README was correct; the check now translates PIL to
Pillow and compares case-insensitively sorted lists. Both fixes
were re-run to a full PASS on the final files.

## Methods checklist

- [x] Count, do not sample: all 10 yearly files pulled in full
  (28,466 building-year records; server counts equal local counts
  for all seven table years; workbook byte sizes equal Hub item
  sizes for 2023-2025; pull record in data/pull_log.json).
- [x] Estimand stated: median site EUI (kBtu per square foot, as
  reported) for fixed matched panels of buildings reporting a known
  EUI in both years (2016-2025 primary, 2019-2025 corroborating),
  with the all-reporters annual series reported separately and
  never mixed with the panels on any graphic without its scope
  label.
- [x] Base rates and exposure: EUI is itself the exposure-adjusted
  rate this program publishes (energy per square foot); no
  occupancy, hours, or output denominator exists in the files, and
  the brief states that limit prominently (opening caveats,
  Finding 2, What this might mean) and implies no causal pattern.
  Every share in the brief is printed on a stated denominator (rows
  of the year, buildings with a known EUI, panel buildings), with
  the unknown-EUI remainder printed alongside (Finding 3).
- [x] Direction of causality considered: stated in Finding 2 and
  What this might mean. Occupancy fell over part of the window and
  lowers EUI without any system change; reporting selection runs
  the same direction. No directional efficiency claim is made;
  the weather-normalized panel is reported as the weather control
  and its limits are stated.
- [x] Category and definition changes over the window: three are
  recorded and handled, none silently. (a) Compliance vocabulary:
  "Out of Compliance" through 2019, "Not Submitted" from 2020,
  "Pending Revisions" added 2021, lowercase in the Excel years;
  reporting is therefore measured by known-EUI presence, with the
  cross-tab published (Finding 3). (b) The 2018 primary-type
  taxonomy break (Finding 5); 2018 excluded from by-type work.
  (c) Coverage phase-in: the 2016 file holds 1,823 buildings
  against 3,026 in 2017; the 2016 panel is labeled a large-building
  cohort wherever it appears.
- [x] Exact date range stated: energy years 2016-2025, files pulled
  October 29, 2026. The Reporting Year offset (each file's internal
  Reporting Year reads energy year + 1; verified on the 2022 table,
  2,914 of 2,914 rows, and the 2023-2025 workbooks) is stated in
  Finding 3's data notes and in stats.json.
- [x] Join match rates: the only join is building ID across years.
  2016 known-EUI buildings also known in 2025: 984 of 1,337
  (73.6 percent); 2019: 1,687 of 2,298 (73.4 percent). Both are
  above the 5 percent unmatched flag line, flagged in the brief's
  data notes with the systematic explanation: unmatched means no
  known EUI in the other year (not submitted, exempt, pending, or
  absent from that year's register), and consistent reporters may
  differ from sporadic ones - the selection caveat is printed in
  What this might mean, and the all-reporters series is printed
  alongside the panels so the two can be compared.
- [x] Small numbers: by-type comparisons are restricted to types
  with 30 or more known-EUI buildings (15 types in 2025); smaller
  types print with their counts (hospitals n=4, data centers n=2,
  supermarkets in 2019 n=29 flagged). Every percentage prints its
  count.
- [x] Official definitions: site EUI and weather-normalized site
  EUI are the datasets' own fields, as described in each dataset's
  Hub description (complete benchmarking datasets with energy usage
  for all buildings covered under the benchmarking ordinance;
  buildings 25,000 square feet and larger report annually). The
  2019 baseline is the program's own reference year for its
  performance targets, as described in the program's published
  guidance; the brief does not compute the program's aggregate
  measure and says so.
- [x] Sentinel handling (Section 10.1.1 and 10.1.2): table-year
  numerics are stored as text; the literal strings "None" and "",
  blank workbook cells, zero, and negative values map to unknown
  and are excluded from every EUI denominator, with per-year
  missing/zero/known counts and matched-vs-excluded samples
  recorded in the audit. Zero-EUI rows exist in 2018 (3) and every
  year from 2020 (34 in 2020, 30 in 2025); none is treated as a
  real intensity anywhere.
- [x] Nullable-denominator trap (10.1.5): every known-EUI share
  uses the full row count of its year as denominator, asserted per
  year in the audit (known + zero + missing == rows, all 10 years),
  and the unknown share is printed alongside (Finding 3).
- [x] Layering test: the master datasets support every figure
  except Finding 4's scale ratio, which adds the parcel register's
  live count (240,492) as a count-only context layer; the brief
  states that no parcel join is performed and no claim rests on
  one. The housing angle is carried by the files' own multifamily
  type counts, not by an added housing layer.
- [x] Sync gate (10.3): README dependency list matches the code's
  actual imports (compiled from a scan of code/: matplotlib,
  numpy, openpyxl, pandas, Pillow, plus the standard library).
  Headline numbers in brief-draft.md were cross-checked against
  stats.json programmatically in the audit (53.1; 64.8; 52.4; 65.9;
  51.5; 66.7; 2,379; 2,700; 984; 1,687; 240,492; 157.8; 49.2; 9.7)
  and by the builder's pass over the remaining figures: panels
  1,704 / 60.8 / 52.5 and 779 / 2,084; WN panels 67.5 / 52.8 and
  63.2 / 52.2; annual medians and counts for all ten years;
  compliance counters for 2025 (2,306 / 234 / 96 / 64) and the 2023
  peak share (92.1 percent, 2,906 of 3,156); floor areas
  332,390,060 and 358,859,791; weighted EUIs 82.5 / 61.5 / 199.7;
  cross-tab 2,306 / 69 / 4; by-type table (all 15 medians and
  counts) and the 2019 contrasts (60.8 / 746; 71.1 / 317; 84.9 / 71;
  47.8 / 134; 10.7 / 45; 191.5 / 29); top-EUI and top-energy lists;
  outlier counts (30 / 3 in 2016, 10 / 1 in 2025) and the 97,144.5
  record; the 2023 test row (ID 9999, 250 unknown of 3,156).

## Section 11 status/fix loop

Builder: this run (package assembled October 29, 2026).
Independent verifier: separate standard-library-only implementation
(code/verify_independent.py) reading the raw JSON pulls and the raw
CSV dump of the workbooks - never the builder's panel - with its own
field matching, number parser, and statistics.median medians, plus
fresh live recounts; see verification-ledger-independent.md. All 65
checks reproduced, none corrected, including both matched panels
exactly (984 and 1,687 buildings) and all 15 charted by-type
medians.
Adversarial pass over definitions: the traps that matter are
disclosed in the brief itself - site EUI is as-reported, not
metered (opening caveats; Finding 7); the Reporting Year field
reads one year after the dataset year (data notes); the compliance
vocabulary changes mid-window, so reporting is measured by
known-EUI presence with the cross-tab published (Finding 3); the
2018 type taxonomy break excludes 2018 from type comparisons
(Finding 5); a stored zero EUI is unknown, never a real zero
(Finding 3, data notes); the raw mean is outlier-dominated and no
headline rests on it (Findings 1 and 7); the 2024 Feature Service
URL is dead and the Excel item is the 2024 source (data notes).
Fix loop: the audit's first run failed two lines; both were
adjudicated (count, mechanism, treatment) and closed on evidence -
see the notes under the audit output above. One brief sentence was
corrected (the 2018 Multifamily Housing count) and one audit check
was corrected (the dependency comparison). The charts were visually
inspected after rendering; one title line on the annual-series
chart clipped at the frame edge, was split across two lines, and
the chart was re-rendered and re-inspected before this record was
written.
Freeze: stats.json, data/building_panel.csv, and brief-draft.md are
in sync as of the final audit run; any edit to a figure after this
point requires re-running code/audit_section10.py and
code/verify_independent.py. Hero: hero.png is intentionally absent
in this build; the story illustration was generated during the
build and is saved in hero_source/ (see hero_source/hero-brief.md),
and the parent run composites the headline with
code/hero_composite.py. The package is not publishable until the
hero is composited and inspected.
