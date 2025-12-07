import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats


def fuel_ec_and_displacement_by_year(df):
    fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharex=True)
    ax1, ax2 = axes.flatten()

    # Helper function to create  line plots more concisely
    def plot_grouped(df, col, agg, ax, title, ylabel):
        data = df.groupby(["year", "origin"])[col].agg(agg).unstack()
        data.plot(ax=ax, marker="o")
        ax.set_title(title)
        ax.set_ylabel(ylabel)
        return ax

    plot_grouped(
        df,
        "fuel_consumption",
        "mean",
        ax1,
        "Average Fuel consumption (l/100km) by Origin",
        "Fuel consumption",
    )
    plot_grouped(
        df,
        "displacement_l",
        "mean",
        ax2,
        "Average Displacement by Origin",
        "Displacement",
    )

    for ax in axes.flatten():
        ax.grid(True)
        ax.legend(title="Origin")
        ax.set_xlabel("Year")
        ax.tick_params(labelbottom=True)

    fig.tight_layout()
    return fig


def cylinder_counts_by_year(df):
    avg_cylinders = df.groupby(["year", "origin"])["cylinders"].mean().unstack()
    fig, ax = plt.subplots(figsize=(10, 6))
    avg_cylinders.plot(ax=ax, marker="o")
    ax.set_title("Average Cylinders by Origin")
    ax.set_ylabel("Cylinders")
    ax.set_xlabel("Year")
    ax.grid(True)
    ax.legend(title="Origin")
    fig.tight_layout()
    return fig


def cylinder_amounts_crosstab(df):
    counts = df["cylinders"].value_counts()
    mean_count = counts.mean()
    rare_cylinders = counts[counts < mean_count].index.tolist()
    others_label = f"Others ({', '.join(map(str, rare_cylinders))})"

    ct = pd.crosstab(
        df["origin"],
        df["cylinders"].apply(
            lambda x: others_label if x in rare_cylinders else str(x)
        ),
    )
    print(f"Cross-tab data between origin and cylinder counts:\n{ct}\n")

    fig, ax = plt.subplots(figsize=(10, 6))
    ct.plot(kind="bar", stacked=False, ax=ax)
    ax.set_ylabel("Count")
    ax.set_xlabel("Origin")
    ax.set_title("Cylinder Counts by Origin")
    ax.grid(True)
    fig.tight_layout()
    return fig


def car_specs_correlation(df):
    def plot_correlation(df, x_col, y_col, x_label, y_label, ax):
        x = df[x_col]
        y = df[y_col]
        r, p = stats.pearsonr(x, y)
        print(f"Correlation between {x_col} and {y_col}: r={r:.2f}, p={p:.20f}")
        ax.scatter(x, y)
        m, b = np.polyfit(x, y, 1)
        ax.plot(x, m * x + b, color="red")
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title(f"{y_label} vs {x_label} (r={r:.2f}, p={p:.4f})")

    fig, axis = plt.subplots(2, 2, figsize=(14, 6))
    ax1, ax2, ax3, ax4 = axis.flatten()
    plot_correlation(
        df, "hp", "fuel_consumption", "Horsepower", "Fuel Consumption (l/100km)", ax1
    )
    plot_correlation(
        df, "weight_kg", "fuel_consumption", "Weight (kg)", "Fuel Consumption (l/100km)", ax2
    )
    plot_correlation(df, "weight_kg", "hp", "Weight (kg)", "Horsepower", ax3)
    plot_correlation(
        df,
        "weight_kg",
        "acceleration",
        "Weight (kg)",
        "Acceleration (0-100 km/h in s)",
        ax4,
    )
    fig.tight_layout()
    return fig
