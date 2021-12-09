# Связные списки

class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(self.first, rest_str)

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ', '
            self = self.rest
        return string + str(self.first) + '>'

# Множества как упорядоченные последовательности

def empty(s):
    return s is Link.empty

def contains(s, v):
    """Возвращает True, если множество содержит элемент, равный v.

    >>> s = Link(1, Link(2, Link(3))) 
    >>> contains(s, 2)
    True
    >>> contains(s, 5)
    False
    """
    if empty(s):
        return False
    elif s.first == v:
        return True
    else:
        return contains(s.rest, v)

def adjoin(s, v):
    """Возвращает множество, содержащее все элементы s и значение v.

    >>> s = Link(1, Link(2, Link(3))) 
    >>> t = adjoin(s, 4)
    >>> t
    Link(4, Link(1, Link(2, Link(3))))
    """
    if contains(s, v):
        return s
    else:
        return Link(v, s)

def intersect(s, t):
    """Возвращает множество всех элементов, общих для множеств s и t.

    >>> s = Link(1, Link(2, Link(3))) 
    >>> t = adjoin(s, 4)
    >>> intersect(t,  Link(1, Link(4, Link(9))))
    Link(4, Link(1))
    """
    if s is Link.empty:
        return Link.empty
    rest = intersect(s.rest, t)
    if contains(t, s.first):
        return Link(s.first, rest)
    else:
        return rest

def union(s, t):
    """Возвращает множество всех элементов, входящих
    одновременно и в s, и в t.

    >>> s = Link(1, Link(2, Link(3))) 
    >>> t = adjoin(s, 4)
    >>> union(t, s)
    Link(4, Link(1, Link(2, Link(3))))
    """
    if s is Link.empty:
        return t
    rest = union(s.rest, t)
    if contains(t, s.first):
        return rest
    else:
        return Link(s.first, rest)

# Множества как упорядоченные (сортированные) последовательности

def contains2(s, v):
    """Возвращает True, если множество содержит элемент, равный v.

    >>> s = Link(1, Link(2, Link(3))) 
    >>> contains2(s, 2)
    True
    >>> contains2(s, 5)
    False
    """
    if empty(s) or s.first > v:
        return False
    elif s.first == v:
        return True
    else:
        return contains2(s.rest, v)

def adjoin2(s, v):
    """Возвращает множество, содержащее все элементы s и значение v.

    >>> s = Link(1, Link(2, Link(3))) 
    >>> t = adjoin2(s, 4)
    >>> t
    Link(1, Link(2, Link(3, Link(4))))
    """
    if empty(s) or s.first > v:
        return Link(v, s)
    elif s.first == v:
        return s
    else:
        return Link(s.first, adjoin2(s.rest, v))

def add(s, v):
    """Добавляет v в множество s, возвращает изменённый s. Если s непустое множество,
    возвращает исходный модифицированный объект.

    >>> s = Link(1, Link(3, Link(5))) 
    >>> add(s, 0)
    Link(0, Link(1, Link(3, Link(5))))
    >>> add(s, 3)
    Link(0, Link(1, Link(3, Link(5))))
    >>> add(s, 4)
    Link(0, Link(1, Link(3, Link(4, Link(5)))))
    >>> add(s, 6)
    Link(0, Link(1, Link(3, Link(4, Link(5, Link(6))))))
    """
    if empty(s):
        return Link(v)
    if s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest)
    elif s.first < v and empty(s.rest):
        s.rest = Link(v, s.rest)
    elif s.first < v:
        add(s.rest, v)
    return s

def intersect2(s, t):
    """Возвращает множество всех элементов, общих для множеств s и t.

    >>> s = Link(1, Link(2, Link(3))) 
    >>> t = Link(2, Link(3, Link(4)))
    >>> intersect2(s, t)
    Link(2, Link(3))
    """
    if empty(s) or empty(t):
        return Link.empty
    else:
        e1, e2 = s.first, t.first
        if e1 == e2:
            return Link(e1, intersect2(s.rest, t.rest))
        elif e1 < e2:
            return intersect2(s.rest, t)
        elif e2 < e1:
            return intersect2(s, t.rest)

def union2(s, t):
    """Возвращает множество всех элементов, входящих
    одновременно и в s, и в t.

    >>> s = Link(1, Link(2, Link(3))) 
    >>> t = Link(2, Link(3, Link(4)))
    >>> union2(s, t)
    Link(1, Link(2, Link(3, Link(4))))
    """
    if empty(s):
        return t
    elif empty(t):
        return s
    else:
        e1, e2 = s.first, t.first
        if e1 == e2:
            return Link(e1, union2(s.rest, t.rest))
        elif e1 < e2:
            return Link(e1, union2(s.rest, t))
        elif e2 < e1:
            return Link(e2, union2(s, t.rest))