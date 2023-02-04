import csv
import matplotlib.pyplot as plt

depths = []
ages = []
linsedrates = []

with open("1050.csv", "r") as f:
    r = csv.reader(f)
    for col in r:
        depths.append(float(col[0]))

with open("1050.csv", "r") as f:
    r = csv.reader(f)
    for col in r:
        ages.append(float(col[1]))


def estimate_lsr(s, d, y, o):
    return ((d - s) * 100) / ((o - y) * 1000)


for i in range(0, len(depths)-1):
    linsedrates.append(estimate_lsr(depths[i], depths[i+1], ages[i], ages[i+1]))

#print(linsedrates)

x = []
y = []

for i in range(0, len(linsedrates)-1):
    x.append(ages[i])
    x.append(ages[i + 1])

for i in range(0, len(linsedrates)-1):
    y.append(linsedrates[i])
    y.append(linsedrates[i])

#print(x)
#print(y)

plt.plot(x, y, c="blue")
plt.title('LSR through time plot for ODP Holes 1050A,C')
plt.xlabel('Age (Ma, GTS2012)')
plt.ylabel('Linear Sedimentation Rate (cm/kyr)')
plt.show()