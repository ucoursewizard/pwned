; Вопрос 1
(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  ; ТВОЙ КОД ЗДЕСЬ
  nil
)

(define (caddr s)
  ; ТВОЙ КОД ЗДЕСЬ
  nil
)

; Вопрос 2
(define (sign x)
  ; ТВОЙ КОД ЗДЕСЬ
  nil
)

; Вопрос 3
(define (square x) (* x x))

(define (pow b n)
  ; ТВОЙ КОД ЗДЕСЬ
  nil
)

; Вопрос 4
(define (ordered? s)
  ; ТВОЙ КОД ЗДЕСЬ
  nil
)

; Вопрос 5
(define (empty? s) (null? s))

(define (add s v)
  ; ТВОЙ КОД ЗДЕСЬ
  nil
)

; Вопрос 6
(define (contains? s v)
  ; ТВОЙ КОД ЗДЕСЬ
  nil
)

; Эквивалентный код на Python:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

; Вопрос 7
(define (intersect s t)
  ; ТВОЙ КОД ЗДЕСЬ
  nil
)

; Эквивалентный код на Python:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
  ; ТВОЙ КОД ЗДЕСЬ
  nil
)