# Linked List

Welcome to Linked List on Exercism's Python Track.
If you need help running the tests or submitting your code, check out `HELP.md`.

## Instructions

Implement a doubly linked list.

Like an array, a linked list is a simple linear data structure.
Several common data types can be implemented using linked lists, like queues, stacks, and associative arrays.

A linked list is a collection of data elements called *nodes*.
In a *singly linked list* each node holds a value and a link to the next node.
In a *doubly linked list* each node also holds a link to the previous node.

You will write an implementation of a doubly linked list.
Implement a Node to hold a value and pointers to the next and previous nodes.
Then implement a List which holds references to the first and last node and offers an array-like interface for adding and removing items:

- `push` (*insert value at back*);
- `pop` (*remove value at back*);
- `shift` (*remove value at front*).
- `unshift` (*insert value at front*);

To keep your implementation simple, the tests will not cover error conditions.
Specifically: `pop` or `shift` will never be called on an empty list.

Read more about [linked lists on Wikipedia][linked-lists].

[linked-lists]: https://en.wikipedia.org/wiki/Linked_list

## How this Exercise is Structured in Python

While linked lists can be implemented in a variety of ways with a variety of underlying data structures, we ask here that you implement your linked list in an OOP fashion.

In the stub file, you will see the start of a `Node` class, as well as a `LinkedList` class.
Your `Node` class should keep track of its value, as well as which other nodes preceed or follow.
Your `push`, `pop`, `shift`, `unshift`, and the special method for `len` should be implemented in the `LinkedList` class.
You might also find it useful to implement a special `iter` method for iteration.

Unlike the core exercise, we will be testing error conditions by calling `pop` and `shift` on empty `LinkedLists`, so you will need to `raise` errors appropriately.

Finally, we would like you to implement `delete` in addition to the methods outlined above.
`delete` will take one argument, which is the value to be removed from the linked list.
If the value appears more than once, only the **first** occurrence should be removed.

<br>

## Exception messages

Sometimes it is necessary to [raise an exception][raising]. When you do this, you should always include a **meaningful error message** to indicate what the source of the error is.
This makes your code more readable and helps significantly with debugging.
For situations where you know that the error source will be a certain type, you can choose to raise one of the [built in error types][error types], but should still include a meaningful message.

This particular exercise requires that you use the [raise statement][raise] to "throw" a `ValueError` when a node value being `delete()`-ed is not found in the linked list.
Additionally, an `IndexError` should be thrown if there are no nodes left to `pop()`.
The tests will only pass if you both `raise` these `exceptions` and include messages with them.

To raise a `ValueError` with a message, write the message as an argument to the `exception` type:

```python
# When the value passed to `delete()` is not found.
if not found:
    raise ValueError("Value not found")

```

To raise an `IndexError` with a message, write the message as an argument to the `exception` type:

```python
# When pop() is called and there are no nodes left in the linked list
if self.length == 0:
    raise IndexError("List is empty")

```


## Special Methods in Python

The tests for this exercise will also be calling `len()` on your `LinkedList`.
In order for `len()` to work, you will need to create a `__len__` special method.
For details on implementing special or "dunder" methods in Python, see [Python Docs: Basic Object Customization][basic customization] and [Python Docs: object.__len__(self)][__len__].

We also recommend creating a special [`__iter__`][__iter__] method to help with iterating over your linked list.

<br>

[__iter__]: https://docs.python.org/3/reference/datamodel.html#object.__iter__
[__len__]: https://docs.python.org/3/reference/datamodel.html#object.__len__
[basic customization]: https://docs.python.org/3/reference/datamodel.html#basic-customization
[error types]: https://docs.python.org/3/library/exceptions.html#base-classes
[raise]: https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement
[raising]: https://docs.python.org/3/tutorial/errors.html#raising-exceptions

## Source

### Created by

- @behrtam

### Contributed to by

- @cmccandless
- @Dog
- @frerich
- @Mofeywalker
- @N-Parsons
- @pheanex
- @tqa236
- @meatball133

### Based on

Classic computer science topic