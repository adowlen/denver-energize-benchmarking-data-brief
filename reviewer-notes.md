# Reviewer notes - Energize Denver benchmarking brief (2026-10-29)

Package state: brief-draft.md, stats.json, the harmonized panel,
and charts are final and in sync; Section 10 audit PASSED on the
final build (after a two-line fix loop, recorded in
verification.md); independent verification reproduced every
decisive figure, including both matched panels exactly, with zero
corrections (65 of 65 checks). Hero: the story illustration was
generated during the build (hero_source/, inspected, on-brief);
the morning QA run composited hero.png on 2026-10-29 per
hero_source/hero-brief.md (headline figure "53.1 vs 64.8" with
scope and source lines printed on the graphic) and inspected the
composite - fully legible on its scrim, scene tells the story.
QA update 2026-10-29: hero gate closed.

## Claims most likely to be challenged

1. The headline (-18.1 percent panel median, 2016 to 2025) rests
   on as-reported data. A challenger can correctly note that
   Portfolio Manager submissions are self-reported and largely
   unaudited at the building level, and that the files carry
   implausible values (Finding 7). The package's defenses are
   printed in the brief: the internal-consistency control (96.8
   percent of building-years reproduce their EUI from their own
   energy and area), the median's insensitivity to the outliers
   (excluding every EUI above 300 moves the 2025 median by 0.1),
   and the weather-normalized panel agreeing. If QA wants a
   harder line, Finding 7 can be promoted into the opening
   caveats; it is already summarized there.
2. Utilization versus efficiency. The brief names this as the
   strongest alternative and does not resolve it, because no
   occupancy field exists. Any summary that converts the panel
   finding into an efficiency claim overstates the package. The
   social draft was written to avoid that conversion; keep it
   that way in the Friday synthesis.
3. Panel selection. The panels condition on reporting in both
   years (match rates 73.6 and 73.4 percent, above the project's
   flag line). The unmatched buildings are characterized (no
   known EUI in the other year) and the all-reporters series is
   printed alongside, but a challenger with the register could
   test whether sporadic reporters trend differently; the brief
   concedes the possibility in What this might mean.
4. The 2023-to-2025 register shrinkage (3,156 to 2,700 rows) is
   reported without a mechanism, because the files do not state
   one. If CASR's published counts for those years differ from
   the file row counts (for example because the register counts
   covered buildings differently from file rows), Finding 3 is
   the figure to correct first; it is phrased as a property of
   the files ("the 2025 register is the smallest since 2016")
   rather than of the program.
5. The 2019-baseline framing. Finding 1 notes the program sets
   targets against a 2019 baseline, and the 2019 panel falls
   20.5 percent. These two facts must not be merged into a
   progress-to-target claim: the program's measure is an
   aggregate on its own basis, which the brief explicitly does
   not compute. The Who can act section asks CASR to publish
   that aggregate precisely so the distinction can be closed
   with data.

## Dataset-quality items, and whom they reflect on (Section 11.3)

- The published files store numbers as text with "None" string
  sentinels (2016-2022), carry a test record in the 2023 register
  (Building ID 9999), use a different property-type taxonomy in
  2018, change compliance vocabulary mid-window, and include
  reported values that are not plausible as physical intensities
  (up to 97,144.5). These are properties of the City and County
  of Denver's published benchmarking datasets (CASR program,
  DenverGIS publication). The brief reports them as measured
  facts about the files and addresses the fix to CASR and the
  open data program in Who can act. This touches a named city
  office, so it is flagged here for extra care; the brief's
  language stays at the published record's contents and makes
  no claim about internal practice.
- The 2024 Feature Service item on the Hub points at a service
  URL the ArcGIS server rejects. The Excel item is used instead
  and the substitution is disclosed in the data notes and
  sources.

## Checks not completed

- Program-basis aggregate (total weather-normalized energy
  against the 2019 baseline): not computed. The files carry the
  inputs, but the program's exact aggregation rules (which
  buildings, which adjustments) are not fully specified in the
  published material available to this package, and an
  approximation presented as the program's measure would be
  worse than none. Finding 1 and Who can act state this openly.
- Occupancy adjustment: impossible from the published files (no
  occupancy, hours, or output field). This is the brief's
  governing limit, printed in the opening caveats and in What
  this might mean.
- Building-to-parcel join: deliberately not performed. A master
  dataset row is a Portfolio Manager building, which does not
  map one-to-one onto parcels; Finding 4 uses the parcel count
  for scale only and says so. A defensible join would need the
  assessor's building records and is a stack project, not a
  brief figure.
- ENERGY STAR Score, GHG, and fuel-mix fields: inspected and
  not used (recorded in sources.md); no claim needed them.
- No verification of any individual building's submission was
  performed; named buildings in Finding 6 are reported as the
  files state them, with the as-reported caveat governing the
  whole brief.

## Surprises worth knowing

- The all-reporters median rose into 2019 (66.7, the window peak)
  before falling: on a like-for-like panel the fall from 2019 is
  larger than the fall from 2016, because 2016's smaller,
  larger-building cohort started lower (panel medians 64.8 in
  2016 against 65.9 in 2019).
- Reporting quality rose steadily (known-EUI share 73.3 percent
  in 2016 to 92.1 percent in 2023) even as the register then
  shrank by 456 rows in two years.
- Four rows labeled "exempt" in 2025 carry a known EUI, and 69 of
  96 "pending revisions" rows do: the compliance label and the
  presence of usable data are close but not identical, which is
  why the brief measures reporting by the data.
- The single highest-EUI record in 2025 is a data center (the
  type with n=2), and the two largest energy totals in the city
  are airport buildings whose EUIs are unremarkable: the
  intensity list and the totals list share almost no names.
