import csv
import numpy
import matplotlib.pyplot as plt


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

mymodel = numpy.poly1d(numpy.polyfit(age_model_ages, age_model_depths, 3))

myline = numpy.linspace(42, 66, 100)

plt.scatter(age_model_ages, age_model_depths, c="black", marker="D")
plt.plot(myline, mymodel(myline))
plt.gca().invert_yaxis()
#plt.plot(age_model_ages, age_model_depths, c="blue")
plt.title('Biomagnetostratigraphic synthesis, ODP Holes 1050A,C')
plt.xlabel('Age (Ma, GTS2012)')
plt.ylabel('Depth (cmbsf)')
plt.show()
