from math import ceil
import numpy as np

def mccf(evt1,evt2,bin_width,deltaT,search_time):
    """
    返回lag和mccf值.
    """
    tmin=min(min(evt1),min(evt2))
    tmax=max(max(evt1),max(evt2))
    bins=ceil((tmax-tmin)/bin_width)
    Ndelt=ceil(search_time/deltaT)
    K=np.arange(-Ndelt,Ndelt+1)
    all_lag=K*deltaT
    lc1,_=np.histogram(a=evt1,bins=bins,range=(tmin,tmax))
    v1=lc1-np.mean(lc1)
    sig1=np.sqrt(sum(v1**2))
    v1=v1/sig1
    LC2=np.array([(np.histogram(a=evt2,bins=bins,\
    range=(tmin+lag,tmax+lag)))[0] for lag in all_lag])
    V2=LC2-LC2.mean(axis=1).reshape(LC2.shape[0],1)
    SIG2=np.sqrt((V2**2).sum(axis=1).reshape(LC2.shape[0],1))
    V2=V2/SIG2
    all_mccf=(v1*V2).sum(axis=1)
    return all_lag,all_mccf

def mccferr(evt1,evt2,bin_width,deltaT,search_time,MCtimes):
    """
    返回mccf误差
    """
    tmin=min(min(evt1),min(evt2))
    tmax=max(max(evt1),max(evt2))
    Ndelt=ceil(search_time/deltaT)
    bins=ceil((tmax-tmin)/bin_width)
    K=np.arange(-Ndelt,Ndelt+1)
    all_lag=K*deltaT
    lc1,_=np.histogram(a=evt1,bins=bins,range=(tmin,tmax))
    lc1err=np.sqrt(lc1)
    LC2=np.array([(np.histogram(a=evt2,bins=bins,\
          range=(tmin+lag,tmax+lag)))[0] for lag in all_lag])
    LC2err=np.sqrt(LC2)
    #LAG=[]
    mccferr=[]
    lengthlc=len(lc1)
    for i in range(MCtimes):
        randomlc1=lc1+lc1err*np.random.normal(0,1,size=lengthlc)
        v1=randomlc1-np.mean(randomlc1)
        sig1=np.sqrt(sum(v1**2))
        v1=v1/sig1
        randomLC2=LC2+LC2err*np.random.normal(0,1,size=[len(K),lengthlc])
        V2=randomLC2-randomLC2.mean(axis=1).reshape(randomLC2.shape[0],1)
        SIG2=np.sqrt((V2**2).sum(axis=1).reshape(randomLC2.shape[0],1))
        V2=V2/SIG2
        all_mccf=(v1*V2).sum(axis=1)
        all_mccf=all_mccf/all_mccf[np.where(all_lag==0)[0][0]]
        mccferr.append(all_mccf)
        #LAG.append(all_lag[np.argmax(all_mccf)])
    return np.std(mccferr,axis=0)#np.std(LAG)
