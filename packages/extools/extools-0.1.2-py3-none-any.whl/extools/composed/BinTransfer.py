from accpac import *

class BinTransfer:
    def __init__(self, id=-1):
        self.oybth   = View("OY0110", id)
        self.oybtd   = View("OY0111", id)
        self.oybtdd  = View("OY0112", id)
        self.oybtds  = View("OY0113", id)
        self.oybtdl  = View("OY0114", id)
        self.oybtho  = View("OY0118", id)
        self.oybtdo  = View("OY0119", id)

        self.oybth.compose(self.oybtd, self.oybtho, self.oybtdd)
        self.oybtd.compose(self.oybth, self.oybtdd, self.oybtds, self.oybtdl, self.oybtdo)
        self.oybtds.compose(self.oybtd)
        self.oybtdl.compose(self.oybtd)
        self.oybtdd.compose(self.oybtd)
        self.oybtdo.compose(self.oybtd)
        self.oybtho.compose(self.oybth)
