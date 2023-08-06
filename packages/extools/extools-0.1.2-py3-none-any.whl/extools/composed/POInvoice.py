from accpac import *

class POInvoice:
    def __init__(self, id=-1):
        self.poinvh = View("PO0420", id)
        self.poinvl = View("PO0430", id)
        self.poinvc = View("PO0416", id)
        self.poinvs = View("PO0440", id)
        self.poinvp = View("PO0436", id)
        self.poinvg = View("PO0419", id)
        self.poinvr = View("PO0438", id)
        self.poinvw = View("PO0444", id)
        self.poinvho= View("PO0423", id)
        self.poinvlo= View("PO0433", id)
        self.poinvso= View("PO0443", id)
        self.poinve = View("PO0417", id)
        self.poinvd = View("PO0415", id)
        self.poinvk = View("PO0424", id)
        self.poinvll = View("PO0819", id)
        self.poinvls = View("PO0810", id)

        self.poinvh.compose(self.poinvc, self.poinvl, self.poinvs, self.poinvp, self.poinvg, self.poinvr, self.poinvw, self.poinvho, self.poinvd)
        self.poinvl.compose(self.poinvh, self.poinvg, None, None, self.poinvlo, self.poinvll, self.poinvls)
        self.poinvc.compose(self.poinvh, self.poinvl)
        self.poinvs.compose(self.poinvh, self.poinvg, None, None, self.poinvr, self.poinvw, self.poinvso, self.poinvd)
        self.poinvp.compose(self.poinvh, self.poinvg)
        self.poinvg.compose(self.poinvh, self.poinvc, self.poinvl, self.poinvp, self.poinvs, self.poinvr, self.poinvw, self.poinvd)
        self.poinvr.compose(self.poinvh, self.poinvg)
        self.poinvw.compose(self.poinvh, self.poinvg, None, None, self.poinvs, self.poinvr, self.poinvl)
        self.poinvho.compose(self.poinvh)
        self.poinvlo.compose(self.poinvl)
        self.poinvso.compose(self.poinvs)
        self.poinve.compose(None, self.poinvd, self.poinvs)
        self.poinvd.compose(self.poinvs, self.poinvh, self.poinvg, self.poinve)
        self.poinvk.compose(self.poinvs, self.poinvd)
        self.poinvll.compose(self.poinvl, None, None)
        self.poinvls.compose(self.poinvl, None, None)

    def load(invnumber):
        self.poinvh.order(1) # INVNUMBER
        self.poinvh.put("INVNUMBER", invnumber, 0)
        return self.poinvh.read()

    def delete():
        return self.poinvh.Delete()

    def loadReceipt(rcpnumber):
        self.poinvg.put("VDCODE", self.poinvh.get("VDCODE"))
        self.poinvg.put("LOADRCPNUM", rcpnumber)
        self.poinvg.put("FUNCTION", 9)
        return self.poinvg.process()
