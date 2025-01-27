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
UST = np.array([]) 
FC = np.array([]) #CO2 flux, mg m-2 s-1
FC_d = np.array([]) #CO2 flux during day, mg m-2 s-1
FC_n = np.array([]) #CO2 flux during night, mg m-2 s-1
accum_FC = np.array([]) 
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
    year = np.append(year, float(line[0]))
#    month = np.append(month, float(line[1])) 
#    day = np.append(day, float(line[2])) 
    time = np.append(time,float(line[3]))
#    p0 = np.append(p0, float(line[4]))
#    RAIN = np.append(RAIN, float(line[5]))
#    RDUR = np.append(RDUR, float(line[6]))
    SWD = np.append(SWD, float(line[7]))
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
    TS00 = np.append(TS00, float(line[7])) #temperature at soil surface interface
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
#    SWI = np.append(SWI, float(line[4]))
#    SWO = np.append(SWO, float(line[5]))
#    LWI = np.append(LWI, float(line[6]))
    LWO = np.append(LWO, float(line[7]))
f4.close()
#creat new arrays
date_16 = np.arange(1,367,1)
date_17 = np.arange(1.366,1)
date_18 = np.arange(1,244,1)

#%%
#constants
R10 = 3.3 #reference respiration at reference temperature T=10 celsius, mumol*m-2*s-1
Ea = 300 #ecosystem activation energy, K
T0 = -46.02 #respiration temperature, Celsius
alpha = 5.670373e-8 #Wm-2K-4
time_n = np.array([]) 
TS00_n = np.array([])
Re_n = np.array([])
temp_lw_n = np.array([])
def respiration(T):
    return R10*np.exp(Ea*(1/(10-T0)-1/(T-T0)))*1e-6*44*1e3 #mg*m-2*s-1
def temp(LW):
    return (LW/alpha)**(1/4) - 273.15
for i in range(52704):
    if SWD[i] <= 0:
        time_n = np.append(time_n, time[i])
        FC_n = np.append(FC_n, FC[i])   
        calc1 = temp(LWO[i])
        temp_lw_n = np.append(temp_lw_n, calc1)
#        TS00_n = np.append(TS00_n, TS00[i])
        calc = respiration(temp_lw_n)
        Re_n = np.append(Re_n, calc)

plt.plot(time_n, FC_n)
plt.plot(time_n, Re_n, c='r')
plt.ylim =((-2, 2))
#plt.plot(time[0:52704],TS00[0:52704],c='r')
#plt.plot(time[0:52704],TS50[0:52704],c='g')

#%%TAYLOR DIAGRAM
'''
index = np.arange(0, 47*3600, 3600)
index = np.append(index, [169199])
u_model = np.array(u[index])
taylor_stats1 = sm.taylor_statistics(u_model,u0_l,'data')
sdev = np.array([taylor_stats1['sdev'][0], taylor_stats1['sdev'][1]])
crmsd = np.array([taylor_stats1['crmsd'][0], taylor_stats1['crmsd'][1]])
ccoef = np.array([taylor_stats1['ccoef'][0], taylor_stats1['ccoef'][1]])
sm.taylor_diagram(sdev,crmsd,ccoef, styleOBS = '-', colOBS = 'r', markerobs = 'o', titleOBS = 'reference')
plt.show()    
'''