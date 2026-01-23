import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(r"C:\Users\welcome\OneDrive\Desktop\TAI LIEU HOC\TRÍ TUỆ NHÂN TẠO\PYTHON CBAN\image2.txt" , skiprows=1)

plt.plot(data[:, 0])   # vẽ cột 0
plt.title("Column 0")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(data, cmap="viridis")
plt.show()

import plotly.express as px
import pandas as pd

df = pd.DataFrame(data)
fig = px.line(df)
fig.show()
