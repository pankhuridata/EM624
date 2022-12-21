#Author: ---
#Date: ---

# importing libraries
from bokeh.plotting import figure, output_file, show
import numpy as np
import pandas as pd

# reading the file into a pandas structure
df = pd.read_csv('SSE_Faculty.csv')
df.replace(np.nan,0, inplace = True) # replacing the "N/A" with zero

# calculating and printing the number of courses per each program per each Academic Year
df1 = df.groupby(['Program']).agg({'Load 19-20':'sum','Load 20-21':'sum','Load 21-22':'sum','Load 22-23':'sum'})
print ('\n---This the is number of courses per each program per each Academic Year\n', df1)

# calculating and printing the number of courses per faculty per Academic Year
df2 = df[['ID','Load 19-20','Load 20-21','Load 21-22','Load 22-23']].set_index('ID')
print ('\n---This is the number of courses per faculty per Academic Year\n', df2)

# calculating and printing the number of courses per faculty overloaded
#   creating a separate dataframe
df3 = df[['ID','Balance 19-20','Balance 20-21','Balance 21-22','Balance 22-23']].set_index('ID')
# printing the results for the different AYs
print ('\n---Faculty overloaded:')
print ('\n   AY 19-20')
print (df3['Balance 19-20'].where(df3['Balance 19-20']>0).dropna())
print ('\n   AY 20-21')
print (df3['Balance 20-21'].where(df3['Balance 20-21']>0).dropna())
print ('\n   AY 21-22')
print (df3['Balance 21-22'].where(df3['Balance 21-22']>0).dropna())
print ('\n   AY 22-23')
print (df3['Balance 22-23'].where(df3['Balance 22-23']>0).dropna())

# calculating and printing the number of courses per faculty underloaded
#   creating a separate dataframe
tot_underloaded = [] # this is collecting all the underloads per AY
print ('\n---Faculty underloaded:')
print ('\n   AY 19-20')
UL_1 = df3['Balance 19-20'].where(df3['Balance 19-20']<0).dropna()
print (UL_1)
tot_underloaded.append(len(UL_1))
print ('\n   AY 20-21')
UL_2 = df3['Balance 20-21'].where(df3['Balance 20-21']<0).dropna()
print(UL_2)
tot_underloaded.append(len(UL_2))
print ('\n   AY 21-22')
UL_3 = df3['Balance 21-22'].where(df3['Balance 21-22']<0).dropna()
print (UL_3)
tot_underloaded.append(len(UL_3))
print ('\n   AY 22-23')
UL_4 = df3['Balance 22-23'].where(df3['Balance 22-23']<0).dropna()
print(UL_4)
tot_underloaded.append(len(UL_4))


# create the list of values for the programs
EM_values = df1.loc["EM"].values.tolist()
SSW_values = df1.loc["SSW"].values.tolist()
SYS_values = df1.loc["SYS"].values.tolist()

# calculating the average load per faculty per year
loads = [df2["Load 19-20"].mean(), df2["Load 20-21"].mean(), df2["Load 21-22"].mean(), df2["Load 22-23"].mean()]

# ---------creating the Bokeh graphs

# the following will be the same for several graphs
x = [1, 2, 3, 4] # this is the x-axis for most of the graphs
colors = ['royalblue', 'lightslategray', 'lightsteelblue'] # setting colors for the 3 programs

# creating the line graph on programs over years
y = EM_values
y1 = SSW_values
y2 = SYS_values

# initializing the plot
output_file("Programs.html")
p = figure(plot_height=600, title="Programs over years", x_axis_label='Years', y_axis_label='Number of courses')



# plotting
p.line(x, y, legend_label="EM", color=colors[0], line_width=4)
p.line(x, y1, legend_label="SSW", color=colors[1], line_width=4)
p.line(x, y2, legend_label="SYS", color=colors[2], line_width=4)
show(p)


# creating the bar graph on average loads for instructors
# initializing the plot
output_file("Loads.html")
p = figure(plot_height=600, title="Average loads for instructors",  x_axis_label='Years', y_axis_label='Loads')

# plotting
p.vbar(x, top=loads, width=.9, fill_alpha=.5, fill_color=colors[0], line_alpha=.5, line_color=colors[1])
show(p)

# creating the line graph on underloaded faculty over years

# initializing the plot
output_file("Underloads.html")
p = figure(plot_height=600, title="Underloads over years", x_axis_label='Years', y_axis_label='Number of courses')

# plotting
p.line(x, tot_underloaded, color=colors[0], line_width=4)
show(p)


# calculating the courses by program in '22-'23
courses_22_23 = df1["Load 22-23"].values.tolist()

# creating the bar graph on average loads for instructors
# initializing the plot
output_file('Programs_distribution.html')

# defining starts/ends for wedges from percentages of a circle

# calculating the sum of all the values
total = np.sum(courses_22_23)

# calculating the % weight of each element in the list
list_elements = [p/total for p in courses_22_23 ]

# calculating wedges start/end points
elem_overlaps = [0]
last = 0
for i in list_elements:
    last += i
    elem_overlaps.append(last)


# converting these values into starting and ending angles for each element of pie chart
starts = [p*2*np.pi for p in elem_overlaps[:-1]]
ends = [p*2*np.pi for p in elem_overlaps[1:]]

# adding a legend for each wedge
legend = ["EM (%.1f%%)" % (100*list_elements[0]),
          "SSW (%.1f%%)" % (100*list_elements[1]),
          "SYS (%.1f%%)" % (100*list_elements[2])]

# defining the plot characteristics
Pie_chart = figure(x_range=(-1,1), y_range=(-1,1), title='Courses per program in AY22-23')
for i in range(0,3):
    Pie_chart.wedge(x=0, y=0, radius=1, start_angle=starts[i],
                    end_angle=ends[i], color=colors[i], legend_label=legend[i], line_color="white")

# showing the plot
show(Pie_chart)

print ('\n----End of the processing----\n')
