import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

csv_file_path = 'data/car-data-2.csv'

def main():
    try:
        # FIX 1: Remove 'delim_whitespace' and 'names'.
        # Let pandas read the comma-separated header automatically.
        data = pd.read_csv(csv_file_path, on_bad_lines='skip')

        # FIX 2: Rename 'model_year' from the file to 'year' as expected by your script
        data.rename(columns={'model_year': 'year'}, inplace=True)

        # Normalize 'origin' to strings if they are integers
        # (Your snippet shows they are already strings like "USA", so this might skip, which is fine)
        origin_map = {1: 'USA', 2: 'EU', 3: 'JP'}
        if data['origin'].dtype in ['int64', 'float64']:
            data['origin'] = data['origin'].map(origin_map)

        # Normalize year (70 -> 1970)
        if data['year'].max() < 100:
            data['year'] = data['year'] + 1900

        data_plotting(data)
        print("Success: Plot saved as 'car_data_plots.png'")

    except Exception as e:
        print(f"Error loading data: {e}")
        # Print the first few rows to debug if it fails again
        try:
            print("Data snapshot:")
            print(pd.read_csv(csv_file_path).head())
        except:
            pass

def data_plotting(data):
    years = range(1970, 1983)
    # Ensure your origins match exactly what is in the CSV (Snippet had 'USA', 'EU', 'JP')
    origins = ['USA', 'EU', 'JP']

    # Pre-aggregate data
    avg_mpg = data.groupby(['year', 'origin'])['mpg'].mean().unstack()
    median_mpg = data.groupby(['year', 'origin'])['mpg'].median().unstack()
    avg_disp = data.groupby(['year', 'origin'])['displacement'].mean().unstack()
    median_disp = data.groupby(['year', 'origin'])['displacement'].median().unstack()

    # ---- Plot ----
    fig, axes = plt.subplots(2, 2, figsize=(14, 9), sharex=True)
    ax1, ax2, ax3, ax4 = axes.flatten()

    # Check if data is not empty before plotting to avoid "no numeric data" error
    if not avg_mpg.empty:
        avg_mpg.plot(ax=ax1, marker='o')
        ax1.set_title('Average MPG by Origin')
        ax1.set_ylabel('MPG')

    if not median_mpg.empty:
        median_mpg.plot(ax=ax2, marker='o')
        ax2.set_title('Median MPG by Origin')
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

    plt.tight_layout()
    plt.savefig('average_median_mpg-displacement.png')

if __name__ == "__main__":
    main()
