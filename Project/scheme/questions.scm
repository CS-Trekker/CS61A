(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement

; (define (zip pairs)
;   (if (or (null? (car pairs))
;           (null? (cadr pairs)))
;       '()
;       (cons (list (caar pairs) (car (cadr pairs)))
;             (zip (list (cdar pairs) (cdr (cadr pairs))))))
; )
; 以上是我的写法，不过在第EC题pass的情况下，无法pass第15题

(define (zip pairs)
  (list (map car pairs) (map cadr pairs))
  )
;; 此处注意,假如pairs是((1 2 3) (4 5 6))那么(cadr pairs)是(4 5 6)而不是4


;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15
;   (define (helper n lst)
;           (if (null? lst)
;               '()
;               (cons n (helper (+ n 1) (cdr lst)))))
;   (zip (list (helper 0 s) s))
; )
  (define (helper s i) 
      (if (null? s) nil
          (cons (list i (car s))
                (helper (cdr s) (+ i 1)))))
  (helper s 0)
 )


  ; END PROBLEM 15



;; Problem 16

;; Merge two lists LIST1 and LIST2 according to COMP and return
;; the merged lists.
(define (merge comp list1 list2)
  ; BEGIN PROBLEM 16
  (if (null? list1)
      list2
      (if (null? list2)
          list1
          (if (comp (car list1) (car list2))
              (cons (car list1) (merge comp (cdr list1) list2))
              (cons (car list2) (merge comp list1 (cdr list2))))))
)
  ; END PROBLEM 16


(merge < '(1 5 7 9) '(4 8 10))
; expect (1 4 5 7 8 9 10)
(merge > '(9 7 5 1) '(10 8 4 3))
; expect (10 9 8 7 5 4 3 1)

;; Problem 17

(define (nondecreaselist s)
    ; BEGIN PROBLEM 17
  (cond
      ((null? (cdr s)) (list s))
      ((> (car s) (cadr s))
          (cons (list (car s)) (nondecreaselist (cdr s))))
      (else
          (cons (cons (car s) (car (nondecreaselist (cdr s)))) (cdr (nondecreaselist (cdr s)))))
      )
)
    ; END PROBLEM 17

;; Problem EC
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
;; https://github.com/Awei0418/cs61a_2020_fall/blob/ff1df88bc1bc79fe44f19b566efe230fd58e4bf3/projects/scheme/questions.scm
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM EC
         expr
         ; END PROBLEM EC
         )
        ((quoted? expr)
         ; BEGIN PROBLEM EC
         expr
         ; END PROBLEM EC
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM EC
           (append (list form params) (map let-to-lambda body))
           ; END PROBLEM EC
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM EC
           (define form (car (zip values)))
           (define params (map let-to-lambda (cadr (zip values))))
           (define body (map let-to-lambda body))
           (cons (append (list 'lambda form) body) params)
           ; END PROBLEM EC
           ))
        (else
         ; BEGIN PROBLEM EC
         (map let-to-lambda expr)
         ; END PROBLEM EC
         )))