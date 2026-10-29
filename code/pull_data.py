"""Pull the Energize Denver Final Master Datasets, reporting years 2016-2025.

Sources (City and County of Denver open data, opendata-geospatialdenver
Hub, ArcGIS services1 host zdB7qR0BtYrg0Xpl):

- 2016-2022: ArcGIS FeatureServer TABLES (one table per reporting
  year), services ODC__<YEAR>_Final_Master_Dataset. Pulled in full via
  paginated query (returnGeometry=false), saved as raw JSON attribute
  dumps (data/master_<year>_raw.json) exactly as returned - numeric
  fields in these tables are stored as STRINGS, with the literal
  string "None" and empty strings standing in for missing values.
  That is the published form of the data and is preserved here.
- 2023-2025: Microsoft Excel items on the same Hub (no FeatureServer
  table is published for these years; the 2024 Feature Service item's
  service URL returns "Invalid URL" from the ArcGIS server, verified
  2026-10-29, so the Excel item is the usable 2024 source as well).
  Downloaded from the ArcGIS sharing data endpoint, saved as
  data/master_<year>.xlsx, plus a raw cell-value CSV dump
  (data/master_<year>_raw.csv) so standard-library tools can re-read
  the same values.

Year convention (verified in this pull, recorded in the brief): each
dataset is titled by its ENERGY year. Its internal Reporting Year
field reads one year later (the 2022 table's Reporting_Year is 2023;
the 2025 workbook's Reporting Year column is 2026), because reports
are submitted the year after the energy year. All years in this
package are dataset (energy) years.

Pull record in data/pull_log.json; server counts are asserted equal
to local counts for every table year.
"""
import json, pathlib, urllib.parse, urllib.request
from collections import Counter

import openpyxl

ROOT = pathlib.Path(__file__).resolve().parent.parent
HOST = "https://services1.arcgis.com/zdB7qR0BtYrg0Xpl/arcgis/rest/services"
HUB = "https://opendata-geospatialdenver.hub.arcgis.com"
TABLES = {
    2016: ("ODC__2016_Final_Master_Dataset", 11, "78eb671c87f9477884fdd5159958c534"),
    2017: ("ODC__2017_Final_Master_Dataset", 14, "450f3ad8376e44b1b0604511237e8bee"),
    2018: ("ODC__2018_Final_Master_Dataset", 17, "7dabd685c7f14eda9b703c948f571e65"),
    2019: ("ODC__2019_Final_Master_Dataset", 20, "4661245413314c01abbc6bfbf5a261e5"),
    2020: ("ODC__2020_Final_Master_Dataset", 23, "3dce8e1321bf499aac2c67771ec8a5de"),
    2021: ("ODC__2021_Final_Master_Dataset", 26, "274ae79d34c644d3ba0363c01c7ea206"),
    2022: ("ODC__2022_Final_Master_Dataset", 28, "6b200ed29b474f76b53bf4d972b36518"),
}
EXCEL = {
    2023: "2da57c7e046b4daa97daf0052d7e7825",
    2024: "f323917ade9149b3a346b8acf110f8e6",
    2025: "169272beebc54212ac08f3f607bef272",
}
PAGE = 2000


def get(url, params=None):
    if params:
        url = url + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "MachineReadable pull"})
    with urllib.request.urlopen(req, timeout=180) as r:
        return r.read()


def getj(url, params=None):
    return json.loads(get(url, params))


def main():
    data = ROOT / "data"
    data.mkdir(parents=True, exist_ok=True)
    log = {"pull_date": "2026-10-29", "hub": HUB, "years": {}}

    for year, (svc, lid, item) in TABLES.items():
        base = f"{HOST}/{svc}/FeatureServer/{lid}"
        meta = getj(base, {"f": "json"})
        total = getj(base + "/query",
                     {"where": "1=1", "returnCountOnly": "true", "f": "json"})["count"]
        rows, offset = [], 0
        while True:
            d = getj(base + "/query",
                     {"where": "1=1", "outFields": "*", "returnGeometry": "false",
                      "orderByFields": "OBJECTID ASC", "resultOffset": offset,
                      "resultRecordCount": PAGE, "f": "json"})
            batch = [f["attributes"] for f in d.get("features", [])]
            rows.extend(batch)
            if len(batch) < PAGE:
                break
            offset += PAGE
        assert len(rows) == total, (year, len(rows), total)
        (data / f"master_{year}_raw.json").write_text(json.dumps(rows))
        comp_field = next(f["name"] for f in meta["fields"]
                          if f["name"].lower() == "compliance_status")
        log["years"][str(year)] = {
            "kind": "ArcGIS table",
            "service": f"{HOST}/{svc}/FeatureServer/{lid}",
            "hub_item_id": item,
            "server_count": total, "local_count": len(rows),
            "fields": [f["name"] for f in meta["fields"]],
            "compliance_counter": dict(Counter(
                str(r.get(comp_field)) for r in rows).most_common()),
        }
        print(year, "table rows", len(rows))

    for year, item in EXCEL.items():
        url = f"https://www.arcgis.com/sharing/rest/content/items/{item}/data"
        raw = get(url)
        (data / f"master_{year}.xlsx").write_bytes(raw)
        wb = openpyxl.load_workbook(data / f"master_{year}.xlsx",
                                    read_only=True, data_only=True)
        ws = wb[wb.sheetnames[0]]
        rows = list(ws.iter_rows(values_only=True))
        header = [str(h) for h in rows[0]]
        import csv, io
        buf = io.StringIO()
        w = csv.writer(buf)
        w.writerow(header)
        for r in rows[1:]:
            w.writerow(["" if v is None else v for v in r])
        (data / f"master_{year}_raw.csv").write_text(buf.getvalue())
        ci = header.index("Compliance Status")
        log["years"][str(year)] = {
            "kind": "Microsoft Excel (Hub item)",
            "download_url": url,
            "hub_item_id": item,
            "sheet": wb.sheetnames[0],
            "server_count": None, "local_count": len(rows) - 1,
            "fields": header,
            "compliance_counter": dict(Counter(
                str(r[ci]) for r in rows[1:]).most_common()),
        }
        print(year, "excel rows", len(rows) - 1)

    # Context layer for scale only: the city's parcel register count.
    parcels = ("https://services1.arcgis.com/zdB7qR0BtYrg0Xpl/arcgis/rest/"
               "services/ODC_PROP_PARCELS_A/FeatureServer/245")
    log["parcels_context"] = {
        "service": parcels,
        "live_count": getj(parcels + "/query",
                           {"where": "1=1", "returnCountOnly": "true",
                            "f": "json"})["count"],
        "note": "Count only; no parcel records are pulled or joined. "
                "Used for one scale comparison in the brief."}

    (data / "pull_log.json").write_text(json.dumps(log, indent=1))
    print("pull log written")


if __name__ == "__main__":
    main()
