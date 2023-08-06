from accpac import *

class ICShipment:
    def __init__(self, id=-1):
        self.icsheh  = View("IC0640", id)
        self.icshed  = View("IC0630", id)
        self.icsheho  = View("IC0645", id)
        self.icshedo  = View("IC0635", id)
        self.icshedl  = View("IC0632", id)
        self.icsheds  = View("IC0636", id)

        self.icsheh.compose(self.icshed, None, self.icsheho)
        self.icshed.compose(self.icsheh, None, None, None, None, None, None, self.icshedo, self.icshedl, self.icsheds)
        self.icsheho.compose(self.icsheh)
        self.icshedo.compose(self.icshed)
        self.icshedl.compose(self.icshed)
        self.icsheds.compose(self.icshed)

    def load(docnum):
        self.icsheh.order(3) # DOCNUM
        self.icsheh.put("DOCNUM", docnum, 0)
        return self.icsheh.read()
