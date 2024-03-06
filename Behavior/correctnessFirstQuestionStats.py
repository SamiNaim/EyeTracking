import os
import pandas as pd
from scipy.stats import chi2
from scipy.stats import kruskal

path = "C:/Users/User/Desktop/Uni/Bachelorarbeit/Analysis/PlayGround"
raw_data = {'correct': [0, 0, 0, 0], 'semiCorrect': [0, 0, 0, 0],'wrong': [0, 0, 0, 0],'notKnow': [0, 0, 0, 0]}

def getStrat(task):
    strat = task[:-1]
    strat = strat[-3:]
    if strat == "tcs":
        return 0
    elif strat == "Cas":
        return 1
    elif strat == "Cos":
        return 2
    else:
        return 3
    
def checkBoard(answer, nr, strat):
    if nr == 1:
        if answer == "Player 1 Lost!":
            raw_data['correct'][strat] += 1
        elif answer == "Player 2 Lost!":
            raw_data['semiCorrect'][strat] += 1
        elif answer == "Player 2 Won!":
            raw_data['wrong'][strat] += 1
        else:
            raw_data['notKnow'][strat] += 1
    elif nr == 2:
        if answer == "Checks whether a, b, and c are either 1 or 2":
            raw_data['correct'][strat] += 1
        elif answer == "Check whether only a is not equal to 0":
            raw_data['semiCorrect'][strat] += 1
        elif answer == "Always returns true":
            raw_data['wrong'][strat] += 1
        else:
            raw_data['notKnow'][strat] += 1
    else:
        if answer == "The makeMove() method":
            raw_data['correct'][strat] += 1
        elif answer == "The main method":
            raw_data['semiCorrect'][strat] += 1
        elif answer == "The player is static":
            raw_data['wrong'][strat] += 1
        else:
            raw_data['notKnow'][strat] += 1
    
def checkBuffer(answer, nr, strat):
    if nr == 1:
        if answer == "null null 15":
            raw_data['correct'][strat] += 1
        elif answer == "2 3 15":
            raw_data['semiCorrect'][strat] += 1
        elif answer == "2 3 10":
            raw_data['wrong'][strat] += 1
        else:
            raw_data['notKnow'][strat] += 1
    elif nr == 2:
        if answer == "No, there is not":
            raw_data['correct'][strat] += 1
        elif answer == "Yes, by calling nextExample()":
            raw_data['semiCorrect'][strat] += 1
        elif answer == "Yes, by calling nextS()":
            raw_data['wrong'][strat] += 1
        else:
            raw_data['notKnow'][strat] += 1
    else:
        if answer == "The output is \"2 3 15\"":
            raw_data['correct'][strat] += 1
        elif answer == "The output is \"2 3 10\"":
            raw_data['semiCorrect'][strat] += 1
        elif answer == "Nothing changes":
            raw_data['wrong'][strat] += 1
        else:
            raw_data['notKnow'][strat] += 1
    
def checkSnake(answer, nr, strat):
    if nr == 1:
        if answer == "Game Over!":
            raw_data['correct'][strat] += 1
        elif answer == "Two times \"Game Over!\"":
            raw_data['semiCorrect'][strat] += 1
        elif answer == "Nothing":
            raw_data['wrong'][strat] += 1
        else:
            raw_data['notKnow'][strat] += 1
    elif nr == 2:
        if answer == "Top-left corner":
            raw_data['correct'][strat] += 1
        elif answer == "Bottom-left corner":
            raw_data['semiCorrect'][strat] += 1
        elif answer == "Centered":
            raw_data['wrong'][strat] += 1
        else:
            raw_data['notKnow'][strat] += 1
    else:
        if answer == "The direction stays \'R\'":
            raw_data['correct'][strat] += 1
        elif answer == "The direction changes to \'L\'":
            raw_data['semiCorrect'][strat] += 1
        elif answer == "An exception is raised":
            raw_data['wrong'][strat] += 1
        else:
            raw_data['notKnow'][strat] += 1
    
def checkString(answer, nr, strat):
    if nr == 1:
        if answer == "I did not eat anything today.!":
            raw_data['correct'][strat] += 1
        elif answer == "I did not eat anything today":
            raw_data['semiCorrect'][strat] += 1
        elif answer == "I Did Not Eat Anything Today":
            raw_data['wrong'][strat] += 1
        else:
            raw_data['notKnow'][strat] += 1
    elif nr == 2:
        if answer == "Removes only the last character if it is equal to \"end\"":
            raw_data['correct'][strat] += 1
        elif answer == "Removes the last occurrence of \"end\"":
            raw_data['semiCorrect'][strat] += 1
        elif answer == "Removes all ending characters that equal \"end\"":
            raw_data['wrong'][strat] += 1
        else:
            raw_data['notKnow'][strat] += 1
    else:
        if answer == "Nothing":
            raw_data['correct'][strat] += 1
        elif answer == "The first word returns to lowercase":
            raw_data['semiCorrect'][strat] += 1
        elif answer == "The second word is capitalized":
            raw_data['wrong'][strat] += 1
        else:
            raw_data['notKnow'][strat] += 1

def collectData(file):
    df = pd.read_csv(file, sep = ';')
    for index, row in df.iterrows():
        
        if row["Task"].startswith("Board"):
            if row["Task"].endswith("1"):
                checkBoard(row["Answer1"], 1, getStrat(row["Task"]))
                
        elif row["Task"].startswith("Buffer"):
            if row["Task"].endswith("1"):
                checkBuffer(row["Answer1"], 1, getStrat(row["Task"]))
                
        elif row["Task"].startswith("Snake"):
            if row["Task"].endswith("1"):
                checkSnake(row["Answer1"], 1, getStrat(row["Task"]))
                
        elif row["Task"].startswith("String"):
            if row["Task"].endswith("1"):
                checkString(row["Answer1"], 1, getStrat(row["Task"]))

for folder_name in os.listdir(path):
    if folder_name.endswith(".py"):
        continue
    folder = path + '/' + folder_name
    for file_name in os.listdir(folder):
        file = folder + '/' + file_name
        if file_name.startswith("Results"):
            collectData(file)

# Define the counts of answers for each group
group1 = [raw_data[key][0] for key in raw_data]
group2 = [raw_data[key][1] for key in raw_data]
group3 = [raw_data[key][2] for key in raw_data]
group4 = [raw_data[key][3] for key in raw_data]

statistic_k, p_value_k = kruskal(group1, group2, group3, group4)
print("Kruskal-Wallis Test:")
print("Statistic:", statistic_k)
print("p-value:", p_value_k)

freedom = len(group1) - 1
alpha = 0.05

critical = chi2.ppf(alpha, freedom)

print("Critical Value:", critical)

print(group1)
print(group2)
print(group3)
print(group4)