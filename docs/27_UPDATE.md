# UPDATE

- used to modify existing rows in a table
- can use the result of a single-row subquery

<br>

**Changing one column**

```sql
update copy_employees
set phone_number = '123456'
where employee_id = 303
```

<br>

**Changing more columns**

```sql
update copy_employees
set phone_number = '654321', last_name = 'Jones'
where employee_id >= 303
```

<br>

## Update using single-row subqueries

<br>

**Updating one column**

```sql
update copy_employees
set salary = (
	select salary
	from copy_employees
	where employee_id = 100
) 
where employee_id = 101 
```

<br>

**Updating multiple columns**

```sql
update copy_employees
set salary = 
(
	select salary
	from copy_employees
	where employee_id = 205
) 
		job_id = 
(
	select job_id
	from copy_employees
	where employee_id = 205
)
where employee_id = 206
```