from accpac import *

# Use BankTransfer to enter a bank transfer.
class BankTransfer:
    def __init__(self, id=-1):
        self.bktfrh = View("BK0036", id)
        self.bktfrd = View("BK0835", id)

        self.bktfrh.compose(self.bktfrd)
        self.bktfrd.compose(self.bktfrh)
