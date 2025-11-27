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

    avg_mpg = data.groupby(['year', 'origin'])['fuel_ec'].mean().unstack()
    median_mpg = data.groupby(['year', 'origin'])['fuel_ec'].median().unstack()
    avg_disp = data.groupby(['year', 'origin'])['displacement_l'].mean().unstack()
    median_disp = data.groupby(['year', 'origin'])['displacement_l'].median().unstack()

    fig, axes = plt.subplots(2, 2, figsize=(14, 9), sharex=True)
    ax1, ax2, ax3, ax4 = axes.flatten()

    if not avg_mpg.empty:
        avg_mpg.plot(ax=ax1, marker='o')
        ax1.set_title('Average fuel consumption (l/100km) by Origin')
        ax1.set_ylabel('MPG')

    if not median_mpg.empty:
        median_mpg.plot(ax=ax2, marker='o')
        ax2.set_title('Median fuel consumption (l/100km) by Origin')
        ax2.set_ylabel('MPG')

    if not avg_disp.empty:
        avg_disp.plot(ax=ax3, marker='o')
        ax3.set_title('Average Displacement by Origin')
        ax3.set_ylabel('Displacement')


    if not median_disp.empty:
        median_disp.plot(ax=ax4, marker='o')
        ax4.set_title('Median Displacement by Origin')
        ax4.set_ylabel('Displacement')

    for ax in axes.flatten():
        ax.grid(True)
        ax.legend(title='Origin')

    for ax in axes.flatten():
        ax.grid(True)
        ax.legend(title='Origin')
        ax.set_xlabel('Year')
        ax.tick_params(labelbottom=True)

    plt.tight_layout()
    plt.savefig('average_median_mpg-displacement.png')

if __name__ == "__main__":
    main()
