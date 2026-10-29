# Independent verification ledger - Energize Denver benchmarking brief (2026-10-29)

Verifier method (independent of the builder): standard-library-only
recomputation (code/verify_independent.py; json, csv, collections,
statistics, urllib; no pandas, no numpy, no openpyxl) from the raw
pulls - the ArcGIS attribute JSON for 2016-2022 and the raw CSV cell
dump of the Excel workbooks for 2023-2025 - with its own field
matching by normalized column name, its own missing-value parser,
and statistics.median for medians. It never reads
data/building_panel.csv. Fresh live recounts against the ArcGIS
services were made during the verification pass itself. Output:
data/verify_independent_output.json. All 65 checks_vs_builder
flags: true.

## Figures: all REPRODUCED, none corrected

| Figure | Builder | Independent | Verdict |
|---|---|---|---|
| Rows per year, 2016-2025 | 1,823 / 3,026 / 3,015 / 3,007 / 3,092 / 2,905 / 2,914 / 3,156 / 2,828 / 2,700 | identical (stdlib recount of every raw file; fresh live counts agree for 2016, 2019, 2022) | REPRODUCED |
| Buildings with a known EUI per year | 1,337 / 2,370 / 2,458 / 2,298 / 2,446 / 2,474 / 2,644 / 2,906 / 2,545 / 2,379 | identical, from the verifier's own parser ("None"/blank/zero/negative to unknown) | REPRODUCED |
| Median site EUI per year | 63.3 / 61.5 / 64.0 / 66.7 / 59.1 / 58.7 / 61.0 / 58.3 / 54.2 / 51.5 | identical within 0.11 on every year (statistics.median) | REPRODUCED |
| Matched panel 2016-2025 | 984 buildings; median 64.8 to 53.1; 73.7 percent fell | identical (verifier's own ID join over the raw files) | REPRODUCED |
| Matched panel 2019-2025 | 1,687 buildings; median 65.9 to 52.4; 81.6 percent fell | identical | REPRODUCED |
| By-type 2025 medians, types with n of 30 or more | 15 types (supermarkets 157.8 down to self-storage 9.7) | all 15 reproduced from case-insensitive grouping of the raw 2025 workbook dump | REPRODUCED |
| Control: energy / sq ft recomputation | 23,062 of 23,816 building-years agree (96.8 percent) | identical count and share | REPRODUCED |
| Compliance counter 2025 | in compliance 2,306 / not submitted 234 / pending revisions 96 / exempt 64 | identical | REPRODUCED |
| Distinct buildings, all years | 3,687 | 3,687 | REPRODUCED |
| Floor area total 2025 | 332,390,060 sq ft | identical | REPRODUCED |
| Top EUI building 2025 | Building ID 6452 at 1,271.3 | identical id and value | REPRODUCED |
| Parcels in the city register | 240,492 | 240,492 (fresh live count during verification) | REPRODUCED |

## Traps examined (adversarial pass over source definitions and samples)

- T1 Site EUI is as-reported, not metered. Values enter through
  ENERGY STAR Portfolio Manager submissions and the city publishes
  what was submitted. Treatment: the caveat is printed in the
  brief's opening, in Finding 6's internal-consistency check, and
  in Finding 7; no figure is phrased as a measurement, and no
  building-level verdict is drawn.
- T2 Stored zeros are not real zeros. An EUI of 0 appears from 2018
  on (3 rows) and in every year from 2020 (30 rows in 2025); a real
  covered building does not use zero energy. Treatment: zero (and
  negative, of which there are none) maps to unknown before any
  figure; per-year zero counts are in the audit and Finding 3.
- T3 Text numerics with string sentinels. The 2016-2022 tables store
  numbers as strings, with the literal string "None" and "" for
  missing. A parser that coerced "None" carelessly, or averaged
  the raw column, would corrupt every figure. Treatment: one
  documented parser in the builder; a second, independently written
  parser in this verifier; identical outputs.
- T4 The Reporting Year field reads one year after the dataset
  year in every file that carries it (2022 table: 2023 on all
  2,914 rows; 2025 workbook: 2026). A reader who trusted the field
  would shift the whole series by a year. Treatment: years are
  dataset (energy) years everywhere, and the offset is printed in
  the brief's data notes and in stats.json.
- T5 Compliance vocabulary changes mid-window ("Out of Compliance"
  to "Not Submitted" in 2020; "Pending Revisions" added 2021;
  lowercase from 2023). Treatment: reporting is measured by
  known-EUI presence, and the known-EUI-by-label cross-tab is
  published (2025: 2,306 in compliance, 69 pending revisions, 4
  exempt), so the label series is never trended naively.
- T6 The 2018 property-type taxonomy break. The 2018 primary-type
  field carries Apartment (531) and Condominium (300) where other
  years carry Multifamily Housing; exactly 3 rows carry Multifamily
  Housing (an early draft of the brief said none; the audit's first
  run asserted the same and failed against the row-level recount,
  which is recorded in verification.md). Treatment: 2018 is
  excluded from every by-type comparison; the break is printed in
  Finding 5.
- T7 Outlier-dominated means. One 2016 record (Building ID 1481)
  reports a site EUI of 97,144.5, internally consistent with its
  reported energy and area, and the raw 2016 mean is 157.1 against
  a median of 63.3. Treatment: headlines are medians; means are
  printed with the sensitivity (mean excluding EUI above 300:
  72.6 in 2016, 59.1 in 2025) and the outlier counts per year.
- T8 A test record sits in the published 2023 register (Building ID
  9999, "test office 1"). Treatment: it is counted openly - one of
  3,156 rows and one of the 250 without a known EUI - and named in
  Finding 7; it touches no figure.
- T9 The 2024 Feature Service is dead. The Hub's 2024 Feature
  Service item points at a service URL the ArcGIS server rejects
  ("Invalid URL"). Treatment: the 2024 Excel item (same Hub, same
  dataset title) is the 2024 source; its byte size matches the Hub
  item record, and its row structure matches the 2023 and 2025
  workbooks.
- T10 Panel selection. The matched panels condition on reporting in
  both years; 26.4 percent of 2016's known-EUI buildings and 26.6
  percent of 2019's are not in the 2025 panel. Treatment: match
  rates are printed in the data notes, the all-reporters series is
  printed alongside with its own composition caveat, and the
  selection reading is carried in What this might mean.

No open finding. Every figure in the brief traces to stats.json,
all rebuilt and re-audited after the final build, and both decisive
panels were reproduced exactly by an independent implementation.
