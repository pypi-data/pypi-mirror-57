from accpac import *

class ICItem:
    def __init__(self, id=-1):
        self.icitem = View("IC0310", id)
        self.icunit = View("IC0750", id)
        self.icitmtx = View("IC0330", id)
        self.icitmv = View("IC0340", id)
        self.icitemo = View("IC0313", id)
        self.icitmc = View("IC0319", id)
        self.icitemso = View("IC0314", id)
        self.icitemlo = View("IC0312", id)

        self.icitem.compose(self.icunit, self.icitmtx, self.icitmv, None, None, None, None, self.icitemo, self.icitmc, self.icitemso, self.icitemlo)
        self.icunit.compose(self.icitem)
        self.icitmtx.compose(self.icitem, None, None)
        self.icitmv.compose(self.icitem, None, self.icunit)
        self.icitemo.compose(self.icitem)
        self.icitmc.compose(self.icitem, None, self.icunit)
        self.icitemso.compose(self.icitem)
        self.icitemlo.compose(self.icitem)

    def load(itemno):
        self.icitem.order(0) # ITEMNO
        self.icitem.put("ITEMNO", itemno, 0)
        return self.icitem.read()
