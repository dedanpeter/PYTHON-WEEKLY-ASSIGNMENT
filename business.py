# business.py
# Task 3: Python Applications in Business

# ---------- Section 1: Store business details in variables ----------
business_name = "Mama Njeri Shop"
product_name = "Sugar (2kg)"
product_price = 320.50      # float: price per item in KES
quantity_purchased = 4      # integer

# ---------- Section 2: Calculate total cost ----------
# Total Cost = Product Price x Quantity
total_cost = product_price * quantity_purchased

# ---------- Section 3: Display the results ----------
print("=== Purchase Receipt ===")
print(f"Business Name: {business_name}")
print(f"Product Name: {product_name}")
print(f"Quantity: {quantity_purchased}")
print(f"Price: KES {product_price:.2f}")
print(f"Total Cost: KES {total_cost:.2f}")

# ---------- Section 4: Why Python suits business applications ----------
print("\n=== Three Characteristics of Python for Business Applications ===")
print("1. Simple and easy to read: staff can learn it quickly and code is easy to maintain.")
print("2. Many libraries: tools like pandas (data), openpyxl (Excel) and Django (web) save time.")
print("3. Cross-platform and free: runs on Windows, Linux and macOS at no licence cost.")
