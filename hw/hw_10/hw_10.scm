
; Хвостовая рекурсия
; Вопрос 1
(define (replicate x n)
  'YOUR-CODE-HERE
  )

; Вопрос 2
(define (accumulate combiner start n term)
  'YOUR-CODE-HERE
)

; Вопрос 3
(define (accumulate-tail combiner start n term)
  'YOUR-CODE-HERE
)

; Потоки
; Вопрос 4
(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define multiples-of-three
  'YOUR-CODE-HERE
)

; Вопрос 5
(define (nondecreastream s)
    'YOUR-CODE-HERE)


(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))