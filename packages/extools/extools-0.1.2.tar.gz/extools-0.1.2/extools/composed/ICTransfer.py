from accpac import *

class ICTransfer:
    def __init__(self, id=-1):
        self.ictreh = View("IC0740", id)
        self.ictred = View("IC0730", id)
        self.ictreho = View("IC0741", id)
        self.ictredo = View("IC0735", id)
        self.ictreds = View("IC0738", id)
        self.ictredl = View("IC0733", id)

        self.ictreh.compose(self.ictred, self.ictreho)
        self.ictred.compose(self.ictreh, None, None, None, None, None, self.ictredo, self.ictreds, self.ictredl)
        self.ictreho.compose(self.ictreh)
        self.ictredo.compose(self.ictred)
        self.ictreds.compose(self.ictred)
        self.ictredl.compose(self.ictred)

    def load(docnum):
        self.ictreh.order(3) # DOCNUM
        self.ictreh.put("DOCNUM", docnum, 0)
        return self.ictreh.read()
