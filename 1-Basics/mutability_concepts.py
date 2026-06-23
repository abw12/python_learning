
# str is immutbale object in python
name = "abhishek"
name.upper()
print(name)
#Why did it not change?
#Because strings are immutable.
#This creates a new string:

name = name.upper()
print(name)

# mutable object like list 
items = ["cement", "steel"]
items.append("sand")

print(items)


#### Most common production bug ###################

def add_items(item,items=[]) -> list:
    items.append(item)
    return items
print(add_items("apple"))
print(add_items("orange"))
print(add_items("chiku"))

# This surprises many developers.
# Why did the list remember old values?
# Because default arguments are created only once, when the function is defined
# the list items=[] is shared across function calls.

# correct version is below

def add_items_fixed(item,items=None):
    if items is None:
        items=[]
    items.append(item)
    return items
print(add_items_fixed("kiwi"))
print(add_items_fixed("mango"))
print(add_items_fixed("orange"))
#Now each function call gets a fresh list.
#This is production-grade safe code.