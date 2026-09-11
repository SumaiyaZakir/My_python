import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Rectangle

SPECIES = [
    "Amphibians", "Birds (Forest)", "Birds (Wetland)",
    "Birds (Grassland)", "Mammals (Large)", "Mammals (Small)"
]

LAND_USE = ["Forest", "Grassland", "Cropland", "Built-up", "Water", "Barren"]

RICHNESS = np.array([
    [27.3, 15.2, 12.5, 8.9, 18.4, 2.5],
    [52.5, 18.3, 14.2, 10.5, 8.2, 1.8],
    [15.3, 12.4, 18.5, 6.9, 42.3, 1.2],
    [22.4, 38.5, 21.3, 12.4, 5.8, 2.1],
    [51.7, 22.3, 8.5, 6.9, 4.2, 1.5],
    [45.3, 25.4, 15.8, 20.7, 3.5, 1.8],
])

RADAR_COLORS = ["#58B6B0", "#F58A6B", "#A868B9",
                "#A9C987", "#D4DC57", "#91A4AD"]

FONT = "Times New Roman"


def draw_heatmap(ax):
    cmap = sns.color_palette("YlGnBu", as_cmap=True)

    sns.heatmap(
        RICHNESS, ax=ax, cmap=cmap, vmin=0, vmax=52.5,
        linewidths=1.2, linecolor="white", annot=False, cbar=True,
        cbar_kws={"label": "Species Richness (%)", "pad": 0.065, "aspect": 18}
    )

    for row, column in np.ndindex(RICHNESS.shape):
        value = RICHNESS[row, column]
        ax.text(column + 0.5, row + 0.5, f"{value:.1f}",
                ha="center", va="center", fontsize=15,
                fontweight="bold",
                color="white" if value > 30 else "#222222")

    ax.set_xticklabels(LAND_USE, rotation=45, ha="right",
                       rotation_mode="anchor", fontsize=13)
    ax.set_yticklabels(SPECIES, rotation=0, fontsize=14)
    ax.set_xlabel("To Land Use Type", fontsize=16, fontweight="bold", labelpad=24)
    ax.set_ylabel("From Species Group", fontsize=16, fontweight="bold", labelpad=18)
    ax.set_title("Species Richness by Land Use Type",
                 fontsize=19, fontweight="bold", pad=18)
    ax.tick_params(length=0)

    ax.add_patch(Rectangle(
        (0, 0), 1, len(SPECIES), fill=False,
        edgecolor="#d62728", linewidth=2.2, linestyle="--", clip_on=False
    ))

    colorbar = ax.collections[0].colorbar
    colorbar.set_label("Species Richness (%)", fontsize=15,
                       fontweight="bold", labelpad=12)
    colorbar.ax.tick_params(labelsize=12, length=0)


def draw_radar(ax):
    n = len(LAND_USE)
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
    closed_angles = np.append(angles, angles[0])

    for species, color, values in zip(SPECIES, RADAR_COLORS, RICHNESS):
        closed_values = np.append(values, values[0])
        ax.plot(closed_angles, closed_values, color=color, linewidth=2,
                marker="o", markersize=5.5, markerfacecolor=color,
                markeredgecolor=color, label=species)
        ax.fill(closed_angles, closed_values, color=color, alpha=0.045)

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_xticks(angles)
    ax.set_xticklabels(LAND_USE, fontsize=14, fontweight="bold")
    ax.tick_params(axis="x", pad=7)
    ax.set_ylim(0, 52)
    ax.set_yticks([10, 20, 30, 40, 50])
    ax.set_yticklabels(["10%", "20%", "30%", "40%", "50%"], fontsize=12)
    ax.set_rlabel_position(22)
    ax.grid(True, linewidth=0.8, linestyle="-", color="gray", alpha=0.45)
    ax.spines["polar"].set_linewidth(1)
    ax.spines["polar"].set_color("#777777")
    ax.set_title("Species Richness Distribution",
                 fontsize=19, fontweight="bold", pad=42)

    legend = ax.legend(title="Species Groups", loc="upper left",
                       bbox_to_anchor=(1.03, 1.18), fontsize=13,
                       frameon=True, fancybox=False, framealpha=1,
                       borderpad=0.5, labelspacing=0.55,
                       handlelength=2.2, handletextpad=0.7)
    legend.get_title().set_fontsize(15)
    legend.get_title().set_fontweight("bold")
    legend.get_frame().set_linewidth(1)
    legend.get_frame().set_edgecolor("#555555")


def create_figure(output_file="images/02_species_richness_heatmap_radar.png", dpi=300):
    plt.rcParams.update({
        "font.family": FONT,
        "font.serif": [FONT, "DejaVu Serif"],
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
    })

    fig = plt.figure(figsize=(16, 7.47), dpi=dpi, facecolor="white")
    heatmap_ax = fig.add_axes([0.120, 0.155, 0.307, 0.690])
    radar_ax = fig.add_axes([0.535, 0.155, 0.325, 0.690], polar=True)

    draw_heatmap(heatmap_ax)
    draw_radar(radar_ax)

    fig.savefig(output_file, dpi=dpi, facecolor="white", edgecolor="none",
                bbox_inches="tight")
    plt.show()
    return fig


if __name__ == "__main__":
    create_figure()
