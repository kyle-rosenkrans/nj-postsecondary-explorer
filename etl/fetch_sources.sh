#!/usr/bin/env bash
# Download every NJDOE source file the panel is built from into data/raw/.
# Total ~310 MB; these are NOT committed (see .gitignore).
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p data/raw

ADD="https://www.nj.gov/education/spr/adddata/doc"
SPR="https://www.nj.gov/education/sprreports/download/DataFiles"

echo "-> postsecondary standalone files"
curl -fsSL "$ADD/2023_24_Postsecondary_Enrollment_Rates.xlsx"                    -o data/raw/ps_2023_24.xlsx
curl -fsSL "$ADD/Postsecondary_Enrollment_Rate_Trends_Fall_16month_Rates.xlsx"   -o data/raw/ps_trends.xlsx

echo "-> per-year School Performance Report databases"
for y in 2018-2019 2019-2020 2020-2021 2021-2022 2022-2023 2023-2024; do
  echo "   $y"
  curl -fsSL "$SPR/$y/Database_SchoolDetail.xlsx" -o "data/raw/spr_${y}.xlsx"
done

echo "-> adjusted cohort graduation rate files (graduate counts by student group)"
ACGR="https://www.nj.gov/education/spr/adddata/doc/acgrdocs"
curl -fsSL "$ACGR/ACGR2019_Cohort2019_4-YearAdjustedCohortGraduationRatesByStudentGroup.xlsx"      -o data/raw/acgr_2019.xlsx
curl -fsSL "$ACGR/Cohort2020_4YearAdjustedCohortGraduationRatesandCountsbyStudentGroup.xlsx"       -o data/raw/acgr_2020.xlsx
curl -fsSL "$ACGR/Cohort2021_4YearAdjustedCohortGraduationRatesandCountsbyStudentGroup.xlsx"       -o data/raw/acgr_2021.xlsx
curl -fsSL "$ACGR/Cohort2022_4YearAdjustedCohortGraduationRatesandCountsbyStudentGroup.xlsx"       -o data/raw/acgr_2022.xlsx
curl -fsSL "$ACGR/Cohort2023_4YearAdjustedCohortGraduationRatesbyStudentGroup.xlsx"                -o data/raw/acgr_2023.xlsx
curl -fsSL "$ACGR/Cohort2024_4YearAdjustedCohortGraduationRatesbyStudentGroup.xlsx"                -o data/raw/acgr_2024.xlsx

echo "done. now: python3 etl/build_panel.py && python3 etl/build_html.py"
