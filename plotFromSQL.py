import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

con = sqlite3.connect("strat.db")
df = pd.read_sql_query("SELECT * FROM strat", con)
con.close()

plt.plot(df['age'], df['avg_depth'], c="blue")
plt.gca().invert_yaxis()
plt.title('Biomagnetostratigraphic synthesis, ODP Holes 1050A,C')
plt.xlabel('Age (Ma, GTS2012)')
plt.ylabel('Depth (cmbsf)')
plt.show()
