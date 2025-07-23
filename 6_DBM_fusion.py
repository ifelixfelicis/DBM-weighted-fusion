##author: ifelixfelicis (https://github.com/ifelixfelicis)
##Email: w15684143509@gmail.com
## des: weighted fusion of six global DBMs using constrained RMSE minimization.

import pandas as pd
import numpy as np
from scipy.optimize import minimize
from sklearn.metrics import mean_squared_error

# Replace with your own file path
file_path = 'data/depth_msl.csv'

data = pd.read_csv(file_path, delimiter=',')
fields = ['MSL', 'etopo15', 'etopo30', 'topo_25_1', 'srtm30_v11', 'srtm15', 'gebco24']
data = data.replace(-9999, np.nan)

def calculate_combined_rmse(weights):
    data['DBM'] = data[fields[1:]].dot(weights)
    valid_data = data[data['DBM'].notnull()]
    rmse = np.sqrt(mean_squared_error(valid_data['MSL'], valid_data['DBM']))
    return rmse

bounds = [(0, 1)] * (len(fields) - 1) 
constraint = {'type': 'eq', 'fun': lambda weights: 1 - np.sum(weights)}
initial_weights = np.ones(len(fields) - 1) / len(fields) - 1

result = minimize(calculate_combined_rmse, initial_weights, method='SLSQP',
                  bounds=bounds, constraints=constraint)

best_weights = result.x
min_rmse = result.fun
print("best_weights：", list(np.round(best_weights, 3)))
print("min_RMSE：", round(min_rmse, 3))
