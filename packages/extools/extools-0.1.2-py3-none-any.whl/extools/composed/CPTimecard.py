from accpac import *

#    from CPTimecard import CPTimecard
#    cptc = CPTimecard()

class CPTimecard:
    def __init__(self, id=-1):
        self.cptchd = View("CP0031", id)
        self.cptcdt = View("CP0032", id)
        self.cptcho = View("CP0127", id)
        self.cptcdo = View("CP0128", id)
        self.cptcjb = View("CP0042", id)
        self.cptcjo = View("CP0141", id)
        
        self.cptchd.compose(self.cptcdt, self.cptcho)
        self.cptcdt.compose(self.cptchd, self.cptcdo, self.cptcjb)
        self.cptcho.compose(self.cptchd)
        self.cptcdo.compose(self.cptcdt)
        self.cptcjb.compose(self.cptcdt, self.cptcjo)
        self.cptcjo.compose(self.cptcjb)
        
