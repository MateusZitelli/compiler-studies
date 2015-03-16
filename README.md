# Compilers studies

Some code developed for study during the enrolment of the compile course at
UFABC (MC3201).

What I've done so far:

- [X] LL(1) parser
- [ ] LR parser

## LL(1) parser

My actual implementation of the LL(1) parser checks if an given input is a
valid LISP like language, it supports just the 4 basic arithmetic operations
(+ - * /) with integers.

e.g.:
```lisp
(+ 2 3)

(* (3 (/ 3 2)) (+ 2 3))
```

### Running

```sh
python3 src/parser.py
```
