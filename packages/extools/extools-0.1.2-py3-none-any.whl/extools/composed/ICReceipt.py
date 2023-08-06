from accpac import *

class ICReceipt:
    def __init__(self, id=-1):
        self.icreeh = View("IC0590", id)
        self.icreed = View("IC0580", id)
        self.icreeho= View("IC0595", id)
        self.icreedo= View("IC0585", id)
        self.icreeds= View("IC0587", id)
        self.icreedl= View("IC0582", id)

        self.icreeh.compose(self.icreed, self.icreeho)
        self.icreed.compose(self.icreeh, None, None, None, None, None, self.icreedo, self.icreeds, self.icreedl)
        self.icreeho.compose(self.icreeh)
        self.icreedo.compose(self.icreed)
        self.icreeds.compose(self.icreed)
        self.icreedl.compose(self.icreed)

    def load(docnum):
        self.icreeh.order(2) # RECPNUMBER
        self.icreeh.put("RECPNUMBER", docnum, 0)
        return self.icreeh.read()
