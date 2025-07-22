# main.py

import pandas as pd
from volumetric import calculate_ooip
from mbe import estimate_reserves_mbe, plot_mbe
from DCA import perform_dca

# Volumetric estimation
df = pd.read_csv("data/sample_volumetric_data.csv")
for index, row in df.iterrows():
    N = calculate_ooip(row['area_acres'], row['thickness_ft'], row['porosity'],
                       row['water_saturation'], row['Bo'])
    print(f"OOIP for Reservoir {index+1}: {N:.2f} STB")

# MBE estimation
N_mbe, model = estimate_reserves_mbe("data/mbe_input_data.csv")
print(f"Estimated Reserves using MBE: {N_mbe:.2f} STB")
plot_mbe("data/mbe_input_data.csv", model)

# DCA estimation
perform_dca("data/dca_production_data.csv")
