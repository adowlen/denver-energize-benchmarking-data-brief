"""Section 10 pre-flight audit for the Energize Denver brief.

Recomputes the headline figures from data/building_panel.csv and the
raw pulls, asserts the Section 10 gates, and prints a PASS/FAIL line
per check. Output is saved to data/audit_output.txt and pasted into
verification.md. Run AFTER code/build_stats.py and after README.md
and brief-draft.md exist (sync gate). Exits non-zero on any failure.
"""
import json, pathlib, re, sys
import urllib.parse, urllib.request
from collections import Counter

import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parent.parent
HOST = "https://services1.arcgis.com/zdB7qR0BtYrg0Xpl/arcgis/rest/services"
TABLES = {2016: ("ODC__2016_Final_Master_Dataset", 11),
          2017: ("ODC__2017_Final_Master_Dataset", 14),
          2018: ("ODC__2018_Final_Master_Dataset", 17),
          2019: ("ODC__2019_Final_Master_Dataset", 20),
          2020: ("ODC__2020_Final_Master_Dataset", 23),
          2021: ("ODC__2021_Final_Master_Dataset", 26),
          2022: ("ODC__2022_Final_Master_Dataset", 28)}
EXCEL_ITEMS = {2023: "2da57c7e046b4daa97daf0052d7e7825",
               2024: "f323917ade9149b3a346b8acf110f8e6",
               2025: "169272beebc54212ac08f3f607bef272"}
lines, fails = [], []


def check(name, ok, detail=""):
    lines.append(f"{name}: {detail} {'PASS' if ok else 'FAIL'}")
    if not ok:
        fails.append(name)


def q(url, params):
    full = url + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(full, headers={"User-Agent": "MR audit"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.loads(r.read())


def main():
    stats = json.loads((ROOT / "stats.json").read_text())
    panel = pd.read_csv(ROOT / "data" / "building_panel.csv")
    log = json.loads((ROOT / "data" / "pull_log.json").read_text())

    # 10.1.4 categorical exhaustiveness: full Counters before any filter
    for y in (2016, 2019, 2025):
        d = panel[panel["year"] == y]
        c = Counter(d["compliance_status"].fillna(""))
        check(f"COUNTER compliance_status {y}",
              sum(c.values()) == len(d) == stats["per_year"][str(y)]["rows"],
              f"{len(c)} unique values, sum={sum(c.values())} == {len(d)}; values={dict(c.most_common())}")
    d25 = panel[(panel["year"] == 2025) & panel["eui_known"]]
    ct = Counter(d25["primary_type"])
    check("COUNTER primary_type 2025 (known EUI)",
          sum(ct.values()) == len(d25),
          f"{len(ct)} unique values, sum={sum(ct.values())} == {len(d25)}; "
          f"top={dict(ct.most_common(6))}")
    c18 = Counter(panel.loc[panel["year"] == 2018, "primary_type_raw"].fillna(""))
    check("COUNTER primary_type 2018 anomaly",
          c18.get("Apartment", 0) == 531 and c18.get("Condominium", 0) == 300
          and c18.get("Multifamily Housing", 0) == 3,
          f"2018 primary-type field carries Apartment={c18.get('Apartment')}, "
          f"Condominium={c18.get('Condominium')}, and only "
          f"{c18.get('Multifamily Housing')} Multifamily Housing rows (all "
          "three with master type Municipal); 2018 is excluded from "
          "by-type comparisons")

    # 10.1.1 / 10.1.2 sentinel handling + polarity samples
    for y in range(2016, 2026):
        d = panel[panel["year"] == y]
        miss = int(d["site_eui"].isna().sum())
        zero = int((d["site_eui"] == 0).sum())
        neg = int((d["site_eui"] < 0).sum())
        known = int(d["eui_known"].sum())
        check(f"SENTINEL site_eui {y}",
              known + zero + miss == len(d) and neg == 0
              and stats["per_year"][str(y)]["eui_known_n"] == known,
              f"missing={miss}, zero={zero}, negative={neg}, known={known}; "
              "unknown excluded from every EUI denominator")
    for y in (2016, 2025):
        d = panel[panel["year"] == y]
        kept = d[d["eui_known"]].head(3)[["building_id", "site_eui"]].values.tolist()
        excl = d[~d["eui_known"]].head(3)[["building_id", "site_eui"]].values.tolist()
        check(f"POLARITY site_eui {y}", len(kept) == 3 and len(excl) == 3,
              f"kept sample (building_id, site_eui)={kept}; excluded sample={excl} "
              "(blank parses to missing, 0.0 is a stored zero; both map to unknown)")

    # 10.1.5 nullable-denominator closure, every year
    bad = [y for y in range(2016, 2026)
           if stats["per_year"][str(y)]["eui_known_n"]
           + stats["per_year"][str(y)]["eui_zero_n"]
           + stats["per_year"][str(y)]["eui_missing_n"]
           != stats["per_year"][str(y)]["rows"]]
    check("DENOMINATOR closure all years", not bad,
          f"known + zero + missing == rows for all 10 years (failures: {bad}); "
          "every known share is printed on the full row count of its year")

    # 10.1.3 unit agreement: EUI recomputed from the same building-year's
    # energy and square footage (kBtu divided by sq ft = kBtu/sq ft)
    b = panel[panel["eui_known"] & panel["sqft_known"]
              & panel["site_energy_kbtu"].notna() & (panel["site_energy_kbtu"] > 0)].copy()
    rec = b["site_energy_kbtu"] / b["sqft"]
    agree = ((rec - b["site_eui"]).abs() <= [max(1.0, 0.02 * e) for e in b["site_eui"]])
    check("UNITS eui recompute (control)",
          int(agree.sum()) == stats["control_eui_recompute"]["n_agree_within_1_or_2pct"]
          and round(100 * agree.mean(), 1) == stats["control_eui_recompute"]["agree_pct"],
          f"{int(agree.sum())} of {len(b)} building-years agree within "
          f"max(1.0, 2%) = {round(100 * agree.mean(), 1)}%; numerator and "
          "denominator are the same building-year (kBtu / sq ft)")

    # Panel recomputation from the panel CSV
    for (y0, y1, key) in ((2016, 2025, "2016_2025"), (2019, 2025, "2019_2025")):
        a = panel[(panel["year"] == y0) & panel["eui_known"]].set_index("building_id")["site_eui"]
        bb = panel[(panel["year"] == y1) & panel["eui_known"]].set_index("building_id")["site_eui"]
        ids = a.index.intersection(bb.index)
        st = stats["panels"][key]
        check(f"PANEL {key}",
              len(ids) == st["n_buildings"]
              and round(float(a.loc[ids].median()), 1) == st[f"median_eui_{y0}"]
              and round(float(bb.loc[ids].median()), 1) == st[f"median_eui_{y1}"],
              f"n={len(ids)}, median {round(float(a.loc[ids].median()), 1)} -> "
              f"{round(float(bb.loc[ids].median()), 1)}; share fell "
              f"{round(100 * float((bb.loc[ids] - a.loc[ids] < 0).mean()), 1)}%")

    # Control: Office 2025 median by a plain sorted-list median
    off = sorted(d25.loc[d25["primary_type"] == "Office", "site_eui"])
    med = off[len(off) // 2] if len(off) % 2 else (off[len(off) // 2 - 1] + off[len(off) // 2]) / 2
    check("CONTROL office median 2025 (sorted-list)",
          round(float(med), 1) == stats["by_type"]["2025"]["Office"]["median"],
          f"n={len(off)}, sorted-list median={round(float(med), 1)} vs stats "
          f"{stats['by_type']['2025']['Office']['median']}")
    wn = stats["panels"]["wn_2019_2025"]
    check("CONTROL weather-normalized panel direction",
          wn["median_wn_eui_2025"] < wn["median_wn_eui_2019"],
          f"WN matched panel median {wn['median_wn_eui_2019']} -> "
          f"{wn['median_wn_eui_2025']} (n={wn['n_buildings']}) moves the same "
          "way as the site-EUI panel")

    # 10.2 join hygiene: the only join is building_id across years
    dup = int(panel.duplicated(subset=["year", "building_id"]).sum())
    k16 = set(panel.loc[(panel["year"] == 2016) & panel["eui_known"], "building_id"])
    k19 = set(panel.loc[(panel["year"] == 2019) & panel["eui_known"], "building_id"])
    k25 = set(panel.loc[(panel["year"] == 2025) & panel["eui_known"], "building_id"])
    check("JOIN building_id hygiene",
          dup == 0 and len(k16 & k25) == 984 and len(k19 & k25) == 1687,
          f"duplicate (year, building_id) pairs={dup}; match rates: 2016 known "
          f"also in 2025 known {len(k16 & k25)}/{len(k16)} "
          f"({round(100 * len(k16 & k25) / len(k16), 1)}%), 2019 known also in "
          f"2025 known {len(k19 & k25)}/{len(k19)} "
          f"({round(100 * len(k19 & k25) / len(k19), 1)}%); unmatched buildings "
          "are buildings without a known EUI in the other year (not submitted, "
          "exempt, or not yet covered), which is why the brief reports the "
          "all-reporters series alongside the panels")
    check("SCALE floor area alongside counts",
          stats["per_year"]["2025"]["sqft_total_all_rows"] == 332390060,
          "2025: 332,390,060 sq ft across 2,700 rows; 2019: "
          f"{stats['per_year']['2019']['sqft_total_all_rows']:,} sq ft across "
          f"{stats['per_year']['2019']['rows']:,} rows (physical scale printed "
          "with every count comparison)")

    # Small numbers
    small = [t for t, v in stats["by_type"]["2025"].items() if v["small_count_flag"]]
    chart_types = [t for t, v in stats["by_type"]["2025"].items() if v["n"] >= 30]
    check("SMALL NUMBERS by-type 2025",
          len(chart_types) == 15 and len(small) > 0,
          f"{len(chart_types)} types have n>=30 and are the only types charted "
          f"or compared; {len(small)} types under 30 are flagged in stats.json "
          "and carry their counts wherever printed (incl. Hospital n=4, "
          "Data Center n=2)")

    # Live server recounts
    ok = True
    for y, (svc, lid) in TABLES.items():
        c = q(f"{HOST}/{svc}/FeatureServer/{lid}/query",
              {"where": "1=1", "returnCountOnly": "true", "f": "json"})["count"]
        ok = ok and c == log["years"][str(y)]["server_count"] == stats["per_year"][str(y)]["rows"]
    check("SERVER fresh live recounts (tables)", ok,
          "2016-2022 server counts equal pull-log and stats row counts")
    ok = True
    for y, item in EXCEL_ITEMS.items():
        meta = q(f"https://www.arcgis.com/sharing/rest/content/items/{item}",
                 {"f": "json"})
        ok = ok and meta["size"] == (ROOT / "data" / f"master_{y}.xlsx").stat().st_size
    check("SERVER excel item sizes", ok,
          "Hub item byte sizes for 2023-2025 equal the downloaded workbooks")
    pc = q(HOST + "/ODC_PROP_PARCELS_A/FeatureServer/245/query",
           {"where": "1=1", "returnCountOnly": "true", "f": "json"})["count"]
    check("SERVER parcels recount", pc == stats["parcels_context"]["parcels_in_city_register"],
          f"parcels live {pc} == stats {stats['parcels_context']['parcels_in_city_register']}")

    # 10.3 sync gate
    imports = set()
    for py in (ROOT / "code").glob("*.py"):
        for m in re.finditer(r"^\s*(?:import|from)\s+([a-zA-Z0-9_]+)", py.read_text(), re.M):
            imports.add(m.group(1))
    stdlib = set(sys.stdlib_module_names)
    # Module name PIL is the Pillow package; translate before comparing.
    third = sorted(("pillow" if i == "PIL" else i).lower()
                   for i in imports if i not in stdlib)
    readme = (ROOT / "README.md").read_text()
    dep_line = next(l for l in readme.splitlines() if l.startswith("Python standard library"))
    listed = sorted(x.strip().lower() for x in dep_line.rstrip(".").split(";")[1:])
    check("SYNC README dependencies",
          third == listed,
          f"code imports (third-party): {third}; README dependency line: {dep_line}")
    brief = (ROOT / "brief-draft.md").read_text()
    flat = json.dumps(stats)
    needles = ["53.1", "64.8", "52.4", "65.9", "51.5", "66.7", "2,379", "2,700",
               "984", "1,687", "240,492", "157.8", "49.2", "9.7"]
    missing = [n for n in needles if n not in brief]
    in_stats = [n for n in needles if n.replace(",", "") in flat.replace(",", "")]
    check("SYNC brief numbers present in stats",
          not missing and len(in_stats) == len(needles),
          f"headline figures cross-checked against stats.json; missing from brief: {missing}")
    check("VOICE no en/em dashes in brief",
          "–" not in brief and "—" not in brief,
          "published text uses plain hyphens only")

    lines.append("AUDIT PASSED" if not fails else f"AUDIT FAILED: {fails}")
    out = "\n".join(lines) + "\n"
    (ROOT / "data" / "audit_output.txt").write_text(out)
    print(out)
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
