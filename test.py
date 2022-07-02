from matplotlib import pyplot as plt

plt.plot([0, 3050], [0, 0], 'k-')
plt.plot([0, 3050], [1950 , 1950], 'k-')
plt.plot([3050 , 3050], [1950 , 0], 'k-')
plt.plot([0 , 0], [0, 1950], 'k-')

plt.plot([0, 0], [0, 5000], 'k-')
plt.plot([0, 5000], [5000, 5000], 'k-')
plt.plot([5000, 5000], [5000, 0], 'k-')
plt.plot([5000, 0], [0, 0], 'k-')

plt.plot([0, 0], [0, 12000], 'k-')
plt.plot([0, 12000], [12000, 12000], 'k-')
plt.plot([12000, 12000], [12000, 0], 'k-')
plt.plot([12000, 0], [0, 0], 'k-')

plt.scatter(1500, 1500, c="r", s=100)
plt.scatter(2500, 2000, c="r", s=100)
plt.scatter(-2000, 2000, c="r", s=100)
plt.scatter(0, 15000, c="r", s=100)
plt.xlabel("x (mm)", fontsize=20)
plt.ylabel("y (mm)", fontsize=20)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.axis('equal')
plt.show()