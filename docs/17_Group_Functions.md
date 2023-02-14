# Group Functions

- can operate on a whole table or on a specific grouping of rows
- each functions returns one result

<br>

## MIN & MAX

- used with columns that store any data type
- returns the minimum / maximum value

```sql
select MAX(salary)
from employees;
```

<br>

## SUM & AVG

- used with columns that store numeric data
- returns the total sum / average  of the values

<br>

## COUNT

- returns the numbers of rows

<br>

## VARIANCE  &  STDDEV

- used with columns that store numeric data
- returns the spread of data around the mean

<br>

Example:  
- Average grade for the class on the last test was 82%
- The student’s scores ranged from 40% to 100% 
- So, `VARIANCE` would be greater than if the student’s scores ranged from 78% to 88%

<br>

Example
- For two sets of data with approximately the same mean, 
- the greater the spread, the greater the standard deviation

<br>

## Properties

### Rules

- Group functions ignore null values
- Group functions can’t be used in where clause
- `MIN`, `MAX` and `COUNT` can be used with any data type
- `SUM`, `AVG`, `STTDEV`, `VARIANCE` can be used only with numeric data

<br>

### Select Clause

- group functions are written in the select clause
- group functions ***CAN NOT*** be used in the where clause

```sql
select col, group_func(col), ...
from table1
where condition
group by col;
```

<br>

### Group Functions and NULL

- groups functions ignore NULL values
- for examplae, they won’t be used to find `AVG(...)`

<br>

### Multiple Group Functions

- you can have multiple group functions in the select clause

```sql
select max(salary), min(salary), min(employee_id)
from employees
where department_id = 60
```

| MAX(SALARY) | MIN(SALARY) | MIN(EMPLOYEE_ID) |
| ----------- | ----------- | ---------------- |
| 9000        | 4200        | 103              |