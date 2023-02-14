# COUNT & DISTINCT & NVL

## Count

- returns number of non-null values
- `COUNT(*)`  —  return number of rows in a table

```sql
select count(*)
from employees
where hire_date < '01-Jan-1996';
```

<br>

## Distinct

- used to return non-duplicate rows or non-duplicate combinations

```sql
select DISTINCT job_id, department_id
from employees;
```

<br>

### NVL

- sometimes it is desirable to include null values in group functions
- for example, now AVG takes into account null values as well

```sql
select AVG(NVL(customer_orders, 0))
from employees;
```