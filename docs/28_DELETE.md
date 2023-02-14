# DELETE

- used to remove existing rows in a table
- if you omit `where`, all rows will be deleted

```sql
delete from copy_employees
where employee_id = 303;
```

<br>

## Delete using subquery

<br>

**Delete employees from certain department**

```sql
delete from copy_employees
where department_id = (
	select department_id
	from departments
	where department_name = 'Shipping');
```

<br>

**Delete rows of all employees who work for a manager of < 2 employees**

```sql
delete from copy_employees e
where e.manager_id IN (
	select d.manager_id
	from employees d
	having count(d.department_id) < 2
	group by d.manager_id);
```