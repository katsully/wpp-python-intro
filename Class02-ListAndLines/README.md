# Lists and Lines

## Lists

A list is another value type, like a str, int or float. What makes a list different is its ability to contain multiple values in an order sequence. Values are contained inside square brackets and separated by commas, for example

```python
my_list = ['Apple', 'Orange', 'Pear']
```

When we look at my_list, we see three values, or elements. Each of these elements has an **index**. The index of an element tells us where the order of the element within the list. When using index, it's important to remember that in programming, we start counting at 0! So 'Apple' is at index 0, 'Orange' is at index 1, and 'Pear' is an index 2. 

Because Python is a dynamically typed language, we are not limited to one type of value when creating lists. Lists in Python can be all strings (like above), a mix of ints and floats, or a mishmash of bools, strings, floats, and other value types. For example

```python
my_crazy_list = [34.23, 3, "hello", True]
```

We can use indexes to get a single value or several values (also called a slice) from a list. The single value will be returned as a single string, float, int, etc depending on the value type. The slice will be returned as a list comprised of the selected values.

```python
my_list[0] # returns 'Apple'
my_crazy_list[0:2] # returns [34.23, 3]
```

Note a slice has two values (beginning integer and ending integer). The beginning integer is inclusive, meaning that value will be included. The ending integer is exclusive, meaning that value will not be included. In the example above, the beginning integer is 0, so 34.23 is included in the slice. The ending integer is 2, the element with an index of 2 in my_crazy_list is "hello", which is not included in the slice. 

You can also create a slice with only the beginning integer or ending integer. If you don't include a beginning integer, Python will assume the beginning integer is 0. If you don't include an ending integer, Python will assume the ending integer is the end of the list.

```python
my_crazy_list[:3] # returns [34.23, 3, "hello"]
my_crazy_list[2:] # returns ["hello", True]
```

## For Loops

A for loop allows us to iterate through a list one element at a time. The following example goes through each element in a list and adds 1.

```python
# TODO - FIX THIS EXAMPLE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
list_nums = [1, 2, 3, 4, 5, 6]
for x in list_nums:
    list_nums[x]++
    
```

Let's break this down. The word **for** is a reserved word. This mean Python already knows what you're trying to do if you type the word for. Python has code (hidden from us) that defines what this word means. x