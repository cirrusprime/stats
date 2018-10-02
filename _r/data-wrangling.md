---
layout: page
title: Data Wrangling
---
Use `dplyr` package for this.

## `dplyr` functions

Function | Purpose
---------|---------
`mutate` | Change data table by adding a new column or changing an existing one
`filter` | Filter data by subsetting rows
`select` | Filter data by subsetting columns

Also note that you can send output of one function as input to another function by using the **pipe operator** `%>%`, e.g.

```r
murders %>% select(state, region, rate) %>% filter(rate >= 0.71)
```

pipes the data frame `murders` into the `select` function, where it is taken as the first argument, and the output from `select` is taken as the first argument in the `filter` call.

