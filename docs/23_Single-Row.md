# Single-Row Subqueries

- return only one row
- Use comparison operators

## Examples

<br>

Return employees working in the marketing department
```sql
select last_name, job_id, department_id
from employees

where department_id = (
	select department_id 
	from departments 
	where department_name = 'Marketing')

order by job_id
```

<br>

Use multiple subqueries to return information for the outer query

```sql
select last_name, job_id, department_id
from employees

where job_id = (
	select job_id
	from employees
	where employee_id = 141)

and department_id = (
	select department_id 
	from departments 
	where location_id = 1500)
```

<br>

## Group Functions

- group functions can be used in subqueries

<br>

**Which employees earn less than the average salary?**

```sql
select last_name, salary
from employees
where salary < (
	select avg(salary)
	from employees);
```

<br>

## HAVING clause

- Subqueries can also be placed in the `having` clause.

<br>

**Which departments with lowest salary > lowest salary in department 50?**

```sql
select department_id, min(salary)
from employees
group by department_id
having min(salary) > (
	select min(salary)
	from employees
	where department_id = 50);
```