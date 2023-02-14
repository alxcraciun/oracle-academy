# NULL

<br>

## NVL

- converts a null value to known value of fixed type
- data types of the null value column and new value must be the same

<br>

**Replaces null values with the string ‘None’**

```sql
select country_name, 
NVL(internet_extension, 'None') as "Internet extn"
from wf_countries
where location = 'Southern Africa'
order by internet_extension desc;
```

<br>

**Replaces null values with the value 0**

```sql
select last_name, NVL(commission_pct, 0)
from employees
where department_id IN(80,90);
```

<br>

**Replaces null values with date (sort of)** <br>
`date_of_independence` is a `varchar2` data type

```sql
select NVL(date_of_independence, 'No date')
from wf_countries;
```

<br>

Arithmetic operations performed with `null` will always return `null`

```sql
select last_name, NVL(commission_pct, 0) * 250 as "Commission"
from employees
where department_id in (80, 90);
```

<br>

## NVL2

- arguments: `expression`, `not_null`, `is_null`
- evaluates an expression and outputs second or third arg

```sql
select last_name, salary,
NVL2(commission_pct, salary + (salary*commissoin_pct), salary)
as income
where department_id in (80, 90);
```

<br>

## NULLIF

- arguments: `exp1`, `exp2`
- if they are equal, return `null`
- if they are not equal, returns `exp1`

```sql
select first_name, LENGTH(first_name) as "Length FN", 
last_name, LENGTH(last_name) as "Length LN", 
NULLIF(LENGTH(first_name), LENGTH(last_name))) as "Compare them"
from employees;
```

| First_Name | Length FN | Last_Name | Length LN | Compare them |
| ---------- | --------- | --------- | --------- | ------------ |
| Ellen      | 5         | Abel      | 4         | 5            |
| Curtis     | 6         | Davies    | 6         | -            |
| Lex        | 3         | De Haan   | 7         | 3            |

<br>

## COALESCENCE

- extension of `NVL` that takes multiple values
- iterates through arguments until if finds `not null` expression

```sql
select last_name, COALESCENCE(commission_pct, salary, 10) as "Comm"
from employees
order by commission_pct;
```

| LAST_NAME | Comm  |
| --------- | ----- |
| Grant     | .15   |
| Zlotkey   | .2    |
| Taylor    | .2    |
| Abel      | .3    |
| Higgins   | 12000 |
| Gietz     | 8300  |