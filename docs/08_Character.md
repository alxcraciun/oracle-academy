# Character

- Character Functions can be used in the `SELECT`, `WHERE` and `ORDER BY` clauses
- There are 2 main usecases for these functions: 
  - Convert the case of character strings
  - `Join`, `extract`, `show`, `find`, `pad` and `trim` character strings

<br>

## Case Manipulation

- helpful when you are searching for data
- helpful when you don’t know case form of value

<br>

### LOWER

- Converts alpha characters to lower-case

```sql
select last_name 
from employees
where LOWER(last_name) = 'abel';
```

<br>

### UPPER

- Converts alpha characters to upper-case

```sql
select last_name
from employees
where UPPER(last_name) = 'ABEL';
```

<br>

### INITCAP

- `UPPER` but only for the first letter of each word

```sql
select last_name
from employees
where initcap(last_name) = 'Abel';
```

<br>

## Character Manipulation

- used to extract, change, format or alter a character string

<br>

### CONCAT

- joins two values together
- could also be writter with `||` operator

```sql
select CONCAT('Hello', 'World')
from DUAL;
```

```sql
select CONCAT(first_name, last_name)
from employees;
```

<br>

### SUBSTR

- extracts a string of a determined length
- arguments are: `string`, `start_position`, `length`

```sql
select SUBSTR('HelloWorld', 1, 5)
from DUAL; 
```

```sql
select SUBSTR('HelloWorld', 6)
from DUAL; 
```

```sql
select SUBSTR(last_name, 1, 3)
from employees;
```

<br>

### LENGTH

- shows the length of a string as a number value

```sql
select LENGTH('HelloWorld')
from DUAL;
```

```sql
select LENGTH(last_name)
from employees;
```

<br>

### INSTR

- finds number position of specified character(s)
- returns first occurance position as number
- if nothing is found, it returns 0.

```sql
select INSTR('HelloWorld', 'W')
from DUAL;
```

```sql
select last_name, INSTR('last_name', 'a')
from employees;
```

<br>

### LPAD & RPAD

- pads the left / right side of a character string
- arguments: `string`, `total_characters`, `pad_character`

```sql
select LPAD('HelloWorld', 15, '*')
from DUAL;
```

```sql
select LPAD(last_name, 8, '*')
from employees;
```

<br>

### TRIM

- removes specified character
- can remove first, last or both recurrences

```sql
select TRIM ( LEADING 'a' FROM 'abcba')
from DUAL;
```

```sql
select TRIM ( TRAILING 'a' FROM 'abcba')
from DUAL;
```

```sql
select TRIM ( TRAILING 'a' FROM 'abcba')
from DUAL;
```

<br>

### REPLACE

- replace sequence of characters in a string with another set
- arguements are: `base_string`, `string_to_replace`, `replacement`

```sql
select REPLACE('JACK and JUE', 'J', 'BL')
from DUAL;
```

```sql
select REPLACE('JACK and JUE', 'J')
from DUAL;
```

```sql
select REPLACE(last_name, 'a', '*')
from employees;
```

<br>

# Column Aliases

- often a column alias is used to name a function
- alias appears in the output insead of function syntax

```sql
select lower(last_name) || lower(substr(first_name, 1, 1)) as "User Name"
from employees;
```

```sql
select lower(last_name) || lower(substr(first_name, 1, 1))
from employees;
```

<br>

# Substitution Variables

> Sometimes, you may need to run the same query with different values. <br>
> For example, when doing a company report, you’re running the a query for each department to find employee data. <br>
> Without substitution variables, you’d have to repeatedly edit the same statement to change the `WHERE` clause.

Use `:variable_name` to create a substitution variable

```sql
select first_name, last_name, salary, department_id
from employees
where department_id = :enter_dept_id;
```