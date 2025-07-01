# Programs to show the operator values

""" Item name, item price, discount_rate, quantity, elligible_items ."""

item_name = "banana"
quantity = 5
discount_rate = 0.1
eligible_items = "orange carrot banana"
item_price = 2 # USD

""" Arithmatic operations """

# calculate the subtotal of item_price * quantity

sub_total = item_price * quantity

print(f"item_name : {item_name} , sub_total : {sub_total} ")

# Initialize discount to 0
discount = 0


# Membership Operator
if item_name in eligible_items:
    print("Eligible for discount")
    discount_rate = 0.1
    discount = (quantity * item_price) * discount_rate


# Check was discount applied or not 

if discount > 0:
    print(f"discount applied --> {discount}")


# Check whether free delivery is applicable or not

if (quantity >= 5 and item_name == 'banana'):
    print("Eligible for free delivery ")



