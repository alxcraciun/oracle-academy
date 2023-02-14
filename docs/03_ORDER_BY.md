# ORDER BY

- used to sort information in a database
- `ORDER BY` must be the last clause used
- can have two parameters: `asc` and `desc`
- also you can have `nulls first` and `nulls last`
- Default state for clase is used with: `asc nulls last`

<br>

**Default State**

```sql
select last_name, hire_date
from employees
order by hire_date;
```

<br>

**Descending Order**

```sql
select last_name, hire_date
from employees
order by hire_date desc;
```

<br>

**Sort using column aliases**

```sql
select last_name, hire_date as "Date Started"
from employees
order by "Date Started";
```

<br>

**Sorting by a column not listed**

```sql
select employee_id, first_name
from employees
where employee_id < 105
order by last_name;
```

<br>

**Sorting with multiple columns**

```sql
select department_id, last_name
from employees
where department_id <= 50
order by department_id desc, last_name;
```

<br>

**Order of execution**

1. `From` clause  —  locates the table with the data
2. `Where` clause  —  restricts the rows to be returned
3. `Select` clause  —  selects from reduced data the columns 
4. `Order by` clause  —  orders the result set previously generated