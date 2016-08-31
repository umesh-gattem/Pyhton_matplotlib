import matplotlib.pyplot as plt

'''This example shows to create a figures with different subplots.
By default figure will take 1 as parameter and subplots start from 111 by default.
One figure may have many subplots.Here we introduce another function plt.setp().
 This will describe the line properties.'''
plt.figure(1)
plt.subplot(211)
plt.axis([0, 6, 0, 130])
plt.title("Graph of Squares")
line = plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
plt.setp(line, color='blue', linewidth=5.0)

'''This is second plot of figure 1'''
plt.subplot(212)
plt.plot([1, 2, 3, 4, 5], [1, 8, 27, 64, 125], linewidth=4.0)
plt.show()

'''This is the figure 2 with one subplot. It takes subplot as 111 by default'''
plt.figure(2)
plt.plot([1, 2, 3, 4], [5, 9, 23, 47], linewidth=5.0)
plt.axis([0, 5, 0, 50])
plt.show()
