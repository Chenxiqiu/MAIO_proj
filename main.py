import numpy as np, matplotlib.pyplot as plt, math as m
#%%creat numpy arrays and read meteo and flux data from txt
#meteo
year = np.array([])
month = np.array([])
day = np.array([]) 
time = np.array([]) #day of year,xxx(.0-.99) 
p0 = np.array([]) #see level pressure
RAIN = np.array([]) #precipitation, mm
RDUR = np.array([]) #rain duration, s
SWD = np.array([]) #SW downward radiation, W/m2
TA2 = np.array([]) #air temperature at 2m, Celsius
TD2 = np.array([]) #dew point temperature at 2m, Celsius
F10 = np.array([]) #wind speed at 10m, m/s
D10 = np.array([]) #wind direction at 10m, degree
#surface fluxes
UST = np.array([]) #friction velocity, m/s
FC = np.array([]) #CO2 flux, mg m-2 s-1
accum_FC = np.array([]) 
SHF = np.array([]) #sensible heat flux, W/m2
LHF = np.array([]) #latent heat flux, W/m2
G = np.array([]) #sub-surface heat flux, W/m2
NET = np.array([]) #net radiation, W/m2

f1=open('surface_meteo.txt','r')
for line in f1:
    line=line.split(';')
    year = np.append(year, float(line[0]))
#    month = np.append(month, float(line[1])) 
#    day = np.append(day, float(line[2])) 
    time = np.append(time,float(line[3]))
#    p0 = np.append(p0, float(line[4]))
#    RAIN = np.append(RAIN, float(line[5]))
#    RDUR = np.append(RDUR, float(line[6]))
#    SWD = np.append(SWD, float(line[7]))
#    TA2 = np.append(TA2, float(line[8]))
#    TD2 = np.append(TD2, float(line[9]))
#    F10 = np.append(F10, float(line[10]))
#    D10 = np.append(D10, float(line[11]))
f1.close()
f2=open('surface_flux.txt','r')
for line in f2:
    line=line.split(';')
#    UST = np.append(UST, float(line[4]))
    FC = np.append(FC, float(line[5]))
#    SHF = np.append(SHF, float(line[6]))
#    LHF = np.append(LHF, float(line[7]))
#    G = np.append(G, float(line[8]))
#    NET = np.append(NET, float(line[9]))
f2.close()
accum_FC = np.cumsum(FC)
plt.plot(time[0:52704],accum_FC[0:52704])