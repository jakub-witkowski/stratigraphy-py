import csv

import plotAgeVsDepth

age_model_table = []

#depths_as_cols = []

#with open("1050.csv", "r") as f:
#    r = csv.reader(f)
#    for col in r:
#        depths_as_cols.append(col[0])

#print(depths_as_cols)

#depths_as_rows = []

#with open("1050.csv", "r") as f:
#    r = csv.reader(f)
#    for row in r:
#        depths_as_rows.append(row[1])

#print(depths_as_rows)

with open("1050_table.csv", "w", newline = '') as f:
    write = csv.writer(f, delimiter=",")
    for i in range (0, len(plotAgeVsDepth.depths)):
        write.writerow(plotAgeVsDepth.depths[0], plotAgeVsDepth.ages[0], plotAgeVsDepth.types[0])
