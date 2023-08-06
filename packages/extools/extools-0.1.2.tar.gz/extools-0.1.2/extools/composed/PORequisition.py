from accpac import *

class PORequisition:
    def __init__(self, id=-1):
        self.porqnh = View("PO0760", id)
        self.porqnl = View("PO0770", id)
        self.porqnc = View("PO0750", id)
        self.porqng = View("PO0759", id)
        self.porqnho = View("PO0763", id)
        self.porqnlo = View("PO0773", id)
        self.porqnlv = View("PO0777", id)
        
        self.porqnh.compose(self.porqnc, self.porqnl, self.porqng, self.porqnho, self.porqnlv)
        self.porqnl.compose(self.porqnh, self.porqnc, self.porqng, self.porqnlo, self.porqnlv)
        self.porqnc.compose(self.porqnh, self.porqnl)
        self.porqng.compose(self.porqnh, self.porqnc, self.porqnl, self.porqnlv)
        self.porqnho.compose(self.porqnh)
        self.porqnlo.compose(self.porqnl)
        self.porqnlv.compose(self.porqnh, self.porqng, self.porqnl)
