# Equijoin & Cartesian Product

<br>

Oracle Proprietary Joins
| Oracle Proprietary Joins | ANSI / ISO SQL: 1999 Equivalent               |
| ------------------------ | --------------------------------------------- |
| Cartesian Product        | Cross Join                                    |
| Equijoin                 | Natural Join                                  |
| Equijoin                 | Join using clause                             |
| Equijoin                 | JOIN ON clause (if equality operator is used) |
| Non-equijoin             | ON clause                                     |

```sql
select table1.col1, table2.col2
from table1, table2
where table1.col = table2.col
```

<br>

### Equijoin

- sometimes called “simple” or “inner” join
- combines rows that have the same values for specified columns

```sql
select employees.last_name, employees.job_id, jobs.job_title
from employees, jobs
where employees.job_id = jobs.job_id
```

<br>

### Aliases

- a table alias is similar to a column alias
- renames the object within a statement

```sql
select last_name, e.job_id, job_title
from employees e, jobs j 
where e.job_id = j.job_id
and department_id = 80
```
If you use alias, specify alias in the SELECT clause, not the table name 

<br>

### Cartesian Product Join

```sql
select e.last_name, d.department_name
from employees e, departments d
```