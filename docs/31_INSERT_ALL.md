# INSERT ALL

***Usecase: Multi-table inserts***

<br>

**Basic syntax**

```sql
insert all 
	into my_employees
		values (hire_date, first_name, last_name)
	into copy_my_employees
		values (hire_date, first_name, last_name)
select hire_date, first_name, last_name
from employees;
```

<br>

**Complex syntax:**

![Image-20](./assets/Image-20.png)