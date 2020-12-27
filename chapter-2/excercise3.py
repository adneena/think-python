'''
Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs
$3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for
60 copies?
'''
book_price = 24.95
discount = 40/100
shipping_cost_for_firstbook = 3
shipping_cost_for_additionalbooks = 0.75
total_books = 60
discount_for_singlebook = book_price*discount
discounted_book_price = book_price - discount_for_singlebook
shipping_cost = shipping_cost_for_additionalbooks*(total_books-1)+shipping_cost_for_firstbook
total_wholesale_cost = discounted_book_price*60 + shipping_cost
print(total_wholesale_cost)
