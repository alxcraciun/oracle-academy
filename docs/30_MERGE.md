# MERGE

- basically this will `insert` and `update` simultaneously
- if a row doesn’t exist, it will create & update it
- can be used with aliases

<br>

```sql
merge into copy_emp c using employees e
on (c.employee_id = e.employee_id)
when matched then update
	set 
		c.last_name = e.last_name
		c.department_id = e.department_id
when not matched then insert
	values (e.employee_id, e.last_name, e.department_id);
```