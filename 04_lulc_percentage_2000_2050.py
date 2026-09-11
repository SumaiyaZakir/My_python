import numpy as np
import matplotlib.pyplot as plt

YEARS = ["2000", "2010", "2020", "2050 (Predicted)"]

LULC = {
    "Buildup Area": [6.7, 7.3, 8.5, 10.2],
    "Bareland": [0.1, 0.0, 0.1, 0.0],
    "Grassland": [9.1, 9.8, 10.7, 10.0],
    "Water body": [5.7, 5.2, 5.5, 6.9],
    "Cropland": [10.6, 9.8, 9.0, 7.5],
    "Forest land": [67.8, 67.9, 66.2, 65.4],
}

COLORS = {
    "Buildup Area": "#FF0000",
    "Bareland": "#ECE352",
    "Grassland": "#B5DFA3",
    "Water body": "#8DBDE6",
    "Cropland": "#33FF00",
    "Forest land": "#267300",
}

FONT = "Times New Roman"
LABEL_THRESHOLD = 5.0


def draw_lulc_bars(ax):
    bottom = np.zeros(len(YEARS))

    for category, values in LULC.items():
        values = np.array(values)
        ax.bar(
            YEARS, values, bottom=bottom, width=0.55,
            color=COLORS[category], edgecolor="none", label=category
        )

        for i, value in enumerate(values):
            if value >= LABEL_THRESHOLD:
                ax.text(
                    i, bottom[i] + value / 2, f"{value:.1f}%",
                    ha="center", va="center", fontsize=12,
                    fontweight="bold",
                    color="white" if category == "Forest land" else "black"
                )

        bottom += values


def create_figure(output_file="images/04_lulc_percentage_2000_2050.png", dpi=300):
    plt.rcParams.update({
        "font.family": FONT,
        "font.serif": [FONT, "DejaVu Serif"],
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
    })

    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=dpi, facecolor="white")
    draw_lulc_bars(ax)

    ax.set_xlabel("Year", fontsize=14, fontweight="bold", labelpad=15)
    ax.set_ylabel("Percentage (%)", fontsize=14, fontweight="bold", labelpad=10)
    ax.set_ylim(0, 100)
    ax.set_yticks(np.arange(0, 101, 20))
    ax.grid(axis="y", color="#E0E0E0", linestyle="-",
            linewidth=0.8, alpha=0.7)
    ax.set_axisbelow(True)

    for spine in ax.spines.values():
        spine.set_color("#888888")
        spine.set_linewidth(1.0)

    ax.tick_params(axis="both", which="major", labelsize=12)

    legend = ax.legend(
        title="LULC Type", loc="upper left",
        bbox_to_anchor=(1.02, 1.0), frameon=True,
        edgecolor="black", facecolor="white", fontsize=12
    )
    legend.get_title().set_fontsize(13)
    legend.get_title().set_fontweight("bold")

    plt.tight_layout()
    plt.savefig(output_file, dpi=dpi, bbox_inches="tight", facecolor="white")
    plt.show()


if __name__ == "__main__":
    create_figure()
