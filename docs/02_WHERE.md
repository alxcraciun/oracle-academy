# WHERE

- In a `select` statement: `select`clause and and `from` clause are mandatory
- However, you can also add an optional `where` clause to restrict data output
- An alias cannot be used in a where clause. 

```sql 
select employee_id, first_name, last_name
from employees
where employee_id = 101;
```

<br>

- When comparing strings remember to take into account case-sensitivity.
- You can leave numbers alone, but enclose strings in single-quotation marks.

```sql
where salary >= 6000

where job_id = 'IT_PROG'

where hire_date < '01-Jan-2020'
```

<br>

### Comparison Operators

- Equal  →  `=`
- Less than →  `<`
- Greater than  →  `>`
- Less or equal to  →  `<=`
- Greater or equal to  →  `>=`
- Not equal to →  `<>`  /  `!=`  /  `^=`

<br>

### BETWEEN ... AND

- used to select and display rows based on a range of values
- returns a range of values between and inclusive the lower and upper limits

```sql
select last_name, salary
from employees
where salary between 9000 and 11000;
```

<br>

### IN

- used to test whether a value is in a specified set of values

```sql
select city, state_province, country_id
from locations
where country_id in ('UK', 'CA');
```

<br>

### LIKE

- select rows that match either character, dates or number patterns
- Wildcards can be used to construct a search string
  - `_`  —  represents a single character
  - `%`  —  represents any sequence of zero or more characters

```sql
select last_name 
from employees
where last_name like '_o%';
```

<br>

### ESCAPE

- you can use `ESCAPE` to override `%` or `_` as string characters
- this example uses the `\` as the backslash character, other work too

```sql
select last_name, job_id
from employees
where job_id like '%\_R%' escape '\';
```

<br>

### IS NULL

- tests for unavailable, unassigned or unknown data

```sql
select last_name, manager_id
from employees
where manager_id is null;
```

<br>

### IS NOT NULL

- tests for data that is available in the database

```sql
select last_name, commission_pct
from employees
where commission_pct is not null;
```

<br>

## Logical Operators - AND, NOT, OR

- it is often desirable to be able to restrict the output and return subsets
- conditional operators such as `AND`, `NOT`, `OR` make these requests easier

<br>

Examples for the `AND` operator

```sql
select last_name, department_id, salary
from employees
where department_id > 50 AND salary > 12000;
```

```sql
select last_name, department_id, salary
from employees
where hire_date > '01-jan-1998' AND job_id like 'SA%';
```

<br>

Examples for the `OR` operator

```sql
select department_name, manager_id, location_id
from departments
where location_id = 2500 or manager_id = 124
```

<br>

Examples for the `NOT` operator

```sql
select department_name, location_id
from departments
where location_id NOT IN (1700, 1800)
```

<br>

## Rules of Precedence

```sql
select last_name || ' ' || salary * 1.05 as "Employee Raise"
from employees
where department_id in (50, 80) 
	AND first_name like 'C%' 
	OR last_name like 's%';
```

<br>

**What happens first?**

1. Paranthesis  →  `(...)`
2. Arithmetic  →  `+ - * /`
3. Concatenation  →  `||`
4. Comparison  →  `<  <=  >  >=  <>` 
5. `IS (NOT) NULL` , `LIKE` , `NOT IN`
6. `(NOT) BETWEEN`
7. `NOT`
8. `AND`
9. `OR`