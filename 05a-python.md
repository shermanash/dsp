# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> lists and tuples both are a sequence of objects such as (these, three, things) or [these, three, things]. lists use square brackets, while tuples use parentheses. the main difference is that tuples are immutable- which means they cannot be changed, while lists are mutable.  For example, if we wanted to sort a tuple, we would first have to convert it to a list.  While somewhat restrictive, the immutable nature of tuples allows them to be used as keys for dictionaries, while lists cannot be used as dictionary keys. generally tuples are used when we care about the order of the data, and lists can be used when the order is not important.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> items in a list are in order, while items in a set are unordered.  lists use square brackets, while sets use curly brackets.  lists can contain duplicates, while duplicate values are not allowed in sets. lists are useful when the collection of data is mixed, or the list needs to contain other lists or dictionaries.  sets are useful when you need to mathematical operations on the data, or when the data is unique.  performance when finding an element will be faster with a set, because the items are hashed, which makes searching through or performing other operations on sets faster than lists.  

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>>  a lambda function is an anonymous function- basically a quick way to write a simple function and return the result.  for example, if we wanted to sort a list of strings by the number of letters they have-
>> stringlist = ['hi', 'this', 'isa', 'coool', 'stringlist']
>> we could use lambda as-
>> stringlist.sort(key=lambda x: len(set(list(x))))


---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> a list comprehension is an easy way to make a list. it loops through a parameter like a range of numbers and populates the list for each item in that range.  for example to make a list of squares from 1 to 15 you could write
>>`squares = [x**2 for x in range(15)]`
>> you could also add a conditional such that the list only populates squares divisble by 3, like-
>> `squares = [x**2 for x in range(15) if x % 3 == 0]`
>> you could do the same thing using map and filter but it would not be as efficient. it would look something like this:
>> `squares = list(map((lambda x: x**2), filter(lambda x: x % 3 == 0, range(15))))`
>> dictinary comprehensions can be useful as well, they look like this-
>> `d = {n: n**2 for n in range(15)}`
>> the above would create a dictionary with the keys being integers from 1 to 15, and the values being the squares of those integers. you could also add a conditionald statement to a dictionary comprehension.
>> a set comprehension is essentially the same as a list comprehension except using the set notation of curly braces instead of square brackets, just like how creating a set uses a curly brace while a list uses a bracket
>> `squares = {x**2 for x in range(15)}`

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





