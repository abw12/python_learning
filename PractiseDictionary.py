from collections import OrderedDict

my_dict= {'abhishek': 27,'adhish':26,'vedant':26,'sarang':26,'keshav':33}

my_dict_keys = list(my_dict) # this returns the keys of the dictionary if wrapped arounf list() method, my_dict.key() will also return the same.
my_dict_keys.sort()
sorted_keys = {i: my_dict[i] for i in my_dict_keys } # this is list comprehensive
my_dict['akshay']=27 # adding the key-value in the dictionary
print(sorted_keys)
print(my_dict['adhish']) # directly access the value by passing the key in []


# sorting the dictionary by key using OrderDict class
print(OrderedDict(sorted(my_dict.items())))

# print keys
print(my_dict.keys())

# print values
print(my_dict.values())

#print key-value
print(my_dict.items())

#iterate over dictionary
for i in my_dict:
    print("%s %d" %(i,my_dict[i]))

# another method to iterate over dictionary (enumerate is useful for obtaining an indexed list)
for index,key in enumerate(my_dict):
    print(index,key,my_dict[key])
# check if key exist
print('abhishek' in my_dict)

# delete a item
del my_dict['akshay']

print('akshay' in my_dict)

## merge the two dict
dict1 ={"a":1,"b":2}
dict2 ={"c":3,"d":4}
merged_dict = {**dict1,**dict2} ## this is possible with the concept called keyword arguments used in python fucntions(**kwargs paramter which we can pass in the functions)
print(merged_dict)