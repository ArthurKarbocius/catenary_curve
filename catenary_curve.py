#=============================================================================================================================
# Initial input values of max. catenary (Latin. l: chain) length S, and max. distance L=(0, S) between two loose ends A and B:
S = 300
L = 275
#=============================================================================================================================
# Maximum curve's height measured from point y=0:
y0 = S / 2
# Curve's midpoint between A=0 and B=L:
x0 = L / 2

# Catenary curve array data set. 
#    Inside cat_array indices are: 
#    [0] - catenary (Latin. l: chain) curve midpoint [x0], it is distance between two loose ends A and B. 
#    [1] - initial angle [theta0] of curve at two loose ends A and B measured in degree units. 
#    [2] - minimum tiping point altitude measured from x-axis - parameter [a]. 
#    [3] - total curve length [S=200].All parameters been obtained by trial and error by applying manual  
#          calculation from variable x0 by step 1 with a task of S=200 length curve as a benchmark value.    

# Scalar needed for parameter values exrtrapolation from an array:
s = y0 / 100    

cat_array = [
[0.0 * s,  90.0,  0.0 * s,     200.0 * s], 
[1.0 * s,  89.92, 0.15 * s,  199.966 * s],
[2.0 * s,  89.82, 0.32 * s,   199.97 * s],  
[3.0 * s,  89.71, 0.53 * s,  199.922 * s],
[4.0 * s,  89.59, 0.72 * s,  199.966 * s], 
[5.0 * s,  89.46, 0.945 * s, 199.956 * s], 
[6.0 * s,  89.33, 1.18 * s,  199.952 * s], 
[7.0 * s,  89.19, 1.43 * s,  199.939 * s],  
[8.0 * s,  89.04, 1.66 * s,  200.002 * s], 
[9.0 * s,  88.88, 1.95 * s,  199.942 * s], 
[10.0 * s, 88.73, 2.2 * s,   200.006 * s], 
[11.0 * s, 88.53, 2.5 * s,   199.969 * s], 
[12.0 * s, 88.35, 2.8 * s,   199.956 * s], 
[13.0 * s, 88.17, 3.1 * s,   199.965 * s], 
[14.0 * s, 88.03, 3.4 * s,   199.996 * s], 
[15.0 * s, 87.79, 3.75 * s,  199.927 * s], 
[16.0 * s, 87.6,  4.05 * s,  199.999 * s], 
[17.0 * s, 87.4,  4.4 * s,   199.973 * s], 
[18.0 * s, 87.19, 4.75 * s,  199.967 * s], 
[19.0 * s, 86.98, 5.1 * s,   199.981 * s], 
[20.0 * s, 86.81, 5.46 * s,  199.992 * s], 
[21.0 * s, 86.58, 5.85 * s,  199.953 * s], 
[22.0 * s, 86.36, 6.21 * s,  200.002 * s], 
[23.0 * s, 86.07, 6.6 * s,     200.0 * s], 
[24.0 * s, 85.82, 7.0 * s,   199.996 * s], 
[25.0 * s, 85.64, 7.42 * s,  199.968 * s], 
[26.0 * s, 85.39, 7.85 * s,  199.935 * s], 
[27.0 * s, 85.13, 8.25 * s,  199.988 * s], 
[28.0 * s, 84.87, 8.7 * s,   199.949 * s], 
[29.0 * s, 84.59, 9.15 * s,  199.929 * s], 
[30.0 * s, 84.32, 9.6 * s,   199.929 * s], 
[31.0 * s, 84.04, 10.05 * s, 199.947 * s], 
[32.0 * s, 83.67, 10.5 * s,  199.983 * s], 
[33.0 * s, 83.45, 11.0 * s,  199.934 * s], 
[34.0 * s, 83.16, 11.45 * s, 200.008 * s], 
[35.0 * s, 82.85, 11.95 * s, 199.996 * s], 
[36.0 * s, 82.53, 12.45 * s, 200.002 * s], 
[37.0 * s, 82.2,  13.0 * s,  199.924 * s], 
[38.0 * s, 81.88, 13.5 * s,   199.97 * s], 
[39.0 * s, 81.54, 14.05 * s, 199.932 * s], 
[40.0 * s, 81.19, 14.6 * s,  199.914 * s], 
[41.0 * s, 80.84, 15.15 * s, 199.916 * s], 
[42.0 * s, 80.48, 15.7 * s,  199.938 * s], 
[43.0 * s, 80.11, 16.25 * s,  199.98 * s], 
[44.0 * s, 79.73, 16.85 * s, 199.942 * s], 
[45.0 * s, 79.34, 17.45 * s, 199.925 * s], 
[46.0 * s, 78.95, 18.05 * s, 199.929 * s], 
[47.0 * s, 78.54, 18.65 * s, 199.954 * s], 
[48.0 * s, 78.14, 19.25 * s,   200.0 * s], 
[49.0 * s, 77.71, 19.9 * s,   199.97 * s], 
[50.0 * s, 77.27, 20.55 * s, 199.963 * s], 
[51.0 * s, 76.83, 21.2 * s,  199.978 * s], 
[52.0 * s, 76.37, 21.9 * s,  199.921 * s], 
[53.0 * s, 75.91, 22.55 * s,  199.98 * s], 
[54.0 * s, 75.43, 23.25 * s,  199.97 * s], 
[55.0 * s, 74.94, 23.95 * s, 199.982 * s], 
[56.0 * s, 74.43, 24.7 * s,  199.928 * s], 
[57.0 * s, 73.92, 25.4 * s,  199.988 * s], 
[58.0 * s, 73.39, 26.15 * s, 199.983 * s], 
[59.0 * s, 72.84, 26.95 * s, 199.914 * s], 
[60.0 * s, 72.29, 27.7 * s,   199.96 * s], 
[61.0 * s, 71.71, 28.5 * s,  199.944 * s], 
[62.0 * s, 71.12, 29.3 * s,  199.954 * s], 
[63.0 * s, 70.51, 30.14 * s, 199.924 * s], 
[64.0 * s, 69.9,  30.95 * s, 199.972 * s], 
[65.0 * s, 69.26, 31.8 * s,  199.981 * s], 
[66.0 * s, 68.59, 32.7 * s,  199.937 * s],
[67.0 * s, 67.91, 33.6 * s,  199.923 * s], 
[68.0 * s, 67.21, 34.5 * s,   199.94 * s], 
[69.0 * s, 66.5,  35.4 * s,  199.988 * s], 
[70.0 * s, 65.76, 36.35 * s, 199.988 * s], 
[71.0 * s, 64.98, 37.35 * s, 199.944 * s], 
[72.0 * s, 64.18, 38.35 * s, 199.936 * s], 
[73.0 * s, 63.36, 39.35 * s, 199.963 * s], 
[74.0 * s, 62.51, 40.4 * s,  199.952 * s], 
[75.0 * s, 61.64, 41.45 * s, 199.978 * s], 
[76.0 * s, 60.72, 42.55 * s, 199.972 * s], 
[77.0 * s, 59.78, 43.65 * s, 200.006 * s], 
[78.0 * s, 58.77, 44.85 * s, 199.943 * s], 
[79.0 * s, 57.76, 46.0 * s,  199.994 * s], 
[80.0 * s, 56.68, 47.25 * s, 199.956 * s], 
[81.0 * s, 55.56, 48.5 * s,  199.968 * s], 
[82.0 * s, 54.4,  49.8 * s,  199.967 * s], 
[83.0 * s, 53.17, 51.15 * s, 199.957 * s], 
[84.0 * s, 51.91, 52.5 * s,  200.004 * s], 
[85.0 * s, 50.52, 54.0 * s,  199.931 * s], 
[86.0 * s, 49.13, 55.45 * s, 199.983 * s], 
[87.0 * s, 47.64, 57.0 * s,   199.99 * s], 
[88.0 * s, 46.03, 58.65 * s, 199.962 * s], 
[89.0 * s, 44.34, 60.35 * s, 199.964 * s], 
[90.0 * s, 42.52, 62.15 * s, 199.954 * s], 
[91.0 * s, 40.62, 64.0 * s,  199.991 * s], 
[92.0 * s, 38.53, 66.0 * s,  199.996 * s], 
[93.0 * s, 36.26, 68.15 * s, 199.991 * s], 
[94.0 * s, 33.73, 70.5 * s,  199.963 * s], 
[95.0 * s, 31.0,  73.0 * s,  199.986 * s], 
[96.0 * s, 27.78, 75.9 * s,  199.928 * s], 
[97.0 * s, 24.27, 79.0 * s,  199.995 * s], 
[98.0 * s, 19.76, 82.95 * s, 199.935 * s], 
[99.0 * s, 14.02, 87.9 * s,  199.972 * s], 
[100.0 * s, 0.0,  100.0 * s,   200.0 * s],
]

# Float x0 convert to an integer before using it as an index:
x0_int = int(x0 / s)

x1 = x0 + y0/100
x2 = cat_array[x0_int][0]

# Extrapolation value of height [a] from array:
a1 = cat_array[x0_int][2]
a2 = cat_array[x0_int + 1][2]
# Linear interpolation of height [a]:
a = a1 - (a1 - a2) * (x0 - x2) / (x1 - x0)

# Catenary curve saging height:
h = y0 - a
print('Saging height h = y0 - a =',round(h, 2))

# Extrapolation value of angle from array:
theta1 = cat_array[x0_int][1]
theta2 = cat_array[x0_int + 1][1]
# Linear interpolation of angle theta:
theta0 = theta1 - (theta1 - theta2) * (x0 - x2) / (x1 - x0)
print('Angle theta0 at points A and B =',round(theta0, 1), 'deg.')

# Check the sum of total length S of our generated catenary curve:
S1 = cat_array[x0_int][3]
S2 = cat_array[x0_int + 1][3]
# Linear interpolation of length S:
S = S1 - (S1 - S2) * (x0 - x2) / (x1 - x0)
print('Total length S =',round(S, 1))

import math
# Calculation of distance b parameter:
b = x0 / math.acosh(y0 / a)   

import numpy as np
import matplotlib.pyplot as plt
# Range from A to B and total number of points to generate smooth curve:
A = -x0
B = x0
num_points = 1000
x_values = np.linspace(A, B, num_points) # equally spaced x values between A and B.

# Hyperbolic cosine function y(x)=a*cosh(x/b) for catenary curve plot:
def y(x):
    return a * np.cosh(x_values / b)  
y = y(x_values)  # Calculation of y values using the function y(x).

# Ploting the curvature:
plt.plot(x0 - x_values, y, label='Catenary', color='black', linewidth=2.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of y(x)=a*cosh((x0 - x)/b)')
plt.grid()
plt.xlim(0, S)  # x-axis range limit from 0 to S.
plt.ylim(0, y0) # y-axis range limit from 0 to y0.

# Calculate the data range for both axes:
x_range = 2 * x0
y_range = y0
# Calculate the aspect ratio to make x and y distance units equal:
aspect = x_range * (S / L/2) / y_range
# Set aspect ratio:
plt.gca().set_aspect(aspect, adjustable='box')

import matplotlib.patches as patches
# Osculating - the circle that has the same tangent, and the same curvature at the point on the curve circle to the plot:
circle = patches.Circle((x0, b**2/a + a), radius=b**2/a, linestyle='--', linewidth=2, edgecolor='red', facecolor='none')
plt.gca().add_patch(circle)
# Visualize the center point of the circle:
plt.scatter(x0, b**2/a + a, color='red', marker='o', s=3)

plt.legend()
plt.show()

















