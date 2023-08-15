# Define the getDataPoint function
def getDataPoint(stock_name, bid_price, ask_price):
    price = (bid_price + ask_price) / 2
    return (stock_name, bid_price, ask_price, price)

# Define the getRatio function
def getRatio(price_stock_a, price_stock_b):
    if price_stock_b == 0:
        return "Cannot calculate ratio, division by zero"
    ratio = price_stock_a / price_stock_b
    return ratio

# Define the main function
def main():
    stock_a_name = "Stock A"
    stock_a_bid = 100
    stock_a_ask = 105
    stock_a_price = getDataPoint(stock_a_name, stock_a_bid, stock_a_ask)[3]

    stock_b_name = "Stock B"
    stock_b_bid = 150
    stock_b_ask = 155
    stock_b_price = getDataPoint(stock_b_name, stock_b_bid, stock_b_ask)[3]

    ratio = getRatio(stock_a_price, stock_b_price)

    print(f"{stock_a_name} Info:")
    print(f"Bid Price: {stock_a_bid}")
    print(f"Ask Price: {stock_a_ask}")
    print(f"Calculated Price: {stock_a_price}")
    
    print(f"\n{stock_b_name} Info:")
    print(f"Bid Price: {stock_b_bid}")
    print(f"Ask Price: {stock_b_ask}")
    print(f"Calculated Price: {stock_b_price}")

    print(f"\nPrice Ratio (Stock A / Stock B): {ratio}")

# Call the main function to execute the code
main()
