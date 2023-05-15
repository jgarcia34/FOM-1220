#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os



#Determination of whether it's 2 spectra or 4 spectra in the file. This depends on the spectrometer configuration
A = pd.read_csv('bkg/' + str(''.join(os.listdir('bkg/'))), sep=" ",skiprows=1)
if A.shape[0] == 415 or A.shape[0] == 207:
    nskip1 = 106
elif A.shape[0] == 103:
    nskip1 = 2
    
    
#Determination of whether it's 2 spectra or 4 spectra in the file. This depends on the spectrometer configuration
A = pd.read_csv('patron/' + str(''.join(os.listdir('patron/'))), sep=" ",skiprows=1)
if A.shape[0] == 415 or A.shape[0] == 207:
    nskip2 = 106
elif A.shape[0] == 103:
    nskip2 = 2
    

#Reading of the numbers of counts
A = pd.read_csv('bkg/' + str(''.join(os.listdir('bkg/'))), sep=" ", skiprows=nskip1, nrows=103, header=None, usecols=range(1,11))
B = A.to_numpy()
C = np.nan_to_num(B, copy=True, nan=0.0, posinf=None, neginf=None)
FON = C.flatten()
    
A = pd.read_csv('patron/' + str(''.join(os.listdir('patron/'))), sep=" ", skiprows=nskip2, nrows=103, header=None, usecols=range(1,11))
B = A.to_numpy()
C = np.nan_to_num(B, copy=True, nan=0.0, posinf=None, neginf=None)
PATRON = C.flatten()

    
#Reading of the measurement times
A= pd.read_csv('bkg/' + str(''.join(os.listdir('bkg/'))), sep=" ", skiprows=1, nrows=1, header=None, engine='python')
tFON=A.iloc[0,-1]
A= pd.read_csv('patron/' + str(''.join(os.listdir('patron/'))), sep=" ", skiprows=1, nrows=1, header=None, engine='python')
t=A.iloc[0,-1]  


#Determination of the cps
PATRON = PATRON/t
FON = FON/tFON

plt.plot(PATRON)
plt.plot(FON*sum(PATRON)/sum(FON))
plt.xlabel('Channel')
plt.ylabel('Counts/s')
plt.legend(['Spectrum','Amplified background for comparison'])
plt.show(block=False)
#Set of a limit: a channel close to the en of the spectrum. This will avoid lengthy calculations
lim = int(input('Maximum channel: '))
plt.close()

#Determinations of the optimal channels
FOMrel=np.empty(shape=(lim, lim), dtype='object')
for j in range(0,lim):
    for i in range(0,j):
        if sum(FON[i:j])!=0:      
            FOMrel[i,j] = (sum(PATRON[i:j])**2)/sum(FON[i:j])
        else:
            FOMrel[i,j] = 0
FOMrel[FOMrel == None] = 0
[ini, fin] = np.where(FOMrel == np.max(FOMrel))
print('Starting channel: ', ini+1)
print('Ending channel: ', fin+1)


#Plot of the results
plt.plot(PATRON)
plt.plot(FON*sum(PATRON)/sum(FON))
plt.axvline(x = ini, color = 'k')
plt.axvline(x = fin, color = 'k')
plt.xlabel('Channel')
plt.ylabel('Counts/s')
plt.legend(['Spectrum','Amplified background for comparison'])
plt.show()


end=input("Press close to exit") 
