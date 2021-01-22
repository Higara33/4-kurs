import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'A': [1, 2, 3, 4],
                   'B': [1, 2, 3, 4]})
print(df, '\n')
df = df.replace({'A': {1: 11, 2: 22}})
plt.figure()
df.plot()
