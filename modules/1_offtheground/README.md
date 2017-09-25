# Engineering Computations

This course assumes no coding experience, so the first three lessons are focused on creating a foundation with Python programming constructs using essentially no mathematics. The fourth lesson introduces the basic data structure in scientific computing: _arrays_. The final lesson is a worked example of linear regression with real data.

## Module 1: Get data off the ground

### [Lesson 1](http://go.gwu.edu/engcomp1lesson1): Interacting with Python.

Background: What is Python? Idea of interpreted vs. compiled language. Why use Python? It is a general-purpose and high-productivity language.
Getting started: interactive Python (IPython).
Using Python as a calculator.
New concepts: function, string, variables, assignment, type, special variables (`True`, `False`, `None`).
Supported operations, logical operations. Reading error messages.


### [Lesson 2](http://go.gwu.edu/engcomp1lesson2): Play with data in Jupyter

What is Jupyter? Working with Jupyter. Playing with Python strings: assignment, indexing, slicing. String methods: count, find, index, strip, startswith, split. Play with Python lists: assignment, nested lists, indexing, slicing. String methods: append, index. List membership. Iteration with for-statements. Conditionals.

### [Lesson 3](http://go.gwu.edu/engcomp1lesson3): Strings and lists in action 

A full example using what you learned in lessons 1 and 2: playing with a text file containing the MAE Bulletin (list of courses with their numbers, description, pre-requisites). Reading a data from a file. Cleaning and organizing text data. 

### [Lesson 4](http://go.gwu.edu/engcomp1lesson4): Play with NumPy arrays

Two of the most important libraries for scientific computing with Python: **NumPy** and **Matplotlib**. Importing libraries. NumPy functions to create arrays: linspace, ones, zeros, empty, copy. Array operations. Multidimensional arrays. Performance advantage of arrays over lists. Drawing 2D line plots of array data.

### [Lesson 5](http://go.gwu.edu/engcomp1lesson5): Linear regression with real data

A full worked example using real data of earth temperature over time. Step 1: reading data from a file. Step 2: plotting the data; making beautiful plots. Step 3: least-squares linear regression. Step 4: applying linear regression using NumPy. Split regression.