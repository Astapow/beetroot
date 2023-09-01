stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_price = 0

for key, val in stock.items():
    if key in prices:
        price = prices[key]
        total_price += val * price

print("Total price: ", total_price)
