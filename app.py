import matplotlib.pyplot as plt
from load_car_data import load_car_data
from plots import (
    fuel_ec_and_displacement_by_year,
    cylinder_counts_by_year,
    cylinder_amounts_crosstab,
    car_specs_correlation,
)


def main():
    """Entry point for generating plots from car data."""
    df = load_car_data()

    # List all plotting functions and their corresponding output filenames
    plot_funcs = [
        (fuel_ec_and_displacement_by_year, "fuel-consumption-and-displacement-by-year.png"),
        (cylinder_counts_by_year, "cylinder-counts-by-year.png"),
        (cylinder_amounts_crosstab, "cylinder-amounts-crosstab.png"),
        (car_specs_correlation, "car-specs-correlation.png"),
    ]

    # Create each plot, save it, and display it.
    # Because plt.show() is blocking, loop continues only after the previous plot window is closed.
    for func, filename in plot_funcs:
        fig = func(df)
        fig.savefig(filename)
        plt.show()


if __name__ == "__main__":
    main()
