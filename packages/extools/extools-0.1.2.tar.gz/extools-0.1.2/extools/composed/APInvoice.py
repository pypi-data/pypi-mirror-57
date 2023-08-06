from accpac import *

class APInvoice:
    def __init__(self, id=-1):
        self.apibc = View("AP0020", id)
        self.apibh = View("AP0021", id)
        self.apibd = View("AP0022", id)
        self.apibs = View("AP0023", id)
        self.apibho = View("AP0402", id)
        self.apibdo = View("AP0401", id)

        self.apivpt = View("AP0039", id)

        self.apibc.compose(self.apibh)
        self.apibh.compose(self.apibc, self.apibd, self.apibs, self.apibho)
        self.apibd.compose(self.apibh, self.apibc, self.apibdo)
        self.apibs.compose(self.apibh)
        self.apibho.compose(self.apibh)
        self.apibdo.compose(self.apibd)

    def createBatch():
        r = 0
        if r == 0:
            r = self.apibc.recordGenerate(1)
        return r

    def createInvoice(vendorId):
        r = 0
        if r == 0:
            r = self.apibh.recordGenerate()
        if r == 0:
            r = self.apibh.put("IDVEND", vendorId)
        if r == 0:
            r = self.apibh.put("TEXTTRX", 1) # Document Type = Invoice
        if r == 0:
            r = self.apibh.put("PROCESSCMD", 4) # Insert Optional Fields
        if r == 0:
            r = self.apibh.process()
        return r

    def createCreditNote(vendorId):
        r = 0
        if r == 0:
            r = self.apibh.recordGenerate()
        if r == 0:
            r = self.apibh.put("IDVEND", vendorId)
        if r == 0:
            r = self.apibh.put("TEXTTRX", 3) # Document Type = Credit Note
        if r == 0:
            r = self.apibh.put("PROCESSCMD", 4) # Insert Optional Fields
        if r == 0:
            r = self.apibh.process()
        return r

    def postBatch():
        r = 0
        if r == 0:
            r = self.apibc.put("BTCHSTTS", 7) # Ready To Post
        if r == 0:
            r = self.apibc.update()

        if r == 0:
            r = self.apivpt.put("BATCHIDFR", self.apibc.get("CNTBTCH"))
        if r == 0:
            r = self.apivpt.put("BATCHIDTO", self.apibc.get("CNTBTCH"))
        if r == 0:
            r = self.apivpt.process()
        return r
