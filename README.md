# Denver Building Energy Benchmarking - a Machine Readable data brief

Among the 984 Denver buildings with a reported site EUI in both 2016 and 2025, the median site EUI fell from 64.8 to 53.1 kBtu per square foot (-18.1 percent), and 73.7 percent of the buildings report a lower EUI in 2025. The larger panel of 1,687 buildings reporting in both 2019 (the program baseline year) and 2025 fell from a median of 65.9 to 52.4 (-20.5 percent). Master datasets pulled October 29, 2026. Site EUI is as reported by building representatives through ENERGY STAR Portfolio Manager; it is not a metered measurement by the city.

Part of Machine Readable: https://adowlen.github.io/machine-readable/

## Contents

- brief-draft.md - the brief (publishable text)
- stats.json - every figure used in the brief, produced by code/build_stats.py
- verification.md - Section 10 pre-flight audit record and methods checklist (AUDIT PASSED)
- verification-ledger-independent.md - the independent verifier's recomputation ledger
- reviewer-notes.md - claims most likely challenged, checks not completed, flags
- sources.md - dataset citations and the per-figure source audit
- social-drafts.md - LinkedIn draft (held for a future Friday synthesis under the Friday-only rule; Machine Readable never posts to X)
- hero.png - hero graphic (generated illustration, headline figure composited; added by the parent run from hero_source/hero-brief.md)
- charts/ - chart_median_eui_by_year.png, chart_eui_by_type_2025.png, chart_matched_panels.png
- data/ - master_<year>_raw.json (2016-2022 ArcGIS table pulls), master_<year>.xlsx and master_<year>_raw.csv (2023-2025 Hub Excel items), building_panel.csv (harmonized building-year panel), pull_log.json, audit_output.txt, verify_independent_output.json
- code/ - pull_data.py, build_stats.py, audit_section10.py, verify_independent.py, charts.py, hero_composite.py

## Dependencies (match code imports)

Python standard library; matplotlib; numpy; openpyxl; pandas; Pillow.

## Reuse and citation

Licensed CC-BY-4.0 (see LICENSE). Cite as: Machine Readable, "Denver's benchmarked buildings: median energy intensity down 18 percent since 2016 for the same buildings" (2026), https://github.com/adowlen/denver-energize-benchmarking-data-brief
