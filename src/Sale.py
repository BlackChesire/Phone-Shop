class Sale:
    def __init__(self, manufacturer, model, date, amount_sold, total_sale, discount_made):
        self.manufacturer = manufacturer
        self.model = model
        self.date = date
        self.amount_sold = amount_sold
        self.total_sale = total_sale
        self.discount_made = discount_made

    def __eq__(self, other):
        if not isinstance(other, Sale):
            # don't attempt to compare against unrelated types
            return NotImplemented
        # compare attr
        return self.manufacturer == other.manufacturer and self.model == other.model and self.date == other.date and self.amount_sold == other.amount_sold and self.total_sale == other.total_sale and self.discount_made == other.discount_made
