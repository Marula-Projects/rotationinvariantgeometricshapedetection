Solution in Theory

The general approximation of the solution can be expressed in following steps:
 First the contour points and the center point of each polygon are located.
 Next for each polygon, the distance (radius) and the angle of each contour point relative to the center is obtained.
 Distances from center of the shape to the contour points are stored and sorted with respect to angles they make with the x axis. As depicted in following figure distances are stored in array with their ascending angle order from (pi) to (- pi) like d1, d2, d3, d4 ...
 This array actually represents a distribution of distance measures over ascending angles from (- pi) to (pi). Distance will increase as we move towards the vertices of the polygon and decreases as we move towards middle of the polygon's edges. This distribution is depicted as follow for different polygons:
As shown in the above figure, becasue the resulted distributions are already sinosoidal waves with the frequency equal to the number of polygon edges, lets say n, thus applying a Discrete Fourier Transform (DFT) to distribution will result in a fourier expression with the biggest coefficient in its n'th term. Therefore the greatest coefficient's term index will represent the polygon's number of edges. Following expressions belong to different polygons that shows this fact explicitely:
