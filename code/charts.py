"""Data charts for the Energize Denver benchmarking brief. Brand
palette: dark charcoal background, amber + teal, white text. Every
chart labels its scope and method on the graphic itself. All figures
come from stats.json; no figure from a different scope is juxtaposed
without its label printed on the graphic.
"""
import json, pathlib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

root = pathlib.Path(__file__).resolve().parent.parent
s = json.loads((root / "stats.json").read_text())
BG, AMBER, TEAL, FG = "#1c1c1e", "#e8a33d", "#2a9d8f", "#f2f2f2"
plt.rcParams.update({"figure.facecolor": BG, "axes.facecolor": BG,
                     "text.color": FG, "axes.labelcolor": FG,
                     "xtick.color": FG, "ytick.color": FG,
                     "axes.edgecolor": "#555555", "font.size": 10})
YEARS = [str(y) for y in range(2016, 2026)]

# 1. Median site EUI by year, all reporters with a known EUI in that year
med = [s["per_year"][y]["site_eui"]["median"] for y in YEARS]
wn = [s["per_year"][y]["wn_site_eui_median"] for y in YEARS]
ns = [s["per_year"][y]["eui_known_n"] for y in YEARS]
fig, ax = plt.subplots(figsize=(8.6, 5.0))
ax.plot(YEARS, med, color=AMBER, marker="o", linewidth=2.2, label="Median site EUI")
ax.plot(YEARS, wn, color=TEAL, marker="s", linewidth=1.6, linestyle="--",
        label="Median weather-normalized site EUI")
for x, v in zip(YEARS, med):
    ax.text(x, v + 1.6, f"{v}", ha="center", fontsize=9)
ax.set_ylim(40, 74)
ax.set_ylabel("kBtu per square foot (median, buildings with a known EUI)")
ax.set_xlabel("Energy year (dataset year; reports are submitted the following year)")
ax.legend(loc="lower left", fontsize=8.5, frameon=False)
ax.set_title("Median site EUI by year - all reporters in each year\n"
             "Scope: a different building set each year; reporters with a known EUI:\n"
             + ", ".join(f"{y}: {n:,}" for y, n in zip(YEARS[:5], ns[:5])) + ",\n"
             + ", ".join(f"{y}: {n:,}" for y, n in zip(YEARS[5:], ns[5:])) + "\n"
             "Composition changes year to year; the matched-panel chart holds buildings constant",
             loc="left", fontsize=10)
fig.tight_layout(); fig.savefig(root / "charts" / "chart_median_eui_by_year.png", dpi=200)
plt.close(fig)

# 2. Median site EUI by primary building type, 2025 (types with n >= 30 only)
bt = [(t, v) for t, v in s["by_type"]["2025"].items() if v["n"] >= 30]
bt.sort(key=lambda kv: kv[1]["median"])
fig, ax = plt.subplots(figsize=(8.6, 5.4))
ax.barh([t for t, _ in bt], [v["median"] for _, v in bt], color=TEAL)
for i, (_, v) in enumerate(bt):
    ax.text(v["median"] + 3, i, f"{v['median']}  (n={v['n']:,})", va="center", fontsize=9)
ax.set_xlim(0, 185)
ax.set_xlabel("Median site EUI, kBtu per square foot (2025, buildings with a known EUI)")
ax.set_title("Median site EUI by primary building type, 2025\n"
             "Scope: 2,379 buildings with a known site EUI in the 2025 master dataset;\n"
             "only types with 30 or more buildings are shown (15 types)",
             loc="left", fontsize=10.5)
fig.tight_layout(); fig.savefig(root / "charts" / "chart_eui_by_type_2025.png", dpi=200)
plt.close(fig)

# 3. Matched panels: median site EUI, same buildings in both years
p16, p19 = s["panels"]["2016_2025"], s["panels"]["2019_2025"]
fig, ax = plt.subplots(figsize=(8.6, 5.0))
labels = [f"2016 panel\n(n={p16['n_buildings']:,})", f"2019 panel\n(n={p19['n_buildings']:,})"]
first = [p16["median_eui_2016"], p19["median_eui_2019"]]
second = [p16["median_eui_2025"], p19["median_eui_2025"]]
x = range(2)
w = 0.36
ax.bar([i - w / 2 for i in x], first, width=w, color="#888888",
       label="First year of panel")
ax.bar([i + w / 2 for i in x], second, width=w, color=AMBER, label="2025")
for i, (a, b) in enumerate(zip(first, second)):
    ax.text(i - w / 2, a + 1.5, f"{a}", ha="center", fontsize=10)
    ax.text(i + w / 2, b + 1.5, f"{b}", ha="center", fontsize=10)
ax.set_xticks(list(x)); ax.set_xticklabels(labels)
ax.set_ylim(0, 76)
ax.set_ylabel("Median site EUI, kBtu per square foot")
ax.legend(loc="upper right", fontsize=9, frameon=False)
ax.set_title("Matched panels: median site EUI for the same buildings in both years\n"
             "Scope: buildings with a known site EUI in both years of the panel;\n"
             "73.7% of the 2016 panel and 81.6% of the 2019 panel report a lower EUI in 2025",
             loc="left", fontsize=10.5)
fig.tight_layout(); fig.savefig(root / "charts" / "chart_matched_panels.png", dpi=200)
plt.close(fig)
print("charts written")
