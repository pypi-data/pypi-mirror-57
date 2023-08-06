from accpac import *

class CSOptionalFields:
    def __init__(self, id=-1):
        self.csoptfh = View("CS0011")
        self.csoptfd = View("CS0012")

        self.csoptfh.compose(self.csoptfd)
        self.csoptfd.compose(self.csoptfh)

    def load(optfield):
        self.exists = True
        self.csoptfh.put("OPTFIELD", optfield, 0)
        return self.csoptfh.read()

    def create(optfield):
        self.exists = False
        self.csoptfh.recordGenerate()
        self.csoptfh.put("OPTFIELD", optfield, 1)
        return 0

    def save():
        if (self.exists == False):
            r = self.csoptfh.insert()
            if r == 0:
                self.exists = True
            return r

        return self.csoptfh.update()

    def addValue(value, desc):
        r = 0
        if r == 0:
            r = self.csoptfd.recordGenerate()
        if r == 0:
            r = self.csoptfd.put("VALUE", value, 1)
        if r == 0:
            r = self.csoptfd.put("VDESC", desc, 1)
        if r == 0:
            r = self.csoptfd.insert()
        return r

    def getValue(value, defaultValue=None):
        self.csoptfd.put("VALUE", value, 0)
        if self.csoptfd.read() == 0:
            return self.csoptfd.get("VDESC")
        return defaultValue

    def setValue(value, desc):
        self.csoptfd.put("VALUE", value, 0)
        if self.csoptfd.read() != 0:
            return self.addValue(value, desc)
        r = 0
        if r == 0:
            r = self.csoptfd.put("VDESC", desc, 1)
        if r == 0:
            r = self.csoptfd.update()
        return r
