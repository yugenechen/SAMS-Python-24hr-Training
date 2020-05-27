# Write a single line of python code that satisfies the following situation:
#  You are ordering some supplies from a store, and
# a. you need to figure out that the total price is - 
#	1. Supplies cost $10.
#	2. you have a Discount = 30% at this store.
#	3.  state tax is 5%
#	4. shippintg will be $7.50
total_price = 10 * (1-0.3) * 1.05 + 7.5
# total_price = supplies * (1-discount) * (1+tax) + shipping
