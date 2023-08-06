from accpac import *

class GLBatch:
    def __init__(self, id=-1):
        self.glbctl = View("GL0008", id)
        self.gljeh = View("GL0006", id)
        self.gljed = View("GL0010", id)
        self.gljedo = View("GL0402", id)
    
        self.glbctl.compose(self.gljeh)
        self.gljeh.compose(self.glbctl, self.gljed)
        self.gljed.compose(self.gljeh, self.gljedo)
        self.gljedo.compose(self.gljed)
