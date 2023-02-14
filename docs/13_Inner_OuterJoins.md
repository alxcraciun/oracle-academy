# Inner & Outer Joins

> **Outer Joins** in ANSI-99 SQL allow you to Retrieve both: <br>
> The data that meets join condition & The data that does not meet the join condition.

<br>

**Inner Join** 

- can join two or more tables
- returns only matched rows

<br>

**Outer Join**

- can join two or more tables  
- returns unmatched rows as well as matched rows

## Outer Joins

- can be `left`, `right` or `full` based on order of the table names
- the three terms take into account the order in the `from clause`

<br>

### Left Outer Join

```sql
select e.last_name, d.department_id, d.department_name
from employees e LEFT OUTER JOIN departments d
ON (e.department_id = d.department_id);
```

| LAST_NAME  | DEPT_ID    | DEPT_NAME      |
| ---------- | ---------- | -------------- |
| Whalen     | 10         | Administration |
| Fay        | 20         | Marketing      |
| .......... | .......... | ..........     |
| Zlotkey    | 80         | Sales          |
| De Haan    | 90         | Executive      |
| Kochhar    | 90         | Executive      |
| King       | 90         | Executive      |
| Gietz      | 110        | Accounting     |
| Higgins    | 110        | Accounting     |
| Grant      | -          | -              |

<br>

### Right Outer Join

```sql
select e.last_name, d.department_id, d.department_name
from employees e RIGHT OUTER JOIN departments d
ON (e.department_id = d.department_id);
```

| LAST_NAME  | DEPT_ID    | DEPT_NAME      |
| ---------- | ---------- | -------------- |
| Whalen     | 10         | Administration |
| Fay        | 20         | Marketing      |
| .......... | .......... | ..........     |
| Zlotkey    | 80         | Sales          |
| De Haan    | 90         | Executive      |
| Kochhar    | 90         | Executive      |
| King       | 90         | Executive      |
| Gietz      | 110        | Accounting     |
| Higgins    | 110        | Accounting     |
| -          | 190        | Contracting    |

<br>

### Full Outer Join

- includes all rows from `left outer join` and  `right outer join` combined

```sql
select e.last_name, d.department_id, d.department_name
from employees e FULL OUTER JOIN departments d
ON (e.department_id = d.department_id);
```

| LAST_NAME  | DEPT_ID    | DEPT_NAME   |
| ---------- | ---------- | ----------- |
| King       | 90         | Executive   |
| Kochhar    | 90         | Executive   |
| .......... | .......... | ..........  |
| Zlotkey    | 80         | Sales       |
| Grant      | -          | -           |
| Mourgos    | 50         | Shipping    |
| .......... | .......... | ..........  |
| Fay        | 20         | Marketing   |
| -          | 190        | Contracting |