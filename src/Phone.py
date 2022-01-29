class Phone:
    def __init__(self, manufacturer, model, price, quantity, IMEI, warranty):
        self.manufacturer = manufacturer
        self.model = model
        self.price = int(price)
        self.quantity = int(quantity)
        self.IMEI = int(IMEI)
        self.warranty = warranty

    def __eq__(self, other):
        if not isinstance(other, Phone):
            # don't attempt to compare against unrelated types
            return NotImplemented
        # comparing attr
        return self.manufacturer == other.manufacturer and self.model == other.model and self.price == other.price and self.quantity == other.quantity and self.IMEI == other.IMEI and self.warranty == other.warranty
