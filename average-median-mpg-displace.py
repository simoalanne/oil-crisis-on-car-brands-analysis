import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv as csv

csv_file_path = 'car-data.csv'

data = pd.read_csv(csv_file_path)
mpg = data['mpg']
displacement = data['displacement']
average_mpg = np.mean(mpg)
median_mpg = np.median(mpg)
average_displacement = np.mean(displacement)
median_displacement = np.median(displacement)