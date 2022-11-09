# Class 3 - Keys and Values

## JSON

**J**ava**S**cript **O**bject **N**otation - it's 'easy' to read and write for humans (that's debatable) and it's very easy for machines to parse and generate.

JSON text format is the same regardless of if you're using P5, Processing, Cinder, Python, or any other language.

An example of JSON: 

```
{
   "eBooks":[
      {
         "language":"Pascal",
         "edition":"third"
      },
      {
         "language":"Python",
         "edition":"four"
      },
      {
         "language":"SQL",
         "edition":"second"
      }
   ]
}
```

## Dictionaries

If you really want to unlock the magic of Python, we need to talk about **dictionaries**. The building blocks of a dictionary are key-value pairs. A key value pair maps a value to a key. Values can be changed but keys cannot. I like to think about houses on a street, the addresses (keys) will stay the same, but the people living there (values) may change over the years. Let's use some famous addresses to illustrate this point.

```python
my_dict = {"Clarence House": "King Charles", "Windsor Castle": "Prince Williams"}
```

Note that dictionaries, unlike lists, are contained in squiggly-brackets {}. The colon : is used to map the key-value pair, and commas separate out the pairs. Does this look a bit like JSON to you? Good catch! They are very similar, but we have more flexibility to manipulate data with dictionaries. 

We can add to the dictionary as well.

```python
my_dict["Gatcombe Park"] = "Princess Anne"

# my_dict is now {"Clarence House": "King Charles", "Windsor Castle": "Prince Williams", "Gatcombe Park": "Princess Anne"}
# note: if "Gatcombe Park" was already a key in the dictionary, it would simply update the associated value with "Princess Anne"
```

However, we may want to make this is little more complex. For example, I also might want to include Camilla and Kate. (Side note: As an American, I have no idea if these women get a title. Are they a duchess? What is a duchess? Will I be deported for not including their titles? But I'm getting carried away here). 

With dictionaries, values can be more complex than a single entity. Values can be lists or even a nested dictionary. Let's redo *my_dict*

```python
my_dict ={"Clarence House": ["King Charles", "Camilla"], "Windsor Castle": ["Prince Williams", "Kate"], "Gatcombe Park": "Princess Anne"}
```

Remember [] means it contains a list, {} means it contains a dictionary.

We can return a value by passing the key to the dictionary.

```python
my_dict["Clarence House"]
# returns ["Prince Charles", "Camilla"]
```

