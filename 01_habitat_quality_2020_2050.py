import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from pathlib import Path

# ============================================================
# DATA
# ============================================================
data = {
    2020: {
        "Bandarban": [88, 8, 3, 1],
        "Rangamati": [83, 12, 4, 1],
        "Khagrachari": [77, 11, 9, 3],
        "Chittagong": [44, 15, 15, 26],
        "Cox's Bazar": [27, 21, 36, 16],
    },
    2050: {
        "Bandarban": [88, 8, 3, 1],
        "Rangamati": [82, 12, 5, 1],
        "Khagrachari": [77, 10, 9, 4],
        "Chittagong": [42, 13, 14, 31],
        "Cox's Bazar": [25, 16, 38, 21],
    },
}

years = [2020, 2050]
districts = ["Bandarban", "Rangamati", "Khagrachari", "Chittagong", "Cox's Bazar"]
categories = ["Excellent", "Good", "Medium", "Low"]

COLORS = {
    "Excellent": "#1C5E20",
    "Good": "#4CB050",
    "Medium": "#FFBC01",
    "Low": "#E63837",
}
FONT = "Times New Roman"


def create_figure(output_file="images/01_habitat_quality_2020_2050.png", dpi=300):
    plt.rcParams["font.family"] = FONT

    fig, axes = plt.subplots(1, 2, figsize=(15, 7), dpi=dpi, facecolor="white")

    x = np.arange(len(districts))
    width = 0.68

    for ax, year in zip(axes, years):
        bottom = np.zeros(len(districts))
        for i, category in enumerate(categories):
            values = np.array([data[year][d][i] for d in districts])
            ax.bar(
                x, values, width, bottom=bottom,
                color=COLORS[category], label=category,
                edgecolor="white", linewidth=0.6
            )
            for j, value in enumerate(values):
                if value >= 5:
                    ax.text(
                        x[j], bottom[j] + value / 2, f"{value}%",
                        ha="center", va="center", fontsize=10,
                        fontweight="bold",
                        color="white" if category == "Excellent" else "black"
                    )
            bottom += values

        ax.set_title(f"Habitat Quality Classification: {year}",
                     fontsize=16, fontweight="bold", pad=12)
        ax.set_xticks(x)
        ax.set_xticklabels(districts, rotation=25, ha="right", fontsize=11)
        ax.set_ylim(0, 100)
        ax.set_ylabel("Area (%)", fontsize=13, fontweight="bold")
        ax.grid(axis="y", alpha=0.25)
        ax.set_axisbelow(True)

    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, title="Habitat Quality",
               loc="upper center", ncol=4, bbox_to_anchor=(0.5, 1.02),
               frameon=False, fontsize=11, title_fontsize=12)

    fig.tight_layout(rect=[0, 0, 1, 0.94])
    fig.savefig(output_file, dpi=dpi, bbox_inches="tight", facecolor="white")
    plt.show()


if __name__ == "__main__":
    create_figure()
