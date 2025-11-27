import matplotlib.pyplot as plt
from fetchalldata import fetchalldata


csv_file_path = 'data/car-data.csv'


def main():
    data = fetchalldata()
    if isinstance(data, Exception):
        print(f"Failed to load data: {data}")
        return

    # Ensure necessary columns are present
    required_columns = ['year', 'origin', 'fuel_ec', 'displacement_l']
    for col in required_columns:
        if col not in data.columns:
            print(f"Missing required column: {col}")
            return

    data_plotting(data)


def data_plotting(data):
    avg_cylinders = data.groupby(['year', 'origin'])['cylinders'].mean().unstack()

    # Create a single plot (one Axes)
    fig, ax = plt.subplots(figsize=(10, 6))

    if not avg_cylinders.empty:
        avg_cylinders.plot(ax=ax, marker='o')
        ax.set_title('Average cylinders by Origin')
        ax.set_ylabel('Cylinders')
        ax.set_xlabel('Year')
        ax.grid(True)
        ax.legend(title='Origin')

    plt.tight_layout()
    plt.savefig('average_cylinders.png')


if __name__ == "__main__":
    main()
