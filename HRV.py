# -*- coding: utf-8 -*-
"""

HRV analysis

1.Time Domain
2.Frequency Domain
3.Nonlinear

"""
#import sys
import numpy as np
from scipy import interpolate
#from spectrum import pburg
from scipy.signal import welch

def read_hrv_text(pathname):
    try:
        file_object = open(pathname,"r+")
    except IOError:
        print("Files Not Found!")
    else:
        values = []
        for line in file_object:
            values.append(list(line.strip('\n').split(',')))
    return(values[0:-1])
    

def time_domain(rri):
    diff = np.diff(rri,1)
    rmssd = np.sqrt(sum(diff ** 2)/(len(rri)-1))
    sdnn = np.std(rri, ddof=1)  # make it calculates N-1
    nn50 = (sum(abs(np.diff(rri)) > 50))
    pnn50 =  nn50 / len(rri) * 100
    nn20 = (sum(abs(np.diff(rri)) < 20))
    pnn20 = nn20/ len(rri) * 100
    mrri = np.mean(rri)
    mhr = np.mean(60 / (rri / 1000.0))
    return dict(zip(['rmssd', 'sdnn', 'nn50', 'pnn50', 'mrri', 'mhr','nn20','pnn20'],
                    [rmssd, sdnn, nn50, pnn50, mrri, mhr,nn20,pnn20]))
    
def frequency_domain(rri,vlf_band=(0, 0.04),lf_band=(0.04, 0.15), hf_band=(0.15, 0.4),
                     fs = 4.0, interp_method = 'cubic',**kwargs):
    alltime = np.cumsum(rri) / 1000.0 
    time = alltime - alltime[0]
    #interpolate:'cubic','linear'
    if interp_method is not None:
        time_resolution = 1 / float(fs)
        time_interp = np.arange(0, time[-1] + time_resolution, time_resolution)
        if interp_method == 'cubic':
            tck = interpolate.splrep(time, rri, s=0)
            rri = interpolate.splev(time_interp, tck, der=0)
        elif interp_method == 'linear':
            rri = np.interp(time_interp, time, rri)
    #psd:'welch'
    fxx, pxx = welch(x = rri, fs = fs, **kwargs)

    vlf_ind = np.logical_and(fxx>=vlf_band[0],fxx<vlf_band[1])
    #print(vlf_ind)
    lf_ind = np.logical_and(fxx>=lf_band[0],fxx<lf_band[1])
    hf_ind = np.logical_and(fxx>=hf_band[0],fxx<hf_band[1])
    vlf_p = np.trapz(y=pxx[vlf_ind],x=fxx[vlf_ind])
    lf_p = np.trapz(y=pxx[lf_ind],x=fxx[lf_ind])
    hf_p = np.trapz(y=pxx[hf_ind],x=fxx[hf_ind])
    total_p = vlf_p + lf_p + hf_p
    lf_hf = lf_p/hf_p
    lfnu = (lf_p / (total_p - vlf_p)) * 100
    hfnu = (hf_p / (total_p - vlf_p)) * 100

    return dict(zip(['total_power', 'vlf', 'lf', 'hf', 'lf_hf', 'lfnu',
                    'hfnu'], [total_p, vlf_p, lf_p, hf_p, lf_hf, lfnu, hfnu]))

def non_linear(rri):
    sd1, sd2 = _poincare(rri)
    return dict(zip(['sd1', 'sd2'], [sd1, sd2]))


def _poincare(rri):
    diff_rri = np.diff(rri)
    sd1 = np.sqrt(np.std(diff_rri, ddof=1) ** 2 * 0.5)
    sd2 = np.sqrt(2 * np.std(rri, ddof=1) ** 2 - 0.5 * np.std(diff_rri,
                                                              ddof=1) ** 2)
    return sd1, sd2

if __name__ == '__main__':
    #rri单位：ms,不能包含零值
    rri = np.loadtxt('jeep_rri.txt')
    #rri = np.delete(rri,0.0)
    
    #1.Time Domain Analysis
    result_time = time_domain(rri)
    print('Time Domain Analysis:',result_time)
    #2.Frequency Domain Analysis
    result_frequency = frequency_domain(rri,vlf_band=(0, 0.04),lf_band=(0.04, 0.15), hf_band=(0.15, 0.4),
                     fs = 4.0, interp_method = 'cubic',detrend='linear')
    print('Frequency Domain Analysis:',result_frequency)
    #3.Nonlinear Analysis
    result_nonlinear = non_linear(rri)
    print('Nonlinear Analysis:',result_frequency)