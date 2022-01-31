class Phone:
    def __init__(self, manufacturer, model, price, quantity, IMEI, warranty):
        self.manufacturer = manufacturer
        self.model = model
        self.price = int(price)
        self.quantity = int(quantity)
        self.IMEI = int(IMEI)
        self.warranty = warranty

    def __eq__(self, other):

        lis = ['manufacturer', 'model', 'price', 'quantity', 'IMEI', 'warranty']
        return all(getattr(self, x) == getattr(other, x) for x in lis)
