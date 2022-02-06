(define fib 
    (lambda (x)
        (if (<= x 1)
            x
            (+ (fib (- x 1)) (fib(- x 2)))
        )
    )
)

(define fac
    (lambda (x)
        (if (= x 0)
            1
            (* x (fac (- x 1)))
        )
    )
)