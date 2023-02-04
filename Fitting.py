import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
from lmfit.models import VoigtModel, LorentzianModel, GaussianModel, PseudoVoigtModel
from scipy.special import wofz
from scipy.special import voigt_profile
import csv
import scipy
from numpy import log 
import math
from numpy.fft import fft, ifft
from lmfit.models import GaussianModel, VoigtModel, LinearModel, ConstantModel
import pylab
from scipy.optimize import fsolve


pi  = 3.1415
e = 2.71828

def voigt2(x,a,m,s,g):
    z = (x-m+complex(0,g))/(s*math.sqrt(2))
    d = wofz(z)
    return (a*d.real)/(s*math.sqrt(2*pi))

file = open('data/2ndlabdata.csv') #23

type(file)
csvreader = csv.reader(file)
rows = []
xval = []
yval = []
i = 0 
for row in csvreader:
    rows.append(row)
    xval.append(row[2])
    yval.append(row[3])
xfval = []
for x in xval:
    xfval.append(float(x))
    
    
yfval = []
for y in yval:
    yfval.append(float(y))
    
xfval = np.asarray(xfval)
yfval = np.asarray(yfval)

plt.plot(xfval, yfval-52, 'b-', label='data')
popt, pcov = curve_fit(voigt2, xfval, yval, bounds=(0, [2.5,70., 0.01, 0.05]), maxfev =10000)
plt.plot(xfval, 10*np.log10(voigt2(xfval, *popt)), 'r-',label='fit: a=%5.3f, b=%5.3f, c=%5.3f   c=%5.3f  ' % tuple(popt))


ma = max(10*np.log10(voigt2(xfval, *popt)))
mi = min(10*np.log10(voigt2(xfval, *popt))) 
mid = (abs(ma) + abs(mi))/2
plt.plot(xfval, 10*np.log10(voigt2(xfval, *popt)), 'r-',label='fit: a=%5.3f, b=%5.3f, c=%5.3f   c=%5.3f  ' % tuple(popt))

colors = ['b',  'g']
max_y = max(10*np.log10(voigt2(xfval, *popt)))
db = [max_y-3, max_y-10, max_y-20, max_y-30, max_y - mid]
div = [2, 2*math.sqrt(9), 2*math.sqrt(99), 2*math.sqrt(999), 1]
plt.hlines(db, 0, 70, ls="--", color=colors)
lw = []
m = 0
plt.xlim(30,40)
plt.ylim(-20,20)
for i, y in enumerate(db):
    
    x0 = fsolve(lambda xfval: 10*np.log10(voigt2(xfval, *popt)) - y, 30)
    x1 = fsolve(lambda xfval: 10*np.log10(voigt2(xfval, *popt)) - y, 40)
    #print(f"Intersection points for {y=}: {x0=} {x1=}") 
    print(abs(x0-x1))
    print('x0',x0 )
    print('x1',x1)
    print(div[m])
    lw.append((abs(x0 -x1)/div[m])*1000)
    m = m+1
    plt.scatter(x0, 10*np.log10(voigt2(x0, *popt)), color=colors[0])
    plt.scatter(x1, 10*np.log10(voigt2(x1, *popt)), color=colors[1])
 
