""" This code is to plot correlation-ship of each city and using different color
  to identify the inputs we need and inputs we want to dropout"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize']=(12.0, 5.0)

corr = np.array([[]]) # 2D array data of correlation ship coefficients

labels = ['Inp-1','Inp-2', 'Inp-3', 'Inp-4', 'Inp-5', 'Inp-6', 'Inp-7', 'Inp-8', 'Inp-9', 
          'Inp-10', 'Inp-11', 'Inp-12', 'Inp-13', 'Inp-14', 'Inp-15'] 
cities = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N']
numbers = ['(a)','(b)','(c)','(d)','(e)','(f)','(g)','(h)','(i)','(j)','(k)','(l)','(m)','(n)']

# below code is to loop data of different cities and change the color of bars according to a certain threshold.
for i in range(14):
    barlist = plt.bar(labels,abs(corr[:,i]), color = '#003AFE',width=0.5)  # light blue
    for j in range(15):
        if abs(corr[j,i]) < 0.6:
            barlist[j].set_color('#BFBFBF')  # grey

    plt.grid(True)

    plt.xticks(size = 17,rotation = 90,fontname='Palatino Linotype')
    plt.yticks(size = 17,fontname='Palatino Linotype')
    plt.xlabel(" Xlabel {}".format(cities[i]),fontdict={'fontname':'Palatino Linotype','fontsize':20}) #str(numbers[i]) +
    plt.ylim(0,1)
    plt.savefig("yourpath\\corr{}.png".format(cities[i]), dpi=330,bbox_inches = 'tight')
    plt.clf()
