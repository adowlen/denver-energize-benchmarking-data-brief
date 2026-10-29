# Denver's benchmarked buildings: median energy intensity down 18 percent since 2016 for the same buildings

**One-line finding:** Among the 984 Denver buildings with a reported site EUI in both 2016 and 2025, the median site EUI fell from 64.8 to 53.1 kBtu per square foot (-18.1 percent), and 73.7 percent of the buildings report a lower EUI in 2025.

Source: City and County of Denver open data, Energize Denver Final Master Datasets for energy years 2016-2025 (ArcGIS tables for 2016-2022, Excel workbooks for 2023-2025), pulled in full on October 29, 2026: 28,466 building-year records covering 3,687 distinct buildings. Parcel scale context: the city's parcel register (ODC_PROP_PARCELS_A), live count on the same day.

Three caveats govern everything below, and they are stated here rather than in a footnote. First, site EUI in these files is as reported: building representatives enter energy data into ENERGY STAR Portfolio Manager and the city publishes what was submitted. No figure in this brief is a metered measurement, and the files carry reported values that are not plausible as physical intensities (Finding 7). Second, benchmarking covers buildings of 25,000 square feet and larger only, and coverage phased in: the 2016 file holds 1,823 buildings against 3,026 in 2017, so the 2016 panel is a large-building cohort, not the full covered stock. Third, a building appears in a year's figures only if it reported a usable EUI that year. The share of each file's rows with a known EUI runs from 73.3 percent in 2016 to 92.1 percent in 2023 and 88.1 percent in 2025; the matched panels in Finding 1 hold the building set constant so that this reporting churn cannot move the headline.

## Finding 1: For the same buildings, median site EUI is down 18.1 percent since 2016 and 20.5 percent since 2019

Joining the yearly files on Denver Building ID, 984 buildings carry a known site EUI in both 2016 and 2025. For that fixed set:

- Median site EUI: 64.8 kBtu per square foot in 2016, 53.1 in 2025 - a fall of 11.7 points, or 18.1 percent of the 2016 median.
- The median building's own change is -9.3 points (-15.5 percent); 73.7 percent of the 984 buildings report a lower EUI in 2025 than in 2016, and 26.2 percent report a higher one.
- 779 of the 984 also report a known EUI in every one of the ten years; 2,084 of the 2,379 buildings with a known EUI in 2025 report one in at least five of the ten years, so the 2025 cross-section is mostly repeat reporters, not one-year entrants.

The program's own baseline year gives the same picture on a larger panel. The Energize Denver performance standard sets its targets against a 2019 baseline; 1,687 buildings carry a known site EUI in both 2019 and 2025, and their median fell from 65.9 to 52.4 (-13.5 points, -20.5 percent), with 81.6 percent of buildings reporting a lower EUI in 2025. The median building's own change on this panel is -12.5 points (-19.7 percent). A third panel, 2017 to 2025 (1,704 buildings), falls from 60.8 to 52.5 (-13.7 percent).

Weather normalization does not explain the panel result away. Repeating both panels on the files' weather-normalized site EUI field: the 2016 panel's median falls from 67.5 to 52.8 (984 buildings), and the 2019 panel's from 63.2 to 52.2 (1,684 buildings). The weather-normalized and as-reported series move together throughout (Finding 2).

The means are printed here because the brief's method requires them, with their limit attached. On the 2016 panel the mean falls from 178.8 to 62.8, a figure dominated by one 2016 record (Finding 7: a single building reporting a site EUI of 97,144.5 as submitted). On the 2019 panel the mean falls from 79.5 to 61.6. The medians above are the figures this brief's headline rests on; they move by less than 1 point when every building reporting an EUI above 300 is removed (Finding 7).

## Finding 2: The all-reporters median peaked in 2019 at 66.7 and stands at 51.5 in 2025

Reading each year on its own reporters (a different building set each year, so composition moves these figures as well as building performance):

- Median site EUI by year: 2016: 63.3 (1,337 buildings with a known EUI); 2017: 61.5 (2,370); 2018: 64.0 (2,458); 2019: 66.7 (2,298); 2020: 59.1 (2,446); 2021: 58.7 (2,474); 2022: 61.0 (2,644); 2023: 58.3 (2,906); 2024: 54.2 (2,545); 2025: 51.5 (2,379).
- The weather-normalized median declines more steadily over the same years: 66.4 in 2016, 63.8 in 2019, 60.9 in 2020, 58.3 in 2023, and 51.4 in 2025.
- The square-footage-weighted site EUI (total reported site energy divided by total reported square footage, same buildings on both sides) is 82.5 in 2019 and 61.5 in 2025, above the medians in both years: larger buildings in the covered stock report higher intensity per square foot than the median building. The 2016 weighted figure (199.7) is not printed as a comparison because one record (Finding 7) contributes most of it.

The 2020 step down in the as-reported median (66.7 to 59.1) coincides with the first pandemic year, when occupancy fell across offices, hotels, and schools; the series partially rebounds in 2022 (61.0) before falling in each of the three most recent years. This brief reports the timing and makes no causal claim from it; the matched panels in Finding 1, not this series, carry the trend finding, because they are not moved by which buildings happen to report in a given year.

## Finding 3: Reporting rose through 2023, then the file shrank; the labels changed mid-window

Each yearly file is a register of covered buildings, not only of reporters:

- Rows per file: 1,823 (2016); 3,026 (2017); 3,015 (2018); 3,007 (2019); 3,092 (2020); 2,905 (2021); 2,914 (2022); 3,156 (2023); 2,828 (2024); 2,700 (2025).
- Rows with a known site EUI as a share of all rows: 73.3 percent in 2016, 76.4 percent in 2019, 90.7 percent in 2022, a peak of 92.1 percent in 2023 (2,906 of 3,156), then 90.0 percent in 2024 and 88.1 percent in 2025 (2,379 of 2,700). The unknown remainder in 2025 is 321 rows: 291 with no EUI value and 30 reporting an EUI of zero, which this package maps to unknown (data notes).
- The compliance labels are the files' own, and their vocabulary changes over the window. Through 2019 the non-reporting label is "Out of Compliance"; from 2020 it is "Not Submitted"; "Pending Revisions" first appears in 2021; the Excel years (2023-2025) carry the same four labels in lowercase. Any compliance trend read across the full window has to cross that vocabulary change, so this brief measures reporting by the presence of a known EUI instead and publishes the cross-tab: in 2025, the 2,379 known-EUI rows are 2,306 labeled "in compliance," 69 labeled "pending revisions," and 4 labeled "exempt." In 2016 all 1,337 known-EUI rows are labeled "In Compliance."
- The 2025 register is the smallest since 2016: 2,700 rows, of which 2,306 (85.4 percent) are labeled "in compliance," 234 "not submitted," 96 "pending revisions," and 64 "exempt." The register held 3,156 rows two years earlier. The files themselves do not state whether the smaller register reflects buildings leaving coverage, buildings being consolidated under single IDs, or register maintenance; the count is reported here as published.

## Finding 4: The covered stock is 3,687 buildings and about a third of a billion square feet

Across the ten files, 3,687 distinct Denver Building IDs appear. The 2025 file's rows total 332,390,060 square feet of floor area (2019: 358,859,791). Set against the city's parcel register (240,492 parcels, live count October 29, 2026), the buildings that have ever appeared in a benchmarking file equal 1.5 percent of parcels by count. That is a scale statement, not a join: a master-dataset row is a building as reported in Portfolio Manager, which does not map one-to-one onto parcels, and no parcel-level join is performed in this package. The covered stock is, by the program's design, the large-building stock: every figure in this brief describes buildings of 25,000 square feet and larger, and says nothing about the energy intensity of smaller buildings, including most single-family housing.

Multifamily housing is the largest single part of the covered stock. In 2025, 896 of the 2,379 buildings with a known EUI (37.7 percent) are multifamily housing under the files' primary property type field; offices are next at 340 (14.3 percent).

## Finding 5: In 2025, supermarkets report the highest median intensity of any large type; self-storage the lowest

Median site EUI by primary property type, 2025, for the 15 types with 30 or more buildings with a known EUI (of 2,379 such buildings in total):

- Supermarket/Grocery Store: 157.8 (41 buildings)
- senior living community: 71.2 (35)
- Hotel: 71.1 (102)
- Medical Office: 68.8 (32)
- mixed use property: 67.4 (81)
- Strip Mall: 62.2 (42)
- Manufacturing/Industrial Plant: 61.5 (54; its mean is 87.2, pulled up by high-intensity plants, Finding 6)
- K-12 School: 53.0 (33)
- Office: 52.9 (340)
- Retail Store: 50.6 (59)
- Multifamily Housing: 49.2 (896)
- Worship Facility: 46.2 (50)
- Distribution Center: 33.8 (128)
- Non-Refrigerated Warehouse: 33.3 (171)
- Self-Storage Facility: 9.7 (50)

Type labels reproduce the files' own values, grouped case-insensitively; the casing differences above ("senior living community," "mixed use property") are in the published files. Types under 30 buildings carry their counts wherever this brief prints them: hospitals (general medical and surgical) post a median of 237.0 across only 4 buildings, and the two buildings typed as data centers report 146.0 and 1,271.3 (Finding 6).

Against the 2019 cross-section (all reporters that year, a different building set), the largest types sit lower in 2025: multifamily housing 60.8 in 2019 (746 buildings) against 49.2 in 2025; office 71.1 (317) against 52.9; hotel 84.9 (71) against 71.1; non-refrigerated warehouse 47.8 (134) against 33.3; self-storage 10.7 (45) against 9.7. Supermarkets are the highest-median large type in both years (191.5 in 2019 across 29 buildings, under this project's 30-building flag line that year, against 157.8 across 41 in 2025).

One taxonomy break sits inside the type data: the 2018 file's primary-type field carries assessor-style values - Apartment on 531 rows and Condominium on 300, with only 3 rows carrying Multifamily Housing (all three with a master type of Municipal) - where the surrounding years carry EPA-style values. This brief therefore makes no by-type comparison that includes 2018, and reports the break here rather than harmonizing it silently.

## Finding 6: The highest intensities in 2025 are a data center, two rental-car operations, and an ice plant; the largest energy totals are airport buildings and hospitals

The ten highest reported site EUIs in 2025 are led by:

- 1850 n pearl street, typed DATA CENTER, 53,075 square feet, site EUI 1,271.3 (the higher of the two data-center records; the other reports 146.0).
- hertz rental car, typed vehicle dealership, 27,755 square feet, site EUI 682.4.
- superior farms, typed Manufacturing/Industrial Plant, 45,775 square feet, site EUI 604.0.
- national/enterprise rental car maintenance, 34,468 square feet, site EUI 477.0.
- airport office building, typed mixed use property, 124,511 square feet, site EUI 411.2.

Intensity and total use rank different buildings. The largest reported site energy totals in 2025 are Denver International Airport's Concourse B (304,250,144 kBtu at a site EUI of 138.5 over 2,196,458 square feet) and its terminal building (281,102,852 kBtu, EUI 108.8), followed by two hospitals: AdventHealth Porter (229,800,430 kBtu, EUI 311.3, 735,291 square feet) and HCA HealthONE Presbyterian St. Luke's (223,169,658 kBtu, EUI 250.3). A building can sit near the top of one list and nowhere on the other; the full top-10 lists are in the package's stats file.

As a check on the reported intensities themselves: for 23,816 of the 28,466 building-year records, site energy use and square footage are also reported, and dividing the one by the other reproduces the reported site EUI within max(1.0, 2 percent) for 23,062 of them (96.8 percent). The EUI field and the energy and area fields are internally consistent in the large majority of records; the remaining 3.2 percent are one of the reasons this brief reports medians rather than building-level verdicts.

## Finding 7: The published record carries values that are not plausible as physical intensities, and the brief's method is built around them

- Every year carries a small set of very high reported EUIs: 30 records above 300 in 2016 (3 above 1,000) and 10 above 300 in 2025 (1 above 1,000). The highest value in the ten files is a 2016 record for Packaging Corporation of America (Building ID 1481) reporting a site EUI of 97,144.5 with site energy use of about 26.2 billion kBtu as submitted. The value is internally consistent (energy divided by the reported 269,200 square feet reproduces it), so it is a reporting artifact carried in the published file, not a transcription error by this package. Removing every record above 300 moves the 2016 all-reporters median from 63.3 to 62.6 and the 2025 median from 51.5 to 51.4; the raw 2016 mean (157.1) falls to 72.6 under the same removal, which is why no headline in this brief is a raw mean.
- The 2023 workbook's last row is a test record: Building ID 9999, "test office 1," 123 benchmarking ln, with no square footage and no EUI. It sits in the unknown-EUI remainder of that file and touches no figure, but it is part of the published register's row count of 3,156.
- The table years (2016-2022) store numeric fields as text, with the literal string "None" and empty strings standing in for missing values; the package's parser maps those, zero, and negative values to unknown before any figure is computed (data notes).

## What this might mean

One reading of Finding 1 is that the covered building stock has become less energy-intensive per square foot on a like-for-like basis: the same buildings report median intensities a fifth lower than in 2019, the direction is the same on the weather-normalized field (which removes year-to-year weather from the comparison), and it holds across every large building type in Finding 5. On that reading, the remaining distance to the program's stated aim (a 30 percent reduction in covered-building energy use by 2030 against the 2019 baseline, as the program describes it) would be measured on the program's own aggregate basis, which this brief does not compute; the panel medians here are consistent with movement in that direction and are not the program's measure.

The strongest alternative explanation is utilization, not efficiency. Site EUI divides energy by floor area, not by occupants, operating hours, or output. The window includes the pandemic years, when offices, hotels, and schools emptied; a building that houses fewer people generally uses less energy per square foot without any change to its systems, and the 2020 step in Finding 2 has exactly that shape. The matched panels control for which buildings report, and the weather-normalized panel controls for weather, but no field in these files measures occupancy, so this brief cannot separate intensity reductions that came from building systems from reductions that came from emptier buildings. A second alternative runs through selection: the panels condition on reporting in both years, and consistent reporters (2,084 of 2025's 2,379 known-EUI buildings report in at least five of the ten years) may differ from the buildings that report sporadically or stopped. The deciding evidence would be occupancy or hours data joined at the building level, and an aggregate weather-normalized total on the program's own basis published alongside the registers; neither is in the published files.

## Who can act

- **Denver's Office of Climate Action, Sustainability and Resiliency (CASR)**, which manages Energize Denver compliance and publishes these datasets, controls both the benchmarking register and the performance standard's public reporting. Concrete action: publish, with each year's master dataset, the program-basis aggregate (total weather-normalized site energy for covered buildings against the 2019 baseline) and a matched-panel median of the kind in Finding 1, so the public trend does not have to be reconstructed from registers whose composition changes. Cost class: low-cost operational change (a derived table on an existing publication). Outcome measure: the next master dataset release on the Denver open data Hub carries the aggregate and panel figures, and this brief's Finding 1 can be checked against them dataset-for-dataset.
- **Denver's open data program (Technology Services / DenverGIS)**, publisher of the Hub items, controls the published files' consistency. Concrete action: carry one field schema and one property-type taxonomy across the yearly files (the 2018 type break in Finding 5), store numeric fields as numbers rather than text with "None" strings (Finding 7), and keep test records such as Building ID 9999 out of the published register. Cost class: low-cost operational change. Outcome measure: the next yearly file parses without per-year field mapping, its primary-type values match the other years' taxonomy, and its row count contains no test records.
- **Denver City Council**, in its oversight of the Energize Denver ordinance, controls the performance standard's targets and reporting requirements. Concrete action: when progress against the 2030 target is weighed, weigh it on figures whose building set is held constant (the Finding 1 panels: median -20.5 percent, 2019 to 2025, 1,687 buildings) alongside the program-basis aggregate, and ask CASR for the occupancy caveat in Finding 2 and What this might mean to be addressed with whatever utilization data the program can publish. Cost class: budget decision only insofar as reporting work is funded; the measurement ask itself is a low-cost operational change for CASR. Outcome measure: a progress figure tabled in the oversight process that names its building set, its basis (site or weather-normalized), and its denominator, each checkable against this package's stats file.

## Data notes

- Snapshot and vintage: all figures are from the pull of October 29, 2026. Table years 2016-2022 were pulled in full from their ArcGIS services (server counts and local counts equal for all seven). Workbook years 2023-2025 were downloaded from their Hub items; the 2024 Feature Service item's service URL returns an "Invalid URL" error from the ArcGIS server, so the 2024 Excel item is the usable published source for that year. Each file is titled by its energy year; its internal Reporting Year field reads one year later (the 2022 table's Reporting_Year is 2023 on all 2,914 rows; the 2025 workbook's Reporting Year column reads 2026), because reports are submitted the year after the energy year. Every year in this brief is the dataset (energy) year.
- EUI definition: site EUI in kBtu per square foot, as reported in each year's file. A value is known only if it parses as a number and is greater than zero: the literal strings "None" and "", blank cells, zeros, and negative values map to unknown and are excluded from every EUI denominator, with the unknown count printed alongside (Finding 3). Weather-normalized site EUI is the files' own weather-normalized field, used for the robustness panels in Finding 1 and the second series in Finding 2.
- Field harmonization: field names change across years (building ID appears as Denver_Building_ID, Denver_Building_Id, Building_Id, Building_ID, and "Building ID"; square footage as Master_Square_Footage, Master_Sq_Ft, and "Master Sq Ft"). Fields were matched by normalized column name, never by position; the mapping is in code/build_stats.py and the per-year field lists are in data/pull_log.json.
- Joins: the only join in this package is the matched-panel join on Denver Building ID across yearly files. Building ID is unique within every year (0 duplicate IDs in all 10 files). Match rates: of the 1,337 buildings with a known EUI in 2016, 984 (73.6 percent) also have one in 2025; of the 2,298 in 2019, 1,687 (73.4 percent) do. Unmatched buildings are buildings without a known EUI in the other year (not submitted, exempt, pending, or not in that year's register); they may differ systematically from matched buildings in exactly the way the selection caveat in What this might mean describes, which is why the brief prints the all-reporters series (Finding 2) alongside the panels with the difference between the two stated.
- Small numbers: by-type medians are compared only for types with 30 or more buildings with a known EUI; smaller types are printed only with their counts (hospitals, 4 buildings; data centers, 2). Percentages print their underlying counts throughout. Supermarkets in 2019 (29 buildings) sit under the flag line and are labeled as such where the 2019 figure appears.
- Building type: the files' Primary Property Type (EPA calculated) field, grouped case-insensitively, with display labels reproducing the files' most common casing for each type. The 2018 taxonomy break is reported in Finding 5; 2018 is excluded from every by-type comparison. One 2025 record carries a primary type of "0"; it is counted under Not reported.
- Test record: the 2023 workbook's Building ID 9999 test row (Finding 7) is retained in that file's row count and in the unknown-EUI remainder, and excluded from no count silently: it is one of the 3,156 rows and one of the 250 rows without a known EUI in 2023 (244 with no value, 6 reporting zero).
- Layering test: the master datasets alone support every figure except the scale comparison in Finding 4, for which the parcel register's live count is the added layer; the comparison is a count ratio with its non-join status stated, and no claim in the brief rests on a parcel-level match.
- Reproduction: code/pull_data.py records the full pulls and server counters; code/build_stats.py builds stats.json and data/building_panel.csv; code/audit_section10.py records the pre-flight audit (output in data/audit_output.txt); code/verify_independent.py is the independent recomputation behind verification-ledger-independent.md; code/charts.py draws the charts.

*Machine Readable is a civic data project by Alex Dowlen. Briefs state measured facts from public data, with methods in the open. Corrections are welcome and will be reflected in the repository.*
