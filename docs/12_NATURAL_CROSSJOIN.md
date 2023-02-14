# NATURAL & CROSS JOIN

## NATURAL JOIN

- combines fields from 2 or more tables
- based on all **columns with the same name**
- selects rows which have equal values in all matched columns
- the `natural join` column does not have to appear in `select`

<br>

**Data Sample**

| EMPLOYEE_ID | FIRST_NAME | LAST_NAME | JOB_ID     |
| ----------- | ---------- | --------- | ---------- |
| 100         | Steven     | King      | AD_PRES    |
| 101         | Neena      | Kochhar   | AD_VP      |
| 102         | Lex        | De Haan   | AD_VP      |
| 103         | Shelley    | Higgins   | AC_MGR     |
| 104         | William    | Gietz     | AC_ACCOUNT |

| JOB_ID     | JOB_TITLE                     |
| ---------- | ----------------------------- |
| AD_PRES    | President                     |
| AD_VP      | Administration Vice President |
| AD_ASST    | Administration Assistant      |
| AC_MGR     | Accounting Manager            |
| AC_ACCOUNT | Public Accountant             |
| SA_MAN     | Sales Manager                 |

```sql
select first_name, last_name, job_id, job_title
from employees NATURAL JOIN jobs
where employee_id > 80;
```

<br>

**Natural Join Output**

| FIRST_NAME | LAST_NAME | JOB_ID     | JOB_TITLE                     |
| ---------- | --------- | ---------- | ----------------------------- |
| Steven     | King      | AD_PRES    | President                     |
| Neena      | Kocchar   | AD_VP      | Administration Vice President |
| Lex        | De Haan   | AD_VP      | Administration Vice President |
| Shelley    | Higgins   | AC_MGR     | Accounting Manager            |
| William    | Gietz     | AC_ACCOUNT | Public Accountant             |

<br>

### CROSS JOIN

- ANSI/ISO SQL-99
- joins each row in one table to every row in the other table
- represents all posisible row combinations from the two tables
- `cross join` a table with 20 rows with a table with 100 rows  →  2000 rows

```sql
select last_name, department_name
from employees CROSS JOIN departments;
```