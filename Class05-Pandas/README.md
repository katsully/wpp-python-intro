# Class 5 - Pandas

## Virtual Environment

While Python is an incredibly strong programming language, sometimes we'll want to add additional packages and modules that's aren't pre-packaged with Python. However, this can get a little tricky. Different modules have different versions, and it's highly likely one of your projects will require version 4.2 of module x, and another project will require version 4.8 of the same module? How do we handle this? Virtual Environments!

A **Virtual Environment** is a self-contained directory that holds all of the required additional modules for each of your Python projects. This means different projects will only have the modules they need, and will have the correct version of each module. If you are installing Python libraries, *you should be using a Virtual Environment!!* How does one use a Virtual Environment? First, make sure it is installed, open your command prompt and type

```
virtualenv --version
```

You should see something like:

```
virtualenv 20.14.1 from c:\users\file\path\to\python\lib
```

Don't worry if you have a different version number, you just want to make sure it's there. If not, install it with

```
pip install virtualenv
```

Once virtualenv is installed, navigate to the directory where you want to create the Virtual Environment and type

```
virtualenv venv
```

venv is going to be the name of the virtual environment, this name can be anything you want but venv is pretty common. Once you have created the virtual environment, activate it by typing

```
venv\Scripts\activate
```

You should notice at the beginning of your command prompt line (venv). Now you call use pip install for your additional libraries. Once you are done using the project, you can deactivate the virtual environment with

```
venv\Scripts\deactivated
```



## Pandas

Pandas is an open-source data analysis and manipulation tool built on top of the Python programming language. It is frequently used in Data Science to assist in providing deeper insights to one's datasets. "Pandas" is a reference to both "Panel Data" and "Python Data Analysis" and was created by Wes McKinney is 2008.

The key data structure for Pandas is called the **DataFrame** (often referred to as dt in code).

![dataframe](./Media/01_table_dataframe.svg)

As we can see, a DataFrame is a two-dimensional structure containing columns and rows. The cell values can contain different types of data such as strings, ints, floats, bools, lists, etc. It offers a lot more functionality than our previous examples using pure Python. Pandas calculations are also typically faster than typical Python objects.

**Series** is a single column in a DataFrame.
