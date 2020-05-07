import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
sns.set()
sns.set_style("darkgrid")
df = pd.read_csv("https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv")
df.rename(columns = {"Country/Region":"Country"},inplace=True)
df.drop(["Province/State","Lat","Long"],axis=1,inplace=True)
df.Date = pd.to_datetime(df.Date)
SW = df[df["Country"] == "Sweden"]
SW["NewDeaths"] = df.Deaths.diff()
SW["Active"] = SW.Confirmed - SW.Deaths - SW.Recovered
SWCases = [[i for i in SW.Deaths],[i for i in SW.Active],[i for i in SW.Recovered]]

DE = df[df["Country"] == "Germany"]
DE["Active"] = DE.Confirmed - DE.Deaths - DE.Recovered

DECases = [[i for i in DE.Deaths],[i for i in DE.Active],[i for i in DE.Recovered]]


US = df[df["Country"] == "US"]
US["Active"] = US.Confirmed - US.Deaths - US.Recovered

USCases = [[i for i in US.Deaths],[i for i in US.Active],[i for i in US.Recovered]]


Ticks = np.linspace(0,180000,num=10)

fig, (ax1,ax2) = plt.subplots(1,2)

ax1.stackplot(DE.Date, DECases,labels=["Deaths", "Confirmed", "Recovered"],
						 colors=["black","red","green"])
ax1.set_xlabel("Date")
ax1.set_ylabel("Cases")
ax1.set_title("Cases in Germany")
ax1.legend(loc="upper left")
ax1.set_yticks(ticks = Ticks)

ax2.stackplot(SW.Date, SWCases,labels=["Deaths", "Confirmed", "Recovered"],
						 colors=["black","red","green"])
ax2.set_xlabel("Date")
ax2.set_ylabel("Cases")
ax2.set_title("Cases in Sweden")
ax2.legend(loc="upper left")
ax2.set_yticks(ticks = Ticks)

# =============================================================================
# ax3.stackplot(US.Date, USCases,labels=["Deaths", "Confirmed", "Recovered"],
# 						 colors=["black","red","green"])
# ax3.set_xlabel("Date")
# ax3.set_ylabel("Cases")
# ax3.set_title("Cases in United States")
# ax3.legend(loc="upper left")
# ax3.set_yticks(ticks = Ticks)
# =============================================================================

plt.show()