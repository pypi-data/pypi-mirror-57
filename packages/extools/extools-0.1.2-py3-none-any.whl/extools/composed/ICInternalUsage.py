from accpac import *

#    from ICInternalUsage import ICInternalUsage
#    icusage = ICInternalUsage()

class ICInternalUsage:
    def __init__(self, id=-1):
        self.iciceh = View("IC0288", id)
        self.iciced = View("IC0286", id)
        self.iciceho = View("IC0289", id)
        self.icicedo = View("IC0287", id)
        self.icicedl = View("IC0282", id)
        self.iciceds = View("IC0284", id)
        
        self.iciceh.compose(self.iciced, self.iciceho)
        self.iciced.compose(self.iciceh, self.icicedo, self.iciceds, None, None, None, None, None, self.icicedl)
        self.iciceho.compose(self.iciceh)
        self.icicedo.compose(self.iciced)
        self.icicedl.compose(self.iciced)
        self.iciceds.compose(self.iciced)

