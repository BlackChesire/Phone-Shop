class Sale:
    def __init__(self, manufacturer, model, date, amount_sold, total_sale, discount_made):
        self.manufacturer = manufacturer
        self.model = model
        self.date = date
        self.amount_sold = amount_sold
        self.total_sale = total_sale
        self.discount_made = discount_made

    def __eq__(self, other):
        lis = ['manufacturer', 'model', 'date', 'amount_sold', 'total_sale', 'discount_made']
        return all(getattr(self, x) == getattr(other, x) for x in lis)