# INSERT

***Usecase: How to create a copy of a table***

<br>

Create the new table

```sql
create table copy_employees
as (select * from employees);
```

<br>

Verify the created table

- `describe copy_employees;`
- `select * from copy_employees;`

<br>

## Insert

- used to add a new row to a table

```sql
insert into copy_departmanets
(department_id, department_name, manager_id, location_id)
values 
(200, 'Human Resources', 205, 1500);
```

<br>

You can also add them by ommiting the column names: 
- the values for each column must match exactly match the default order (as shown in the describe statement)
-  a value must be provided for each column.

<br>

**Date format used for INSERT** <br> 
DD-Mon-YYYY

<br>

### Insert multiple rows

- this can be achieved by using a subquery
- all results from the subquery are inserted into the table

```sql
insert into sales_reps(id, name, salary, comission_pct)
	select employee_id, last_name, salary, comission_oct
	from employees
	where job_id like '%REP%';
```