---
layout: page
title: Data Types
---
* The main data type used in R is the data frame
* Vectors are lists of only one type
* Logical vectors contain either `TRUE` or `FALSE` values
* Factors are a data type for holding categorical variables, and it's more memory-efficient to actually store what look like character strings (the categories) as integers
* The value used for missing data is `NA`

## Data frames (`data.frame` type)

Create a data frame using the `data.frame` function: `data.frame(header1 = datavector1, header2 = datavector2, ...)`. 

The **accessor** enables us to access a specific column of a data frame, and is denoted by `$`: `data_frame$column_header`.  The alternative option is to use double square brackets `[[]]`: `data_frame[["column_header"]]`.

You can **subset** data from a data frame using single square brackets `[]`: `data_frame["column_header"]`.

## Vectors

Indexes in R start at 1, in contrast to Python, C(++), and similar (which all start at 0).

Vector function     | Purpose
--------------------|-------------------------------
`c(a, b, c)`        | Concatenate `a`, `b`, and `c`
`names(vector)`     | Set column names for `vector` (or data frame)
`sort(vector)`      | Sort `vector` numerically/alphabetically (equivalent to output of `vector[order(vector)]`)
`order(vector)`     | Return index that puts `vector` in order, i.e. the original index of each element in `sort` order
`max(vector)`       | Return highest value in `vector`
`which.max(vector)` | Return index of highest value in `vector`
`min(vector)`       | Return lowest value in `vector`
`which.min(vector)` | Return index of lowest value in `vector`
`rank(vector)`      | Return rank of each element in `vector` (its position in sorted order)

You can also grab multiple separate elements of a vector as a **subset** (using single square brackets) with e.g. `vector[c(1, 3)]`, which will give you the first and third elements of `vector` concatenated into a new vector (subset).

Vectors can be **coerced**, which means their elements get forced into being the same type, even if they appear as different types to start with.  For example, feeding a vector a bunch of both numeric and character variables will produce a coerced vector that contains the originally-numeric variables as character strings instead, and the vector class will be `character`.  However, if R fails to coerce something, it will be replaced by `NA`, the value for missing data.

You can also force conversions yourself, using functions like `as.numeric()` and `as.character()`.

## Integers

Force an integer, as opposed to a numeric variable, by adding `L` after a whole number, e.g. `class(3L)` will return `integer`.  Integers take up less memory than numerics do.

## Sequencing

The `seq` function is useful for populating vectors with numeric values.  The usual arguments are for a starting value, a maximum value (not necessarily the actual stopping point), and an increment (if not the default of 1).  It also allows for a different sort of argument, `length.out`, which must be specified by name, and which will create an equally-spaced sequence with the specified length.