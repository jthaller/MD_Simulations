# %%
import numpy as np 
import matplotlib.pyplot as plt 

plt.plot(*np.loadtxt("system_energy.dat",unpack=True),
            marker='')
plt.title('system energy')
plt.xlabel('time (ps)')
plt.show()

# %%
plt.plot(*np.loadtxt("system_pressure.dat",unpack=True),
            marker='')
plt.title('system pressure')
plt.xlabel('time (ps)')
plt.show()

# %%
plt.plot(*np.loadtxt("system_volume.dat",unpack=True),
            marker='')
plt.title('system volume')
plt.xlabel('time (ps)')
plt.show()

# %%
plt.plot(*np.loadtxt("temperature.dat",unpack=True),
            marker='')
plt.title('system volume')
plt.title('temperature')
plt.xlabel('time (ps)')
plt.show()


# %%
import pandas as pd 
import seaborn as sns

df = pd.read_table('field_forces.txt', delimiter =r"\s+")
def calc_potential(r, r0, k):
    return k*(r-r0)**2
df.head()

r = np.linspace(0,100)
plt.plot(r,calc_potential(r,df["r0"][0],df["k"][0]))
plt.title("Potential")
plt.xlabel("distance, r")
plt.ylabel("Potential, v(r)")
for i in range(1, df.r0.size):
    plt.plot(r,calc_potential(r,df["r0"][i],df["k"][i]))
plt.show()


# %%
df = pd.read_table('field_angles.txt', delimiter=r"\s+")
df.head()

r = np.linspace(0,200)
plt.plot(r,calc_potential(r,df["theta"][0],df["theta_0"][0]))
plt.title("Potential")
plt.xlabel("Angles, theta")
plt.ylabel("Potential, v(theta)")
for i in range(1, df.theta.size):
    plt.plot(r,calc_potential(r,df["theta"][i],df["theta_0"][i]))
plt.show()

print(df.theta.size)