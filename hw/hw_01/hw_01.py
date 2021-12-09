""" Домашнее задание № 1 """

# Вопрос 1.

from operator import add, sub
def a_plus_abs_b(a, b):
    """Возвращает a+abs(b), но не использует abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        op = _____
    else:
        op = _____
    return op(a, b)

# Вопрос 2.

def two_of_three(a, b, c):
    """Возвращает x*x + y*y, где x и y — два наибольших значения среди a, b, c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return _____

# Вопрос 3.

def if_function(condition, true_result, false_result):
    """Возвращает true_result, если условие condition истинно и false_result в противном случае.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result

def with_if_statement():
    """
    >>> result = with_if_statement()
    2
    >>> print(result)
    None
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    """
    >>> result = with_if_function()
    1
    2
    >>> print(result)
    None
    """
    return if_function(c(), t(), f())

def c():
    "*** ТВОЙ КОД ЗДЕСЬ ***"

def t():
    "*** ТВОЙ КОД ЗДЕСЬ ***"

def f():
    "*** ТВОЙ КОД ЗДЕСЬ ***"

# Вопрос 4.

def hailstone(n):
    """Выводит сиракузскую последовательность (числа-градины), начинающуюся с n, и возвращает её длину.

    >>> a = hailstone(10)  # Семь элементов: 10, 5, 16, 8, 4, 2, 1
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** ТВОЙ КОД ЗДЕСЬ ***"

# Вопрос 5.

challenge_question_program = """
"*** ТВОЙ КОД ЗДЕСЬ ***"
"""