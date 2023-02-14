# Indexes

- a schema object which can speed up retrieval of rows by using a pointer
- if you do not have an index on the selected column, a full table scan occurs
- when you drop a table, corresponding indexes are also dropped

<br>

**Types of indexes:**

- Unique  —  created automatically by PRIMARY KEY OR UNIQUE constraint
- Non-unique  —  created manually by the user to speed up access to rows

<br>

```sql
CREATE INDEX index_name
ON table_name( col_x.... col_y )
```

<br>

**Indexes should be created only if:**

- the table is not updated frequently
- column contains a wide range of values
- column cotains a large number of null values
- table is large and and queries are expected to retrieve 2% - 4% of rows
- one or more columns are frequently used together in a where / join clause

<br>

**Important** <br>
Indexes must be updated every time a DML operation is used.

<br>

**Confirming Indexes (simple)**

```sql
select *
from USER_INDEXES;
```

<br>

**Confirming Indexes (advanced)**

```sql
select distinct 
ic.index_name, ic.column_name, ic.column_position, id.uniqueness

from user_indexes id, user_ind_columns ic
where id.table_name = ic.table_name
AND ic.table_anme = 'Desired_Table_Name';

```

<br>

## Composite Indexes

- an index that you create on multiple columns in a table
- null values are not included in the composite index

<br>

```sql
CREATE INDEX emps_name_idx
ON employees(first_name, last_name);
```

<br>

## Function-based Indexes

- an index based on expressions
- built from table columns, constants, SQL functions, user-defined functions

<br>

## Example  1  —  UPPER and LOWER

**When you don’t know in that case the data was stored**

```sql
CREATE INDEX upper_last_name_idx
ON employees(UPPER(last_name));
```

<br>

```sql
select *
from employees
where upper(last_name) = 'KING';
```

<br>

**Make sure that function doesn’t return null in subsequent queries!** <br>
*Otherwise the Oracle Server will perform a full table scan.*

<br>

```sql
select *
from employees
where upper(last_name) IS NOT NULL
ORDER BY UPPER(last_name)
```

<br>

## Example 2  —  TO_CHAR

```sql
CREATE INDEX emp_hire_year_idx
ON employees (TO_CHAR(hire_date, 'yyyy'));
```

<br>

```sql
select first_name, last_name, hire_date
from employees
where TO_CHAR(hire_date, 'yyyy') = '1987'
```
*Now Oracle uses the index instead of performing a full table scan*

<br>

## Index Operations

- You cannot modify indexes, but you can delete and re-create one.
- When you drop an index, constraints are automatically dropped.
- **Dropping an index**  —  `DROP INDEX upper_last_name_idx;`