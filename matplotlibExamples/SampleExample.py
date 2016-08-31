import matplotlib.pyplot as plt
import numpy as np

'''The following three lines will us used to draw a graph between two axis.
The Y axis label is some numbers and it takes the numbers from 1,2,3,4.
Here X axis values are not specified but it takes the same values as Y axis .
But x axis starts values from 0 and ends at 3.0 as axis length is 4.'''
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')

'''The following three lines used to plot a graph between two axis.
Here X axis takes the  values and Y axis takes the squares of the values taken in x axis.
the third parameter 'ro' is nothing but r means red color and 'o' means shape of the plotting.
This graph takes red circles to plot the values. plt.axis() gives the boundaries of the graph .
In the following graph X axis boundaries is 0-6 and Y axis boundaries is 0-20 .'''
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])

''' Here we have taken the list of numbers by using arange function of the numpy.
 arange functions takes the three parameters , first one is starting index,
 second one is stopping index, third one is interval .
 It means following statement takes the index from 0 to 5 with 0.2 interval .Y axis takes squares of the X axis.'''
list_numbers = np.arange(0.0, 5.0, 0.2)
plt.plot(list_numbers, list_numbers ** 2, 'ro', list_numbers, list_numbers ** 3, 'b^')
plt.axis([0, 6, 0, 130])

# The following statement mentions about the width of the line plotted.
line,  = plt.plot(list_numbers, list_numbers + 5, linewidth=5.0)
plt.title("Line Width is 2.0")
plt.axis([0, 6, 0, 30])

'''The following statements use the keyword anti aliased which means line should me aliased or not.'''
plt.plot(list_numbers, list_numbers + 2, antialiased='False')
plt.axis([0, 6, 0, 30])
plt.show()


