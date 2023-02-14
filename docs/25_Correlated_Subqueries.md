# Correlated subqueries

![Untitled](Correlated%20subqueries%20553636f07d42498ca99d9a4dae27a26d/Untitled.png)

<br>

> Oracle server performs a correlated subquery when <br>
> the subquery references a column from a table referred to in the parent statement.

- parent statements can be a `select`, `update` or `delete`
- correlated subqueries run once for each row considered

<br>

**Whose salary is higher than the average salary of their department?**

```sql
select o.first_name, o.last_name, o.salary
from employees o
where o.salary > 
	(
	select avg(i.salary)
	from employees i 
	where i.department_id = o.department_id
	);
```

<br>

### EXISTS & NOT EXISTS

- Subquery  —  selects employees that are managers
- Query  —  returns rows that do NOT EXIST in subquery

<br>

```sql
select last_name as "Not a Manager"
from employees emp
where NOT EXISTS (
	select * 
	from employees mgr 
	where mgr.manager_id = emp.employee_id 
	);
```

<br>

| Not a Manager |
| ------------- |
| Whalen        |
| Gietz         |
| Abel          |
| Taylor        |
| ....          |

<br>

***Same query, but with NOT IN ...*** 

> This suggests there are no employees who who are also not managers. <br>
> So all employees are managers, which we already know is not true

<br>

```sql
select last_name as "Not a Manager"
from employees emp
where emp.employee_id NOT IN (
	select mgr.manager_id
	from employees mgr
	);
```

<br>

**Important!** <br>
Beware of NULLS in subqueries when using IN or NOT IN.

<br>

## WITH clause

- retrieves the results of one or more query blocks
- stores query blocks results for the user who runs it
- `WITH` clause should be used because it: 
  - improves performance
  - makes queries easier to read

<br>

```sql
WITH ***managers*** AS (
	select distinct manager_id 
	from employees 
	where manager_id is not null) 

select last_name as "Not a manager"
from employees
where employee_id NOT IN 
	(
	select *
	from ***managers***
	);
```