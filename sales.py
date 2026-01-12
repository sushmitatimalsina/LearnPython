sales = [
    {"product": "Pen", "quantity": 10, "price": 5},
    {"product": "Notebook", "quantity": 5, "price": 50}
]

for items in sales:
    print(items["product"], items["quantity"])
    items["total_price"] = items["quantity"] * items["price"]

print("----- After Adding Total Price -----")
for items in sales:
    print(items["product"], "Total Price:", items["total_price"])

for i in sales:
    if i["price"]== None:
        i["price"]= "Not Available"
    print(i["product"], "-", i["price"])
    
        
