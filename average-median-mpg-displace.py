import pandas as pd
import matplotlib.pyplot as plt

csv_file_path = 'data/car-data.csv'

def main():
    try:
        data = pd.read_csv(csv_file_path, on_bad_lines='skip')

        data.rename(columns={'model_year': 'year'}, inplace=True)

        origin_map = {1: 'USA', 2: 'EU', 3: 'JP'}
        if data['origin'].dtype in ['int64', 'float64']:
            data['origin'] = data['origin'].map(origin_map)

        if data['year'].max() < 100:
            data['year'] = data['year'] + 1900

        data_plotting(data)
        print("Success: Plot saved as 'car_data_plots.png'")

    except Exception as e:
        print(f"Error loading data: {e}")
        try:
            print("Data snapshot:")
            print(pd.read_csv(csv_file_path).head())
        except:
            pass

def data_plotting(data):
    years = range(1970, 1982)
    origins = ['USA', 'EU', 'JP']

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
        ax.set_xlabel('Year')             # Ensure label is set for all
        ax.tick_params(labelbottom=True)

    plt.tight_layout()
    plt.savefig('average_median_mpg-displacement.png')

if __name__ == "__main__":
    main()
