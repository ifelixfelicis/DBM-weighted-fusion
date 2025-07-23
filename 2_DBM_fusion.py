##author: ifelixfelicis (https://github.com/ifelixfelicis)
##Email: w15684143509@gmail.com
## des: weighted fusion of two global DBMs using constrained RMSE minimization.

import pandas as pd
import numpy as np
from scipy.optimize import minimize
from sklearn.metrics import mean_squared_error

# Replace with your own file path
file_path = 'data/depth_msl.csv'

data = pd.read_csv(file_path, delimiter=',')
fields = ['MSL', 'etopo15', 'etopo30', 'topo_25_1', 'srtm30_v11', 'srtm15', 'g24']
data = data.replace(-9999, np.nan)

min_rmse = float('inf')
best_weights = None
best_combination = None

weights = np.arange(0, 1.01, 0.01)

for i in range(1, len(fields)):
    for j in range(i+1, len(fields)):
        dbm1 = fields[i]
        dbm2 = fields[j]
        
        for a in weights:
            for b in weights:
                if a + b == 1:
                    Z = a * data[dbm1] + b * data[dbm2]
                    
                    valid_data = data.dropna(subset=[dbm1, dbm2, 'MSL'])
                    
                    rmse = np.sqrt(mean_squared_error(valid_data['MSL'], valid_data[dbm1] * a + valid_data[dbm2] * b))
                    
                    if rmse < min_rmse:
                        min_rmse = rmse
                        best_weights = (a, b)
                        best_combination = (dbm1, dbm2)

print("best_combination:", best_combination)
print("best_weights:", best_weights)
print("min_RMSE:", round(min_rmse, 3))