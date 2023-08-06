from accpac import *

class ICAdjustment:
    def __init__(self, id=-1):
        self.icadeh  = View("IC0120", id)
        self.icaded  = View("IC0110", id)
        self.icadeho  = View("IC0125", id)
        self.icadedo  = View("IC0115", id)
        self.icadeds  = View("IC0117", id)
        self.icadedl  = View("IC0113", id)

        self.icadeh.compose(self.icaded, self.icadeho)
        self.icaded.compose(self.icadeh, None, None, None, None, None, None, self.icadedo, self.icadeds, self.icadedl)
        self.icadeho.compose(self.icadeh)
        self.icadedo.compose(self.icaded)
        self.icadeds.compose(self.icaded)
        self.icadedl.compose(self.icaded)

    def load(docnum):
        self.icadeh.order(3) # DOCNUM
        self.icadeh.put("DOCNUM", docnum, 0)
        return self.icadeh.read()
