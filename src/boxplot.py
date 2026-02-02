"""
boxplot.py
----------
Generates a boxplot of the California Housing dataset features.
Uses scikit-learn's built-in California Housing dataset and
matplotlib for visualization.

Assignment: A01_5512
"""

# ------------------------------------------------------------
# STEP 1: Import Libraries
# ------------------------------------------------------------
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# STEP 2: Load the California Housing Dataset
# ------------------------------------------------------------
housing = fetch_california_housing(as_frame=True)

df = housing.data.copy()
df["MedHouseVal"] = housing.target

print("Dataset shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nBasic statistics:")
print(df.describe())

# ------------------------------------------------------------
# STEP 3: Standardize the Data
# ------------------------------------------------------------
df_standardized = (df - df.mean()) / df.std()

# ------------------------------------------------------------
# STEP 4: Create the Boxplot
# ------------------------------------------------------------
fig, ax = plt.subplots(figsize=(14, 7))

bp = ax.boxplot(
    df_standardized.values,
    tick_labels=df_standardized.columns,
    patch_artist=True,
    showfliers=False,
    widths=0.6,
    medianprops=dict(color="black", linewidth=2),
)

# ------------------------------------------------------------
# STEP 5: Color Each Box
# ------------------------------------------------------------
colors = plt.cm.tab10.colors
for patch, color in zip(bp["boxes"], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

# ------------------------------------------------------------
# STEP 6: Add Titles and Labels
# ------------------------------------------------------------
ax.set_title(
    "California Housing Dataset — Feature Distribution (Standardized)",
    fontsize=16, fontweight="bold", pad=15
)
ax.set_xlabel("Feature", fontsize=13, labelpad=10)
ax.set_ylabel("Standardized Value (z-score)", fontsize=13, labelpad=10)

plt.xticks(rotation=30, ha="right", fontsize=10)
plt.yticks(fontsize=10)

ax.yaxis.grid(True, linestyle="--", alpha=0.5)
ax.set_axisbelow(True)

# ------------------------------------------------------------
# STEP 7: Save and Show
# ------------------------------------------------------------
output_path = "figs/boxplot.png"
plt.tight_layout()
plt.savefig(output_path, dpi=150, bbox_inches="tight")
print(f"\n✅ Boxplot saved to: {output_path}")

plt.show()
E

cat > src/boxplot.py << 'EOF'
"""
boxplot.py
----------
Generates a boxplot of the California Housing dataset features.
Uses scikit-learn's built-in California Housing dataset and
matplotlib for visualization.

Assignment: A01_5512
"""

# ------------------------------------------------------------
# STEP 1: Import Libraries
# ------------------------------------------------------------
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# STEP 2: Load the California Housing Dataset
# ------------------------------------------------------------
housing = fetch_california_housing(as_frame=True)

df = housing.data.copy()
df["MedHouseVal"] = housing.target

print("Dataset shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nBasic statistics:")
print(df.describe())

# ------------------------------------------------------------
# STEP 3: Standardize the Data
# ------------------------------------------------------------
df_standardized = (df - df.mean()) / df.std()

# ------------------------------------------------------------
# STEP 4: Create the Boxplot
# ------------------------------------------------------------
fig, ax = plt.subplots(figsize=(14, 7))

bp = ax.boxplot(
    df_standardized.values,
    tick_labels=df_standardized.columns,
    patch_artist=True,
    showfliers=False,
    widths=0.6,
    medianprops=dict(color="black", linewidth=2),
)

# ------------------------------------------------------------
# STEP 5: Color Each Box
# ------------------------------------------------------------
colors = plt.cm.tab10.colors
for patch, color in zip(bp["boxes"], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

# ------------------------------------------------------------
# STEP 6: Add Titles and Labels
# ------------------------------------------------------------
ax.set_title(
    "California Housing Dataset — Feature Distribution (Standardized)",
    fontsize=16, fontweight="bold", pad=15
)
ax.set_xlabel("Feature", fontsize=13, labelpad=10)
ax.set_ylabel("Standardized Value (z-score)", fontsize=13, labelpad=10)

plt.xticks(rotation=30, ha="right", fontsize=10)
plt.yticks(fontsize=10)

ax.yaxis.grid(True, linestyle="--", alpha=0.5)
ax.set_axisbelow(True)

# ------------------------------------------------------------
# STEP 7: Save and Show
# ------------------------------------------------------------
output_path = "figs/boxplot.png"
plt.tight_layout()
plt.savefig(output_path, dpi=150, bbox_inches="tight")
print(f"\n✅ Boxplot saved to: {output_path}")

plt.show()
