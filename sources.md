# Sources - Energize Denver benchmarking brief (2026-10-29)

Every figure in the brief traces to one of the sources below. Derived
figures are labeled derived and state their inputs.

## Energize Denver Final Master Datasets, 2016-2022 (Findings 1-7)

- Source: City and County of Denver open data, Energize Denver
  yearly Final Master Datasets, ArcGIS FeatureServer tables on
  services1.arcgis.com/zdB7qR0BtYrg0Xpl, via
  opendata-geospatialdenver.hub.arcgis.com. Dataset description
  (same text on each year): "These are the complete benchmarking
  datasets from reporting year 2016 onward with energy usage for all
  buildings covered under the City and County of Denver's Energy
  Benchmarking Ordinance. The Climate Action, Sustainability, &
  Resiliency team manages compliance with the Energize Denver
  regulatory program that requires buildings 25,000 square feet and
  larger to submit their energy benchmarking data once a year."
- Services and layers: ODC__2016_Final_Master_Dataset table 11
  (Hub item 78eb671c87f9477884fdd5159958c534); 2017 table 14
  (450f3ad8376e44b1b0604511237e8bee); 2018 table 17
  (7dabd685c7f14eda9b703c948f571e65); 2019 table 20
  (4661245413314c01abbc6bfbf5a261e5); 2020 table 23
  (3dce8e1321bf499aac2c67771ec8a5de); 2021 table 26
  (274ae79d34c644d3ba0363c01c7ea206); 2022 table 28
  (6b200ed29b474f76b53bf4d972b36518).
- Pull: October 29, 2026, full tables without geometry
  (data/master_<year>_raw.json; pull record in data/pull_log.json).
  Server counts and local counts equal for all seven years: 1,823 /
  3,026 / 3,015 / 3,007 / 3,092 / 2,905 / 2,914 rows.
- Figures taken directly: row counts; compliance counters per year
  (in data/pull_log.json and stats.json); all building-level fields
  as published (numerics are stored as strings in these tables; the
  parsing rule is in the brief's data notes).

## Energize Denver Master Datasets, 2023-2025 (Findings 1-7)

- Source: the same Hub, as Microsoft Excel items (no FeatureServer
  table is published for 2023 or 2025; the 2024 Feature Service
  item 5f6f15cf7a864195a318b7d8c27af4f1 points at a service URL the
  ArcGIS server rejects with "Invalid URL," verified October 29,
  2026, so the Excel item is the usable 2024 source).
- Items and download URLs (ArcGIS sharing data endpoint):
  2023 "Energize Denver 2023 Final Master Data Set," item
  2da57c7e046b4daa97daf0052d7e7825,
  https://www.arcgis.com/sharing/rest/content/items/2da57c7e046b4daa97daf0052d7e7825/data
  (sheet "MasterDataSet Report (1)," 3,156 data rows);
  2024 "Energize Denver 2024 Master Dataset," item
  f323917ade9149b3a346b8acf110f8e6,
  https://www.arcgis.com/sharing/rest/content/items/f323917ade9149b3a346b8acf110f8e6/data
  (sheet "2024 Data," 2,828 data rows);
  2025 "Energize Denver 2025 Master Dataset," item
  169272beebc54212ac08f3f607bef272,
  https://www.arcgis.com/sharing/rest/content/items/169272beebc54212ac08f3f607bef272/data
  (sheet "2025MasterDataSet Report," 2,700 data rows).
- Pull: October 29, 2026 (data/master_<year>.xlsx plus the raw
  cell-value dump data/master_<year>_raw.csv). Downloaded byte
  sizes equal the Hub item records' sizes for all three years.

## Derived figures (all in stats.json, built by code/build_stats.py)

- Known-EUI populations, medians, means, quartiles, and shares per
  year: derived from the parsed site EUI field under the stated
  rule (parses as a number and greater than zero; "None," blank,
  zero, and negative values are unknown). Per-year values in
  stats.json per_year.
- Matched panels: derived by joining yearly files on Denver
  Building ID (unique within every year; 0 duplicates in 10 files).
  2016-2025: 984 buildings, medians 64.8 and 53.1. 2019-2025: 1,687
  buildings, medians 65.9 and 52.4. 2017-2025: 1,704 buildings,
  60.8 and 52.5. 2019-2024: 1,884 buildings, 66.5 and 54.8.
  Weather-normalized panels: 2016-2025 (984 buildings, 67.5 to
  52.8); 2019-2025 (1,684 buildings, 63.2 to 52.2).
- Square-footage-weighted site EUI: derived as total reported site
  energy divided by total reported square footage over building-
  years with known EUI, known area, and known energy (2019: 82.5;
  2025: 61.5; 2016: 199.7, printed only with its distortion note).
- Internal-consistency control: derived per building-year as site
  energy use divided by square footage, compared with the reported
  site EUI: 23,062 of 23,816 building-years agree within
  max(1.0 kBtu per square foot, 2 percent) (96.8 percent).
- By-type medians: derived from the primary property type field
  grouped case-insensitively (2025 table and 2019 contrasts in
  stats.json by_type). The 2018 taxonomy break (Apartment 531,
  Condominium 300, Multifamily Housing 3) is from the 2018 file's
  own counter, reproduced in the audit.
- Outlier counts and sensitivities: records with a known EUI above
  300 and above 1,000 per year, and medians/means excluding records
  above 300, in stats.json per_year.

## Parcel register (Finding 4 scale context only)

- Source: City and County of Denver open data, ODC_PROP_PARCELS_A
  ("Parcels"), ArcGIS FeatureServer layer 245,
  services1.arcgis.com/zdB7qR0BtYrg0Xpl.
- Figure taken directly: live record count 240,492, queried
  October 29, 2026 (recorded in data/pull_log.json). No parcel
  records were pulled and no join was performed.
- Derived: the ratio of distinct benchmarked buildings (3,687) to
  parcels (240,492) = 1.5 percent, labeled a scale statement in the
  brief, with the non-one-to-one building-to-parcel mapping stated.

## Program framing (brief's Who can act and What this might mean)

- The 25,000-square-foot coverage threshold and annual reporting
  requirement are from the datasets' own Hub description (quoted
  above). The 2019 baseline and the 30 percent reduction aim for
  covered buildings by 2030 are the Energize Denver program's
  published framing, referenced in the brief only to identify whose
  measure the program-basis aggregate is; no figure in this brief
  is computed on that basis, and the brief says so where the
  framing appears.

## Not used as measured data (deliberate exclusions)

- ENERGY STAR Score: published in the files but not used; it is a
  relative 1-100 score against a national reference population, not
  an intensity, and mixing it with site EUI would juxtapose two
  different measures.
- Total GHG emissions and per-fuel use fields: published in the
  files but not used; no claim in the brief needs them.
- Baseline EUI and interim/final target EUI columns (present from
  2022 and in the workbooks): building-level program targets, not
  outcomes; not used, so no target-attainment figure is implied.
- The internal Reporting Year field: used only to establish the
  year convention (it reads energy year + 1); never used as a
  figure's year.
