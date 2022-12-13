from matplotlib import pyplot as plt
import numpy as np
#data 
Berlin_dict= {1250:1200,1307:7000,1400:8500,1576:12000,1600:9000,1631:8100,1648:6000,1685:17500,1709:57000,1750:113289,1775:136137,1800:172132,1825:219968,1840:322626,1852:426600,1864:632700,1875:969050,1919:1902509,1933:4242501,1945:2807405,1970:3208719,2000:3382169,2020:3664088}
Berlin_years = Berlin_dict.keys()
print(Berlin_years)
Berlin_popul = Berlin_dict.values()
print(Berlin_popul)
# plot
fig, ax = plt.subplots()
plt.title("Berlin population growth")
plt.xlabel("Years")
#plt.yticks(range(min(Berlin_popul), max(Berlin_popul)))
plt.gca().set_xscale("linear")
plt.ylabel("Population as millions")
ax.plot (Berlin_years, Berlin_popul, ".:r", linewidth=1.5)
ax.set(xlim=(1250, 2020), xticks = np.arange(100,2020),
ylim=(1200, 4000000), yticks = np.arange(100000, 4000000))
plt.grid()
plt.show()