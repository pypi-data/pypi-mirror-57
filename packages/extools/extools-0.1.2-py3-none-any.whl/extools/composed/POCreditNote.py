from accpac import *

class POCreditNote:
    def __init__(self, id=-1):
        self.pocrnh = View("PO0311", id)
        self.pocrnl = View("PO0315", id)
        self.pocrnc = View("PO0309", id)
        self.pocrns = View("PO0320", id)
        self.pocrng = View("PO0310", id)
        self.pocrnw = View("PO0325", id)
        self.pocrnho = View("PO0314", id)
        self.pocrnlo = View("PO0318", id)
        self.pocrnso = View("PO0323", id)
        self.pocrne = View("PO0327", id)
        self.pocrnd = View("PO0326", id)
        self.pocrnk = View("PO0319", id)
        self.pocrnll = View("PO0829", id)
        self.pocrnls = View("PO0820", id)
        
        self.pocrnh.compose(self.pocrnc, self.pocrnl, self.pocrns, self.pocrng, self.pocrnw, self.pocrnho, self.pocrnd)
        self.pocrnl.compose(self.pocrnh, self.pocrnc, self.pocrng, None, None, self.pocrnlo, self.pocrnll, self.pocrnls)
        self.pocrnc.compose(self.pocrnh, self.pocrnl)
        self.pocrns.compose(self.pocrnh, self.pocrng, None, None, self.pocrnw, self.pocrnso, self.pocrnd)
        self.pocrng.compose(self.pocrnh, self.pocrnc, self.pocrnl, self.pocrns, None, self.pocrnw, self.pocrnd, self.pocrnll, self.pocrnls)
        self.pocrnw.compose(self.pocrnh, self.pocrng, None, None, self.pocrns, self.pocrnl)
        self.pocrnho.compose(self.pocrnh)
        self.pocrnlo.compose(self.pocrnl)
        self.pocrnlo.compose(self.pocrns)
        self.pocrne.compose(None, self.pocrnd, self.pocrns)
        self.pocrnd.compose(self.pocrns, self.pocrnh, self.pocrng, self.pocrne)
        self.pocrnk.compose(self.pocrns, self.pocrnd)
        self.pocrnll.compose(self.pocrnl, None, None)
        self.pocrnls.compose(self.pocrnl, None, None)
        
