import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import shapiro
from scipy.stats import bartlett
from scipy.stats import friedmanchisquare

fixaiton_times = {"StCS": [], "CaS": [], "CoS": [], "RaS": []}

def checkPrefix(df, prefix, strat):
    filtered_df = df[df['AOI'].str.startswith(prefix)]
    average_length_df = filtered_df.groupby('SubjectName')['Length'].mean().reset_index()
    average_length_df['Length'] = average_length_df['Length'].astype(int)
    fixaiton_times[strat].extend(average_length_df["Length"].tolist())
        
path = "C:/Users/User/Desktop/Uni/Bachelorarbeit/Analysis/Eye Tracking"
for file_name in os.listdir(path):
    if file_name.endswith(".py"):
        continue
    file = path + '/' + file_name
    df = pd.read_csv(file, sep='\t', index_col=False)
    match file_name:
        case "CaCoRaSt.txt":
            checkPrefix(df, "Bo", "CaS")
            checkPrefix(df, "Bu", "CoS")
            checkPrefix(df, "Sn", "RaS")
            checkPrefix(df, "St", "StCS")
        case "CoRaStCa.txt":
            checkPrefix(df, "Bo", "CoS")
            checkPrefix(df, "Bu", "RaS")
            checkPrefix(df, "Sn", "StCS")
            checkPrefix(df, "St", "CaS")
        case "RaStCaCo.txt":
            checkPrefix(df, "Bo", "RaS")
            checkPrefix(df, "Bu", "StCS")
            checkPrefix(df, "Sn", "CaS")
            checkPrefix(df, "St", "CoS")
        case "StCaCoRa.txt":
            checkPrefix(df, "Bo", "StCS")
            checkPrefix(df, "Bu", "CaS")
            checkPrefix(df, "Sn", "CoS")
            checkPrefix(df, "St", "RaS")

stcs = np.array(fixaiton_times["StCS"])
cas = np.array(fixaiton_times["CaS"])
cos = np.array(fixaiton_times["CoS"])
ras = np.array(fixaiton_times["RaS"])

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

ras = np.append(ras, 115)

# Perform Friedman test
f_statistic, p_value = friedmanchisquare(stcs, cas, cos, ras)

print("Friedman test F-statistic:", f_statistic)
print("p-value:", p_value)


'''
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