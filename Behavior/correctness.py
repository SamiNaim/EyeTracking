import os
import pandas as pd
import matplotlib.pyplot as plt

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
            elif row["Task"].endswith("2"):
                checkBoard(row["Answer2"], 2, getStrat(row["Task"]))
            elif row["Task"].endswith("3"):
                checkBoard(row["Answer3"], 3, getStrat(row["Task"]))
                
        elif row["Task"].startswith("Buffer"):
            if row["Task"].endswith("1"):
                checkBuffer(row["Answer1"], 1, getStrat(row["Task"]))
            elif row["Task"].endswith("2"):
                checkBuffer(row["Answer2"], 2, getStrat(row["Task"]))
            elif row["Task"].endswith("3"):
                checkBuffer(row["Answer3"], 3, getStrat(row["Task"]))
                
        elif row["Task"].startswith("Snake"):
            if row["Task"].endswith("1"):
                checkSnake(row["Answer1"], 1, getStrat(row["Task"]))
            elif row["Task"].endswith("2"):
                checkSnake(row["Answer2"], 2, getStrat(row["Task"]))
            elif row["Task"].endswith("3"):
                checkSnake(row["Answer3"], 3, getStrat(row["Task"]))
                
        elif row["Task"].startswith("String"):
            if row["Task"].endswith("1"):
                checkString(row["Answer1"], 1, getStrat(row["Task"]))
            elif row["Task"].endswith("2"):
                checkString(row["Answer2"], 2, getStrat(row["Task"]))
            elif row["Task"].endswith("3"):
                checkString(row["Answer3"], 3, getStrat(row["Task"]))

for folder_name in os.listdir(path):
    if folder_name.endswith(".py"):
        continue
    folder = path + '/' + folder_name
    for file_name in os.listdir(folder):
        file = folder + '/' + file_name
        if file_name.startswith("Results"):
            collectData(file)

# Data
r = [0,1,2,3]
df = pd.DataFrame(raw_data)

# From raw value to percentage
totals = [i+j+k+l for i,j,k,l in zip(df['correct'], df['semiCorrect'], df['wrong'], df['notKnow'])]
correct = [i / j * 100 for i,j in zip(df['correct'], totals)]
semiCorrect = [i / j * 100 for i,j in zip(df['semiCorrect'], totals)]
wrong = [i / j * 100 for i,j in zip(df['wrong'], totals)]
notKnow = [i / j * 100 for i,j in zip(df['notKnow'], totals)]

# plot
barWidth = 0.6
names = ('StCS','CaS','CoS','RaS')
# Create green Bars
plt.bar(r, correct, color='#59ae70', width=barWidth, label="Correct")
# Create orange Bars
plt.bar(r, semiCorrect, bottom=correct, color='#80c694', width=barWidth, label="Partially correct")
# Create blue Bars
plt.bar(r, wrong, bottom=[i+j for i,j in zip(correct, semiCorrect)], color='#af5151', width=barWidth, label="Wrong")
# Create blue Bars
plt.bar(r, notKnow, bottom=[i+j+l for i,j,l in zip(correct, semiCorrect, wrong)], color='#de7a77', width=barWidth, label="I do not know")

# Custom x axis
plt.xticks(r, names)
plt.xlabel("Method Ordering Strategies")
plt.ylabel("Percentage")

# Add a legend
plt.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1)

# Show graphic
plt.show()