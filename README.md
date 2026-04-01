# 🍛 The Flavours of India — A Data Storytelling Project

> *"What do 255 Indian dishes, 365 ingredients, and 25 states tell us about how India eats?"*

An interactive **Tableau data story** exploring the patterns behind Indian cuisine — from regional ingredient identity to how quickly different states cook their food.

📊 **[View on Tableau Public](#)** ← *replace with your Tableau Public link after publishing*

---

## The Story in 4 Acts

**Act 1 — The Map:** India doesn't have one cuisine. It has six regional ones, each shaped by climate, religion, and trade history. The North cooks slow and rich; the South cooks fast and fiery.

**Act 2 — The Ingredients:** Sugar appears in 48 dishes. Ginger in 29. Garam masala in 27. Behind every regional identity is a fingerprint of shared ingredients — and a few surprising ones that cross every border.

**Act 3 — The Time:** 88% of dishes are vegetarian. Yet non-vegetarian dishes take significantly longer to prepare. And a handful of dishes clock in under 10 minutes total — snacks that feed millions daily.

**Act 4 — The Flavour:** Spice isn't just heat. The data shows that sweet, bitter, and sour profiles cluster regionally in ways that mirror India's agricultural zones — jaggery in the West, tamarind in the South, mustard in the East.

---

## Dashboard Previews

### 📊 Tableau Dashboards
> *Screenshots coming — open the `.twbx` file in Tableau Desktop or Tableau Public to explore interactively.*

| Dashboard | Description |
|-----------|-------------|
| `screenshots/tableau/01_overview_dashboard.png` | Full overview KPI dashboard |
| `screenshots/tableau/02_regional_map.png` | Choropleth map of dishes by state |
| `screenshots/tableau/03_ingredient_treemap.png` | Treemap of ingredient frequency |
| `screenshots/tableau/04_flavor_kpi.png` | Flavor profile KPI cards |
| `screenshots/tableau/05_time_analysis.png` | Prep vs cook time scatter |

---

### 📈 Python Chart Recreations

Key insights recreated in Python from the same dataset:

**Dishes by Region**
![Regional Distribution](screenshots/python-charts/01_regional_distribution.png)

**Top 15 Most-Used Ingredients**
![Top Ingredients](screenshots/python-charts/02_top_ingredients.png)

**Flavor Profiles Across Regions**
![Flavor by Region](screenshots/python-charts/03_flavor_by_region.png)

**Prep Time vs Cook Time**
![Prep vs Cook](screenshots/python-charts/04_prep_vs_cook_time.png)

**Vegetarian vs Non-Vegetarian Split**
![Diet Split](screenshots/python-charts/05_diet_split.png)

**Course Types Across Regions**
![Course by Region](screenshots/python-charts/06_course_by_region.png)

**Top 10 Quickest Dishes**
![Quickest Dishes](screenshots/python-charts/07_quickest_dishes.png)

---

## Dataset

**File:** `data/final_ingredient_analysis.csv`

| Field | Description |
|-------|-------------|
| `name` | Dish name |
| `diet` | `vegetarian` / `non vegetarian` |
| `prep_time` | Preparation time (minutes) |
| `cook_time` | Cooking time (minutes) |
| `clean_total_time` | Total time (minutes) |
| `flavor_profile` | `spicy` / `sweet` / `bitter` / `sour` |
| `course` | `main course` / `dessert` / `snack` / `starter` |
| `state` | Indian state of origin |
| `region` | Aggregated region (North / South / East / West / Central / North East) |
| `individual_ingredient` | One ingredient per row (long format) |
| `shift_category` | Cook-time tier (Quick / Standard / Long) |

**Quick stats:**
- 255 unique dishes across 25 states
- 365 unique ingredients
- 88% vegetarian
- Average total cook time: 65 minutes
- Most-used ingredient: Sugar (48 dishes)

---

## Project Structure

```
├── Prasad_Watane_DA2.twbx              # Tableau workbook (open in Tableau Desktop/Public)
├── data/
│   └── final_ingredient_analysis.csv   # Source dataset
├── screenshots/
│   ├── tableau/                        # Add your Tableau screenshots here
│   │   ├── 01_overview_dashboard.png
│   │   ├── 02_regional_map.png
│   │   ├── 03_ingredient_treemap.png
│   │   ├── 04_flavor_kpi.png
│   │   └── 05_time_analysis.png
│   └── python-charts/                  # Auto-generated Python chart exports
│       ├── 01_regional_distribution.png
│       ├── 02_top_ingredients.png
│       ├── 03_flavor_by_region.png
│       ├── 04_prep_vs_cook_time.png
│       ├── 05_diet_split.png
│       ├── 06_course_by_region.png
│       └── 07_quickest_dishes.png
└── generate_charts.py                  # Script to regenerate Python charts
```

---

## How to Open the Tableau Workbook

1. Download and install [Tableau Public](https://public.tableau.com/en-us/s/download) (free)
2. Open `Prasad_Watane_DA2.twbx` — the data is embedded, no separate file needed
3. Explore the 30+ worksheets or publish to your Tableau Public profile

To regenerate the Python charts:

```bash
pip install matplotlib seaborn pandas
python generate_charts.py
```

---

## Key Findings

- **South India** leads in total dish count, with a strong dominance of spicy and sour flavor profiles
- **North India** has the highest proportion of slow-cooked dishes (60+ minutes)
- **Sugar** is the single most cross-regional ingredient — appearing in desserts from every region
- **Vegetarian dishes** account for 88% of the dataset, yet show greater flavor diversity than non-vegetarian ones
- The **North East** has the most distinct ingredient profile — fewest overlapping ingredients with other regions
- **Snacks** are the fastest course category, averaging under 40 minutes total time

---

## Tools Used

| Tool | Purpose |
|------|---------|
| Tableau Desktop / Public | Interactive dashboards and storytelling |
| Python (pandas, matplotlib, seaborn) | Exploratory analysis and static chart exports |
| Microsoft Excel | Initial data cleaning and bucketing |

---

## Author

**Prasad Watane**
Data Visualisation & Storytelling Portfolio Project
