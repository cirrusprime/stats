---
layout: page
title: Functions
---
Most functions require at least one parameter/argument to go inside their parentheses when they're called.

## Some useful functions

Function                | Purpose
------------------------|--------------------------------
`log`                   | Natural log (base e (`exp(1)`)
`log10`                 | Common log (base 10)
`log2`                  | Binary log (base 2)
`log(x, base)`          | Log of `x` with specified `base`
`exp`                   | Exponential
`help("function_name")` | Show documentation for `function_name`
`?function_name`        | Show documentation for `function_name` (shorthand for `help`)
`args`                  | Show arguments and their defaults for given function
`data`                  | Show list of included practice datasets
`str(data_frame)`       | Show structure of `data_frame`
`names(data_frame)`     | Show list of headers (i.e. variables that can be accessed)
`head(data_frame)`      | Show first six rows of `data_frame`
`class(variable)`       | Show data type of `variable`
`levels(factor)`        | List categories in `factor`
`identical(x, y)`       | Return boolean of whether `x` and `y` are identical
`table(vector)`         | Return frequency of each unique element in `vector`
`seq(start, stop, inc)` | Return vector of numeric values (not necessarily integers) ranging from `start` to `stop`, with an optional increment of `inc` (default 1)


## Arithmetic, logical, and relational operators

These are technically functions, but (mostly) have symbols instead of names.

Operator | Purpose
---------|---------
`+`      | Addition
`-`      | Subtraction
`*`      | Multiplication
`/`      | Division
`%/%`    | Integer division
`%%`     | Modulo
`^`      | Exponentiation
`!`      | Logical negation (NOT)
`&`      | Logical AND (elementwise)
`&&`     | Logical AND (left-to-right; use in `if` statements)
`|`      | Logical OR (elementwise)
`||`     | Logical OR (left-to-right; use in `if` statements)
`xor`    | Logical exclusive OR (elementwise)
`isTRUE` | Check if argument is `TRUE`
`==`     | Relational equality check



## Nested functions

This just means you can call a function on the output from another function.  So you can do

```r
log(exp(1))
```

and R will evaluate the nested functions from the inside out, i.e. it will calculate `exp(1)` first, and then pass the result of that to `log()`.

## Arguments

The output of `args(function_name)` will show which arguments are expected and which are optional.  Arguments can be assigned by name using the equals sign, `=`.  You can also assign values to objects using the equals sign, but to avoid confusion, best practice is to use `<-` for object assignment and `=` for argument assignment.

If no argument names are used, R assumes you're following the order given in the documentation (or equivalently by `args`).