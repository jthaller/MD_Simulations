# %%
import numpy as np 
import matplotlib.pyplot as plt 

plt.plot(*np.loadtxt("system_energy.dat",unpack=True),
            marker='')
plt.title('system energy')
plt.show()

# %%
plt.plot(*np.loadtxt("system_pressure.dat",unpack=True),
            marker='')
plt.title('system pressure')
plt.show()

# %%
plt.plot(*np.loadtxt("system_volume.dat",unpack=True),
            marker='')
plt.title('system volume')
plt.show()

# %%
plt.plot(*np.loadtxt("temperature.dat",unpack=True),
            marker='')
plt.title('system volume')
plt.title('temperature')
plt.show()


# %%
import pandas as pd 
import seaborn as sns

df = pd.read_table('field_forces.txt', delimiter = '     ')
def calc_potential(r, r0, k):
    return k*(r-r0)**2
df.head()

r = np.linspace(1,50)
plt.plot(r,calc_potential(r,df["r0"][0],df["k"][0]))
plt.title("Potential")
plt.xlabel("distance, r")
plt.ylabel("Potential, v(r)")
for i in range(1, df.r0.size):
    plt.plot(r,calc_potential(r,df["r0"][i],df["k"][i]))
plt.show()


# %%
