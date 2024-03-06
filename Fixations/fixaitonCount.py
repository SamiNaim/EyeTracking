import os
import pandas as pd
import matplotlib.pyplot as plt

fixaiton_counts = {"StCS": [], "CaS": [], "CoS": [], "RaS": []}

def checkPrefix(df, prefix, strat):
    counts = df[df['AOI'].str.startswith(prefix)].groupby('SubjectName').size()
    result_dict = counts.to_dict()
    for value in result_dict.values():
        fixaiton_counts[strat].append(value)
        
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

print(fixaiton_counts)

# Create the box plot
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
plt.boxplot([fixaiton_counts["StCS"], fixaiton_counts["CaS"], fixaiton_counts["CoS"], fixaiton_counts["RaS"]], boxprops=dict(color="#59ae70"), medianprops=dict(color="#de7a77"), showfliers=False)

# Add labels and title
plt.ylabel('Fixation Count')
plt.xlabel('Method Ordering Strategies')

# Show the plot
plt.xticks([1, 2, 3, 4], ['StCS', 'CaS', 'CoS', 'RaS'])  # Set y-axis labels
plt.grid(True)  # Add grid lines for better readability
plt.show()