from accpac import *

class ICAssembly:
    def __init__(self, id=-1):
        self.icasen = View("IC0160", id)
        self.icaseno = View("IC0165", id)
        self.icasenl = View("IC0162", id)
        self.icasens = View("IC0167", id)

        self.icasen.compose(None, None, None, self.icaseno, self.icasenl, self.icasens)
        self.icaseno.compose(self.icasen)
        self.icasenl.compose(self.icasen)
        self.icasens.compose(self.icasen)

    def load(self, docnum):
        self.icasen.order(5) # DOCNUM
        self.icasen.put("DOCNUM", docnum, 0)
        return self.icasen.read()

    def post(self):
        self.icasen.put("STATUS", 2)
        return self.icasen.update()
