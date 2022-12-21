#Author: Pankhuri
#Description: This program will create four plots from data using pandas and bokeh.

import pandas as pd
from math import pi
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.palettes import Category20c
from bokeh.plotting import figure, show
from bokeh.transform import cumsum

df = pd.read_csv('SSE_Faculty.csv')                 #read the csv file

a=df.groupby(['Program'])['Load 19-20'].agg('sum')                 #finding the number of courses using groupby function of pandas
print('Number of courses per program in year 19-20: \n', a.to_string())
b=df.groupby(['Program'])['Load 20-21'].agg('sum')
print('Number of courses per program in year 20-21: \n', b.to_string())
c=df.groupby(['Program'])['Load 21-22'].agg('sum')
print('Number of courses per program in year 21-22: \n', c.to_string())
d=df.groupby(['Program'])['Load 22-23'].agg('sum')
print('Number of courses per program in year 22-23: \n', d.to_string())

print('\n')
e=df.groupby(['ID'])[['Load 19-20','Load 20-21', 'Load 21-22','Load 22-23']].mean()   #finding the avg of courses by each professor using inbuilt mean
print('Average number of courses per faculty per Academic Year: \n', e.to_string())

print('\n')
limit = 0                                                #finding the number of faculty who are underloaded
column = df['Balance 19-20']
count1 = column[column < limit].count()
print('Number of faculty who are underloaded in the year 19-20:', count1)

column = df['Balance 20-21']
count2 = column[column < limit].count()
print('Number of faculty who are underloaded in the year 20-21:', count2)

column = df['Balance 21-22']
count3 = column[column < limit].count()
print('Number of faculty who are underloaded in the year 21-22:', count3)

column = df['Balance 22-23']
count4 = column[column < limit].count()
print('Number of faculty who are underloaded in the year 22-23:', count4)

print('\n')

limit = 0                                                #finding the number of faculty who are overloaded
column = df['Balance 19-20']
count5 = column[column > limit].count()
print('Number of faculty who are overloaded in year 19-20:', count5)

column = df['Balance 20-21']
count6 = column[column > limit].count()
print('Number of faculty who are overloaded in year 20-21:', count6)

column = df['Balance 21-22']
count7 = column[column > limit].count()
print('Number of faculty who are overloaded in year 21-22:', count7)

column = df['Balance 22-23']
count8 = column[column > limit].count()
print('Number of faculty who are overloaded in year 22-23:', count8)


#plot graph using Bokeh

#1st plot
# file to save the model
output_file("line1.html")

# instantiating the figure object
graph = figure(title="Courses per program per Academic Year")

# name of the x-axis
graph.xaxis.axis_label = "Years"

# name of the y-axis
graph.yaxis.axis_label = "Courses"

# plotting line 1
# generating the points to be plotted
x = [19,20,21,22]
y = [39,29,48,52]

# parameters of line 1
line_color = "red"
line_dash = "solid"
legend_label = "EM"

# plotting the line
graph.line(x, y,
           line_color=line_color,
           line_dash=line_dash,
           legend_label=legend_label)

# plotting line 2
# generating the points to be plotted
x = [19,20,21,22]
y = [3,6,19,24]

# parameters of line 2
line_color = "green"
line_dash = "solid"
legend_label = "SSW"

# plotting the line
graph.line(x, y,
           line_color=line_color,
           line_dash=line_dash,
           legend_label=legend_label)

# plotting line 3
# generating the points to be plotted
x = [19,20,21,22]
y = [28,28,31,22]

# parameters of line 3
line_color = "blue"
line_dash = "solid"
legend_label = "SYS"

# plotting the line
graph.line(x, y,
           line_color=line_color,
           line_dash=line_dash,
           legend_label=legend_label)

# displaying the model
show(graph)

#2nd graph
output_file("bar.html")

# the points to be plotted
ID = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27']
years = ["2019", "2020", "2021", "2022"]
colors = ["#c9d9d3", "#718dbf", "#e84d60","#ffe136"]

data = {'ID' : ID,
        '2019'   : [6,0,3,2,2,0,2,1,0,3,2,6,0,6,5,6,2,0,0,2,9,2,0,2,0,0,9],
        '2020'   : [4,0,3,3,3,0,3,2,0,1,3,7,0,3,3,1,3,1,1,2,6,3,0,3,0,0,8],
        '2021'   : [8,1,3,2,3,0,3,4,2,3,2,4,3,9,6,9,3,1,5,2,6,5,1,1,0,7,5],
        '2022'   : [8,2,3,3,4,5,3,3,4,2,1,0,2,5,5,8,2,2,3,2,3,4,2,4,5,5,8]}

p = figure(x_range=ID, height=250, title="Average number of courses per faculty over the years",
           toolbar_location=None, tools="")

p.vbar_stack(years, x='ID', width=0.9, color=colors, source=data,
             legend_label=years)

p.y_range.start = 0
p.x_range.range_padding = 0.1
p.xgrid.grid_line_color = None
p.axis.minor_tick_line_color = None
p.outline_line_color = None
p.legend.location = "top_left"
p.legend.orientation = "horizontal"
p.xaxis.axis_label = "ID"
p.yaxis.axis_label = "Number of courses"

# displaying the model
show(p)


#3rd Plot
output_file("line2.html")

# instantiating the figure object
graph = figure(title="Number of underloaded faculty over the years")

# name of the x-axis
graph.xaxis.axis_label = "Years"

# name of the y-axis
graph.yaxis.axis_label = "ID"

# the points to be plotted
x = [20,21,22,23]
y = [11, 5, 8, 9]

# color of the line
line_color = "red"

# type of line
line_dash = "solid"

# offset of line dash
line_dash_offset = 1


# plotting the line graph
graph.line(x, y,
           line_color=line_color,
           line_dash=line_dash,
           line_dash_offset=line_dash_offset,
           )

# displaying the model
show(graph)

#4th plot
output_file("pie.html")
# generating the points to be plotted
x = {
    'EM': 52,
    'SWS': 24,
    'SYS': 22
}

data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'program'})
data['angle'] = data['value']/data['value'].sum() * 2*pi
data['color'] = Category20c[len(x)]

p1 = figure(height=350, title="Courses by program in '22-'23", toolbar_location=None,
           tools="hover", tooltips="@program: @value", x_range=(-0.5, 1.0))

p1.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="black", fill_color='color', legend_field='program', source=data)

p1.axis.axis_label = None
p1.axis.visible = False
p1.grid.grid_line_color = None

# displaying the model
show(p1)


