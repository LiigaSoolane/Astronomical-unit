import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from uncertainties import unumpy as unp
import uncertainties as uno
from scipy.optimize import curve_fit

# read values
image,idd,otime,xcenter,ycenter,ifilter,mag,merr = np.genfromtxt('bxpeg.txt', unpack=True)


stars=unp.uarray(mag, merr)
print(stars)
# We look at 6540/3=2180 images /3 -> 726 images each
vdiff = np.array([stars[0:726], stars[0:726], stars[0:726]])
vtime = np.zeros(726, dtype=float)
bdiff = np.array([stars[0:726], stars[0:726], stars[0:726]])
btime = np.zeros(726, dtype=float)
rdiff =  np.array([stars[0:726], stars[0:726], stars[0:726]])
rtime = np.zeros(726, dtype=float)

i=0
a=0
while (a<726):

    bdiff[0,a] = stars[i+1]-stars[i]
    bdiff[1,a] = stars[i+2]-stars[i]
    bdiff[2,a] = stars[i+2]-stars[i+1]
    vdiff[0,a] = stars[i+4]-stars[3+i]
    vdiff[1,a] = stars[i+5]-stars[3+i]
    vdiff[2,a] = stars[i+5]-stars[4+i]
    rdiff[0,a] = mag[i+7]-mag[6+i]
    rdiff[1,a] = mag[i+8]-mag[6+i]
    rdiff[2,a] = mag[i+8]-mag[7+i]
    vtime[a] = otime[i+3]
    rtime[a] = otime[i+6]
    btime[a] = otime[i]
    i=i+9
    a=a+1



print(vdiff)

plt.clf()
#plt.plot(rtime, r, 'r.', label='Messwerte')
#plt.plot(lam_plot, params[0]*lam_plot + params[1], '-', label='Lineare Regression')
plt.errorbar(vtime, vdiff[0,:], fmt='r_')
#plt.legend()
#plt.xlabel(r'Wellenlänge $\lambda$')
#plt.ylabel(r'Transmission')
plt.savefig('transmission.pdf')

#kalpha_ = unp.uarray(kalpha, 0.1)
#kbeta_ = unp.uarray(kbeta, 0.1)
## K_alpha y K_beta energias
#lam_alpha = 2 * d_LiF * unp.sin(kalpha_ * np.pi / 180)
#lam_beta = 2 * d_LiF * unp.sin(kbeta_ * np.pi / 180)
#
#E_alpha = h * c / lam_alpha
#E_beta = h * c / lam_beta
#
#E_alpha *= 6.242 * 10**(18)
#E_beta *= 6.242 * 10**(18)
#
#print(f'E_a = {E_alpha}')
#print(f'E_b = {E_beta}')
#
##plot Emission spectrum
#plt.plot(theta, N, 'r.', label='Messwerte')
#plt.plot(theta, N, 'b-', linewidth=0.5)
#
## mark Kalpha and Kbeta lines
#plt.plot([kbeta, kbeta], [0, 1599.0], color='red', linestyle='--')
#plt.scatter([kbeta], [1599.0], s=20, marker='o', color='red')
#plt.annotate(r'$K_{\beta}$',
#            xy = (kbeta, 1599.0), xycoords='data', xytext=(-50, -25),
#            textcoords='offset points', fontsize=12,
#            arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=.2"))
#plt.plot([kalpha, kalpha], [0, 5050.0], color='red', linestyle='--')
#plt.scatter([kalpha], [5050.0], s=20, marker='o', color='red')
#plt.annotate(r'$K_{\alpha}$',
#            xy = (kalpha, 5050.0), xycoords='data', xytext=(+10, -2),
#            textcoords='offset points', fontsize=12,
#            arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=.2"))
#
## mark Bremsberg
#plt.plot([11.1, 11.1], [0, 420.0], color='red', linestyle='--')
#plt.scatter([11.1], [420.0], s=20, marker='o', color='red')
#plt.annotate(r'Bremsberg', 
#            xy = (11.1, 420.0), xycoords='data', xytext=(-10, 20),
#            textcoords='offset points', fontsize=12, 
#            arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=.2"))
#
#plt.xlabel('Einfallswinkel in °')
#plt.ylabel('Anzahl Impulse pro s')
#plt.tight_layout()
#plt.legend()
#plt.savefig('emission.pdf')
#plt.clf()
#
## ------ Transmission als Funktion der Wellenlänge  -------
#
## read values for with and without Aluminum absorber
#a_0, N_0_ = np.genfromtxt('ComptonOhne.txt', unpack=True)
#a_Al, N_Al_ = np.genfromtxt('ComptonAl.txt', unpack=True)
#Tau = 90
#Tau *= 10**(-6)
#d_LiF = 201.4 
#d_LiF *= 10**(-12)
#
#N_0_err = np.sqrt(N_0_)
#N_Al_err = np.sqrt(N_Al_)
#
#N_0 = unp.uarray(N_0_, N_0_err)
#N_Al = unp.uarray(N_Al_, N_Al_err)
#
## Totzeitkorrektur
#I_o = N_0 / (1 - Tau * N_0)
#I_Al = N_Al / (1 - Tau * N_Al)
#
## Transmission bestimmen
#T = I_Al / I_o
#
## calcular taman~o de las ondas
#
#lam = 2 * d_LiF * np.sin(a_0 * np.pi / 180)
#
## crear lineare Regression
#params, cov = np.polyfit(lam, unp.nominal_values(T), deg=1, cov=True)
#errs = np.sqrt(np.diag(cov))
#for name, value, error in zip('ab', params, errs):
#    print(f'{name} = {value:.3f} +- {error:.3f}')
#
## grafico
#l_start = 2* d_LiF * np.sin(7 * np.pi /180)
#l_fin = 2 * d_LiF *np.sin(10* np.pi/180)
#lam_plot = np.linspace(l_start, l_fin)
#

#
## ----- Compton-Wellenlänge bestimmen ------
#
## Transmissionen
#I_0 = 2731.0
#I_1 = 1180.0
#I_2 = 1024.0
#
#T_1 = I_1/I_0
#T_2 = I_2/I_0
#
#print(f'T_1 = {T_1:.3f}, T_2 = {T_2:.3f}')
#
## calcular tamanos de ondas correspendientes
#a = unp.uarray(params[0], errs[0])
#b = unp.uarray(params[1], errs[1])
#lam_1 = (T_1 - b)/a
#lam_2 = (T_2 - b)/a
#
#lam_c = lam_2 - lam_1
#
#print(f'Lambda 1 = {lam_1}')
#print(f'Lambda 2 = {lam_2}')
#print(f'Compton = {lam_c}')
#
## ----- Abweichungen von Literaturwerten ------
#E_alpha_theo = 8048.11
#E_beta_theo = 8906.9
#lam_c_theo = 2.427 * 10**(-12)
#
#ab_E_alpha = (E_alpha_theo - E_alpha)/E_alpha_theo * 100
#ab_E_beta = (E_beta_theo - E_beta)/E_beta_theo * 100
#ab_lam_c = (lam_c_theo - lam_c)/lam_c_theo * 100
#
#print(f'Abweichung Kalpha = {ab_E_alpha} Prozent')
#print(f'Abweichung Kbeta = {ab_E_beta} Prozent')
#print(f'Abweichung compton = {ab_lam_c} Prozent')