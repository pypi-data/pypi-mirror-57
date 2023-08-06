from accpac import *

class POPurchaseOrder:
    def __init__(self, id=-1):
        self.poporh = View("PO0620", id)
        self.poporl = View("PO0630", id)
        self.poporc = View("PO0610", id)
        self.poporr = View("PO0632", id)
        self.poporg = View("PO0619", id)
        self.poporho = View("PO0623", id)
        self.poporlo = View("PO0633", id)

        self.poporh.compose(self.poporc, self.poporl, self.poporr, self.poporg, self.poporho)
        self.poporl.compose(self.poporh, self.poporc, self.poporg, None, None, self.poporlo)
        self.poporc.compose(self.poporh, self.poporl)
        self.poporr.compose(self.poporh, self.poporg)
        self.poporg.compose(self.poporh, self.poporc, self.poporl, self.poporr)
        self.poporho.compose(self.poporh)
        self.poporlo.compose(self.poporl)

    def load(ponumber):
        self.poporh.order(1) # PONUMBER
        self.poporh.put("PONUMBER", ponumber, 0)
        return self.poporh.read()

    def delete():
        return self.poporh.Delete()

    def setHeaderOptionalField(optfield, value):
        self.poporho.put("OPTFIELD", optfield, 0)
        if self.poporho.read() == 0:
            # already exists
            if self.poporho.put("VALUE", value) != 0:
                return False
            if self.poporho.update() != 0:
                return False
            return True
        self.poporho.recordGenerate()
        if self.poporho.put("OPTFIELD", optfield) != 0:
            return False
        if self.poporho.put("VALUE", value) != 0:
            return False
        if self.poporho.insert() != 0:
            return False
        return True
