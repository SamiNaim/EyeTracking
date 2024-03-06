import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

path = "C:/Users/User/Desktop/Uni/Bachelorarbeit/Analysis/PlayGround"
stcs = []
cas = []
cos = []
ras = []

def collectTimes(file):
    df = pd.read_csv(file, sep = ';')
    stcsTime = 0
    casTime = 0
    cosTime = 0
    rasTime = 0
    
    for index, row in df.iterrows():
        if row["Task"].endswith("Stcs"):
            stcsTime += row["Time"]
        elif row["Task"].endswith("Cas"):
            casTime += row["Time"]
        elif row["Task"].endswith("Cos"):
            cosTime += row["Time"]
        elif row["Task"].endswith("Ras"):
            rasTime += row["Time"]
    stcs.append(stcsTime)
    cas.append(casTime)
    cos.append(cosTime)
    ras.append(rasTime)
            

for folder_name in os.listdir(path):
    if folder_name.endswith(".py"):
        continue
    folder = path + '/' + folder_name
    for file_name in os.listdir(folder):
        file = folder + '/' + file_name
        if file_name.startswith("Results"):
            collectTimes(file)

# Normalize the data
def normalize_data(data):
    min_val = min(data)
    max_val = max(data)
    normalized_data = (data - min_val) / (max_val - min_val)
    return normalized_data

stcs_normalized = normalize_data(np.array(stcs))
cas_normalized = normalize_data(np.array(cas))
cos_normalized = normalize_data(np.array(cos))
ras_normalized = normalize_data(np.array(ras))

# Combine the normalized data into a list of arrays
normalized_data = [stcs_normalized, cas_normalized, cos_normalized, ras_normalized]

# Create the box plot
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
plt.boxplot(normalized_data, vert=False, boxprops=dict(color="#59ae70"), medianprops=dict(color="#de7a77"))

# Add labels and title
plt.xlabel('Normalized Response Time')
plt.ylabel('Method Ordering Strategies')

# Show the plot
plt.yticks([1, 2, 3, 4], ['StCS', 'CaS', 'CoS', 'RaS'])  # Set y-axis labels
plt.grid(True)  # Add grid lines for better readability
plt.show()