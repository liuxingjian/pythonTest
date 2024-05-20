# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt


num_list1 = [2.5, 0.6, 3.8, 6.6,1.2,9.5,4.2]
num_list2 = [-6.6,-1.2,-3.5,-4.2,-2.5, -3.6, -10]


name_list = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

plt.bar(range(len(num_list1)), num_list1,color='r',label='girl',tick_label=name_list)

plt.bar(range(len(num_list2)), num_list2,color='y',label='boy',tick_label=name_list)

plt.legend()

plt.show()