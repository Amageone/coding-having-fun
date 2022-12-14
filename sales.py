"""
Write a code using functions 
that will add items in your grocery cart and 
return total in a receipt.

"""
#  global
order = {'tomato': 30, 'thyme': 4.50, 'garlic': 7.50, 'rice': 10, 'onions': 4, 'fish': 9.99,}

def items(total):
    with open('receipt.txt', 'w') as file:
        file.write(f'the total of my order is: ${total}')
    return True

def total_of_value():
    return sum(order.values())

# body of the main
if __name__ == "__main__":
    # getting the total of the value from the dic.
    total = int(total_of_value())
    print(f'the total of my order will be: ${total}')

# creating the file.
items(total)