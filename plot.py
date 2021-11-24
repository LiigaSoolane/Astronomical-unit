import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from uncertainties import unumpy as unp
import uncertainties as uno
from scipy.optimize import curve_fit

#######################################################
data = open('bxpeg.txt', 'r')
lines = data.readlines()

image = []
idd = []
otime = []
xcenter = []
ycenter = []
ifilter = []
mag = []
merr = []

for value in lines:
    image.append(str(value.split()[0]))
    idd.append(str(value.split()[1]))
    otime.append(float(value.split()[2]))
    xcenter.append(str(value.split()[3]))
    ycenter.append(str(value.split()[4]))
    ifilter.append(str(value.split()[5]))
    mag.append(float(value.split()[6]))
    merr.append(float(value.split()[7]))

stars = unp.uarray(mag,merr)

vdiff = np.array([stars[0:744], stars[0:744], stars[0:744]])
vtime = otime[0:744]
bdiff = np.array([stars[0:734], stars[0:734], stars[0:734]])
btime = otime[0:734]
rdiff = np.array([stars[0:702], stars[0:702], stars[0:702]])
rtime = otime[0:702]
a=0
b=0
c=0
i=0
d=len(stars)

for i in range(0,d):
    if (i%3==0):
        if (ifilter[i]=="V"):
            vdiff[0,a] = stars[i+1]-stars[i]
            vdiff[1,a] = stars[i+2]-stars[i]
            vdiff[2,a] = stars[i+2]-stars[i+1]
            vtime[a] = otime[i]
            a=a+1
        else:
            if (ifilter[i]=="B"):
                bdiff[0,b] = stars[i+1]-stars[i]
                bdiff[1,b] = stars[i+2]-stars[i]
                bdiff[2,b] = stars[i+2]-stars[i+1]
                btime[b] = otime[i]
                b=b+1
            else:
                rdiff[0,c] = stars[i+1]-stars[i]
                rdiff[1,c] = stars[i+2]-stars[i]
                rdiff[2,c] = stars[i+2]-stars[i+1]
                rtime[c] = otime[i]
                c=c+1

plt.figure(0)
plt.errorbar(vtime, unp.nominal_values(np.array(vdiff[0,:])), yerr=unp.std_devs(vdiff[0,:]), xerr=None, fmt='gx', linewidth=0.05, label='diff21')
#plt.errorbar(vtime, unp.nominal_values(np.array(vdiff[1,:])), yerr=unp.std_devs(vdiff[1,:]), xerr=None, color='c', linewidth=0.05)
#plt.errorbar(vtime, unp.nominal_values(np.array(vdiff[2,:])), yerr=unp.std_devs(vdiff[2,:]), xerr=None, color='b', linewidth=0.05)
plt.legend()
plt.xlabel(r'local time [s]')
plt.ylabel(r'difference between SW Lac and comparison star')
plt.savefig('V-Filter.pdf')

plt.figure(1)
plt.errorbar(btime, unp.nominal_values(bdiff[0,:]), yerr=unp.std_devs(bdiff[0,:]), xerr=None, fmt='bx', linewidth=0.05, label='diff21')
#plt.errorbar(vtime, unp.nominal_values(np.array(vdiff[1,:])), yerr=unp.std_devs(vdiff[1,:]), xerr=None, color='c', linewidth=0.05)
#plt.errorbar(vtime, unp.nominal_values(np.array(vdiff[2,:])), yerr=unp.std_devs(vdiff[2,:]), xerr=None, color='b', linewidth=0.05)
plt.legend()
plt.xlabel(r'local time [s]')
plt.ylabel(r'difference between SW Lac and comparison star')
plt.savefig('B-Filter.pdf')

plt.figure(2)
plt.errorbar(rtime, unp.nominal_values(rdiff[0,:]), yerr=unp.std_devs(rdiff[0,:]), xerr=None, fmt='rx', linewidth=0.05, label='diff21')
#plt.errorbar(vtime, unp.nominal_values(np.array(vdiff[1,:])), yerr=unp.std_devs(vdiff[1,:]), xerr=None, color='c', linewidth=0.05)
#plt.errorbar(vtime, unp.nominal_values(np.array(vdiff[2,:])), yerr=unp.std_devs(vdiff[2,:]), xerr=None, color='b', linewidth=0.05)
plt.legend()
plt.xlabel(r'local time [s]')
plt.ylabel(r'difference between SW Lac and comparison star')
plt.savefig('R-Filter.pdf')
#################################################################################

