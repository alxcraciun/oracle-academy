# Introduction & Join Clauses

> SQL provides join conditions that enable information to be queried from separate tables and combined in one report.

**There are two sets of syntax which can be used:**
- Oracle proprietary joins
- ANSI / ISO SQL 99 joins

<br>

## ANSI

- The American National Standards Institute
- Founded in 1918, private non-profit organization

<br>

## SQL

- Structured Query Language
- the information-processing industry standard language
- used for relational database management systems (RDBMS)
- originally designed by IBM in the mid 1970s, adopted by ANSI in 1986

<br>

**So far there have been 3 ANSI standardizations of SQL:**

- ANSI-86
- ANSI-92
- ANSI-99

<br>

## JOIN Clauses

### USING

- `USING` specifies the columns that should be used for join.
- you can also add a `WHERE` clause to restrict rows from output

<br>

> In a `natural join` if the tables have columns with same name, but different data types the join causes an error. <br>
> To avoid this situation, the join clause can be modified with a `using clause`.

<br>

```sql
select first_name, last_name, department_id, department_name
from employees JOIN departments USING (department_id)
where last_name = 'Higgins';
```

<br>

### ON

- used if the columns to be joined have different names
- if join uses non-equality comparison operatiors such as <, > or `BETWEEN`

> When using an `ON` clause on columns with the same name in both tables... <br>
> Add a qualifier (either the table name or alias), otherwise an error will be returned.

```sql
select last_name, job_title 
from employees e JOIN jobs j ON (e.job_id = j.job_id)
where last_name LIKE 'H%';
```
you can also write it without an alias  →  (employees.job_id = jobs.job_id)

<br>

### ON clause with non-equality operator

> Sometimes you may need to retrieve data from a table that has no corresponding column in another table.

job_grades table 

| GRADE_LEVEL | LOWEST_SAL | HIGHEST_SAL |
| ----------- | ---------- | ----------- |
| A           | 1000       | 2999        |
| B           | 3000       | 5999        |
| C           | 6000       | 9999        |
| D           | 10000      | 14999       |
| E           | 15000      | 24999       |
| F           | 25000      | 40000       |

```sql
select last_name, salary, grade_level, lowest_sal, highest_sal
from employees JOIN job_grades 
ON (salary BETWEEN lowest_sal and highest_sal);
```

<br>

### Joining Three Tables

```sql
select last_name, department_name as "Department" , city
from employees 
JOIN departments USING (departmen_id)
JOIN locations USING (location_id)
```