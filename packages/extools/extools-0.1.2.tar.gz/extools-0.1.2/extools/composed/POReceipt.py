from accpac import *

class POReceipt:
    def __init__(self, id=-1):
        self.porcph = View("PO0700", id)
        self.porcpl = View("PO0710", id)
        self.porcpc = View("PO0695", id)
        self.porcpv = View("PO0718", id)
        self.porcps = View("PO0714", id)
        self.porcpg = View("PO0699", id)
        self.porcpr = View("PO0705", id)
        self.porcpho= View("PO0703", id)
        self.porcpd = View("PO0696", id)
        self.porcplo= View("PO0717", id)
        self.porcpco= View("PO0721", id)
        self.porcpso= View("PO0719", id)
        self.porcpe = View("PO0697", id)
        self.porcpk = View("PO0704", id)
        self.porcpls = View("PO0780", id)
        self.porcpll = View("PO0789", id)

        self.porcph.compose(self.porcpc, self.porcpl, self.porcpv, self.porcps, self.porcpg, self.porcpr, self.porcpho, self.porcpd)
        self.porcpl.compose(self.porcph, self.porcpc, self.porcpg, None, None, self.porcplo, self.porcpll, self.porcpls)
        self.porcpc.compose(self.porcph, self.porcpl)
        self.porcpv.compose(self.porcph, self.porcps, self.porcpg, self.porcpco)
        self.porcps.compose(self.porcpv, self.porcpg, self.porcph, None, None, self.porcpso, self.porcpd)
        self.porcpg.compose(self.porcph, self.porcpc, self.porcpl, self.porcps, self.porcpv, self.porcpr, self.porcpd)
        self.porcpr.compose(self.porcph, self.porcpg)
        self.porcpho.compose(self.porcph)
        self.porcpd.compose(self.porcps, self.porcpv, self.porcph, self.porcpg, self.porcpe)
        self.porcplo.compose(self.porcpl)
        self.porcpco.compose(self.porcpv)
        self.porcpso.compose(self.porcps)
        self.porcpe.compose(None, self.porcpd, self.porcps)
        self.porcpk.compose(self.porcpd, self.porcpl)
        self.porcpls.compose(self.porcpl, None, None)
        self.porcpll.compose(self.porcpl, None, None)

    def load(rcpnumber):
        self.porcph.order(1) # RCPNUMBER
        self.porcph.put("RCPNUMBER", rcpnumber, 0)
        return self.porcph.read()

    def delete():
        return self.porcph.Delete()
