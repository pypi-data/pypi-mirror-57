from astropy.io import fits
from astropy.stats import sigma_clipped_stats
from astropy.wcs import WCS
from astropy.coordinates import SkyCoord
from scipy.optimize import curve_fit
from scipy.integrate import quad
from drizzlepac import astrodrizzle
from photutils import CircularAnnulus,CircularAperture,aperture_photometry
from photutils.utils import calc_total_error
from photutils import centroid_sources,centroid_2dg,centroid_com

from kbastroutils.grismconf import GrismCONF
from kbastroutils.grismsens import GrismSens
from kbastroutils.grismapcorr import GrismApCorr
from kbastroutils.dqmask import DQMask
from kbastroutils.make_sip import make_SIP
from kbastroutils.photapcorr import PhotApCorr
from kbastroutils.grismmeta import GrismMeta

import copy,os,pickle,sys
from shutil import copyfile
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class GND:
    def __init__(self,files):
        meta = GrismMeta(files)
        self.files = copy.deepcopy(meta.files)
        self.meta = copy.deepcopy(meta.meta)
        self.gid = copy.deepcopy(meta.gid)
        self.did = copy.deepcopy(meta.did)
        self.nid = copy.deepcopy(meta.nid)        
    ####################
    ####################
    ####################
    def make_pair(self,pairs=None):
        if pairs:
            self.pairs = copy.deepcopy(pairs)
            for i in pairs.keys():
                gids = pairs[i]
                for j in gids:
                    self.meta[j]['DIRECT'] = i
                    self.meta[j]['XYDIF'] = self.find_xydif(j,i)
        else:
            pairs = self.make_pairauto(by='EXPSTART')
            self.make_pair(pairs)
    def make_pairauto(self,by):
        gid = copy.deepcopy(self.gid)
        did = copy.deepcopy(self.did)
        dmeta = {}
        for i in self.did:
            dmeta[i] = self.meta[i]
        dtab = pd.DataFrame(dmeta).T
        did,dval = dtab['ID'].values,dtab[by].values
        tmp = []
        for i in self.gid:
            gval = self.meta[i][by]
            tmpp = np.abs(dval-gval)
            tmppp = np.where(tmpp == np.min(tmpp))[0][0]
            tmp.append((did[tmppp],i))
        out = {}
        for i in tmp:
            if i[0] not in out.keys():
                out[i[0]] = [i[1]]
            else:
                tmpppp = out[i[0]]
                tmpppp.append(i[1])
        return out
    def find_xydif(self,gid,did):
        post1g,post2g = self.meta[gid]['POSTARG1'],self.meta[gid]['POSTARG2']
        post1d,post2d = self.meta[did]['POSTARG1'],self.meta[did]['POSTARG2']
        scaleg,scaled = self.meta[gid]["IDCSCALE"],self.meta[did]['IDCSCALE']
        dx = post1g/scaleg - post1d/scaled
        dy = post2g/scaleg - post2d/scaled
        xydif = (dx,dy)
        return xydif
    ####################
    ####################
    ####################
    def make_xyd(self,XYD=None
                 ,inittype='header'
                 ,adjust=True,box_size=25,maskin=[0]
                ):
        if XYD:
            for i in XYD:
                self.meta[i]['XYD'] = XYD[i]
        else:
            init = self.make_xydinit(inittype)
            if not init:
                print('Error: cannot initiate. Terminate')
                sys.exit()
            if adjust:
                try:
                    xyd = self.make_xydadjust(init,box_size,maskin)
                except:
                    print('Error: cannot make_xydadjust. Set to initials')
                    xyd = copy.deepcopy(init)
                self.make_xyd(xyd)
            else:
                self.make_xyd(init)
    def make_xydinit(self,inittype):
        out = {}
        if inittype=='header':
            for i in self.did:
                try:
                    tmp = self.meta[i]['XYD']
                    continue
                except:
                    pass
                ra,dec = self.meta[i]['RA_TARG'],self.meta[i]['DEC_TARG']
                w = WCS(header=fits.open(self.files[i])[self.meta[i]['EXT']]
                        ,fobj=fits.open(self.files[i])
                       )
                coord = SkyCoord(ra,dec,unit='deg')
                xx,yy = w.all_world2pix(coord.ra,coord.dec,1)
                out[i] = copy.deepcopy((xx,yy))
            return out
        else:
            print("Error: only inittype='header' is available. Terminate")
            return False 
    def make_xydadjust(self,init,box_size,maskin):
        out = {}
        for i in self.did:
            try:
                tmp = self.meta[i]['XYD']
                continue
            except:
                pass
            x = fits.open(self.files[i])
            xdata = x[self.meta[i]['EXT']].data
            xdq = x['DQ',self.meta[i]['EXT'][1]].data
            xi,yi = int(init[i][0]),int(init[i][1])
            mask = DQMask(maskin)
            mask.make_mask(xdq)
            xx,yy = centroid_sources(xdata,xi,yi,box_size=box_size,mask=~mask.mask)
            tmp = np.full_like(xdata,False,dtype=bool)
            xi,yi = int(xx[0]),int(yy[0])
            tmp[yi-box_size:yi+box_size+1,xi-box_size:xi+box_size+1] = True
            newmask = (mask.mask & tmp)
            xx,yy = centroid_2dg(xdata,mask=~newmask)            
            out[i] = copy.deepcopy((xx,yy))
        return out
    ####################
    ####################
    ####################
    def make_photparams(self,method='aperture',apsize=5,apunit='pix',maskin=None
                        ,sigma=3.,iters=5
                        ,dobkgann=True,bkgann=(20.,25.)
                       ):
        for j in self.did:
            instrument = '-'.join((self.meta[j]['TELESCOP'],self.meta[j]['INSTRUME'],self.meta[j]['DETECTOR']))
            self.meta[j]['PHOT_PARAMS'] = {}
            self.meta[j]['PHOT_PARAMS']['INSTRUMENT'] = instrument
            nchip = self.meta[j]['NCHIP']
            string = 'FILTER1' if nchip > 1 else 'FILTER'
            self.meta[j]['PHOT_PARAMS']['FILTER'] = self.meta[j][string]
            self.meta[j]['PHOT_PARAMS']['METHOD'] = method
            self.meta[j]['PHOT_PARAMS']['APSIZE'] = apsize
            self.meta[j]['PHOT_PARAMS']['APUNIT'] = apunit
            self.meta[j]['PHOT_PARAMS']['MASKIN'] = maskin
            self.meta[j]['PHOT_PARAMS']['SIGMA'] = sigma
            self.meta[j]['PHOT_PARAMS']['ITERS'] = iters
            self.meta[j]['PHOT_PARAMS']['DOBKGANN'] = dobkgann
            self.meta[j]['PHOT_PARAMS']['BKGANN'] = bkgann
    def make_phot(self):
        mean,median,std,error = [],[],[],[]
        for i in self.did:
            xdata = fits.open(self.files[i])[self.meta[i]['EXT']].data
            exptime = self.meta[i]['EXPTIME']
            photparams = copy.deepcopy(self.meta[i]['PHOT_PARAMS'])
            photapcorr = PhotApCorr()
            if photparams['APUNIT']!='pix':
                print('Error: apunit must be pix. Terminate')
                continue
            if photparams['MASKIN']:
                print('Error: maskin is not implemented in this version. Terminate')
                continue
            if photparams['INSTRUMENT'] not in photapcorr.instrument:
                print('Error: instrument does not match PhotApCorr.instrument. Terminate')
                continue
            m = np.isfinite(xdata)
            error = calc_total_error(data=xdata,bkg_error=np.zeros_like(xdata),effective_gain=exptime)
            xyd = self.meta[i]['XYD']
            ap = CircularAperture((xyd[0],xyd[1]),r=photparams['APSIZE'])
            aptab = aperture_photometry(xdata,ap,error=error)
            ann = CircularAnnulus((xyd[0],xyd[1]),r_in=photparams['BKGANN'][0],r_out=photparams['BKGANN'][1])
            bkgtab = aperture_photometry(xdata,ann,error=error)
            bkg,bkg_error = None,None
            if photparams['DOBKGANN']:
                bkg = bkgtab['aperture_sum'] * ap.area / ann.area
                ebkg = bkgtab['aperture_sum_err'] * ap.area / ann.area
            else:
                bkg,bkg_error = 0.,0.
            wave,ZP = None,None  
            if photapcorr.table[photparams['INSTRUMENT']]['ZP'][photparams['FILTER']]:
                tmp = photapcorr.table[photparams['INSTRUMENT']]['ZP'][photparams['FILTER']]
                wave = tmp[0]
                ZP = tmp[1]
                self.meta[i]['PHOT_PARAMS']['ZP'] = copy.deepcopy(tmp)
            else:
                print('Error: filter does not match PhotApCorr.table. Terminate')
                continue
            apsize = copy.deepcopy(photparams['APSIZE'])
            if photparams['APUNIT']=='pix':
                if photapcorr.table[photparams['INSTRUMENT']]['scaleunit']=='arcsec/pix':
                    apsize = apsize * photapcorr.table[photparams['INSTRUMENT']]['scale']
                elif photapcorr.table[photparams['INSTRUMENT']]['scaleunit']=='pix/arcsec':
                    apsize = apsize / photapcorr.table[photparams['INSTRUMENT']]['scale']
            EE = photapcorr.table[photparams['INSTRUMENT']]['model'](wave,apsize)
            mag = -2.5 * np.log10((aptab['aperture_sum'] - bkg) / EE) + ZP
            emag = -2.5 * np.sqrt(aptab['aperture_sum_err']**2 + ebkg**2) / ((aptab['aperture_sum'] - bkg) * np.log(10.))
            self.meta[i]['ABMAG'] = (mag[0],emag[0])
    ####################
    ####################
    ####################
    def make_conf(self,conf,keys=['BEAMA'
                                  ,'DYDX_ORDER_A'
                                  ,'XOFF_A','YOFF_A'
                                  ,'DISP_ORDER_A'
                                 ]):
        for i in self.gid:
            if i in conf.keys():
                self.meta[i]['CONF'] = GrismCONF(conf[i])
                self.meta[i]['CONF'].fetch()
            else:
                self.meta[i]['CONF'] = None
    ####################
    ####################
    ####################
    def make_sens(self,sens):
        for i in self.gid:
            if i in sens.keys():
                self.meta[i]['SENS'] = GrismSens(sens[i])
            else:
                self.meta[i]['SENS'] = None
    ####################
    ####################
    ####################
    def make_bkg(self,bkg=None,maskin=[0],method='median',sigma=3.,iters=5):
        for j in self.gid:
            x = fits.open(self.files[j])
            ext = self.meta[j]['EXT']
            xdq = x[('DQ',ext[1])].data
            xdata = x[ext].data
            a = DQMask(maskin)
            a.make_mask(xdq)
            mean,median,std = sigma_clipped_stats(xdata[a.mask],sigma=sigma,maxiters=iters)
            self.meta[j]['BKG'] = None
            self.meta[j]['BKG_FILE'] = None
            if method=='median':
                bkgim = np.full_like(xdata,median,dtype=float)
                self.meta[j]['BKG'] = bkgim
                self.meta[j]['BKG_FILE'] = (method,median,'No file')
            elif method=='master':
                if not bkg:
                    print('Error: bkg file is required. Set to None')
                elif bkg:
                    mask = np.full_like(a.mask,True,dtype=bool)
                    mask[np.where(np.abs(xdata/std) > sigma)] = False
                    mask = (mask & a.mask)
                    bkgdata = fits.open(bkg[j])[0].data
                    scale = self.make_mastersky(xdata,mask,bkgdata)
                    self.meta[j]['BKG'] = scale[0] * bkgdata
                    self.meta[j]['BKG_FILE'] = (method,scale,bkg)
    ####################
    ####################
    ####################
    def make_mastersky(self,xdata,xmask,bkgdata):
        x,y = bkgdata[xmask],xdata[xmask]
        popt,pcov = curve_fit(lambda x, *p: p[0]*x, x,y,p0=[1.])
        return (popt,pcov)
    ####################
    ####################
    ####################
    def make_xyoff(self):
        for i in self.gid:
            coefxoff = self.meta[i]['CONF'].value['XOFF_A']
            coefyoff = self.meta[i]['CONF'].value['YOFF_A']
            orderx,ordery = self.make_xyofforder(coefxoff),self.make_xyofforder(coefyoff)
            xyd = self.meta[self.meta[i]['DIRECT']]['XYD']
            xoff = make_SIP(coefxoff,xyd[0],xyd[1],startx=True)
            yoff = make_SIP(coefyoff,xyd[0],xyd[1],startx=True)
            self.meta[i]['XYOFF'] = (xoff[0],yoff[0])
    def make_xyofforder(self,coef):
        ncoef = len(coef)
        out,n = 0,1
        while n!=ncoef:
            out += 1
            n += out+1
        return out
    ####################
    ####################
    ####################
    def make_xyref(self):
        for j in self.gid:
            xyoff = self.meta[j]['XYOFF']
            xydif = self.meta[j]['XYDIF']
            xyd = self.meta[self.meta[j]['DIRECT']]['XYD']
            xref = xyd[0] + xyoff[0] + xydif[0]
            yref = xyd[1] + xyoff[1] + xydif[1]
            xyref = (xref,yref)
            self.meta[j]['XYREF'] = xyref 
    ####################
    ####################
    ####################
    def make_trace(self):
        for j in self.gid:
            xhbound = self.meta[j]['CONF'].value['BEAMA']
            xh = np.arange(xhbound[0],xhbound[1]+1,step=1)
            xyref = self.meta[j]['XYREF']
            order = self.meta[j]['CONF'].value['DYDX_ORDER_A']
            sip = []
            for k in np.arange(order+1):
                string = 'DYDX_A_' + str(int(k))
                coef = self.meta[j]['CONF'].value[string]
                x = make_SIP(coef,*xyref,startx=True)
                sip.append(x)
            yh = np.full_like(xh,0.,dtype=float)
            for k,kk in enumerate(sip):
                yh += kk*xh**k
            xg = xh + xyref[0]
            yg = yh + xyref[1]
            self.meta[j]['XG'] = xg
            self.meta[j]['YG'] = yg
            self.meta[j]['DYDX'] = sip
    ####################
    ####################
    ####################
    def make_wavelength(self):
        varclength = np.vectorize(self.arclength)
        for j in self.gid:
            xhbound = self.meta[j]['CONF'].value['BEAMA']
            xh = np.arange(xhbound[0],xhbound[1]+1,step=1)
            xyref = self.meta[j]['XYREF']
            order = self.meta[j]['CONF'].value['DISP_ORDER_A'].astype(int)
            dydx = self.meta[j]['DYDX']
            d = []
            sip = []
            for k in np.arange(order+1):
                string = 'DLDP_A_' + str(int(k))
                coef = self.meta[j]['CONF'].value[string]
                x = make_SIP(coef,*xyref,startx=True)
                sip.append(x)
            arc,earc = np.array(varclength(xh,*dydx))
            ww = np.full_like(xh,0.,dtype=float)
            for k,kk in enumerate(sip):
                ww += kk*arc**k
            self.meta[j]['WW'] = ww    
            self.meta[j]['WWUNIT'] = r'$\AA$'
    ####################
    ####################
    ####################
    def arclength_integrand(self,Fa,*coef):
        s = 0
        for i,ii in enumerate(coef):
            if i==0:
                continue
            s += i * ii * (Fa**(i-1))
        return np.sqrt(1. + np.power(s,2))
    def arclength(self,Fa,*coef):
        integral,err = quad(self.arclength_integrand, 0., Fa, args=coef)
        return integral,err    
    ####################
    ####################
    ####################    
    def make_flat(self,method='uniform',flatfile=None):
        for j in self.gid:
            x = fits.open(self.files[j])
            xdata = x[self.meta[j]['EXT']].data
            self.meta[j]['FLAT'] = None
            self.meta[j]['FLAT_FILE'] = None
            if method=='uniform':
                flatim = np.full_like(xdata,1.,dtype=float)
                self.meta[j]['FLAT'] = flatim
                self.meta[j]['FLAT_FILE'] = (method,'No file')
            elif method=='master':
                if not flatfile:
                    print('Error: flat file is required. Set to None')
                else:
                    flatim = np.full_like(xdata,np.nan,dtype=float)
                    nrow,ncol = xdata.shape[0],xdata.shape[1]
                    y = fits.open(flatfile[j])
                    wmin,wmax = y[0].header['WMIN'],y[0].header['WMAX']
                    a = {}
                    for k,kk in enumerate(y):
                        a[k] = y[k].data
                    x1 = np.copy(self.meta[j]['XG'].astype(int))
                    w1 = np.copy(self.meta[j]['WW'])
                    w1[np.where(w1<=wmin)],w1[np.where(w1>=wmax)] = wmin,wmax
                    x1min,x1max = np.min(x1),np.max(x1)
                    x0,x2 = np.arange(0,x1min),np.arange(x1max+1,ncol)
                    w0,w2 = np.full_like(x0,wmin,dtype=float),np.full_like(x2,wmax,dtype=float)
                    ww = np.concatenate((w0,w1,w2))
                    ww = (ww - wmin) / (wmax - wmin)
                    xx = np.concatenate((x0,x2,x2))
                    s = 0.
                    for k,kk in enumerate(a):
                        s += a[k] * ww**k
                    self.meta[j]['FLAT'] = np.copy(s)
                    self.meta[j]['FLAT_FILE'] = (method,flatfile)
    ####################
    ####################
    ####################
    def make_pam(self,method='uniform',pamfile=None):
        for j in self.gid:
            x = fits.open(self.files[j])
            xdata = x[self.meta[j]['EXT']].data
            self.meta[j]['PAM'] = None
            self.meta[j]['PAM_FILE'] = None
            if method=='uniform':
                self.meta[j]['PAM'] = np.full_like(xdata,1.,dtype=float)
                self.meta[j]['PAM_FILE'] = (method,'No file')
            elif method=='custom':
                if not pamfile:
                    print('Error: pamfile is required. Terminate')
                    return
                self.meta[j]['PAM'] = np.copy(fits.open(pamfile[j])[1].data)
                self.meta[j]['PAM_FILE'] = (method,pamfile)
            elif method=='master':
                print('Error: master method is not available in this version. Terminate')
                return
    ####################
    ####################
    ####################
    def make_clean(self,method=[True,True,True]):
        for j in self.gid:
            x = fits.open(self.files[j])
            xdata = x[self.meta[j]['EXT']].data
            bkg = self.meta[j]['BKG'] if method[0]==True else 0.
            flat = self.meta[j]['FLAT'] if method[1]==True else 1.
            pam = self.meta[j]['PAM'] if method[2]==True else 1.
            cleandata = (xdata - bkg) * pam / flat
            self.meta[j]['CLEAN'] = np.copy(cleandata)
    ####################
    ####################
    ####################
    def make_stamp(self,padx=5,pady=50):
        for j in self.gid:
            xg = self.meta[j]['XG']
            yg = self.meta[j]['YG']
            xgmin,xgmax = xg.min().astype(int)-padx,xg.max().astype(int)+padx
            ygmin,ygmax = yg.min().astype(int)-pady,yg.max().astype(int)+pady
            self.meta[j]['STAMP'] = ((xgmin,xgmax),(ygmin,ygmax))
    ####################
    ####################
    ####################
    def make_wavebin(self,method='WW',wavebin=None):
        for j in self.gid:
            self.meta[j]['WAVEBIN'] = None
            if method=='custom':
                if not wavebin:
                    print('Error: wavebin is required. Set to None')
                else:
                    self.meta[j]['WAVEBIN'] = wavebin
            elif (method=='WW') or (method=='median'):
                ww = np.copy(self.meta[j]['WW'])
                wavebin = np.diff(ww)
                median = np.median(wavebin)
                if method=='median':
                    wavebin = np.full_like(ww,median,dtype=float)
                elif method=='WW':
                    wavebin = np.concatenate((wavebin,[median]))
                self.meta[j]['WAVEBIN'] = np.copy(wavebin)
    ####################
    ####################
    ####################
    def make_exparams(self,method='aperture',apsize=5,apunit='pix',maskin=None):
        for j in self.gid:
            self.meta[j]['EX_PARAMS'] = {}
            nchip = self.meta[j]['NCHIP']
            string = 'FILTER1' if nchip > 1 else 'FILTER'
            instrument = '-'.join((self.meta[j]['TELESCOP']
                                   ,self.meta[j]['INSTRUME']
                                   ,self.meta[j]['DETECTOR']
                                   ,self.meta[j][string]
                                  ))
            self.meta[j]['EX_PARAMS']['INSTRUMENT'] = instrument
            self.meta[j]['EX_PARAMS']['METHOD'] = method
            self.meta[j]['EX_PARAMS']['APSIZE'] = apsize
            self.meta[j]['EX_PARAMS']['APUNIT'] = apunit
            self.meta[j]['EX_PARAMS']['MASKIN'] = maskin
    ####################
    ####################
    ####################
    def make_apcorr(self,replace='median'):
        grismapcorr = GrismApCorr()
        for j in self.gid:
            instrument = self.meta[j]['EX_PARAMS']['INSTRUMENT']
            ww = self.meta[j]['WW']
            apsize = self.meta[j]['EX_PARAMS']['APSIZE']
            apunit = self.meta[j]['EX_PARAMS']['APUNIT']
            self.meta[j]['APCORR'] = grismapcorr.make_apcorr(instrument,ww,apsize,apunit,replace)
    ####################
    ####################
    ####################
    def make_count(self,replace=None):
        for j in self.gid:
            xg = self.meta[j]['XG'].astype(int)
            yg = self.meta[j]['YG'].astype(int)
            xdata = self.meta[j]['CLEAN']
            bunit = self.meta[j]['BUNIT']
            apsize = self.meta[j]['EX_PARAMS']['APSIZE']
            apunit = self.meta[j]['EX_PARAMS']['APUNIT']
            method = self.meta[j]['EX_PARAMS']['METHOD']
            maskin = self.meta[j]['EX_PARAMS']['MASKIN']
            if apunit!='pix':
                print('Error: apunit must be pix. Terminate')
                sys.exit()
            if method=='aperture':
                cc = np.full_like(xg,np.nan,dtype=float)
                for k,kk in enumerate(xg):
                    cc[k] = np.sum(xdata[yg[k]-apsize:yg[k]+apsize+1,xg[k]])
                self.meta[j]['COUNT'] = np.copy(cc)  
            else:
                print('Error: method must be aperture. Terminate')
                sys.exit()
    ####################
    ####################
    ####################
    def make_flam(self):
        for j in self.gid:
            count = self.meta[j]['COUNT']
            apcorr = self.meta[j]['APCORR']
            wavebin = self.meta[j]['WAVEBIN']
            ww = self.meta[j]['WW']
            ss = self.meta[j]['SENS'].model(ww)
            flam = count / (wavebin * apcorr * ss)
            self.meta[j]['FLAM'] = np.copy(flam)
            if self.meta[j]['BUNIT'] == 'ELECTRONS':
                self.meta[j]['FLAM'] = copy.deepcopy(self.meta[j]['FLAM'] / self.meta[j]['EXPTIME'])
            self.meta[j]['FLAMUNIT'] = r'erg/s/cm$^2$/$\AA$'
    ####################
    ####################
    ####################
    def save(self,path=None,filename='GND.pickle'):
        if not path:
            print('Error: path is required. Terminate')
            return
        if path[-1] != '/':
            path += '/'
        try:
            os.mkdir(path)
        except:
            pass
        file = path + filename
        f = open(file,'wb')
        pickle.dump(self,f)
        f.close()
    ####################
    ####################
    ####################
    def show(self,method='meta'
             ,column=None,dosort=True,sort = ['EXPSTART','POSTARG1','POSTARG2','FILTER']
             ,traceon=False,dqon=False
             ,normalize=False
             ,showconf='long'
             ,zoom=False,dx=50,dy=50
             ,apsize=5,tracefrom='original'
             ,xmin=None, xmax=None
             ,ymin=None, ymax=None
             ,output=False
            ):
        if method=='meta':
            tab = pd.DataFrame(self.meta).T
            if output:
                return tab
            else:
                if dosort:
                    display(tab.sort_values(sort))
                else:
                    display(tab)
        if method=='direct':
            for i in self.did:
                x = fits.open(self.files[i])
                xdata = x[self.meta[i]['EXT']].data
                m = np.where(np.isfinite(xdata))
                vmin,vmax = np.percentile(xdata[m],5.),np.percentile(xdata[m],95.)
                plt.figure(figsize=(10,10))
                plt.imshow(xdata,origin='lower',cmap='viridis',vmin=vmin,vmax=vmax)
                plt.title('{0} {1}'.format(i,self.files[i]))
                xyd = self.meta[i]['XYD']
                plt.scatter(*xyd,s=500,lw=4,edgecolor='red',facecolor='None',label='XYD')
                plt.legend()
                if zoom:
                    x,y = xyd[0],xyd[1]
                    plt.xlim(x-dx,x+dx+1)
                    plt.ylim(y-dx,y+dy+1)
        if method=='grism':
            for i in self.pairs:
                for j in self.pairs[i]:
                    x = fits.open(self.files[j])
                    xdata = x[self.meta[i]['EXT']].data
                    m = np.where(np.isfinite(xdata))
                    vmin,vmax = np.percentile(xdata[m],5.),np.percentile(xdata[m],95.)
                    plt.figure(figsize=(10,10))
                    plt.imshow(xdata,origin='lower',cmap='viridis',vmin=vmin,vmax=vmax)
                    plt.title('{0} {1}'.format(j,self.files[j]))
                    ############
                    xyd = self.meta[i]['XYD']
                    xyref = self.meta[j]['XYREF']
                    plt.scatter(*xyref,s=30,color='red',label='XYREF')
                    plt.scatter(*xyd,s=30,color='orange',label='XYD')
                    plt.legend()
                    if traceon:
                        xg = self.meta[j]['XG']
                        yg = self.meta[j]['YG']
                        plt.plot(xg,yg,color='red',label='trace')
                        plt.legend()
                    if zoom:
                        xmin = self.meta[j]['XG'].min() - dx
                        xmax = self.meta[j]['XG'].max() + dx + 1
                        plt.xlim(xmin,xmax)
                        ymin = self.meta[j]['YG'].min() - dy
                        ymax = self.meta[j]['YG'].max() + dy + 1
                        plt.ylim(ymin,ymax)
        if (method=='CONF') & (showconf=='long'):
            for i in self.pairs:
                for j in self.pairs[i]:
                    x = open(self.meta[j]['CONF'].file,'r')
                    print('gid ',j,self.meta[j]['CONF'].file,'\n')
                    for i,ii in enumerate(x.readlines()):
                        print(i,ii)
                    print('\n############################\n')
        elif (method=='CONF') & (showconf=='short'):
            for i in self.pairs:
                for j in self.pairs[i]:
                    print('gid',j,self.meta[j]['CONF'].file,'\n')
                    display(self.meta[j]['CONF'].value)
                    print('\n############################\n')
        if method=='count':
            for i in self.pairs:
                plt.figure(figsize=(10,10))
                for j in self.pairs[i]:
                    xg = self.meta[j]['XG'].astype(int)
                    yg = self.meta[j]['YG'].astype(int)
                    ww = self.meta[j]['WW']
                    if tracefrom=='original':
                        x = fits.open(self.files[j])
                        xdata = x[self.meta[j]['EXT']].data
                    elif tracefrom=='clean':
                        xdata = self.meta[j]['CLEAN']
                    cc = np.full_like(xg,np.nan,dtype=float)
                    for k,kk in enumerate(xg):
                        cc[k] = np.sum(xdata[yg[k]-apsize:yg[k]+apsize+1,xg[k]])
                    plt.plot(ww,cc,label='{0} {1}'.format(j,self.files[j].split('/')[-1]))
                plt.ylabel('{0} \n apsize={1}'.format(self.meta[j]['BUNIT'],apsize))
                plt.xlabel('Wavelength ($\AA$)')
                plt.legend(bbox_to_anchor=(1.04,1),loc='upper left',ncol=1)                     
        if method=='bkg':
            for i in self.pairs:
                for j in self.pairs[i]:
                    fig,ax = plt.subplots(1,3,figsize=(30,10))
                    xdata = fits.open(self.files[j])[self.meta[j]['EXT']].data
                    bkgdata = self.meta[j]['BKG']
                    subdata = xdata - bkgdata
                    m = np.where(np.isfinite(xdata))
                    vmin,vmax = np.percentile(xdata[m],5.),np.percentile(xdata[m],95.)
                    ax[0].imshow(xdata,origin='lower',cmap='viridis',vmin=vmin,vmax=vmax)
                    ax[1].imshow(bkgdata,origin='lower',cmap='viridis'
                                 ,vmin=np.percentile(bkgdata,5.),vmax=np.percentile(bkgdata,95.)
                                )
                    ax[2].imshow(subdata,origin='lower',cmap='viridis',vmin=vmin,vmax=vmax)
                    ax[0].set_title('{0} {1}'.format(j,self.files[j].split('/')[-1]))
                    ax[1].set_title('bkg')
                    ax[2].set_title('subtract')
        if method=='flat':
            for i in self.pairs:
                for j in self.pairs[i]:
                    fig,ax = plt.subplots(1,3,figsize=(30,10))
                    xdata = fits.open(self.files[j])[self.meta[j]['EXT']].data
                    flatdata = self.meta[j]['FLAT']
                    normdata = xdata / flatdata
                    m = np.where(np.isfinite(xdata))
                    vmin,vmax = np.percentile(xdata[m],5.),np.percentile(xdata[m],95.)
                    ax[0].imshow(xdata,origin='lower',cmap='viridis',vmin=vmin,vmax=vmax)
                    ax[1].imshow(flatdata,origin='lower',cmap='viridis'
                                 ,vmin=np.percentile(flatdata,5.),vmax=np.percentile(flatdata,95.)
                                )
                    ax[2].imshow(normdata,origin='lower',cmap='viridis',vmin=vmin,vmax=vmax)
                    ax[0].set_title('{0} {1}'.format(j,self.files[j].split('/')[-1]))
                    ax[1].set_title('flat')
                    ax[2].set_title('normalized')
        if method=='pam':
            for i in self.pairs:
                for j in self.pairs[i]:
                    fig,ax = plt.subplots(1,3,figsize=(30,10))
                    xdata = fits.open(self.files[j])[self.meta[j]['EXT']].data
                    pamdata = self.meta[j]['PAM']
                    correctdata = xdata * pamdata
                    m = np.where(np.isfinite(xdata))
                    vmin,vmax = np.percentile(xdata[m],5.),np.percentile(xdata[m],95.)
                    ax[0].imshow(xdata,origin='lower',cmap='viridis',vmin=vmin,vmax=vmax)
                    ax[1].imshow(pamdata,origin='lower',cmap='viridis'
                                 ,vmin=np.percentile(pamdata,5.),vmax=np.percentile(pamdata,95.)
                                )
                    ax[2].imshow(correctdata,origin='lower',cmap='viridis',vmin=vmin,vmax=vmax)
                    ax[0].set_title('{0} {1}'.format(j,self.files[j].split('/')[-1]))
                    ax[1].set_title('pam')
                    ax[2].set_title('corrected')
        if method=='stamp':
            for i in self.pairs:
                for j in self.pairs[i]:
                    ext = self.meta[j]['EXT']
                    xdata = fits.open(self.files[j])[ext].data
                    xdq = fits.open(self.files[j])[('DQ',ext[1])].data
                    m = np.where(np.isfinite(xdata))
                    vmin,vmax = np.percentile(xdata[m],5.),np.percentile(xdata[m],95.)
                    stamp = self.meta[j]['STAMP']
                    plt.figure(figsize=(10,10))
                    plt.imshow(xdata,origin='lower',cmap='viridis',vmin=vmin,vmax=vmax)
                    plt.xlim(stamp[0][0],stamp[0][1])
                    plt.ylim(stamp[1][0],stamp[1][1])
                    plt.title('{0} {1}'.format(j,self.files[j].split('/')[-1]))
                    if dqon:
                        plt.figure(figsize=(10,10))
                        plt.imshow(xdq,origin='lower',cmap='viridis',vmin=0,vmax=1)
                        plt.xlim(stamp[0][0],stamp[0][1])
                        plt.ylim(stamp[1][0],stamp[1][1])
                        plt.title('DQ vmin=0, vmax=1')
        if method=='WW':
            for i in self.pairs:
                for j in self.pairs[i]:
                    ww = np.copy(self.meta[j]['WW'])
                    xg = np.copy(self.meta[j]['XG'])
                    if normalize:
                        xg -= self.meta[j]['XYREF'][0]
                    plt.plot(xg,ww,label='{0} {1}'.format(j,self.files[j].split('/')[-1]))
                    plt.xlabel('pix X')
                    plt.ylabel('wavelength')
                    plt.legend(bbox_to_anchor=(1.04,1),loc='upper left',ncol=1)                     
        if method=='trace':
            for i in self.pairs:
                for j in self.pairs[i]:
                    yg = np.copy(self.meta[j]['YG'])
                    xg = np.copy(self.meta[j]['XG'])
                    if normalize:
                        xg -= self.meta[j]['XYREF'][0]
                        yg -= self.meta[j]['XYREF'][1]
                    plt.plot(xg,yg,label='{0} {1}'.format(j,self.files[j].split('/')[-1]))
                    plt.xlabel('pix x')
                    plt.ylabel('pix y')
                    plt.legend(bbox_to_anchor=(1.04,1),loc='upper left',ncol=1)
        if method=='clean':
            for i in self.pairs:
                for j in self.pairs[i]:
                    fig,ax = plt.subplots(1,2,figsize=(20,10))
                    xdata = fits.open(self.files[j])[self.meta[j]['EXT']].data
                    cleandata = self.meta[j]['CLEAN']
                    m = np.where(np.isfinite(xdata))
                    vmin,vmax = np.percentile(xdata[m],5.),np.percentile(xdata[m],95.)
                    ax[0].imshow(xdata,origin='lower',cmap='viridis',vmin=vmin,vmax=vmax)
                    ax[1].imshow(cleandata,origin='lower',cmap='viridis',vmin=vmin,vmax=vmax)
                    ax[0].set_title('{0} {1}'.format(j,self.files[j].split('/')[-1]))
                    ax[1].set_title('clean')
                    if traceon:
                        xg = self.meta[j]['XG']
                        yg = self.meta[j]['YG']
                        ax[0].plot(xg,yg,color='red',label='trace')
                        ax[1].plot(xg,yg,color='red',label='trace')
                        plt.legend()
                    if zoom:
                        xmin = self.meta[j]['XG'].min() - dx
                        xmax = self.meta[j]['XG'].max() + dx + 1
                        ax[0].set_xlim(xmin,xmax)
                        ax[1].set_xlim(xmin,xmax)
                        ymin = self.meta[j]['YG'].min() - dy
                        ymax = self.meta[j]['YG'].max() + dy + 1
                        ax[0].set_ylim(ymin,ymax)
                        ax[1].set_ylim(ymin,ymax)
        if method=='flam':
            for i in self.pairs:
                plt.figure(figsize=(10,10))
                for j in self.pairs[i]:
                    flam = self.meta[j]['FLAM']
                    flamunit = self.meta[j]['FLAMUNIT']
                    ww = self.meta[j]['WW']
                    wwunit = self.meta[j]['WWUNIT']
                    if not xmin:
                        xmin = np.min(ww)
                    if not xmax:
                        xmax = np.max(ww)
                    mask = np.where((ww>=xmin) & (ww<=xmax))
                    plt.plot(ww[mask],flam[mask],label='{0} {1}'.format(j,self.files[j].split('/')[-1]))
                plt.ylabel('{0}'.format(flamunit))
                plt.xlabel('{0}'.format(wwunit))
                if ymin or ymax:
                    ymin = np.min(flam[mask]) if not ymin else ymin
                    ymax = np.max(flam[mask]) if not ymax else ymax
                    plt.ylim(ymin,ymax)
                plt.legend(bbox_to_anchor=(1.04,1),loc='upper left',ncol=1)                     
    ####################
    ####################
    ####################                
#     def make_drz(self):
#         num = len(self.files)
#         self.make_clean(method=[True,True,False])
#         for i in self.pairs:
#             x = []
#             for j in self.pairs[i]:
#                 dst = os.getcwd() + '/' + self.files[j].split('/')[-1]
#                 copyfile(self.files[j],dst)
#                 xx = fits.open(dst)
#                 stamp = self.meta[j]['STAMP']
#                 xx['SCI'].data[stamp[1][0]:stamp[1][1],stamp[0][0]:stamp[0][1]] = np.copy(self.meta[j]['CLEAN'][stamp[1][0]:stamp[1][1],stamp[0][0]:stamp[0][1]])
#                 xx.writeto(dst,overwrite=True)
#                 xx.close()                  
#                 x.append(dst)
#             path = os.getcwd() + '/{0}'.format(num)
#             drz = path + '_drz.fits'
#             astrodrizzle.AstroDrizzle(x
#                                       ,output=path
#                                       ,build=True
#                                       ,clean=True
#                                       ,skysub='no'
#                                       ,final_wcs=True
#                                       ,final_kernel='gaussian'
#                                       ,combine_type='median'
#                                       ,final_refimage=x[0]
#                                      ) 
#             self.make_drzmeta(i,num,drz,ref=0)
#             for j in x:
#                 os.remove(j)
#             num += 1
#     def make_drzmeta(self,direct,num,drz,ref=0):
#         self.files.append(drz)
#         self.pairs[direct].append(num)
#         i = self.pairs[direct][ref]
#         xdata = fits.open(drz)['SCI'].data
#         self.meta[num] = copy.deepcopy(self.meta[i])
#         self.meta[num]['ID'] = num
#         self.meta[num]['FILE'] = drz
#         self.meta[num]['BKG'],self.meta[num]['BKG_FILE'] = np.full_like(xdata,0.,dtype=float),'drz'
#         self.meta[num]['FLAT'],self.meta[num]['FLAT_FILE'] = np.full_like(xdata,1.,dtype=float),'drz'
#         self.meta[num]['PAM'],self.meta[num]['PAM_FILE'] = np.full_like(xdata,1.,dtype=float),'drz'
    ####################
    ####################
    ####################
