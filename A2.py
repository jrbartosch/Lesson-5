original_price = float(input('Please Enter the Original Price of the Product.'))
new_price = float(input('Please Enter the New Price of the Product.'))
if new_price > original_price:
    profit = new_price - original_price
    print ('You have $', profit, 'in profit.')
else:
    print ('No Profit.')