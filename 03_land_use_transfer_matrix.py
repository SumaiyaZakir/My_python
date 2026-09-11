import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

LAND_USE = ["Forest", "Grassland", "Cropland", "Built-up", "Water", "Barren"]

TRANSFER_2010_2020 = np.array([
    [np.nan, 180.0, 355.2, 95.6, 25.0, 5.0],
    [45.0, np.nan, 74.7, 45.0, 138.6, 8.0],
    [65.0, 85.0, np.nan, 120.0, 35.0, 10.0],
    [5.0, 15.0, 25.0, np.nan, 8.0, 2.0],
    [30.0, 50.0, 40.0, 15.0, np.nan, 3.0],
    [2.0, 5.0, 8.0, 3.0, 2.0, np.nan],
])

TRANSFER_2020_2050 = np.array([
    [np.nan, 292.8, 79.8, 30.0, 20.0, 3.0],
    [35.0, np.nan, 80.0, 97.6, 262.1, 5.0],
    [25.0, 162.0, np.nan, 201.0, 45.0, 8.0],
    [3.0, 12.0, 18.0, np.nan, 5.0, 1.0],
    [15.0, 45.0, 28.0, 10.0, np.nan, 2.0],
    [1.0, 3.0, 5.0, 2.0, 1.0, np.nan],
])

FONT = "Times New Roman"
CELL_SIZE = 20
TITLE_SIZE = 18
AXIS_SIZE = 18
TICK_SIZE = 16
COLORBAR_LABEL_SIZE = 16
COLORBAR_TICK_SIZE = 14
CONTRAST_LIMIT = 150


def draw_transfer_matrix(ax, data, title, period, maximum):
    color_map = sns.color_palette("YlOrRd", as_cmap=True)
    color_map.set_bad("white")

    sns.heatmap(
        data, ax=ax, cmap=color_map, vmin=0, vmax=maximum,
        xticklabels=LAND_USE, yticklabels=LAND_USE, linewidths=0,
        cbar_kws={"label": "Area Transferred (km²)", "pad": 0.03}
    )

    for row, column in np.ndindex(data.shape):
        value = data[row, column]
        if np.isnan(value):
            continue
        ax.text(column + 0.5, row + 0.5, f"{value:.1f}",
                ha="center", va="center", fontsize=CELL_SIZE,
                fontweight="bold",
                color="white" if value >= CONTRAST_LIMIT else "black")

    ax.set_title(title, fontsize=TITLE_SIZE, fontweight="bold", pad=22)
    ax.set_xlabel("To Land Use Type", fontsize=AXIS_SIZE,
                  fontweight="bold", labelpad=14)
    ax.set_ylabel("From Land Use Type", fontsize=AXIS_SIZE,
                  fontweight="bold", labelpad=14)

    ax.text(0.04, 1.05, period, transform=ax.transAxes,
            ha="center", va="center", fontsize=18, fontweight="bold",
            bbox={"boxstyle": "round,pad=0.3",
                  "facecolor": "#d9ead3", "edgecolor": "none"})

    ax.set_xticklabels(LAND_USE, rotation=45, ha="right", fontsize=TICK_SIZE)
    ax.set_yticklabels(LAND_USE, rotation=0, fontsize=TICK_SIZE)

    colorbar = ax.collections[0].colorbar
    colorbar.set_label("Area Transferred (km²)",
                       fontsize=COLORBAR_LABEL_SIZE, fontweight="bold")
    colorbar.ax.tick_params(labelsize=COLORBAR_TICK_SIZE)
    colorbar.outline.set_visible(False)


def create_figure(output_file="images/03_land_use_transfer_matrix.png", dpi=300):
    plt.rcParams.update({
        "font.family": FONT,
        "font.serif": [FONT, "DejaVu Serif"],
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
    })

    fig, axes = plt.subplots(1, 2, figsize=(18, 8), facecolor="white")

    draw_transfer_matrix(
        axes[0], TRANSFER_2010_2020,
        "Land Use Transfer: 2010 → 2020", "2010 →", maximum=360
    )
    draw_transfer_matrix(
        axes[1], TRANSFER_2020_2050,
        "Land Use Transfer: 2020 → 2050 (Projected)", "2020 →", maximum=300
    )

    plt.tight_layout()
    plt.savefig(output_file, dpi=dpi, bbox_inches="tight", facecolor="white")
    plt.show()


if __name__ == "__main__":
    create_figure()
