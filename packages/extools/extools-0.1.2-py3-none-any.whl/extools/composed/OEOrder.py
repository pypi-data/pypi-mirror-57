from accpac import *

#    from OEOrder import OEOrder
#    order = OEOrder()
#    order.create("1200")
#    order.oeordho.setOptionalField("AC", "1979")
#    order.oeordd.recordGenerate()
#    order.oeordd.put("ITEM", "A11030")
#    order.oeordd.put("QTYORDERED", 10)
#    order.oeordd.insert()
#    if order.save() == 0:
#        message("Created order " + order.oeordh.get("ORDNUMBER"))
#    else:
#        error("Error creating order.")
class OEOrder:
    def __init__(self, id=-1):
        self.oeordh = View("OE0520", id)
        self.oeordd = View("OE0500", id)
        self.oetermo = View("OE0740", id)
        self.oecoino = View("OE0180", id)
        self.oeordq = View("OE0526", id)
        self.oeordho = View("OE0522", id)
        self.oeordds = View("OE0508", id)
        self.oeorddl = View("OE0507", id)
        self.oeorddo = View("OE0501", id)
        self.oeorddd = View("OE0502", id)
        self.oeorddds = View("OE0504", id)
        self.oeordddl = View("OE0506", id)
        self.oeorddb = View("OE0503", id)

        self.oeordh.compose(self.oeordd, None, self.oecoino, self.oetermo, self.oeordq, self.oeordho)
        self.oeordd.compose(self.oeordh, self.oeorddo, self.oeorddb, self.oeorddd, self.oeordds, self.oeorddl)
        self.oetermo.compose(self.oeordh)
        self.oecoino.compose(self.oeordh, self.oeordd)
        self.oeordq.compose(self.oeordh)
        self.oeordho.compose(self.oeordh)
        self.oeorddo.compose(self.oeordd)
        self.oeordds.compose(self.oeordd)
        self.oeorddl.compose(self.oeordd)
        self.oeorddd.compose(self.oeordd, self.oeorddds, self.oeordddl)
        self.oeorddds.compose(self.oeorddd)
        self.oeordddl.compose(self.oeorddd)
        self.oeorddb.compose(self.oeordd)

    def load(self, orderNumber):
        self.exists = True
        self.oeordh.order(1) # ORDNUMBER
        self.oeordh.put("ORDNUMBER", orderNumber, 0)
        return self.oeordh.read()

    def create(self, idcust):
        self.exists = False
        self.oeordh.order(0) # ORDUNIQ
        self.oeordh.recordGenerate()
        self.oeordh.put("CUSTOMER", idcust, 1)

    def shipAll(self):
        self.oeordh.put("GOSHIPALL", 1)
        self.oeordh.process()

    def createInvoice(self):
        self.oeordh.put("INVPRODUCE", 1)

    def save(self):
        if self.exists == False:
            r = self.oeordh.insert()
            if (r == 0):
                self.exists = True
            return r

        return self.oeordh.update()

    def goToLineNumber(self, lineNumber):
        self.oeordd.put("LINENUM", -32000, 0)
        self.oeordd.browse("", 1)
        while (self.oeordd.fetch() == 0):
            if (lineNumber == 0):
                return 0
            lineNumber = lineNumber - 1
        return -1

    def drilldown(self):
        openUI("OE1100", "KEY=" + str(self.oeordh.get("ORDUNIQ")), False)

