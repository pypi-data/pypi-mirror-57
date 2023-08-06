from accpac import *

class OECreditNote:
    def __init__(self, id=-1):
        self.oecrdh   = View("OE0240", id)
        self.oecrdd   = View("OE0220", id)
        self.oecoinc  = View("OE0140", id)
        self.oecrddl  = View("OE0226", id)
        self.oecrdds  = View("OE0227", id)
        self.oecrdho  = View("OE0242", id)
        self.oecrddo  = View("OE0221", id)
        self.oecrddd  = View("OE0222", id)
        self.oecrddds = View("OE0224", id)
        self.oecrdddl = View("OE0225", id)
        self.oecrddb  = View("OE0223", id)

        self.oecrdh.compose(self.oecrdd, None, self.oecoinc, self.oecrdho)
        self.oecrdd.compose(self.oecrdh, self.oecrddo, self.oecrddb, self.oecrddd, self.oecrdds, self.oecrddl)
        self.oecoinc.compose(self.oecrdh)
        self.oecrddl.compose(self.oecrdd)
        self.oecrdds.compose(self.oecrdd)
        self.oecrdho.compose(self.oecrdh)
        self.oecrddo.compose(self.oecrdd)
        self.oecrddd.compose(self.oecrdd, self.oecrddds, self.oecrdddl)
        self.oecrddds.compose(self.oecrddd)
        self.oecrdddl.compose(self.oecrddd)
        self.oecrddb.compose(self.oecrdd)

    def load(crdNumber):
        self.oecrdh.order(1) # CRDNUMBER
        self.oecrdh.put("CRDNUMBER", crdNumber, 0)
        return self.oecrdh.read()
