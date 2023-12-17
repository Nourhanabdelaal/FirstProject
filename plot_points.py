points_2D = [(1,2), (2,4), (0,0), (5,4)]

import matplotlib.pyplot as plt

xs = [i[0] for i in points_2D]
ys = [i[1] for i in points_2D]

plt.plot(xs, ys, 'o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Points_2D')
plt.show()
plt.savefig('Points_2D')

print('""""""""""""""3D"""""""""""""')

import matplotlib.pyplot as pltt

points_3D = [[1, 2, 4], [2, 4, 3], [0, 0, 1], [5, 4, 0]]

x = [i[0] for i in points_3D]
y = [i[1] for i in points_3D]
z = [i[2] for i in points_3D]

fig = pltt.figure()
ax = fig.add_subplot(projection = '3d')
ax.scatter(x, y, z, '*')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
pltt.show()
pltt.savefig('Points3D')









