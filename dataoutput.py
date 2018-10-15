import numpy as np, matplotlib.pyplot as plt, math as m
#%%
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
UST = np.array([]) 
FC = np.array([]) #CO2 flux, mg m-2 s-1
SHF = np.array([]) #sensible heat flux, W/m2
LHF = np.array([]) #latent heat flux, W/m2
G = np.array([]) #sub-surface heat flux, W/m2
NET = np.array([]) #net radiation, W/m2
#surface radiation
FG0 = np.array([]) 
G05 = np.array([]) 
G10 = np.array([]) 
TS00 = np.array([]) 
TS02 = np.array([]) 
TS00 = np.array([])
TS02 = np.array([])
TS06 = np.array([])
TS12 = np.array([])
TS20 = np.array([])
TS30 = np.array([])
TS50 = np.array([])
SWI = np.array([])
SWO = np.array([])
LWI = np.array([])
LWO = np.array([])


f1=open('surface_meteo.txt','r')
for line in f1:
    line=line.split(';')
#    year = np.append(year, float(line[0]))
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
f3=open('soil_heat.txt','r')
for line in f3:
    line=line.split(';')
#    FG0 = np.append(FG0, float(line[4])) #soil heat flux at the surface interface
#    G05 = np.append(G05, float(line[5])) #soil heat flux at 5cm averaged over three sensors
#    G10 = np.append(G10, float(line[6])) #soil heat flux at 10cm averaged over three sensors
#    TS00 = np.append(TS00, float(line[7])) #temperature at soil surface interface
#    TS02 = np.append(TS02, float(line[8])) #temperature at -2cm below surface
#    TS06 = np.append(TS06, float(line[9]))
#    TS12 = np.append(TS12, float(line[10]))
#    TS20 = np.append(TS20, float(line[11]))
#    TS30 = np.append(TS30, float(line[12]))
#    TS50 = np.append(TS50, float(line[13]))
f3.close()
f4=open('surface_radiation.txt','r')
for line in f4:
    line=line.split(';')
    SWI = np.append(SWI, float(line[4]))
#    SWO = np.append(SWO, float(line[5]))
#    LWI = np.append(LWI, float(line[6]))
    LWO = np.append(LWO, float(line[7]))
f4.close()

#%%
#creat new arrays
date_16 = np.arange(1,367,1)
TS00n_16 = np.zeros(len(date_16))
LWOn_16 = np.zeros(len(date_16))
for j in range(0,366):
    addup = 0
    k = 0
    for i in range(52704):
            if int(time[i]) == j:
                if SWI[i]<=0:
                    k+=1
                    addup = addup + LWO[i]
#    if k > 0:
    LWOn_16[j] = addup/k

plt.plot(LWOn_16)
np.savetxt('LWOn_16.txt', LWOn_16)        
    
