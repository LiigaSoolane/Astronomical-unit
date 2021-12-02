import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from uncertainties import unumpy as unp
import uncertainties as uno
import datetime as dt
from scipy.optimize import curve_fit

##########################################################
def get_seconds(time_str):
    #print('Time in hh:mm:ss:', time_str)
    # split in hh, mm, ss
    hh = []
    mm = []
    ss = []
    for value in time_str:
        hh.append(float(value.split(':')[0]))
        mm.append(float(value.split(':')[1]))
        ss.append(float(value.split(':')[2]))
    print(hh)
    hh = [hh * 3600.0 in hh]
    mm = [mm * 60.0 in mm]
    return hh + mm + ss
########################################################
#constants
period = 0.3207209
epoch = 49594.4684
########################################################
data = open('bxpeg.txt', 'r')
lines = data.readlines()
data.close()

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
vstars = np.array([stars[0:744], stars[0:744], stars[0:744]])
vdiff = np.array([stars[0:744], stars[0:744], stars[0:744]])
vtime = otime[0:744]
bstars = np.array([stars[0:734], stars[0:734], stars[0:734]])
bdiff = np.array([stars[0:734], stars[0:734], stars[0:734]])
btime = otime[0:734]
rstars = np.array([stars[0:702], stars[0:702], stars[0:702]])
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
            vstars[0,a] = stars[i]  
            vstars[1,a] = stars[i+1]
            vstars[2,a] = stars[i+2] 
            vdiff[0,a] = stars[i+1]-stars[i]
            vdiff[1,a] = stars[i+2]-stars[i]
            vdiff[2,a] = stars[i+2]-stars[i+1]
            vtime[a] = otime[i]
            a=a+1
        else:
            if (ifilter[i]=="B"):
                bstars[0,b] = stars[i]  
                bstars[1,b] = stars[i+1]
                bstars[2,b] = stars[i+2]
                bdiff[0,b] = stars[i+1]-stars[i]
                bdiff[1,b] = stars[i+2]-stars[i]
                bdiff[2,b] = stars[i+2]-stars[i+1]
                btime[b] = otime[i]
                b=b+1
            else:
                rstars[0,c] = stars[i]  
                rstars[1,c] = stars[i+1]
                rstars[2,c] = stars[i+2] 
                rdiff[0,c] = stars[i+1]-stars[i]
                rdiff[1,c] = stars[i+2]-stars[i]
                rdiff[2,c] = stars[i+2]-stars[i+1]
                rtime[c] = otime[i]
                c=c+1

#np.savetxt('Vdiff21.txt', np.column_stack([Un, N])vdiff[0,:], fmt='%r', delimiter=', ', newline='\n', header='', encoding=None)
k=0
plt.figure(k)
plt.errorbar(vtime, unp.nominal_values(np.array(vdiff[0,:])), yerr=unp.std_devs(vdiff[0,:]), xerr=None, color='#000000', fmt='.', linewidth=0.05, label='diff21', markersize=1)
#plt.errorbar(vtime, unp.nominal_values(np.array(vdiff[0,:])), yerr=unp.std_devs(vdiff[0,:]), xerr=None, fmt='g.', linewidth=0.05, label='V-Filter', markersize=1)
#plt.errorbar(vtime, unp.nominal_values(np.array(vdiff[0,:])), yerr=unp.std_devs(vdiff[0,:]), xerr=None, fmt='g.', linewidth=0.05, label='V-Filter', markersize=1)
plt.legend()
plt.title('Magnitude Difference between SW Lacertae and TYC 3215-1586-1 in V-Filter')
plt.xlabel(r'local time [s]')
plt.ylabel(r'difference between SW Lac and comparison star')
plt.savefig('V-Filter.pdf')

k=k+1
plt.figure(k)
plt.errorbar(vtime, unp.nominal_values(np.array(vstars[0,:])), yerr=unp.std_devs(vstars[0,:]), xerr=None, fmt='g.', linewidth=0.05, label='V-Filter', markersize=1)
plt.errorbar(btime, unp.nominal_values(np.array(bstars[1,:])), yerr=unp.std_devs(bstars[1,:]), xerr=None, fmt='b.', linewidth=0.05, label='B-Filter', markersize=1)
plt.errorbar(rtime, unp.nominal_values(np.array(rstars[2,:])), yerr=unp.std_devs(rstars[2,:]), xerr=None, fmt='r.', linewidth=0.05, label='R-Filter', markersize=1)
plt.legend()
plt.title('Depiction of the recorded CCD data')
plt.xlabel(r'local time [s]')
plt.ylabel(r'Magnitude')
plt.savefig('Magnitude.pdf')

#k+1
#plt.figure(k)
#plt.errorbar(btime, unp.nominal_values(bdiff[0,:]), yerr=unp.std_devs(bdiff[0,:]), xerr=None, fmt='bx', linewidth=0.05, label='diff21')
##plt.errorbar(vtime, unp.nominal_values(np.array(vdiff[1,:])), yerr=unp.std_devs(vdiff[1,:]), xerr=None, color='c', linewidth=0.05)
##plt.errorbar(vtime, unp.nominal_values(np.array(vdiff[2,:])), yerr=unp.std_devs(vdiff[2,:]), xerr=None, color='b', linewidth=0.05)
#plt.legend()
#plt.xlabel(r'local time [s]')
#plt.ylabel(r'difference between SW Lac and comparison star')
#plt.savefig('B-Filter.pdf')
#
#k+1
#plt.figure(k)
#plt.errorbar(rtime, unp.nominal_values(rdiff[0,:]), yerr=unp.std_devs(rdiff[0,:]), xerr=None, fmt='rx', linewidth=0.05, label='diff21')
##plt.errorbar(vtime, unp.nominal_values(np.array(vdiff[1,:])), yerr=unp.std_devs(vdiff[1,:]), xerr=None, color='c', linewidth=0.05)
##plt.errorbar(vtime, unp.nominal_values(np.array(vdiff[2,:])), yerr=unp.std_devs(vdiff[2,:]), xerr=None, color='b', linewidth=0.05)
#plt.legend()
#plt.xlabel(r'Julian Time (5 Nov 2021) [s]')
#plt.ylabel(r'Magnitude difference between SW Lac and comparison star')
#plt.savefig('R-Filter.pdf')
#################################################################################


vtime[:] = [((x - 2400000 - epoch)%period)/period for x in vtime]
btime[:] = [((x - 2400000 - epoch)%period)/period for x in btime]
rtime[:] = [((x - 2400000 - epoch)%period)/period for x in rtime]

#np.savetxt('Vphase.txt', vtime, fmt='%.18e', delimiter=', ', newline='\n', header='', encoding=None)
#np.savetxt('Bphase.txt', btime, fmt='%.18e', delimiter=', ', newline='\n', header='', encoding=None)
#np.savetxt('Rphase.txt', rtime, fmt='%.18e', delimiter=', ', newline='\n', header='', encoding=None)

k=k+1
plt.figure(k)
plt.errorbar(vtime, unp.nominal_values(np.array(vdiff[0,:])), yerr=unp.std_devs(vdiff[0,:]), xerr=None, fmt='g.', linewidth=0.05, label='V-Fliter', markersize=1)
plt.errorbar(btime, unp.nominal_values(np.array(bdiff[1,:])), yerr=unp.std_devs(bdiff[1,:]), xerr=None, fmt='bx', linewidth=0.05, label='B-Fliter', markersize=1)
plt.errorbar(rtime, unp.nominal_values(np.array(rdiff[2,:])), yerr=unp.std_devs(rdiff[2,:]), xerr=None, fmt='r+', linewidth=0.05, label='R-Fliter', markersize=1)
plt.legend()
plt.xlim(0, 1)
plt.title("Light Curve for SW Lacertae" )
plt.xlabel(r'Phase')
plt.ylabel(r'Magnitude difference between SW Lac and *comparison star*')
plt.savefig('Phase.pdf')

############################################################################

gbs1, gbs1err, gbs2, gbs2err, gbs3, gbs3err, gbHJD, gb21, gb31, gb32, gbepoch, gberr32, gberr21, gberr31, doof, gbphase = np.genfromtxt('datagb.txt', dtype='float', delimiter=None, skip_header=1, names=None, unpack=True)
gvs1, gvs1err, gvs2, gvs2err, gvs3, gvs3err, gbHJD, gv21, gv31, gv32, gvepoch, gverr32, gverr21, gverr31, doof, gvphase = np.genfromtxt('datagv.txt', dtype='float', delimiter=None, skip_header=1, names=None, unpack=True)
grs1, grs1err, grs2, grs2err, grs3, grs3err, gbHJD, gr21, gr31, gr32, grepoch, grerr32, grerr21, grerr31, grphase = np.genfromtxt('datagr.txt', dtype='float', delimiter=None, skip_header=1, names=None, unpack=True)

k=k+1
plt.figure(k)
plt.errorbar(vtime, unp.nominal_values(np.array(vdiff[0,:])), yerr=unp.std_devs(vdiff[0,:]), xerr=None, color='#000000', fmt='.', linewidth=0.05, label='diff21', markersize=1)
plt.errorbar(btime, unp.nominal_values(np.array(bdiff[1,:])), yerr=unp.std_devs(bdiff[1,:]), xerr=None, color='#000000', fmt='.', linewidth=0.05, markersize=1)
plt.errorbar(rtime, unp.nominal_values(np.array(rdiff[2,:])), yerr=unp.std_devs(rdiff[2,:]), xerr=None, color='#000000', fmt='.', linewidth=0.05, markersize=1)
plt.errorbar(gbphase+0.147, gb21, yerr=gberr21, xerr=None, fmt='bx', linewidth=0.05, label='diff21 from supplementary data', markersize=1)
plt.errorbar(gvphase+0.147, gv21, yerr=gverr21, xerr=None, fmt='bx', linewidth=0.05, markersize=1)
plt.errorbar(grphase+0.147, gr31, yerr=grerr31, xerr=None, fmt='bx', linewidth=0.05, markersize=1)
plt.legend()
#plt.title("Light Curve for SW Lac" )
plt.xlabel(r'Phase')
plt.ylabel(r'Magnitude difference between SW Lac and comparison star')
plt.savefig('gdPhase.pdf')

############################################################################################
#
#hdata = open('rawdata.txt', 'r')
#hlines = hdata.readlines()
#
#himage = []
#hidd = []
#hotime = []
#hxcenter = []
#hycenter = []
#hmag = []
#hmerr = []
#
#for value in hlines:
#    himage.append(str(value.split()[0]))
#    hidd.append(str(value.split()[1]))
#    hotime.append(str(value.split()[2]))
#    hxcenter.append(str(value.split()[3]))
#    hycenter.append(str(value.split()[4]))
#    hmag.append(float(value.split()[5]))
#    hmerr.append(float(value.split()[6]))
#
#hstars = unp.uarray(hmag,hmerr)
#hdiff = np.array([hstars[0:4099], hstars[0:4099], hstars[0:4099]])
#htime = hotime[0:4099]
#a=0
#d=len(hstars)
#
#for i in range(0,d-1):
#    if (i%3==0):
#        hdiff[0,a] = hstars[i+1]-hstars[i]
#        hdiff[1,a] = hstars[i+2]-hstars[i]
#        hdiff[2,a] = hstars[i+2]-hstars[i+1]
#        htime[a] = hotime[i]
#        a=a+1
#
#hdtime = get_seconds(htime)
#print(hdtime)
#phase= [((x - 2400000 - epoch)%period)/period for x in hdtime]
#
#k=k+1
#plt.figure(k)
#plt.errorbar(phase, unp.nominal_values(hdiff[0,:]), yerr=unp.std_devs(hdiff[0,:]), xerr=None, fmt='b.', linewidth=0.05, label='diff21', markersize=1)
##plt.errorbar(vtime, unp.nominal_values(np.array(vdiff[1,:])), yerr=unp.std_devs(vdiff[1,:]), xerr=None, color='c', linewidth=0.05)
##plt.errorbar(vtime, unp.nominal_values(np.array(vdiff[2,:])), yerr=unp.std_devs(vdiff[2,:]), xerr=None, color='b', linewidth=0.05)
#plt.legend()
#plt.xlabel(r'local time [s]')
#plt.ylabel(r'difference between SW Lac and comparison star')
#plt.savefig('hB-Filter.pdf')
#