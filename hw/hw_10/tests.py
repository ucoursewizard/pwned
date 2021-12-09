# Вопрос 1
def replicate_test():
    """
    >>> scm = scm_fixture();\
        scm("(load 'hw_10)")
    <BLANKLINE>
    >>> scm("(replicate 1 5)")
    (1 1 1 1 1)
    >>> scm("(replicate 'a 7)")
    (a a a a a a a)
    >>> scm("(replicate 5 0)")
    ()
    >>> scm("(replicate 4 1)")
    (4)
    >>> scm("(define a (replicate 'a 1000))")
    a
    >>> scm("(length a)")
    1000
    >>> scm("(define b (replicate 3 2000))")
    b
    >>> scm("(length b)")
    2000
    """
    pass

# Вопрос 2
def accumulate_test():
    """
    >>> scm = scm_fixture();\
        scm("(load 'hw_10)")
    <BLANKLINE>
    >>> scm("(define (identity x) x)")
    identity
    >>> scm("(accumulate * 1 5 identity)")
    120
    >>> scm("(define (square x) (* x x))")
    square
    >>> scm("(accumulate + 0 5 square)")
    55
    >>> scm("(accumulate + 5 5 square)")
    60
    """
    pass

# Вопрос 3
def accumulate_tail_test():
    """
    >>> scm = scm_fixture();\
        scm("(load 'hw_10)")
    <BLANKLINE>
    >>> scm("(define (identity x) x)")
    identity
    >>> scm("(accumulate-tail * 1 5 identity)")
    120
    >>> scm("(define (square x) (* x x))")
    square
    >>> scm("(accumulate-tail + 0 5 square)")
    55
    >>> scm("(accumulate-tail + 5 5 square)")
    60
    >>> scm("(define (identity x) x)")
    identity
    >>> scm("(accumulate-tail + 0 1000 identity)")
    500500
    >>> scm("(accumulate-tail + 0 5000 identity)")
    12502500
    """
    pass

# Вопрос 4
def multiples_3_test():
    """
    >>> scm = scm_fixture();\
        scm("(load 'hw_10)")
    <BLANKLINE>
    >>> scm("(define (first-k s k) (if (or (null? s) (= k 0)) nil (cons (car s) (first-k (cdr-stream s) (- k 1)))))")
    first-k
    >>> scm("(define (length lst) (if (null? lst) 0 (+ 1 (length (cdr lst)))))")
    length
    >>> scm("(car multiples-of-three)")
    3
    >>> scm("(list? (cdr multiples-of-three)) ; Check to make sure variable contains a stream")
    #f
    >>> scm("(list? (cdr (cdr-stream multiples-of-three))) ; Check to make sure rest of stream is a stream")
    #f
    >>> scm("(equal? (first-k multiples-of-three 5) '(3 6 9 12 15))")
    #t
    >>> scm("(equal? (first-k multiples-of-three 10) '(3 6 9 12 15 18 21 24 27 30))")
    #t
    >>> scm("(length (first-k multiples-of-three 100))")
    100
    """
    pass

# Вопрос 5
def nondecreastream_test():
    """
    >>> scm = scm_fixture();\
        scm("(load 'hw_10)")
    <BLANKLINE>
    >>> scm("(define (first-k s k) (if (or (null? s) (= k 0)) nil (cons (car s) (first-k (cdr-stream s) (- k 1)))))")
    first-k
    >>> scm("(first-k (nondecreastream finite-test-stream) 100)")
    ((1 2 3) (1 2 2) (1))
    >>> scm("(first-k (nondecreastream infinite-test-stream) 4)")
    ((1 2 2) (1 2 2) (1 2 2) (1 2 2))
    """
    pass


import sys, os
import importlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))+'/scheme')
scheme = importlib.import_module('scheme')

def scm_fixture():
    _frame = scheme.create_global_frame()
    def eval_line(code_line):
        exp = scheme.read_line(code_line)
        result = scheme.scheme_eval(exp, _frame)
        if result==None: return
        if type(result) == bool:
            if result==True:
                print('#t')
            elif result==False:
                print('#f')
        else:
            print(result)
        return
    return eval_line