# CASE & DECODE

## SQL Syntax

> Use of ANSI/ISO SQL 99 syntax is recommended. 

<br>

**Use can write SQL statements in different syntaxes:**

- ANSI/ISO SQL 99
- Oracle proprietary statements

<br>

**Example of functions returning the same information**

- CASE  →  an ANSI/ISO SQL 99 compliant statement
- DECODE  →  an Oracle Proprietary statement

<br>

### CASE

- does the work of an IF-THEN-ELSE statement
- data types of `CASE`, `WHEN`, `ELSE` must be the same

```sql
select last_name, 
CASE department_id
WHEN 90 THEN 'Management'
WHEN 80 THEN 'Sales'
WHEN 60 THEN 'It'
ELSE 'Other dept'
END AS "Department"
from employees;
```

| LAST_NAME | Department  |
| --------- | ----------- |
| King      | Management  |
| De Haan   | Management  |
| Higgins   | Other dept  |
| Zlotkey   | Sales       |
| Abel      | Sales       |
| Taylor    | Sales       |
| Hunoid    | It          |
| Hartstein | Other dept. |

<br>

### DECODE

- does the work of an IF-THEN-ELSE statement
- compares an expression to each of the search values
- if the final `default` is omitted a `null` value is returned

```sql
select last_name
DECODE
(
department_id,
90, 'Management',
80, 'Sales',
60, 'It',
'Other dept'
)
as "Department"
from employees;
```
- Returns exactly same results as the previous CASE example