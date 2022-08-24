# Setting up your Environment

### Python

First, we need to make sure Python has been installed. (This is only for Window users, Python comes standard in Mac). Open the Command Prompt and type *python* and press enter. If it says Python 3.x.xx ...., you're all set! If not, please download [Python](https://www.python.org/downloads/windows). Under 'Stable Releases' search for the Windows installer (64-bit). Open the installer and **make sure the "Add Python 3.x to PATH" is selected**. Click Install Now. You'll need to close and reopen Command Prompt after installation.

Be sure Python is installed before moving on the next steps!

### Pip

If all went according to plan, you should have pip installed as well. In the command prompt type

```
pip --version
```

and hit enter. It should give a version number and at the end you should see Python 3.x that corresponds to whichever Python you have installed. If you're here - great! If not, reinstall Python and be sure that you include pip in your installation!

Next install Jupyter by typing the following into the command line

```
pip install jupyter
```

and hit enter. The installation will take a few minutes - don't worry! If it seems like it has stalled, just wait a little bit. To start the notebook server type

```
jupyter notebook
```

and hit enter.  This should open the notebook in your browser. Note your location in the command prompt determines where the notebook is opened - be mindful of this! To close the notebook hit 'Quit' in the browser or hit Ctrl+C in the command prompt.



# Python Basics

### Print Statements

In our code, we'll be using a lot of print statements. Print statements print whatever you put inside parenthesis on the screen. For example

```python
print("Hello World!")
```

will result in

```
Hello World!
```

If you're looking at older Python code, you may notice it is written as 

```python
print "Hello World"
```

This is because the parenthesis were only required for print statements at the start of Python 3. Print statements can also confirm that certain variables are what we expect them to be during a debugging process, but we'll get there later. 

### Operators

Like any computer program, Python is capable of performing mathematical calculations. We have your classic operators such as + , -, *, and / (addition, subtraction, multiplication, and division). There are plenty of complicated mathematical operations as well, but let's start here. Just like typical mathematics, Python observes the order of operations:

1. Parenthesis
2. Exponents
3. Multiply/Divide
4. Addition/Subtraction

Meaning 8 - 2 * 4 = 0, but (8-2) * 4 = 24. We also have the operator % which is called **modulus**. This refers to the remainder when performing division. It will become extremely useful later, but let's see a few examples first. 24 % 2 = 0, 23 % 2 = 1, and 26 % 3 = 2.

### Variables

You probably have already used variables before in math class, and just like in math class, variables are named entities that contain a value. To create a new variable and assign it a value we use something called an **assignment statement**.

```python
x = 8 - 2 * 4
y = (8 - 2) * 4
welcome_string = "Welcome to the world of variables"
```

Note that naming syntax varies from programming language to programming language, but in Python, we name our variable using all lowercase separating words with underscores. While we can use numbers in our names, we cannot start a variable name with a number.

### Value Types

#### String

Strings are written expressions, or anything that appears in quotes. "Hello" is a string, "k" is a string, and "3534" is also a string. Python classifies type of value as a **str**.

#### Boolean

Boolean values (named after George Boole) are used when we want to express whether something is true or false. They are frequently used with **comparison operators**. You have all used comparison operators before such as <, >, <=, and >=. 

We also have the equal operator "==" and not equal to operator "!=". These are not to be confused with the single equal sign "="! 

A single equal sign is used to assign value. For example,

```python
x = 5
hello_str = "This is a string"
has_it_occured = False
```

These statements do not evaluate to True or False, they only take our variable and give it a value.

However, the comparison operators will equal to True or False

```python
10 * 2 == 30 >>> False
10 * 2 != 30 >>> True
4 > 5 >>> False
```

