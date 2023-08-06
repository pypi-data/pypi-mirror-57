from accpac import *

class POReturn:
    def __init__(self, id=-1):
        self.poreth = View("PO0731", id)
        self.poretl = View("PO0735", id)
        self.poretc = View("PO0729", id)
        self.poretg = View("PO0730", id)
        self.poretho = View("PO0738", id)
        self.poretlo = View("PO0739", id)
        self.poretll = View("PO0799", id)
        self.poretls = View("PO0790", id)

        self.poreth.compose(self.poretc, self.poretl, self.poretg, self.poretho)
        self.poretl.compose(self.poreth, self.poretc, self.poretg, None, None, self.poretlo, self.poretll, self.poretls)
        self.poretc.compose(self.poreth, self.poretl)
        self.poretg.compose(self.poreth, self.poretc, self.poretl)
        self.poretho.compose(self.poreth)
        self.poretlo.compose(self.poretl)
        self.poretll.compose(self.poretl, None, None)
        self.poretls.compose(self.poretl, None, None)

    def load(retnumber):
        self.poreth.order(1) # RETNUMBER
        self.poreth.put("RETNUMBER", retnumber, 0)
        return self.poreth.read()

    def delete():
        return self.poreth.Delete()
