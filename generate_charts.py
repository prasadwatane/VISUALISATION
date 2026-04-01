import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec
import numpy as np

# ── Palette ────────────────────────────────────────────────────────────────────
SAFFRON   = "#FF9933"
GREEN     = "#138808"
NAVY      = "#000080"
GOLD      = "#FFB347"
ROSE      = "#E85D75"
TEAL      = "#2BBFB0"
PURPLE    = "#9B59B6"
WARM_BG   = "#FDF6EC"
CARD_BG   = "#FFFFFF"

REGION_COLORS = {
    "North":      "#FF9933",
    "South":      "#138808",
    "East":       "#2BBFB0",
    "West":       "#E85D75",
    "North East": "#9B59B6",
    "Central":    "#FFB347",
}

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.facecolor": WARM_BG,
    "axes.facecolor": CARD_BG,
})

df = pd.read_csv("/home/claude/data.csv")
df_dishes = df.drop_duplicates(subset="name")
df_clean  = df[~df["region"].isin(["-1", None]) & df["region"].notna()]
df_dishes_clean = df_clean.drop_duplicates(subset="name")

OUT = "/home/claude/fairlend/screenshots/python-charts"


# ── 1. Regional Distribution ───────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 5), facecolor=WARM_BG)
ax.set_facecolor(CARD_BG)

region_counts = df_dishes_clean["region"].value_counts()
colors = [REGION_COLORS.get(r, GOLD) for r in region_counts.index]
bars = ax.barh(region_counts.index, region_counts.values, color=colors,
               edgecolor="white", linewidth=1.5, height=0.6)

for bar, val in zip(bars, region_counts.values):
    ax.text(val + 0.5, bar.get_y() + bar.get_height()/2,
            str(val), va="center", fontsize=12, fontweight="bold", color="#333")

ax.set_xlabel("Number of Dishes", fontsize=12, color="#555")
ax.set_title("🗺️  Dishes by Region", fontsize=16, fontweight="bold", pad=15, color="#222")
ax.tick_params(axis="y", labelsize=12)
ax.tick_params(axis="x", labelsize=10)
ax.set_xlim(0, region_counts.max() + 12)
fig.tight_layout(pad=2)
fig.savefig(f"{OUT}/01_regional_distribution.png", dpi=150, bbox_inches="tight")
plt.close()
print("✓ Chart 1: Regional distribution")


# ── 2. Top 15 Ingredients ──────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6), facecolor=WARM_BG)
ax.set_facecolor(CARD_BG)

top_ing = df["individual_ingredient"].value_counts().head(15)
gradient = plt.cm.YlOrRd(np.linspace(0.35, 0.85, len(top_ing)))
bars = ax.barh(top_ing.index[::-1], top_ing.values[::-1],
               color=gradient[::-1], edgecolor="white", linewidth=1.2, height=0.65)

for bar, val in zip(bars, top_ing.values[::-1]):
    ax.text(val + 0.3, bar.get_y() + bar.get_height()/2,
            str(val), va="center", fontsize=10, fontweight="bold", color="#333")

ax.set_xlabel("Frequency across dishes", fontsize=11, color="#555")
ax.set_title("🌶️  Top 15 Most-Used Ingredients", fontsize=16, fontweight="bold", pad=15, color="#222")
ax.set_xlim(0, top_ing.max() + 8)
fig.tight_layout(pad=2)
fig.savefig(f"{OUT}/02_top_ingredients.png", dpi=150, bbox_inches="tight")
plt.close()
print("✓ Chart 2: Top ingredients")


# ── 3. Flavor Profile by Region ───────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(11, 5.5), facecolor=WARM_BG)
ax.set_facecolor(CARD_BG)

flavor_region = (df_dishes_clean[df_dishes_clean["flavor_profile"] != "-1"]
                 .groupby(["region", "flavor_profile"])
                 .size().unstack(fill_value=0))

flavor_colors = {
    "spicy":  SAFFRON,
    "sweet":  ROSE,
    "bitter": TEAL,
    "sour":   GREEN,
}
flavor_region.plot(kind="bar", ax=ax, color=[flavor_colors.get(c, GOLD) for c in flavor_region.columns],
                   edgecolor="white", linewidth=1.2, width=0.7)

ax.set_xlabel("")
ax.set_title("🎨  Flavor Profiles Across Regions", fontsize=16, fontweight="bold", pad=15, color="#222")
ax.set_xticklabels(flavor_region.index, rotation=30, ha="right", fontsize=11)
ax.legend(title="Flavor", bbox_to_anchor=(1.01, 1), loc="upper left", fontsize=10)
ax.set_ylabel("Number of Dishes", fontsize=11, color="#555")
fig.tight_layout(pad=2)
fig.savefig(f"{OUT}/03_flavor_by_region.png", dpi=150, bbox_inches="tight")
plt.close()
print("✓ Chart 3: Flavor by region")


# ── 4. Prep Time vs Cook Time ──────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 6), facecolor=WARM_BG)
ax.set_facecolor(CARD_BG)

scatter_df = df_dishes_clean.copy()
region_list = scatter_df["region"].unique()
for region in region_list:
    subset = scatter_df[scatter_df["region"] == region]
    ax.scatter(subset["prep_time"], subset["cook_time"],
               color=REGION_COLORS.get(region, GOLD),
               alpha=0.7, s=60, label=region, edgecolors="white", linewidth=0.5)

ax.set_xlabel("Prep Time (mins)", fontsize=12, color="#555")
ax.set_ylabel("Cook Time (mins)", fontsize=12, color="#555")
ax.set_title("⏱️  Prep Time vs Cook Time by Region", fontsize=16, fontweight="bold", pad=15, color="#222")
ax.legend(title="Region", bbox_to_anchor=(1.01, 1), loc="upper left", fontsize=10)
ax.axline((0, 0), slope=1, color="#ccc", linewidth=1, linestyle="--", label="Equal time")
fig.tight_layout(pad=2)
fig.savefig(f"{OUT}/04_prep_vs_cook_time.png", dpi=150, bbox_inches="tight")
plt.close()
print("✓ Chart 4: Prep vs cook time")


# ── 5. Diet Split Donut ────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 6), facecolor=WARM_BG)
ax.set_facecolor(WARM_BG)

diet_counts = df_dishes["diet"].value_counts()
wedge_colors = [GREEN, ROSE]
wedges, texts, autotexts = ax.pie(
    diet_counts.values,
    labels=None,
    autopct="%1.1f%%",
    colors=wedge_colors,
    startangle=90,
    pctdistance=0.75,
    wedgeprops=dict(width=0.55, edgecolor="white", linewidth=3),
)
for at in autotexts:
    at.set_fontsize(14)
    at.set_fontweight("bold")
    at.set_color("white")

legend_patches = [mpatches.Patch(color=wedge_colors[i], label=diet_counts.index[i].title())
                  for i in range(len(diet_counts))]
ax.legend(handles=legend_patches, loc="lower center", bbox_to_anchor=(0.5, -0.05),
          fontsize=12, ncol=2, frameon=False)
ax.set_title("🥗  Vegetarian vs Non-Vegetarian", fontsize=16, fontweight="bold", pad=15, color="#222")
fig.tight_layout(pad=2)
fig.savefig(f"{OUT}/05_diet_split.png", dpi=150, bbox_inches="tight")
plt.close()
print("✓ Chart 5: Diet split")


# ── 6. Course Distribution by Region ──────────────────────────────────────────
fig, ax = plt.subplots(figsize=(11, 5.5), facecolor=WARM_BG)
ax.set_facecolor(CARD_BG)

course_region = (df_dishes_clean
                 .groupby(["region", "course"])
                 .size().unstack(fill_value=0))

course_colors = {
    "dessert":      ROSE,
    "main course":  SAFFRON,
    "snack":        TEAL,
    "starter":      PURPLE,
}
course_region.plot(kind="bar", ax=ax,
                   color=[course_colors.get(c, GOLD) for c in course_region.columns],
                   edgecolor="white", linewidth=1.2, width=0.7)

ax.set_xlabel("")
ax.set_title("🍽️  Course Types Across Regions", fontsize=16, fontweight="bold", pad=15, color="#222")
ax.set_xticklabels(course_region.index, rotation=30, ha="right", fontsize=11)
ax.legend(title="Course", bbox_to_anchor=(1.01, 1), loc="upper left", fontsize=10)
ax.set_ylabel("Number of Dishes", fontsize=11, color="#555")
fig.tight_layout(pad=2)
fig.savefig(f"{OUT}/06_course_by_region.png", dpi=150, bbox_inches="tight")
plt.close()
print("✓ Chart 6: Course by region")


# ── 7. Quick-Cook Dishes (Top 10 fastest total time) ──────────────────────────
fig, ax = plt.subplots(figsize=(10, 5.5), facecolor=WARM_BG)
ax.set_facecolor(CARD_BG)

quick = (df_dishes_clean[["name", "clean_total_time", "course"]]
         .sort_values("clean_total_time").head(10))

bar_colors = [course_colors.get(c, GOLD) for c in quick["course"]]
bars = ax.barh(quick["name"], quick["clean_total_time"],
               color=bar_colors, edgecolor="white", linewidth=1.2, height=0.6)

for bar, val in zip(bars, quick["clean_total_time"]):
    ax.text(val + 0.5, bar.get_y() + bar.get_height()/2,
            f"{int(val)} min", va="center", fontsize=10, fontweight="bold", color="#333")

ax.set_xlabel("Total Time (mins)", fontsize=11, color="#555")
ax.set_title("⚡  Top 10 Quickest Dishes", fontsize=16, fontweight="bold", pad=15, color="#222")
ax.set_xlim(0, quick["clean_total_time"].max() + 15)

legend_patches = [mpatches.Patch(color=course_colors[c], label=c.title())
                  for c in course_colors]
ax.legend(handles=legend_patches, loc="lower right", fontsize=10, frameon=False)
fig.tight_layout(pad=2)
fig.savefig(f"{OUT}/07_quickest_dishes.png", dpi=150, bbox_inches="tight")
plt.close()
print("✓ Chart 7: Quickest dishes")

print("\n✅ All 7 charts saved to", OUT)
