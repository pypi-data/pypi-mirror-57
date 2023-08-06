from accpac import *

class OEInvoice:
    def __init__(self, id=-1):
        self.oeinvh  = View("OE0420", id)
        self.oeinvd  = View("OE0400", id)
        self.oetermi = View("OE0720", id)
        self.oecoini = View("OE0160", id)
        self.oeinvr  = View("OE0427", id)
        self.oeinvdl = View("OE0406", id)
        self.oeinvds = View("OE0407", id)
        self.oeinvho = View("OE0422", id)
        self.oeinvdo = View("OE0401", id)
        self.oeinvdd = View("OE0402", id)
        self.oeinvdds= View("OE0404", id)
        self.oeinvddl= View("OE0405", id)
        self.oeinvdb = View("OE0403", id)

        self.oeinvh.compose(self.oeinvd, None, self.oecoini, self.oetermi, self.oeinvr, self.oeinvho)
        self.oeinvd.compose(self.oeinvh, self.oeinvdo, self.oeinvdb, self.oeinvdd, self.oeinvds, self.oeinvdl)
        self.oetermi.compose(self.oeinvh)
        self.oecoini.compose(self.oeinvh)
        self.oeinvr.compose(self.oeinvh)
        self.oeinvdl.compose(self.oeinvd)
        self.oeinvds.compose(self.oeinvd)
        self.oeinvho.compose(self.oeinvh)
        self.oeinvdo.compose(self.oeinvd)
        self.oeinvdd.compose(self.oeinvd, self.oeinvdds, self.oeinvddl)
        self.oeinvdds.compose(self.oeinvdd)
        self.oeinvddl.compose(self.oeinvdd)
        self.oeinvdb.compose(self.oeinvd)
        self.exists = False

    def load(invoiceNumber):
        self.exists = True
        self.oeinvh.order(6) # INVNUMBER
        self.oeinvh.put("INVNUMBER", invoiceNumber, 0)
        return self.oeinvh.read()

    def create():
        self.exists = False
        self.oeinvh.order(0) # INVUNIQ
        self.oeinvh.recordGenerate()
        return 0

    def create(idcust):
        self.exists = False
        self.oeinvh.order(0) # INVUNIQ
        self.oeinvh.recordGenerate()
        self.oeinvh.put("CUSTOMER", idcust, 1)
        return 0

    def loadShipment(shipmentNumber):
        self.oeinvh.put("SHINUMBER", shipmentNumber)
        self.oeinvh.put("INV1SHIPMT", 1)
        self.oeinvh.process()
        return 0

    def save():
        if self.exists == False:
            r = self.oeinvh.insert()
            if r == 0:
                self.exists = True
            return r

        return self.oeinvh.update()
