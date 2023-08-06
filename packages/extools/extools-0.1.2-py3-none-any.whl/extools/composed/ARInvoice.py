from extools.composed.composed_view import ComposedExView

class ARInvoice(ComposedExView):
    """
    AR Invoice - a fully composed AR Invoice object based on ExViews.

    A fully composed set of ExViews for an AR Invoice.

    .. code-block:: python

        all_items_in_invoice = []
        try:
            arinvoice = ARInvoice()
            arinvoice.aribh.put("IDINVC", "INV00000001")
            arinvoice.read()

            for entry in arinvoice.aribd.fetch_all():
                # Store the item for processing.
                all_items_in_invoice.append(entry.get("IDITEM"))

    """
    COMPOSE = [
                ('AR0031', 'aribc', ('aribh', ), ),
                ('AR0032', 'aribh', ('aribc',
                                    'aribd',
                                    'aribs',
                                    'aribho', ), ),
                ('AR0033', 'aribd', ('aribh',
                                     'aribc',
                                     'aribdo', ), ),
                ('AR0034', 'aribs', ('aribh', ), ),
                ('AR0402', 'aribho', ('aribh', ), ),
                ('AR0401', 'aribdo', ('aribd', ), ),
                ('AR0048', 'aribdo', (), ),
            ]

    def createBatch():
        """Create a new AR Invoice Batch."""
        return self.aribc.recordGenerate(1)

    def createInvoice(customerId):
        """Create a new AR Invoice document.

        :param customer_id: ID of the customer to create the invoice for.
        """
        self.aribh.recordGenerate()
        self.aribh.put("IDCUST", customerId)
        self.aribh.put("TEXTTRX", 1) # Document Type = Invoice
        self.aribh.put("PROCESSCMD", 4) # Insert Optional Fields
        return self.aribh.process()

    def postBatch():
        """Set the current batch Ready to Post and post it."""
        self.aribc.put("BTCHSTTS", 7) # Ready To Post
        self.aribc.update()

        self.arivpt.put("BATCHIDFR", self.aribc.get("CNTBTCH"))
        self.arivpt.put("BATCHIDTO", self.aribc.get("CNTBTCH"))
        return self.arivpt.process()
