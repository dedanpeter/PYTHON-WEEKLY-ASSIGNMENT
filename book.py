class Book:
    # (i) Class named Book with attributes title, author, price and copies
    # (ii) Constructor to initialize the four attributes
    def __init__(self, title, author, price, copies):
        self.title = title
        self.author = author
        self.price = price
        self.copies = copies

    # (iii) Calculate and return the stock value: Stock Value = Price * Copies
    def calculate_stock_value(self):
        return self.price * self.copies

    # (iv) Return "In Stock" if copies is greater than zero, else "Out of Stock"
    def check_stock(self):
        if self.copies > 0:
            return "In Stock"
        else:
            return "Out of Stock"


# (v) Create two objects and display each book's stock value and status
book1 = Book("Python Basics", "John Simiyu", 1200, 5)
book2 = Book("Database Systems", "Mary Mueni", 2500, 0)

print("Title:", book1.title)
print("Author:", book1.author)
print("Stock Value:", book1.calculate_stock_value())
print("Status:", book1.check_stock())
print()

print("Title:", book2.title)
print("Author:", book2.author)
print("Stock Value:", book2.calculate_stock_value())
print("Status:", book2.check_stock())
