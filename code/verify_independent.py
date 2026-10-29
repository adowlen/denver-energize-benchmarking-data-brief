"""Independent verifier for the Energize Denver brief.

Standard library only (json, csv, collections, statistics, pathlib,
urllib). Recomputes the decisive figures from the RAW pulls - the
ArcGIS attribute JSON for 2016-2022 and the raw CSV cell dump of the
Excel workbooks for 2023-2025 - with its own field matching (by
normalized column name), its own number parser, and statistics.median
for medians. It never reads building_panel.csv or any builder output
except stats.json (the comparison target). Live recounts are made
against the ArcGIS services during the verification pass itself.
Output: data/verify_independent_output.json.
"""
import csv, json, pathlib, re, statistics, urllib.parse, urllib.request
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parent.parent
YEARS = list(range(2016, 2026))
MISS = {"", "none", "nan", "n/a", "na", "null"}


def norm(s):
    return re.sub(r"[^a-z0-9]", "", str(s).lower())


def num(v):
    if v is None or isinstance(v, bool):
        return None
    if isinstance(v, (int, float)):
        return float(v) if v == v else None
    s = str(v).strip().replace(",", "")
    if s.lower() in MISS:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def pick(row, prefixes=(), exact=()):
    for k, v in row.items():
        nk = norm(k)
        if nk in exact or any(nk.startswith(p) for p in prefixes):
            return v
    return None


def load(year):
    if year <= 2022:
        rows = json.loads((ROOT / "data" / f"master_{year}_raw.json").read_text())
    else:
        with open(ROOT / "data" / f"master_{year}_raw.csv", newline="",
                  encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
    out = []
    for r in rows:
        bid = num(pick(r, exact=("denverbuildingid", "buildingid")))
        out.append({
            "id": int(bid) if bid is not None else None,
            "eui": num(pick(r, ("siteeui",))),
            "energy": num(pick(r, ("siteenergyuse",))),
            "sqft": num(pick(r, exact=("mastersquarefootage", "mastersqft"))),
            "type": str(pick(r, ("primarypropertytype",)) or "").strip(),
            "comp": str(pick(r, exact=("compliancestatus",)) or "").strip(),
        })
    return out


def med(vals):
    return round(statistics.median(vals), 1)


def main():
    stats = json.loads((ROOT / "stats.json").read_text())
    data = {y: load(y) for y in YEARS}
    checks = {}

    def chk(name, builder, mine, tol=0.0):
        ok = (builder == mine) if tol == 0 else abs(builder - mine) <= tol
        checks[name] = {"builder": builder, "independent": mine, "ok": bool(ok)}

    for y in YEARS:
        rows = data[y]
        known = [r["eui"] for r in rows if r["eui"] is not None and r["eui"] > 0]
        chk(f"rows_{y}", stats["per_year"][str(y)]["rows"], len(rows))
        chk(f"known_{y}", stats["per_year"][str(y)]["eui_known_n"], len(known))
        chk(f"median_{y}", stats["per_year"][str(y)]["site_eui"]["median"],
            med(known), tol=0.11)

    def panel(y0, y1, key):
        a = {r["id"]: r["eui"] for r in data[y0]
             if r["id"] is not None and r["eui"] is not None and r["eui"] > 0}
        b = {r["id"]: r["eui"] for r in data[y1]
             if r["id"] is not None and r["eui"] is not None and r["eui"] > 0}
        ids = sorted(set(a) & set(b))
        ea = [a[i] for i in ids]
        eb = [b[i] for i in ids]
        st = stats["panels"][key]
        chk(f"panel_{key}_n", st["n_buildings"], len(ids))
        chk(f"panel_{key}_median_{y0}", st[f"median_eui_{y0}"], med(ea), tol=0.11)
        chk(f"panel_{key}_median_{y1}", st[f"median_eui_{y1}"], med(eb), tol=0.11)
        fell = sum(1 for x, yv in zip(ea, eb) if yv < x)
        chk(f"panel_{key}_share_fell", st["share_buildings_eui_fell_pct"],
            round(100 * fell / len(ids), 1), tol=0.11)

    panel(2016, 2025, "2016_2025")
    panel(2019, 2025, "2019_2025")

    # By-type 2025 medians for every type with n >= 30 (builder grouping
    # is case-insensitive; group here on casefold and compare)
    casing = {}
    alltypes = Counter()
    for y in YEARS:
        for r in data[y]:
            if r["type"]:
                alltypes[(r["type"].casefold(), r["type"])] += 1
    disp = {}
    for (cf, raw), _ in alltypes.most_common():
        disp.setdefault(cf, raw)
    groups = defaultdict(list)
    for r in data[2025]:
        if r["eui"] is not None and r["eui"] > 0:
            key = disp.get(r["type"].casefold(), "Not reported") if r["type"] else "Not reported"
            groups[key].append(r["eui"])
    n_type_checks = 0
    for t, vals in groups.items():
        if len(vals) >= 30 and t in stats["by_type"]["2025"]:
            chk(f"type2025_{t}", stats["by_type"]["2025"][t]["median"],
                med(vals), tol=0.11)
            n_type_checks += 1
    checks["type2025_groups_compared"] = {"builder": 15, "independent": n_type_checks,
                                          "ok": n_type_checks == 15}

    # Control: energy / sq ft recomputation agreement (all years pooled)
    tot, agree = 0, 0
    for y in YEARS:
        for r in data[y]:
            if (r["eui"] and r["eui"] > 0 and r["sqft"] and r["sqft"] > 0
                    and r["energy"] and r["energy"] > 0):
                tot += 1
                if abs(r["energy"] / r["sqft"] - r["eui"]) <= max(1.0, 0.02 * r["eui"]):
                    agree += 1
    chk("control_recompute_n", stats["control_eui_recompute"]["n_checked"], tot)
    chk("control_recompute_pct", stats["control_eui_recompute"]["agree_pct"],
        round(100 * agree / tot, 1), tol=0.11)

    chk("compliance_2025_counter",
        stats["per_year"]["2025"]["compliance_counter"],
        dict(Counter(r["comp"] for r in data[2025]).most_common()))
    chk("distinct_buildings", stats["distinct_buildings_all_years"],
        len({r["id"] for y in YEARS for r in data[y] if r["id"] is not None}))
    chk("sqft_total_2025", stats["per_year"]["2025"]["sqft_total_all_rows"],
        int(sum(r["sqft"] for r in data[2025] if r["sqft"] and r["sqft"] > 0)))
    top = max((r for r in data[2025] if r["eui"] and r["eui"] > 0),
              key=lambda r: r["eui"])
    chk("top_eui_2025_id", stats["top_buildings_2025_by_eui"][0]["building_id"], top["id"])
    chk("top_eui_2025_value", stats["top_buildings_2025_by_eui"][0]["site_eui"],
        top["eui"], tol=0.11)

    # Fresh live recounts (table years + parcels)
    def q(url, params):
        full = url + "?" + urllib.parse.urlencode(params)
        req = urllib.request.Request(full, headers={"User-Agent": "MR verifier"})
        with urllib.request.urlopen(req, timeout=90) as r:
            return json.loads(r.read())

    host = "https://services1.arcgis.com/zdB7qR0BtYrg0Xpl/arcgis/rest/services"
    svc = {2016: ("ODC__2016_Final_Master_Dataset", 11),
           2019: ("ODC__2019_Final_Master_Dataset", 20),
           2022: ("ODC__2022_Final_Master_Dataset", 28)}
    for y, (s, lid) in svc.items():
        c = q(f"{host}/{s}/FeatureServer/{lid}/query",
              {"where": "1=1", "returnCountOnly": "true", "f": "json"})["count"]
        chk(f"live_count_{y}", stats["per_year"][str(y)]["rows"], c)
    pc = q(host + "/ODC_PROP_PARCELS_A/FeatureServer/245/query",
           {"where": "1=1", "returnCountOnly": "true", "f": "json"})["count"]
    chk("live_parcels", stats["parcels_context"]["parcels_in_city_register"], pc)

    n_ok = sum(1 for v in checks.values() if v["ok"])
    out = {"checks": checks, "n_checks": len(checks), "n_ok": n_ok,
           "all_ok": n_ok == len(checks)}
    (ROOT / "data" / "verify_independent_output.json").write_text(
        json.dumps(out, indent=1))
    print(f"{n_ok}/{len(checks)} checks OK")
    for k, v in checks.items():
        if not v["ok"]:
            print("MISMATCH", k, v)


if __name__ == "__main__":
    main()
