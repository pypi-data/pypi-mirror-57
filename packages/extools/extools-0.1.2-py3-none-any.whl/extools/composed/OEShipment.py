from accpac import *

class OEShipment:
    def __init__(self, id=-1):
        self.oeshih  = View("OE0692", id)
        self.oeshid  = View("OE0691", id)
        self.oeterms = View("OE0745", id)
        self.oecoins = View("OE0190", id)
        self.oeshir  = View("OE0694", id)
        self.oeshiho = View("OE0704", id)
        self.oeshidl = View("OE0708", id)
        self.oeshids = View("OE0709", id)
        self.oeshido = View("OE0702", id)
        self.oeshidd = View("OE0703", id)
        self.oeshidds= View("OE0706", id)
        self.oeshiddl = View("OE0707", id)
        self.oeshidb = View("OE0705", id)

        self.oeshih.compose(self.oeshid, None, self.oecoins, self.oeterms, self.oeshir, self.oeshiho)
        self.oeshid.compose(self.oeshih, None, self.oeshido, self.oeshidb, self.oeshidd, self.oeshids, self.oeshidl)
        self.oeterms.compose(self.oeshih)
        self.oecoins.compose(self.oeshih, self.oeshid)
        self.oeshir.compose(self.oeshih)
        self.oeshiho.compose(self.oeshih)
        self.oeshido.compose(self.oeshid)
        self.oeshidd.compose(self.oeshid, self.oeshidds, None, self.oeshiddl)
        self.oeshidds.compose(self.oeshidd, None)
        self.oeshidb.compose(self.oeshid)
        self.oeshiddl.compose(self.oeshidd, None)
        self.oeshids.compose(self.oeshid, None)
        self.oeshidl.compose(self.oeshid, None)

    def load(shipmentNumber):
        self.oeshih.order(1) # SHINUMBER
        self.oeshih.put("SHINUMBER", shipmentNumber, 0)
        return self.oeshih.read()
