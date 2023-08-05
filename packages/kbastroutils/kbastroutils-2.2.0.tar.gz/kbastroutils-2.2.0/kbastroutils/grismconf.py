class GrismCONF:
    """
    Example:
    x = GrismCONF('WFC3.UVIS.G280.CHIP1.V2.0.conf')
    x.show() >>> read the file each line
    x.fetch() >>> fecth lines with given keys, and wrap them
    ----------
    
    GrismCONF is a class handling the read of the .conf files for grism reduction.
    """
    def __init__(self,file):
        self.file = file
        self.value = None
    ##############################
    def show(self):
        x = open(self.file,'r')
        out = {}
        for i,ii in enumerate(x.readlines()):
            print(i,ii)
    ##############################
    def fetch(self,keys=['BEAMA'
                         ,'DYDX_ORDER_A'
                         ,'XOFF_A','YOFF_A'
                         ,'DISP_ORDER_A'
                        ]):
        import numpy as np
        import copy
        x = open(self.file,'r')
        xx = x.readlines()
        if self.value:
            out = copy.deepcopy(self.value)
        else:
            out = {}
        for i,ii in enumerate(xx):
            y = ii.split()
            if len(y) > 0:
                if y[0] in keys:
                    try:
                        a = np.array(y[1:]).astype(float)
                    except:
                        a = np.array(y[1:])
                    out[y[0]] = np.copy(a)
                    if 'ORDER' in y[0]:
                        imin = i+1
                        imax = i+1+np.array(y[1]).astype(int)
                        for j in np.arange(imin,imax+1):
                            yy = xx[j].split()
                            out[yy[0]] = np.array(yy[1:]).astype(float)
        self.value = out