import csv
import matplotlib.pyplot as plt

types = []
labels = []
depths = []
ages = []

with open("1050_biostrat.csv", "r") as f:
    r = csv.reader(f)
    for col in r:
        types.append(col[0])

with open("1050_biostrat.csv", "r") as f:
    r = csv.reader(f)
    for col in r:
        labels.append(col[1])

with open("1050_biostrat.csv", "r") as f:
    r = csv.reader(f)
    for col in r:
        depths.append(float(col[2]))

with open("1050_biostrat.csv", "r") as f:
    r = csv.reader(f)
    for col in r:
        ages.append(float(col[3]))

age_model_depths = []
age_model_ages = []

with open("1050.csv", "r") as f:
    r = csv.reader(f)
    for col in r:
        age_model_depths.append(float(col[0]))

with open("1050.csv", "r") as f:
    r = csv.reader(f)
    for col in r:
        age_model_ages.append(float(col[1]))

for i in range(0, len(types)):
    if "M" in types[i]:
        plt.scatter(ages[i], depths[i], c="black", marker="D")
    elif "N" in types[i]:
        plt.scatter(ages[i], depths[i], c="green", marker="D")
    elif "F" in types[i]:
        plt.scatter(ages[i], depths[i], c="orange", marker="D")
    elif "R" in types[i]:
        plt.scatter(ages[i], depths[i], c="blue", marker="D")
plt.gca().invert_yaxis()
plt.plot(age_model_ages, age_model_depths, c="blue")
plt.title('Biomagnetostratigraphic synthesis, ODP Holes 1050A,C')
plt.xlabel('Age (Ma, GTS2012)')
plt.ylabel('Depth (cmbsf)')
plt.show()
