#Author: Pankhuri


from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


def get_index(parts):                                                  # to create a dataframe

    if parts[3] == "0-24":
        return 0
    elif parts[3] == "25-34":
        return 1
    elif parts[3] == "35-44":
        return 2
    elif parts[3] == "45-54":
        return 3
    elif parts[3] == "55-64":
        return 4
    elif parts[3] == "65-74":
        return 5
    elif parts[3] == "75-84":
        return 6
    elif parts[3] == "85+":
        return 7

counts_conditions = [0, 0, 0, 0, 0, 0, 0, 0]                                 #To create list of counters
counter_dict= []
with open('covid_comorbidities_USsummary.csv', 'r') as covid:

    for i in covid:                                                # create a loop for split white space
        line = i.strip().split(",")
        if line[0] == "COVID-19" and line[3] == '0-24':
            counter_dict.append(line[4])

        if line[0] == "COVID-19" and line[3] == '25-34':
            counter_dict.append(line[4])

        if line[0] == "COVID-19":                                      # skip covid-19 row
            pass
        else:
            index = get_index(line)
            if index is None:
                pass
            else:
                counts_conditions[index] += int(line[4])                       # to add all data

print('Number of deaths per each one of the 8 age categories:',counts_conditions)
print('The comorbidity with the highest number of Covid deaths for the population of less than 35 years of age:',counter_dict)

count=[]
with open('covid_comorbidities_USsummary.csv', 'r') as file:
  for i in file:  # create a loop for split white space
    line = i.strip().split(",")
    if line[0] == "COVID-19" and line[3] == '0-24':
        count.append(line[4])

    if line[0] == "COVID-19" and line[3] == '25-34':
        count.append(line[4])

    if line[0] == "COVID-19" and line[3] == '35-44':
        count.append(line[4])

    if line[0] == "COVID-19" and line[3] == '45-54':
        count.append(line[4])

    if line[0] == "COVID-19" and line[3] == '55-64':
        count.append(line[4])

    if line[0] == "COVID-19" and line[3] == '65-74':
        count.append(line[4])

    if line[0] == "COVID-19" and line[3] == '75-84':
        count.append(line[4])

    if line[0] == "COVID-19" and line[3] == '85+':
        count.append(line[4])

print('Number of deaths due to COVID-19 per each one of the 8 age categories:',count)

a=counts_conditions
b=count
numbers = np.array([a,b])
newnumbers = numbers.astype(float)
matrix = np.corrcoef(newnumbers)                    # Compute the correlation matrix
print('The Correlation matrix:\n',matrix)
mask = np.triu(np.ones_like(matrix, dtype=bool))      # Generate a mask for the upper triangle

f, ax = plt.subplots(figsize=(11, 9))                # Set up the matplotlib figure

cmap = sns.diverging_palette(230, 20, as_cmap=True)        # Generate a custom diverging colormap

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(matrix, mask=mask, cmap=cmap, vmax=.3, center=0,square=True, linewidths=.5, cbar_kws={"shrink": .5})

x = ['0-24', '25-34', '35-44', '45-54', '55-64', '65-74', '75-84', '85+']
y = counts_conditions
labels = x
fig, (cx1,cx2) = plt.subplots(1,2, figsize = (12,6))                      # to create subplot
cx1.bar(x,y)                                                               #bar graph
cx1.set_xlabel("Class_Ages")
cx1.set_ylabel("Count")

cx2.pie(y, autopct='%.3f%%',labels=labels, pctdistance=1.2, labeldistance=1.3)   #pie chart
cx2.axis('equal')

plt.title("The comorbidity with the highest number of deaths for the population")

fig.tight_layout()

plt.show()


print('This is the end of the files processing')