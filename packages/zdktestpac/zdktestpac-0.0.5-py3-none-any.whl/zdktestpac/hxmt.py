from astropy.io import fits
import os
from stingray.events import EventList
class Hsingel(object):
    def __init__(self,hefolder):
        self.grbName=os.path.split(hefolder)[-1]
        self.ttefile=os.path.abspath(os.path.join(hefolder,'{}_HE-Evt.fits'.format(self.grbName)))
        self.__eventsdata,evheader=fits.getdata(self.ttefile,extname='events',header=True)
        self.trigtime=evheader['trigtt']
        self.mjdref=evheader['mjdrefi']+evheader['mjdreff']
        rsppath=os.path.join(hefolder,'docs/rspgenerator_CLI_GECAM_FITS/')
        self.ebounds=fits.getdata([os.path.join(rsppath,i) for i in os.listdir(rsppath) if 'DA' in i][0],extname='ebounds')
        self.events=EventList(time=self.__eventsdata.field('time')-self.trigtime,mjdref=self.mjdref,pi=self.__eventsdata.field('pi'))
        self.events.selectenergy=self.__selectenergy
        pulseWidthTruthTable = self.__eventsdata.field('Pulse_Width')>75
        eventTypeTruthTable = self.__eventsdata.field('Event_Type')==0
        acdTruthTable = self.__eventsdata.field('ACD').sum(axis=1)==0
        comTru=pulseWidthTruthTable & eventTypeTruthTable & acdTruthTable
        self.events.time=self.events.time[comTru]
        self.events.pi=self.events.pi[comTru]
        self.__getenergyrange()
    
    def __getenergyrange(self):
        minpi=min(self.events.pi)
        maxpi=max(self.events.pi)
        self.events.energyrange=[self.ebounds[minpi-1][1],self.ebounds[maxpi-1][2]]
    
    def __energy2channel(self,energy):
        index=self.ebounds.field('E_MAX').searchsorted(energy)
        return self.ebounds.field('CHANNEL')[index]
        
    def __selectenergy(self,emin,emax):
        self.events.time=self.__eventsdata.field('time')-self.trigtime
        self.events.pi=self.__eventsdata.field('pi')
        chanMax=self.__energy2channel(emax)
        chanMin=self.__energy2channel(emin)
        greaterTruthTable = self.events.pi>=chanMin
        lesserTruthTable = self.events.pi<=chanMax
        combinedSelection = greaterTruthTable & lesserTruthTable
        self.events.time=self.events.time[combinedSelection]
        self.events.pi=self.events.pi[combinedSelection]
        self.__getenergyrange()
