## empty tuples

empty_tuple = ()
# print(type(empty_tuple))

## declaration and assignment of the tuple

nums = (1,2,2,3)
words =("one","two","three","two")
mixed_tup = (1,"one",2,"two", 3.13)
# print(nums)
# print(words)
# print(mixed_tup)

## accessing the element from tuples
# print(nums[1])

## slicing
# print(mixed_tup[1:2])
# print(mixed_tup[::-1]) # reverse accessing the tuples from backward

## for loop
# for num in nums:
    # print(num)

## Tuple methods commonly used

# print(words.count("two"))   ## return the number of occurences of the element
# print(words.index("two")) ## return the index position of first occurence of the element

#packing and unpacking the tuple
packed_tuple =1,"Hello",3.10
# print(packed_tuple)
## unpakcing the tuple
a,b,c =packed_tuple
# print(a)
# print(b)
# print(c)

## unpakcing with the *
first,*middle,last = words
print(first)
print(middle)
print(last)

## Nested tuples

nested_tups = ((1,2,3,4),("one","two","three"),(1.1,2.2,3.3))
print(nested_tups[0])
print(nested_tups[2][0:2])
print(nested_tups[1][::-1])