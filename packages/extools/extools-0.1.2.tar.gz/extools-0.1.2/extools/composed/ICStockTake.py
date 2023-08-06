from accpac import *

class ICStockTake:
    def __init__(self, id=-1):
        self.icwkuh  = View("IC0790", id)
        self.icwkud  = View("IC0780", id)
        self.icwkuho = View("IC0795", id)
        self.icwkuhl = View("IC0793", id)
        self.icwkuhs = View("IC0797", id)

        self.icwkuh.compose(self.icwkud, None, None, None, self.icwkuho, self.icwkuhl, self.icwkuhs)
        self.icwkud.compose(self.icwkuh, None)
        self.icwkuho.compose(self.icwkuh)
        self.icwkuhl.compose(self.icwkuh)
        self.icwkuhs.compose(self.icwkuh)

    def getQuantityCounted(location, itemno):
        self.icwkuh.put("LOCATION", location)
        self.icwkuh.put("SORTCODE", itemno)
        self.icwkuh.put("ITEMNO", itemno)
        self.icwkuh.read()
        return self.icwkuh.get("QTYCOUNTED")

    def getVariance(location, itemno):
        self.icwkuh.put("LOCATION", location)
        self.icwkuh.put("SORTCODE", itemno)
        self.icwkuh.put("ITEMNO", itemno)
        self.icwkuh.read()
        return self.icwkuh.get("QTYVAR")
