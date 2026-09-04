# NJ Postsecondary Enrollment Explorer

A self-contained explorer for New Jersey postsecondary (college) enrollment rates —
every high school in the state, classes of 2016 through 2024.

**Current build:** `Postsecondary_Explorer.html` (~2 MB). Just double-click it.
All data is baked into the file; it works offline, with no server and no CDN.

**Live tool:** https://kyle-rosenkrans.github.io/nj-postsecondary-explorer/ — open it in any browser, or share that link.

A **class of 2024** graduated at the end of the **2023–24 school year**, so the nine
cohorts here cover school years **2015–16 through 2023–24**.

## What it does

Five views, sharing one filter bar (class year · fall vs 16-month · **enrolled in any / 4-year /
2-year** · city · sector · search):

- **KIPP overview** — stat tiles for TEAM Academy (Newark) and KIPP: Cooper Norcross
  (Camden) against New Jersey, their home district, and their own prior class; a nine-year
  trend line against Newark Public Schools, Camden City, Paterson Public Schools and the
  state; and a per-city breakdown where Newark, Camden and Paterson each get their own
  ranked list (toggle any city on or off), with the KIPP schools highlighted against the
  other high schools in that same city.
- **Trends** — pick up to eight schools or districts and chart them over the nine cohorts,
  plus a diverging chart of change since each school's first reported class.
- **Demographics** — enrollment by student group for any school and class, each bar carrying its
  graduate count, with the school's all-student rate as a reference line; the 2-year/4-year,
  public/private and in-state/out-of-state mix; one group tracked over time; and within-school gaps.
- **Compare schools** — sortable table of every high school matching the filters, with both
  measures, graduate counts, gap to the state, change since first reported class and a sparkline. Click a row for a
  full profile.
- **Notes & method** — sources, the range methodology, cohort labelling, and coverage gaps.

### Filters
- **Enrolled in** — any institution, 4-year only, or 2-year only. Switching this re-expresses every
  rate in every view (see the derivation note below).
- **City** — Newark, Camden, Paterson, all three at once, or all New Jersey. City is the
  school's own mailing city from the NJDOE directory, so charters and county vocational
  campuses sit in the city they are physically in, not their chartering county.
- **Sector** — District, Charter, Renaissance (the three Camden Urban Hope Act projects) and
  County vocational.

## Data notes that matter

**2-year and 4-year rates are derived.** NJDOE publishes the overall rate as a share of *graduates*,
then the 2-year and 4-year figures as shares of the students who *enrolled*. The "enrolled in" filter
multiplies the two, so a school where 60% of graduates enrolled anywhere and 80% of those chose a
4-year institution reads as 48% of graduates enrolled in a 4-year institution. Both factors come from
one source row, so the result is internally consistent. Validated against NJDOE's own graduate-based
2-year/4-year figures (published in the pre-2022 SPR summary sheets) across 7,412 cells — worst
discrepancy 0.12 points, i.e. rounding. Because a student who attended both a 2-year and a 4-year
institution is counted in both, the two derived rates can sum to slightly more than the
all-institutions rate. The split is published only in the per-year student-group files, so switching
off "any institution" covers schools in all nine classes but districts only from the class of 2024.

**Graduate counts ("n") come from a different file, and are not the exact denominator.** The
postsecondary files publish percentages only — no counts, in any year, at any level. The counts shown
throughout come from NJDOE's **4-year Adjusted Cohort Graduation Rate** report for the same class,
which publishes graduates by school, class and student group. That is the closest published measure of
how many students a rate rests on, but the definitions differ: ACGR counts graduates of the four-year
adjusted cohort, while the postsecondary denominator is graduates as reported by the district, which
can include students outside that cohort. Across all 39,320 cells where both files report, they agree
on the fewer-than-10 privacy threshold 94.0% of the time; in 5.3% the postsecondary file suppresses a
group while the graduation file shows 10 or more (concentrated in the earliest classes), and in 0.4%
the reverse. **Read the count as the scale of the group, not as an exact denominator** — don't
recompute a numerator from it.

**Two series, deliberately.** NJDOE restates earlier cohorts as Clearinghouse matching
improves, so the same school and class can carry two slightly different published values.
Headline rates (tiles, tables, trend lines) come from NJDOE's restated trend file — the
consistent series, and the only one covering districts in every year. Student-group rates
come from each year's own SPR release, the only place they are published. Read group
figures against that same file's all-student row, which is the reference line on the chart.

**Ranges.** From the class of 2023 NJDOE publishes a range, because a small share of
graduates cannot be matched. The lower bound is the share actually matched; the upper bound
is that count over 97% of the cohort (mechanically, lower ÷ 0.97). **The tool shows the
lower bound everywhere** — the only figure published on a consistent basis across all nine
cohorts. Where NJDOE published a range, the full range appears in tooltips and on the
overview tiles.

**Cohort labelling — a trap in the source files.** The per-year SPR workbooks label their
postsecondary *summary* sheet with a `ClassYear` that is the **start** year of the school
year, so the 2018–19 file reads `2018` for what is really the class of 2019. The
student-group sheets carry no year label at all. Rather than trust the label, each file's
sheets were matched value-by-value against NJDOE's own published trend series across every
school in the state. Each file's group sheets align with the class that graduated *that*
school year and with no other cohort (median absolute difference 0.1–0.3 points on the
16-month measure; the 2022–23 file matches to the tenth on 100% of schools). See the
docstring in `etl/build_panel.py`.

**Suppression.** `N` means no graduating cohort that year; `*` means fewer than 10
graduates and NJDOE withheld the value. The tool keeps these distinct and never shows one
as the other. KIPP Cooper Norcross graduated its first Camden high-school class in 2024,
which is why its earlier cohorts read "no graduates".

**Known gaps.** Classes 2016–2018 are school-level only and predate NJDOE's restated trend file, so their headline rate is the original student-group figure and district/state trend lines begin at 2019. The class of 2016 has the 16-month measure only, so fall trend lines begin at 2017. Graduate counts run 2019–2024. District-level *group* cuts exist for the class of 2024 only (district trend lines run 2019 on). Gender, homelessness, foster care, military-connected and migrant
groups begin with the class of 2022. Statewide *by group* is class of 2024 only. The
**2-year/4-year split is published for every class and both measures**; public/private and
in-state/out-of-state are 16-month-only before the class of 2024. NJDOE suppresses some
graduate counts for small groups, so a few rates appear with no count.

The tool contains no student-level data and no personally identifiable information — only
NJDOE's published school- and district-level aggregates.

## Sources

Both from the NJ Department of Education School Performance Reports:

- [Additional data files](https://www.nj.gov/education/spr/adddata/) —
  `2023_24_Postsecondary_Enrollment_Rates.xlsx` (class of 2024 by student group) and
  `Postsecondary_Enrollment_Rate_Trends_Fall_16month_Rates.xlsx` (classes 2019–2023 trend).
- [Adjusted Cohort Graduation Rate reports](https://www.nj.gov/education/spr/adddata/acgr.shtml) —
  the 4-year cohort file for each class 2019–2024, the source of the graduate counts. File naming is
  inconsistent across years (`...RatesandCountsbyStudentGroup` vs `...RatesbyStudentGroup`) and
  cohort 2019 uses a different column layout, so `etl/fetch_sources.sh` pins each URL and
  `etl/build_panel.py` carries a per-year column map.
- [Downloadable data](https://www.nj.gov/education/spr/download/) — the per-year
  `Database_SchoolDetail.xlsx` (2015–16 onward; older files use different sheet/column layouts, handled in `build_panel.py`) for 2018–19 through 2023–24, sheets
  `PostsecondaryEnrRatesFall`, `PostsecondaryEnrRates16mos`, and `Header and Contact`
  (city, grade span). The 2023–24 database's postsecondary sheets ship empty, which is why
  the standalone class-of-2024 file is needed.

## Pipeline (reproducible)

```bash
bash   etl/fetch_sources.sh     # NJDOE .xlsx -> data/raw/  (~310 MB, not committed)
python3 etl/build_panel.py      # data/raw/   -> data/panel.json  (~2 MB, committed)
python3 etl/build_html.py       # panel.json + app/template.html -> Postsecondary_Explorer.html
```

Only `openpyxl` is required. Edit the UI in `app/template.html` (the `__PANEL_JSON__`
placeholder is where the data is injected) and re-run `build_html.py`.

`data/panel.json` is committed so the tool can be rebuilt without re-downloading 310 MB of
source workbooks.

## Refreshing for a new year

When NJDOE posts the next class:

1. Add the new year to the loop in `etl/fetch_sources.sh`.
2. In `etl/build_panel.py`, append the year to `SPR_FILES` (or point at the new standalone
   postsecondary file) and add the class to `CLASSES`.
3. **Re-verify the cohort mapping** before trusting it — the class-year alignment is
   empirical, not documented by NJDOE, and the label in the summary sheet is off by one.
4. Rebuild and re-run the audit against the raw files.

## Accessibility

Light and dark themes (system default, with a toggle). Categorical colours are the
validated eight-slot palette, assigned per entity so filtering never repaints a series;
every chart carries a legend or direct labels plus a hover tooltip, and the Compare table is
a full text view of the same numbers.
