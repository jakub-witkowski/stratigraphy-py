import math

import matplotlib

import stratigraphy as st

import matplotlib.pyplot as plt

import numpy as np

site = st.Site(1050, 'A,C')

types = []
labels = []
min_depths = []
max_depths = []
depths = []
ages = []

tiepoint0 = st.Tiepoint(0, 'pmag', 'B C19n', 4.2, 11.23, 41.39)
types.append(tiepoint0.type)
labels.append(tiepoint0.label)
depths.append(st.average_depth(tiepoint0.min_depth, tiepoint0.max_depth))
min_depths.append(tiepoint0.min_depth)
max_depths.append(tiepoint0.max_depth)
ages.append(tiepoint0.age)

tiepoint1 = st.Tiepoint(1, "pmag", "B C19r", 24.14, 26.41, 42.30)
types.append(tiepoint1.type)
labels.append(tiepoint1.label)
depths.append(st.average_depth(tiepoint1.min_depth, tiepoint1.max_depth))
min_depths.append(tiepoint1.min_depth)
max_depths.append(tiepoint1.max_depth)
ages.append(tiepoint1.age)

tiepoint2 = st.Tiepoint(2, "pmag", "B C20n", 61.62, 62.19, 43.43)
types.append(tiepoint2.type)
labels.append(tiepoint2.label)
depths.append(st.average_depth(tiepoint2.min_depth, tiepoint2.max_depth))
min_depths.append(tiepoint2.min_depth)
max_depths.append(tiepoint2.max_depth)
ages.append(tiepoint2.age)

tiepoint3 = st.Tiepoint(3, "pmag", "B C20r", 137.27, 140.28, 45.72)
types.append(tiepoint3.type)
labels.append(tiepoint3.label)
depths.append(st.average_depth(tiepoint3.min_depth, tiepoint3.max_depth))
min_depths.append(tiepoint3.min_depth)
max_depths.append(tiepoint3.max_depth)
ages.append(tiepoint3.age)

tiepoint4 = st.Tiepoint(4, "pmag", "B C21n", 151.603, 153.190, 47.35)
types.append(tiepoint4.type)
labels.append(tiepoint4.label)
depths.append(st.average_depth(tiepoint4.min_depth, tiepoint4.max_depth))
min_depths.append(tiepoint4.min_depth)
max_depths.append(tiepoint4.max_depth)
ages.append(tiepoint4.age)

tiepoint5 = st.Tiepoint(5, "nanno", "B NP14a", 151.603, 153.190, 49.11)
types.append(tiepoint5.type)
labels.append(tiepoint5.label)
depths.append(st.average_depth(tiepoint5.min_depth, tiepoint5.max_depth))
min_depths.append(tiepoint5.min_depth)
max_depths.append(tiepoint5.max_depth)
ages.append(tiepoint5.age)

tiepoint6 = st.Tiepoint(6, "pmag", "B C22n", 153.71, 154.43, 49.34)
types.append(tiepoint6.type)
labels.append(tiepoint6.label)
depths.append(st.average_depth(tiepoint6.min_depth, tiepoint6.max_depth))
min_depths.append(tiepoint6.min_depth)
max_depths.append(tiepoint6.max_depth)
ages.append(tiepoint6.age)

tiepoint7 = st.Tiepoint(7, "pmag", "T C23n", 182.657, 183.359, 50.63)
types.append(tiepoint7.type)
labels.append(tiepoint7.label)
depths.append(st.average_depth(tiepoint7.min_depth, tiepoint7.max_depth))
min_depths.append(tiepoint7.min_depth)
max_depths.append(tiepoint7.max_depth)
ages.append(tiepoint7.age)

tiepoint8 = st.Tiepoint(8, "nanno", "B C. crassus", 193.2, 194.64, 51.64)
types.append(tiepoint8.type)
labels.append(tiepoint8.label)
depths.append(st.average_depth(tiepoint8.min_depth, tiepoint8.max_depth))
min_depths.append(tiepoint8.min_depth)
max_depths.append(tiepoint8.max_depth)
ages.append(tiepoint8.age)

tiepoint9 = st.Tiepoint(9, "nanno", "B NP12", 193.2, 194.64, 53.7)
types.append(tiepoint9.type)
labels.append(tiepoint9.label)
depths.append(st.average_depth(tiepoint9.min_depth, tiepoint9.max_depth))
min_depths.append(tiepoint9.min_depth)
max_depths.append(tiepoint9.max_depth)
ages.append(tiepoint9.age)

tiepoint10 = st.Tiepoint(10, "pmag", "B C24n", 198.37, 199.08, 53.98)
types.append(tiepoint10.type)
labels.append(tiepoint10.label)
depths.append(st.average_depth(tiepoint10.min_depth, tiepoint10.max_depth))
min_depths.append(tiepoint10.min_depth)
max_depths.append(tiepoint10.max_depth)
ages.append(tiepoint10.age)

tiepoint11 = st.Tiepoint(11, "pmag", "B C24r", 252.95, 253.84, 57.10)
types.append(tiepoint11.type)
labels.append(tiepoint11.label)
depths.append(st.average_depth(tiepoint11.min_depth, tiepoint11.max_depth))
min_depths.append(tiepoint11.min_depth)
max_depths.append(tiepoint11.max_depth)
ages.append(tiepoint11.age)

tiepoint12 = st.Tiepoint(12, "pmag", "B C25n", 257.19, 257.67, 57.66)
types.append(tiepoint12.type)
labels.append(tiepoint12.label)
depths.append(st.average_depth(tiepoint12.min_depth, tiepoint12.max_depth))
min_depths.append(tiepoint12.min_depth)
max_depths.append(tiepoint12.max_depth)
ages.append(tiepoint12.age)

tiepoint13 = st.Tiepoint(13, "pmag", "B C25r", 275.06, 275.54, 58.96)
types.append(tiepoint13.type)
labels.append(tiepoint13.label)
depths.append(st.average_depth(tiepoint13.min_depth, tiepoint13.max_depth))
min_depths.append(tiepoint13.min_depth)
max_depths.append(tiepoint13.max_depth)
ages.append(tiepoint13.age)

tiepoint14 = st.Tiepoint(14, "pmag", "B C26n", 279.02, 279.59, 59.24)
types.append(tiepoint14.type)
labels.append(tiepoint14.label)
depths.append(st.average_depth(tiepoint14.min_depth, tiepoint14.max_depth))
min_depths.append(tiepoint14.min_depth)
max_depths.append(tiepoint14.max_depth)
ages.append(tiepoint14.age)

tiepoint15 = st.Tiepoint(15, "pmag", "B C26r", 331.856, 333.215, 62.22)
types.append(tiepoint15.type)
labels.append(tiepoint15.label)
depths.append(st.average_depth(tiepoint15.min_depth, tiepoint15.max_depth))
min_depths.append(tiepoint15.min_depth)
max_depths.append(tiepoint15.max_depth)
ages.append(tiepoint15.age)

tiepoint16 = st.Tiepoint(16, "pmag", "B C27n", 343.41, 346.49, 62.52)
types.append(tiepoint16.type)
labels.append(tiepoint16.label)
depths.append(st.average_depth(tiepoint16.min_depth, tiepoint16.max_depth))
min_depths.append(tiepoint16.min_depth)
max_depths.append(tiepoint16.max_depth)
ages.append(tiepoint16.age)

# print(types)
# print()
# print(labels)
# print()
# print(depths)
# print()
# print(ages)

# plt.gca().grid()
# plt.scatter(ages, depths, c="cyan", marker="D")

for i in range(0, len(types)):
    if types[i] == 'pmag':
        plt.scatter(ages[i], depths[i], c="cyan", marker="D")
    elif types[i] == 'nanno':
        plt.scatter(ages[i], depths[i], c="blue", marker="D")

plt.plot(ages, depths, c="blue")
plt.gca().invert_yaxis()
plt.title('Age vs depth plot for ODP Holes 1050A,C')
plt.xlabel('Age (Ma, GTS2012)')
plt.ylabel('Depth (cmbsf)')
#matplotlib.figure.Figure.savefig()
plt.show()
