# Multiple-Row

- subqueries that return more than one value
- multiple-row comparison operators are: `in`, `any`, `all`
- the `not` operator can also be used with any of those three

<br>

## IN

- used within the outer query `where` clause
- selects only those rows which are in a list of values
- the list of values are the values returned by the subquery

<br>

**All employees hired in same year as an employee in department 90**

```sql
select last_name, hire_date
from employees
where extract(year from hire_date) IN (
	select extract(year from hire_date)
	from employees
	where department_id = 90);
```

<br>

## ANY

- used in the outer-query `where` clause
- selects rows which match the criteria of at least one value

<br>

Employee whose hired_date < at least one of hired_dates of an employees from department 90

```sql
select last_name, hire_date
from employees
where extract(year from hire_date) < ANY (
	select extract(year from hire_date)
	from employees
	where department_id = 90);
```

<br>

## ALL

- used in the outer-query `where` clause
- selects rows which match the criteria of all values

<br>

```sql
select last_name, hire_date
from employees
where extract(year from hire_date) < ALL (
	select extract(year from hire_date)
	from employees
	where department_id = 90);
```

<br>

## Null Values

- suppose that one of the values returned by a subquery is null

<br>

if `IN` or `ANY` are used, outer query will return rows which match non-null


```sql
select last_name, employee_id
from employees
where employee_id in (
	select manager_id 
	from employees);
```

<br>

if `ALL` is used, the outer query returns no rows

```sql
select last_name, employee_id 
from employees 
where employee_id <= ALL(
	select manager_id
	from employees);
```

<br>

### Group by & Having

- `group by` and `having` can be used with multiple-row subqueries

<br>

**Departments with min(salary) < salary of any employee at dept 10 or dept 20**

```sql
select department_id, min(salary)
from employees
group by department_id
having min(salary) < ANY ( 
	select salary
	from employees
	where department_id in (10, 20)) 
order by department_id;
```

<br>

## Multiple Column Subqueries

- Subqueries can also use more columns

<br>

Employees with ***(manager, dept)*** same as those of employees 149 or 174

```sql
select employee_id, manager_id, department_id
from employees
where (manager_id, department_id) in
	(
	select manager_id, department_id
	from employees
	where employee_id IN (149, 174)
	)
AND employee_id NOT IN (149, 174)
```
	*this is called a pair-wise multiple column subquery*

<br>

**Same thing, but with a non-pair-wise multiple-column subquery**

```sql
select employee_id, manager_id, department_id
from employees
where manager_id in
	(
	select manager_id
	from employees
	where employee_id IN (149, 174)
	)
AND department_id in 
	(
	select department_id
	from employees
	where employee_id IN (149, 174)
	)
AND employee_id NOT IN (149, 174)
```

<br>

## Multiple vs Single Subqueries

> Some subqueries may return a single-row or multiple-rows. <br>
> It depends on the data values existing currently in the table.

<br>

**Generally, it’s better to use a multiple-row subqueries.** <br>
If you use a single-row subquery and data changes the program will crash.