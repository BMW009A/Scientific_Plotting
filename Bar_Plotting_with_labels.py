""" This code aims to plot horizontal bar figure in which each bar has two columns """
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['figure.figsize']=(9.0, 5.0)

labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
io = 'C:\\yourdata.xlsx'

plt.rcParams['xtick.direction'] = 'in'   # inner xtick
plt.rcParams['font.sans-serif'] = ['SimSun']  # display Chinese

# data = pd.read_excel(io = io)  # read data using pandas
# print(data)

data_1= np.array(yourdata)  # fit your data into numpy array
data_2= np.array(yourdata)  # fit your data into numpy array

x = np.arange(len(labels))  # the label locations
width = 0.9  # the width of the bars
y_pos = np.linspace(0,26,14)  # define the middle position of two bars

fig, ax = plt.subplots()
rects1 = ax.barh(y_pos - width/2, # adjust vertical position of  bar 1. (It is recommended not to modify)
                 data_1, 
                 width, label='XX', edgecolor="k",color='grey', alpha = 0.6) # using "hatch ='///' " when you want the contrast theme
rects2 = ax.barh(y_pos + width/2, # adjust vertical position of  bar 2. (It is recommended not to modify)
                 data_2, 
                 width, label='XX', color='white', edgecolor="k") # using "hatch ='\\\\\\' " when you want the contrast theme

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('X', fontsize = 14.5, weight = 'heavy')
ax.set_ylabel('Y', fontsize = 14.5, weight = 'heavy')
ax.set_xticks(range(0,int(max(pollution_total_2030)+200),100), # Define the xticks according to the max value of your data
              fontsize = 14, 
              family ='Times New Roman', 
              weight = 'heavy')
ax.set_yticks(y_pos, labels, fontsize = 10, family ='SimSun')

ax.bar_label(rects1, fontsize = 9.5, family ='Times New Roman') # add "label_type='center' " to center the label
ax.bar_label(rects2, fontsize = 9.5, family ='Times New Roman')

font1 = {'family' : 'Times New Roman', 'weight' : 'normal', 'size' : 10,}
ax.legend(prop=font1)

ax.invert_yaxis()  # labels read top-to-bottom

plt.savefig('C:yourpath\\Horz_bar.png', dpi=330,bbox_inches = 'tight')
plt.show()
