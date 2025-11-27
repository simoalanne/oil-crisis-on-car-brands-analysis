import pandas as pd
csv_file_path = 'data/car-data.csv'


def fetchalldata():
    try:
        data = pd.read_csv(csv_file_path, on_bad_lines='skip')

        data.rename(columns={'model_year': 'year'}, inplace=True)

        origin_map = {1: 'USA', 2: 'EU', 3: 'JP'}
        if data['origin'].dtype in ['int64', 'float64']:
            data['origin'] = data['origin'].map(origin_map)

        if data['year'].max() < 100:
            data['year'] = data['year'] + 1900
        return data

    except Exception as e:
        return e