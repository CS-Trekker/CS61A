(define (first_n lst n)
        (if (and (null? lst)
                 (> n 0))
            lst
            (if (= n 0)
                '()
                (cons (car lst) (first_n (cdr lst) (- n 1)))))
)


(define (del_first_n lst n)
        (if (and (null? lst)
                 (> n 0))
            nil
            (if (= n 0)
                lst
                (del_first_n (cdr lst) (- n 1))))
)

(define (split-at lst n)
        (if (= n 0)
            (cons nil lst)
            (cons (first_n lst n)
                  (del_first_n lst n)))
)


(define (compose-all funcs)
        (define (helper n)
            (if (null? funcs)
                n
                ((compose-all (cdr funcs))
                 ((car funcs) n))))
        helper
)

