# Milestone-4

## Overview
The goal of Milestone 4 is to extend the `BeautifulSoup` object so that it becomes fully iterable.  
This allows application code to traverse **every node** in the HTML/XML parse tree using a simple loop:
```python
for node in soup:
    print(node)
```
## Implementation
A custom iterator `__iter__` is added to the `BeautifulSoup` class. The iterator performs a **depth-first traversal (DFS)** using an  stack and yields one node at a time.
##### How It Works
1. Start with the soup object itself on a stack  
2. Repeatedly pop a node and yield it
3. Push its children onto the stack in **reverse order** to preserves the natural document order
4. Continue until the stack is empty

> ##### Change Log
| File             | Line          | Description                            |
|:----------------:|:-------------:|----------------------------------------|
| `bs4/__init__.py`| `1163 ~ 1187`          | Added `__iter__` method to `BeautifulSoup`|


## Testing
Run all Milestone-4 tests with:
> ```python
> pytest -v bs4/tests/test_iterationSoup.py
> ```
The test file contains 5 test cases using pytest:
* `test_html_root()`  Verifies total node count and ensures the soup object itself appears during iteration of an HTML document.
* `test_html_tag()`  Verifies all tag nodes (including document root) are visited in a HTML document.
* `test_html_text()`  Verifies text `"bold 1"`, `"bold 2"` and `"bold 3"` are yielded during iteration.
* `test_xml_tagNroot()`  Verifies all XML tags nodes (including document root) are visited, and ensures the soup object itself and `<p>` appear during iteration.
* `test_xml_text()`  Verifies all XML text nodes are yielded during iteration.

## Application
#### Sample data
> #### [**Cs231n.html**](https://cs231n.stanford.edu)

#### task0.py
* Print out the type of each nodes in iteration

> ##### Output preview
> ```python
> <class 'bs4.BeautifulSoup'>
> <class 'bs4.element.Doctype'>
> <class 'bs4.element.NavigableString'>
> <class 'bs4.element.Tag'>
> ```

#### task2.py
* Print out all the hyperlinks (`<a>` tags) using iteration

> ##### Output preview
> ```python
> index.html
> schedule.html
> assignments.html
> project.html
> office_hours.html
> https://canvas.stanford.edu/courses/205350/external_tools/69960
> ```

#### task3.py
* Print all the tags using iteration

> ##### Output preview
> ```python
> [document]
> html
> head
> meta
> meta
>  ```

#### task4.py
* Print all the tags that have an `id` attribute using iteration

> ##### Output preview
> ```html
> <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
>  <ul class="nav navbar-nav navbar-right">
>   <li> ...
> <div id="header" style="text-align:center">
>  <a href="http://svl.stanford.edu">
>   <img class="logo-left" src="img/svl_logo.png"/> ...
>  ```

#### task6.py
* Change all `<b>` to `<blockquote>`

> ##### Output preview
> ```html
> <li>
>  <blockquote>
>   Lectures:
>  </blockquote>
>  Tuesday/Thursday 12:00-1:20PM Pacific Time at ...
> ```

#### task7.py
* Find all the `<p>` tags and add (or replace) a class attribute `class="test"`

> ##### Output preview
> ```html
> <p class="test">
>  See the
>  <a href="assignments.html">
>   Assignments
>  </a>
>  page for details regarding assignments, late days and collaboration policies.
> </p>
> ```