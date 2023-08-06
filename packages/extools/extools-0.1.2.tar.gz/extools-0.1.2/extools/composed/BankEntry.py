from accpac import *

class BankEntry:
    def __init__(self, id=-1):
        self.bkenth = View("BK0450", id)
        self.bkentd = View("BK0460", id)

        self.bkenth.compose(self.bkentd, None, None, None, None, None)
        self.bkentd.compose(self.bkenth, None, None)

    def read(self, sequenceno):
        self.bkenth.put("SEQUENCENO", sequenceno, 0)
        return self.bkenth.read()
