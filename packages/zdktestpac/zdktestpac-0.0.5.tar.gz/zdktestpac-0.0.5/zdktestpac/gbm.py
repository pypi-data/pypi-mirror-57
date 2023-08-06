from astropy.io import fits
from stingray.events import EventList
import os

def trigfiles(bnfolder):
    bnfolder=os.path.abspath(bnfolder)
    absFilePath=os.path.join(bnfolder,'current')
    files=[i for i in os.listdir(absFilePath) if ('tte' in i) or ('trigdat' in i)]
    trigdatfile=[i for i in files if 'trigdat' in i][0]
    naittefiles=[i for i in files if '_tte_n' in i]
    for i in files:
        if '_tte_b0' in i:
            bgo0ttefiles=i
        elif '_tte_b1' in i:
            bgo1ttefiles=i
    det_mask=fits.getval(os.path.join(absFilePath,trigdatfile),'det_mask')
    trigttefiles=[]
    flag1,flag2=0,0
    for j in naittefiles:
        if j[9]=='a':
            number=10
        elif j[9]=='b':
            number=11
        else:
            number=int(j[9])
        if det_mask[number]=='1':
            trigttefiles.append(os.path.join(absFilePath,j))
            if number in list(range(6)):flag1=1
            if number in list(range(6,11)):flag2=1
    if flag1==1:trigttefiles.append(os.path.join(absFilePath,bgo0ttefiles))
    if flag2==1:trigttefiles.append(os.path.join(absFilePath,bgo1ttefiles))
    return trigttefiles

class GSingel(object):
    def __init__(self,ttefile):
        self.ttefile=os.path.abspath(ttefile)
        self.__eventsdata,evheader=fits.getdata(self.ttefile,extname='events',header=True)
        self.trigtime=evheader['trigtime']
        self.mjdref=(evheader['mjdrefi']+evheader['mjdreff'])
        self.grbName=evheader['object']
        self.ebounds=fits.getdata(self.ttefile,extname='ebounds')
        self.events=EventList(time=self.__eventsdata.field('time')-self.trigtime,mjdref=self.mjdref,pi=self.__eventsdata.field('pha'))
        self.events.selectenergy=self.__selectenergy
        self.__getenergyrange()
    
    def __getenergyrange(self):
        minpi=min(self.events.pi)
        maxpi=max(self.events.pi)
        self.events.energyrange=[self.ebounds[minpi][1],self.ebounds[maxpi][2]]
        
    def __energy2channel(self,energy):
        index=self.ebounds.field('E_MAX').searchsorted(energy)
        return self.ebounds.field('CHANNEL')[index]
    
    def __selectenergy(self,emin,emax):
        self.events.time=self.__eventsdata.field('time')-self.trigtime
        self.events.pi=self.__eventsdata.field('pha')
        chanMax=self.__energy2channel(emax)
        chanMin=self.__energy2channel(emin)
        greaterTruthTable=self.events.pi>=chanMin
        lesserTruthTable=self.events.pi<=chanMax
        combinedSelection=greaterTruthTable & lesserTruthTable
        self.events.time=self.events.time[combinedSelection]
        self.events.pi=self.events.pi[combinedSelection]
        self.__getenergyrange()
