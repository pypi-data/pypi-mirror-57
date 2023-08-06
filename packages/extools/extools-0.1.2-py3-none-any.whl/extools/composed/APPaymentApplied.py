from accpac import *

class APPaymentApplied:
    def __init__(self, id=-1):
        self.apbta = View("AP0030", id)
        self.aptcr = View("AP0031", id)
        self.aptcp = View("AP0033", id)
        self.aptcu = View("AP0034", id)
        self.aptcn = View("AP0032", id)
        self.appoop = View("AP0048", id)
        self.aptcc = View("AP0170", id)
        self.aptcro = View("AP0406", id)

        self.apbta.compose(self.aptcr)
        self.aptcr.compose(self.apbta, self.aptcn, self.aptcp, self.aptcro, self.aptcc)
        self.aptcp.compose(self.aptcr, self.aptcu, self.appoop)
        self.aptcu.compose(self.aptcp)
        self.aptcn.compose(self.aptcr)
        self.appoop.compose(self.apbta, self.aptcr, self.aptcn, self.aptcp, self.aptcu)
        self.aptcc.compose(self.aptcr)
        self.aptcro.compose(self.aptcr)

        self.appypt = View("AP0040")

    def createBatch():
        r = 0
        if r == 0:
            r = self.apbta.put("PAYMTYPE", "PY")
        if r == 0:
            r = self.apbta.recordGenerate(1)
        return r

    def postBatch():
        r = 0
        if r == 0:
            r = self.appypt.put("TYPEBTCH", "PY")
        if r == 0:
            r = self.appypt.put("BATCHIDFR", self.apbta.get("CNTBTCH"))
        if r == 0:
            r = self.appypt.put("BATCHIDTO", self.apbta.get("CNTBTCH"))
        if r == 0:
            r = self.appypt.process()
        return r
