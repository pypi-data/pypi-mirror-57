from accpac import *

class GLAccount:
    def __init__(self, id=-1):
        self.glamf = View("GL0001")
        self.glais = View("GL0004")
        self.glavc = View("GL0012")
        self.glcas = View("GL0107")
        self.glamfo = View("GL0400")
        self.glamfto = View("GL0401")
        self.glachd = View("GL0057")
        self.glpachd = View("GL0063")

        self.glamf.compose(None, self.glais, self.glavc, None, self.glcas, self.glamfo, self.glamfto, self.glachd, self.glpachd)
        self.glais.compose(self.glamf)
        self.glavc.compose(self.glamf, None)
        self.glcas.compose(self.glamf)
        self.glamfo.compose(self.glamf)
        self.glamfto.compose(self.glamf)
        self.glachd.compose(self.glamf)
        self.glpachd.compose(self.glamf)

    def read(account):
        self.glamf.put("ACCTID", account, 0)
        return self.glamf.read()
