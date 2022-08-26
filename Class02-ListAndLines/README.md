# Lists and Lines

## Lists

A list is another value type, like str, int or float. What makes a list different is its ability to contain multiple values in an ordered sequence. Values are contained inside square brackets and separated by commas. 

```python
my_list = ['Apple', 'Orange', 'Pear']
```

When we look at *my_list*, we see three values, or elements. Each of these elements has an **index**. The index of an element tells us where we can find it inside the list. When using index, it's important to remember that in programming, we start counting at 0! So 'Apple' is at index 0, 'Orange' is at index 1, and 'Pear' is an index 2. 

Because Python is a dynamically typed language, we are not limited to one type of value when creating lists. Lists in Python can be all strings (like above), a mix of ints and floats, or a mishmash of bools, strings, floats, and other value types. 

```python
my_crazy_list = [34.23, 9, "hello", True]
```

We can use indexes to get a single value or several values (also called a slice) from a list. The single value will be returned as one entity, not a list. The slice will be returned as a list comprised of the selected values.

```python
my_list[0] # returns 'Apple'
my_crazy_list[0:2] # returns [34.23, 9]
```

Note a slice has two values (beginning integer and ending integer). The beginning integer is inclusive, meaning that value will be included. The ending integer is exclusive, meaning that value will not be included. In the example above, the beginning integer is 0, so 34.23 is included in the slice. The ending integer is 2, the element with an index of 2 in *my_crazy_list* is "hello", which is not included in the slice. 

You can also create a slice with only the beginning integer or ending integer. If you don't include a beginning integer, Python will assume the beginning integer is 0. If you don't include an ending integer, Python will assume the ending integer is the end of the list.

```python
my_crazy_list[:3] # returns [34.23, 9, "hello"]
my_crazy_list[2:] # returns ["hello", True]
```

## For Loops

A for loop allows us to iterate through a list one element at a time. The following example goes through each element in a list and adds 1.

```python
list_nums = [1, 2, 3, 4, 5, 6]
for num in list_nums:
    print(num+1)
    
# prints the following:
#    2
#    3
#    4
#    5
#    6
#    7
```

Let's break this down. The word **for** is a reserved word. This mean Python already knows what you're trying to do if you type the word for. Python has code (hidden from us) that defines what for means. *num* is a variable that represents each element in the list. *num* can be called anything you want, as long as you use the same name in your code. The word **in** is also reserved word and tells Python we are looking at all the elements in the specified list. The indented code, in this case *print(num+1)*, gets executed as many times as there are elements in the list. So if our list *list_nums* has 6 elements, *print(num+1)* will get executed 6 times!

Let's try making another for loop. In this loop, I'm going to create a new list, that is a duplicate of my original list, but all the words will be in upper case.

```python
original_list = ['spring', 'summer', 'fall', 'winter']
new_list = []
for season in original_list:
    new_list.append(season.upper())
  
# new_list returns ['SPRING', 'SUMMER', 'FALL', 'WINTER']
```

For this loop, the code gets executed four times because there are four elements in my list. I then add the uppercase version of the season to my *new_list*. 

## List Comprehensions

In programming, particularly in Python, we like to write the least amount of code as possible. The above code uses three lines to create the new list. What if I only needed to write one? As a Python programmer, or Pythonista as we are sometimes refer to, I love this idea! That's where list comprehensions come in.

Let's try the same code as above but using a list comprehension.

```python
original_list = ['spring', 'summer', 'fall', 'winter']
new_list = [season.upper() for season in original_list]

# new_list returns ['SPRING', 'SUMMER', 'FALL', 'WINTER']
```

Let's look at that syntax. First, you should note we are assigning the *new_list* to the value returned by the list comprehension. This tells us that list comprehensions returns a value! Second, the list comprehension is inside square brackets. Then it gets a bit stranger...let's break it down.

A list comprehension that simply returns the original list would be

```python
[season for season in original_list]
```

Just like our for loop, we have *season*, a variable (that can be called anything) that represents each element in our list. In our first comprehension we had *season.upper()*, this is the code that gets executed as many times as there are elements in our list - in that case it would be executed four times. 

We can also use conditional expressions to extract certain elements from the original list based on some logic. For example, we could pull out only seasons that start with the letter 's'

```
list_with_s_seasons = [season for season in original_list if season[0] == 's']

# list_with_s_seasons returns ['spring', 'summer']
```

So the 'code' part of our list comprehension is simply returning value. But the conditional (the if statement) elevates if the element starts with s. If and only if the element meets the conditional, is it added to the new list.

And let's combine our two list comprehensions

```
list_with_s_caps = [season.upper() for season in original_list if season[0] == 's']

# list_with_s_caps returns ['SPRING', 'SUMMER']
```

So we go through each element (or *season* as we call it here) of the original list, and if the first letter begins with s, we execute the code *season.upper()* and add the result to our new list!