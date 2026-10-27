class Product:
    def __init__(self, product_name, unit_price, quantity_purchased):
        self.product_name = product_name
        self.unit_price = unit_price
        self.quantity_purchased = quantity_purchased

    def calculate_total(self):
        total_cost = self.unit_price * self.quantity_purchased
        return total_cost


product1 = Product("Sugar", 150, 4)
print("Product:", product1.product_name)
print("Total cost:", product1.calculate_total())
