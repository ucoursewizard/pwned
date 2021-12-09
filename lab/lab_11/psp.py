def _q_01():
    """
    ============================================================================
    Часть 1
    ----------------------------------------------------------------------------
    >>> scm = scm_fixture()                                     # doctest: +SKIP
    >>> scm("+")
    ______

    >>> scm("list")                                             # doctest: +SKIP
    ______

    >>> scm("(define-macro (f x) (car x))")                     # doctest: +SKIP
    ______

    >>> scm("(f (2 3 4))")                                      # doctest: +SKIP
    ______

    >>> scm("(f (+ 2 3))")                                      # doctest: +SKIP
    ______

    >>> scm("(define x 2000)")                                  # doctest: +SKIP
    ______

    >>> scm("(f (x y z))")                                      # doctest: +SKIP
    ______

    >>> scm("(f (list 2 3 4))")                                 # doctest: +SKIP
    ______

    >>> scm("(f (quote (2 3 4)))")                              # doctest: +SKIP
    ______

    >>> scm("(define quote 7000)")                              # doctest: +SKIP
    ______

    >>> scm("(f (quote (2 3 4)))")                              # doctest: +SKIP
    ______

    ============================================================================
    Часть 2
    ----------------------------------------------------------------------------
    >>> scm = scm_fixture()                                     # doctest: +SKIP
    >>> scm("(define-macro (g x) (+ x 2))")                     # doctest: +SKIP
    ______

    >>> scm("(g 2)")                                            # doctest: +SKIP
    ______

    >>> scm("(g (+ 2 3))")                                      # doctest: +SKIP
    ______

    >>> scm("(define-macro (h x) (list '+ x 2))")               # doctest: +SKIP
    ______

    >>> scm("(h (+ 2 3))")                                      # doctest: +SKIP
    ______

    ============================================================================
    Часть 3
    ----------------------------------------------------------------------------
    >>> scm = scm_fixture()                                     # doctest: +SKIP
    >>> scm("(define-macro (if-else-5 condition consequent) `(if ,condition ,consequent 5))") # doctest: +SKIP
    ______

    >>> scm("(if-else-5 #t 2)")                                 # doctest: +SKIP
    ______

    >>> scm("(if-else-5 #f 3)")                                 # doctest: +SKIP
    ______

    >>> scm("(if-else-5 #t (/ 1 0))")                           # doctest: +SKIP
    ______

    >>> scm("(if-else-5 #f (/ 1 0))")                           # doctest: +SKIP
    ______

    >>> scm("(if-else-5 (= 1 1) 2)")                            # doctest: +SKIP
    ______
    """
    return 0

def _q_02():
    """
    >>> scm = scm_fixture()                                     # doctest: +SKIP
    >>> scm("'(1 x 3)")                                         # doctest: +SKIP
    ______

    >>> scm("(define x 2)")                                     # doctest: +SKIP
    ______

    >>> scm("`(1 x 3)")                                         # doctest: +SKIP
    ______

    >>> scm("`(1 ,x 3)")                                        # doctest: +SKIP
    ______

    >>> scm("'(1 ,x 3)")                                        # doctest: +SKIP
    ______

    >>> scm("`(,1 x 3)")                                        # doctest: +SKIP
    ______

    >>> scm("`,(+ 1 x 3)")                                      # doctest: +SKIP
    ______

    >>> scm("`(1 (,x) 3)")                                      # doctest: +SKIP
    ______

    >>> scm("`(1 ,(+ x 2) 3)")                                  # doctest: +SKIP
    ______

    >>> scm("(define y 3)")                                     # doctest: +SKIP
    ______

    >>> scm("`(x ,(* y x) y)")                                  # doctest: +SKIP
    ______

    >>> scm("`(1 ,(cons x (list y 4)) 5)")                      # doctest: +SKIP
    ______
    """



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

if __name__ == '__main__':
    import doctest, sys
    finder = doctest.DocTestFinder()
    runner = doctest.DocTestRunner(doctest.OutputChecker(), optionflags=doctest.FAIL_FAST)
    doctest.OutputChecker.output_difference = lambda a, b, c, d: ""
    m = sys.modules.get('__main__')
    for test in finder.find(m, m.__name__):
        if test.name == '__main__': continue
        if test.name.split('.')[1][:2] != '_q': continue
        for example in test.examples: example.options[doctest.SKIP] = False
        if  runner.run(test).failed != 0: break