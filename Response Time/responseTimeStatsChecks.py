import os
import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from scipy.stats import shapiro
from scipy.stats import bartlett
from scipy.stats import f_oneway

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

stcs_array = np.array([milliseconds // 1000 for milliseconds in stcs])
cas_array = np.array([milliseconds // 1000 for milliseconds in cas])
cos_array = np.array([milliseconds // 1000 for milliseconds in cos])
ras_array = np.array([milliseconds // 1000 for milliseconds in ras])

# Calculate mean, standard deviation, minimum, and maximum
mean_value = np.mean(stcs_array)
sd_value = np.std(stcs_array)
min_value = np.min(stcs_array)
max_value = np.max(stcs_array)

# Print the results
print("Mean:", mean_value)
print("Standard Deviation:", sd_value)
print("Minimum:", min_value)
print("Maximum:", max_value)

# Calculate mean, standard deviation, minimum, and maximum
mean_value = np.mean(cas_array)
sd_value = np.std(cas_array)
min_value = np.min(cas_array)
max_value = np.max(cas_array)

# Print the results
print("Mean:", mean_value)
print("Standard Deviation:", sd_value)
print("Minimum:", min_value)
print("Maximum:", max_value)

# Calculate mean, standard deviation, minimum, and maximum
mean_value = np.mean(cos_array)
sd_value = np.std(cos_array)
min_value = np.min(cos_array)
max_value = np.max(cos_array)

# Print the results
print("Mean:", mean_value)
print("Standard Deviation:", sd_value)
print("Minimum:", min_value)
print("Maximum:", max_value)

# Calculate mean, standard deviation, minimum, and maximum
mean_value = np.mean(ras_array)
sd_value = np.std(ras_array)
min_value = np.min(ras_array)
max_value = np.max(ras_array)

# Print the results
print("Mean:", mean_value)
print("Standard Deviation:", sd_value)
print("Minimum:", min_value)
print("Maximum:", max_value)

'''
print("Shapiro-Wilk Test for CaS:")
stat, p_value = shapiro(cas)
print("Test Statistic:", stat)
print("P-value:", p_value)
if p_value < 0.05:
    print("Data is not normally distributed (reject null hypothesis)")
else:
    print("Data is normally distributed (fail to reject null hypothesis)")

print("Shapiro-Wilk Test for CoS:")
stat, p_value = shapiro(cos)
print("Test Statistic:", stat)
print("P-value:", p_value)
if p_value < 0.05:
    print("Data is not normally distributed (reject null hypothesis)")
else:
    print("Data is normally distributed (fail to reject null hypothesis)")

print("Shapiro-Wilk Test for RaS:")
stat, p_value = shapiro(ras)
print("Test Statistic:", stat)
print("P-value:", p_value)
if p_value < 0.05:
    print("Data is not normally distributed (reject null hypothesis)")
else:
    print("Data is normally distributed (fail to reject null hypothesis)")

print("Shapiro-Wilk Test for StCS:")
stat, p_value = shapiro(stcs)
print("Test Statistic:", stat)
print("P-value:", p_value)
if p_value < 0.05:
    print("Data is not normally distributed (reject null hypothesis)")
else:
    print("Data is normally distributed (fail to reject null hypothesis)")

bartlett_stat, bartlett_p_value = bartlett(cas, cos, ras, stcs)

print("Bartlett's Test:")
print("Test Statistic:", bartlett_stat)
print("P-value:", bartlett_p_value)
if bartlett_p_value < 0.05:
    print("Variances are not homogeneous (reject null hypothesis)")
else:
    print("Variances are homogeneous (fail to reject null hypothesis)")
'''