# DEFAULT

- each column in a table can have a default value specified for it
- default values will be assigned instead of the null values
- can be specified when a table is created

<br>

**When creating a table:**

```sql
create table my_employees(
	hire_date date default sysdate, 
	first_name varchar2(15),
	last_name varchar2(15)
);
```

<br>

**Explicit use of default**

```sql
insert into my_emplyoees
	(hire_date, first_name, last_name) 
values 
	(default, 'Angelina', 'Wright')
```

<br>

**Implicit use of default**

```sql
insert into my_emplyoees
	(first_name, last_name) 
values 
	('Angelina', 'Wright')
```