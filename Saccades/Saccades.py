import os
import pandas as pd
import matplotlib.pyplot as plt

pd.options.mode.chained_assignment = None

saccades = {"StCS": [], "CaS": [], "CoS": [], "RaS": []}

def checkPrefix(df, prefix, strat):
    df = df[df['Saccade Target AOI'].str.startswith(prefix)]
    df['Distance'] = df['Distance'].str.replace(',', '.')
    df['Distance'] = df['Distance'].astype(float)
    df['Distance'] = df['Distance'].round()
    df['Distance'] = df['Distance'].astype(int)
    average_length_df = df.groupby('SubjectName')['Distance'].mean().reset_index()
    average_length_df['Distance'] = average_length_df['Distance'].astype(int)
    saccades[strat].extend(average_length_df["Distance"].tolist())
        
path = "C:/Users/User/Desktop/Uni/Bachelorarbeit/Analysis/Eye Tracking Saccades"
for file_name in os.listdir(path):
    if file_name.endswith(".py"):
        continue
    file = path + '/' + file_name
    df = pd.read_csv(file, sep='\t', index_col=False)
    match file_name:
        case "CaCoRaStSaccades.txt":
            checkPrefix(df, "Bo", "CaS")
            checkPrefix(df, "Bu", "CoS")
            checkPrefix(df, "Sn", "RaS")
            checkPrefix(df, "St", "StCS")
        case "CoRaStCaSaccades.txt":
            checkPrefix(df, "Bo", "CoS")
            checkPrefix(df, "Bu", "RaS")
            checkPrefix(df, "Sn", "StCS")
            checkPrefix(df, "St", "CaS")
        case "RaStCaCoSaccades.txt":
            checkPrefix(df, "Bo", "RaS")
            checkPrefix(df, "Bu", "StCS")
            checkPrefix(df, "Sn", "CaS")
            checkPrefix(df, "St", "CoS")
        case "StCaCoRaSaccades.txt":
            checkPrefix(df, "Bo", "StCS")
            checkPrefix(df, "Bu", "CaS")
            checkPrefix(df, "Sn", "CoS")
            checkPrefix(df, "St", "RaS")

# Create the box plot
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
plt.boxplot([saccades["StCS"], saccades["CaS"], saccades["CoS"], saccades["RaS"]], boxprops=dict(color="#59ae70"), medianprops=dict(color="#de7a77"), showfliers=False)

# Add labels and title
plt.ylabel('Average Saccade Length (px)')
plt.xlabel('Method Ordering Strategies')

# Show the plot
plt.xticks([1, 2, 3, 4], ['StCS', 'CaS', 'CoS', 'RaS'])  # Set y-axis labels
plt.grid(True)  # Add grid lines for better readability
plt.show()
