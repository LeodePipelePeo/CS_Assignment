import pandas as pd
import matplotlib.pyplot as plt

year = []
wo = []
beer_consumption = []

df = pd.read_csv("istherecorrelation.csv", sep=';', decimal=',')
print(df.corr())

plt.rcParams['figure.figsize'] = [10,5]
fig, ax1 = plt.subplots()

ax1.set_ylabel('NL Beer consumption [x1000 hectoliter]', color = 'tab:red')
ax1.plot(df['Year'],df['NL Beer consumption [x1000 hectoliter]'], color = 'tab:red', linewidth= 1)

ax2 = ax1.twinx()
ax2.set_ylabel('WO [x1000]', color = 'tab:blue')
ax2.plot(df['Year'],df['WO [x1000]'], color = 'tab:blue', linewidth= 1)



plt.title("NL beer consumption and WO", fontsize = 15)
plt.savefig('beer.png', dpi=300)
