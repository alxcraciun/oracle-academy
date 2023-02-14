# Non-equijoins & Outer Joins

## Non-equijoins

- used to retrieve data from tables with no corresponding columns

```sql
select last_name, salary, grade, lowest_sal, highest_sal
from employees, job_grades
where salary between lowest_sal and highest_sal
```

| LAST_NAME | SALARY  | GRADE   | LOWEST_SAL | HIGHEST_SAL |
| --------- | ------- | ------- | ---------- | ----------- |
| Vargas    | 2500    | A       | 1000       | 2999        |
| Matos     | 2600    | A       | 1000       | 2999        |
| Davies    | 3100    | B       | 3000       | 5999        |
| Rajs      | 3500    | B       | 3000       | 5999        |
| Lorentz   | 4200    | B       | 3000       | 5999        |
| Whalen    | 4400    | B       | 3000       | 5999        |
| Mourgos   | 5800    | B       | 3000       | 5999        |
| Fay       | 6000    | C       | 6000       | 9999        |
| .......   | ....... | ....... | .......    | .......     |

<br>

### Left Outer Join

- used to see rows that have no mathing value in the other table

```sql
select e.last_name, d.department_id, d.department_name
from employees e, departments d
where e.department_id = d.department_id(+)
```

| LAST_NAME | DEPT_ID | DEPT_NAME      |
| --------- | ------- | -------------- |
| Whalen    | 10      | Administration |
| Fay       | 20      | Marketing      |
| Grant     | -       | -              |

<br>

### Right Outer Join

- used to see rows that have no mathing value in the other table

```sql
select e.last_name, d.department_id, d.department_name
from employees e, departments d
where e.department_id (+) = d.department_id
```

| LAST_NAME | DEPT_ID | DEPT_NAME      |
| --------- | ------- | -------------- |
| Whalen    | 10      | Administration |
| Fay       | 20      | Marketing      |
| -         | 190     | Contracting    |

<br>

### Full Outer Join

- it is not possible to have the equivalent of a FULL OUTER JOIN
- adding (+) to both columns would results in an error