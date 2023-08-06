from accpac import *

class ARReceipt:
    def __init__(self, id=-1):
        self.arbta = View("AR0041", id)
        self.artcr = View("AR0042", id)
        self.artcp = View("AR0044", id)
        self.artcu = View("AR0045", id)
        self.artcn = View("AR0043", id)
        self.arpoop = View("AR0061", id)
        self.artcro = View("AR0406", id)
        self.artcc = View("AR0170", id)

        self.arpypt = View("AR0049", id)

        self.arbta.compose(self.artcr)
        self.artcr.compose(self.arbta, self.artcn, self.artcp, self.artcro, self.artcc)
        self.artcro.compose(self.artcr)
        self.artcc.compose(self.artcr)
        self.artcp.compose(self.artcr, self.artcu, self.arpoop)
        self.artcu.compose(self.artcp)
        self.artcn.compose(self.artcr)
        self.arpoop.compose(self.arbta, self.artcr, self.artcn, self.artcp, self.artcu)

    def createBatch():
        r = 0
        if (r == 0):
            r = arbta.put("CODEPYMTYP", "CA")
        if (r == 0):
            r = arbta.RecordGenerate(1)
        return r

    def postBatch():
        r = 0
        if (r == 0):
            r = self.arpypt.put("TYPEBTCH", "CA")
        if (r == 0):
            r = self.arpypt.put("BATCHIDFR", self.arbta.get("CNTBTCH"))
        if (r == 0):
            r = self.arpypt.put("BATCHIDTO", self.arbta.get("CNTBTCH"))
        if (r == 0):
            r = self.arpypt.Process()
        return r
