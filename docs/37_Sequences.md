# Sequences

## SEQUENCE Object


> SQL has a process for automaticaly generating unique numbers that eliminates the worry about the details of duplicate numbers. <br>
> The numbering process is handled through a database object called a sequence.

<br>

- **A sequence** is the third database object, after the table and the view.
- Because it is a shareable object, multiple users can access it.
- Usually, sequences are used to create a primary-key value.
- Stored and generated independently of tables.
- Same sequence can be used for multiple tables.

<br>

## **Sequence Syntax**

```sql
CREATE SEQUENCE sequence
[INCREMENT BY n]
[START WITH n]
[{MAXVALUE n | NOMAXVALUE}]
[{MINVALUE n | NOMINVALUE}]
[{CYCLE | NOCYCLE}]
[{CACHE n | NOCACHE}]
```

<br>

| sequence              | name of the sequence generator (object)                                                                                          |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| INCREMENT BY n        | specifies the interval between sequence numbers where n is an integer (if ommited, sequence increments by 1)                     |
| START WITH n          | specifies the first sequence number to be generated (if ommited, sequence starts with 1)                                         |
| MAXVALUE n            | specifies the maximum value the sequence can generate                                                                            |
| NOMAXVALUE            | specifes a maximum value of 10^27 for an ascending sequence and -1 for a descending sequence (default)                           |
| MINVALUE n            | specifies the maximum value the sequence can generate                                                                            |
| NOMINVALUE            | specifes a minimum value of 1 for an ascending sequence and -(10^26) for a descending sequence (default)                         |
| CYCLE / NOCYCLE       | specifies whether the sequence continues to generate values after reaching its max or min value (default NOCYCLE) 		  	   |
| CACHE n / NOCACHE     | specifies how many values the Oracle server pre-allocates and keeps in memory                                                    |

<br>

**Note** <br>
By default, the Oracle server caches 20 values.) If the system crashes, the values are lost.

<br>

Example 

```sql
CREATE SEQUENCE runner_id_seq
INCREMENT BY 1
START WITH 1
MAXVALUE 50000
NOCACHE
NOCYCLE;
```

<br>

> `NOCACHE` prevents value in the `SEQUENCE` from being cached in memory. <br> 
> In the event of system failures prevents pre-allocated and held in memory from being lost.

<br>

## Confirming sequences

**Verify that a sequence was created**

```sql
select *
from user_objects;
```

<br>

**To see all of the sequence settings**

```sql
select * 
from user_sequences;
```

<br>

> If `NOCACHE` is specified, the `last_number` column in the query displays the next available sequence number. <br>
> If `CACHE` is specified, the `last_number` column displays the next available number in the sequence which has not been cached into memory.

<br>

### NEXTVAL & CURRVAL

- pseudocolumns used to extract successive sequence numbers
- NEXTVAL must be referenced before CURRVAL can be referenced

<br>

```sql
INSERT INTO departments
	(department_id, department_name, location_id)
VALUES (departments_seq.NEXTVAL, 'Support', 2500);
```

<br>

**You can use NEXTVAL and CURRVAL in following cases:**

- SELECT list of a SELECT statement is not part of a subquery
- SELECT list of a subquery in an INSERT statement
- VALUES clause of an INSERT STATEMENT
- SET clause of an UPDATE STATEMENT

<br>

**You can’t use NEXTVAL and CURRVAL in following cases:**

- SELECT list of a view
- SELECT statement with DISTINCT keywords
- Subquery in a SELECT, DELETE or UPDATE statement
- SELECT statement with GROUP BY, HAVING, ORDER BY
- DEFAULT expressoin in a CREATE TABLE OR ALTER TABLE

<br>

### Manipulation of sequences

Creating the sequence

```sql
CREATE TABLE runners (
	runner_id NUMBER(6,0) CONSTRAINT runners_id_pk PRIMARY KEY,
	first_name VARCHAR2(30),
	last_name VARCHAR2(30)
);
```

<br>

Using the sequence

```sql
CREATE SEQUENCE runner_id_seq
	INCREMENT BY 1
	START WITH 1
	MAXVALUE 50000
	NOCACHE
	NOCYCLE;
```
*This allows new participants to have auto-generated runner_id*

<br>

Adding a new runner

```sql
INSERT INTO runners
	(runner_id, first_name, last_name)
VALUES (runner_id_seq.NEXTVAL, 'Joanne', 'Everely');
```
*Automatically be assigned to 1*

<br>

```sql
INSERT INTO runners
	(runner_id, first_name, last_name)
VALUES (runner_id_seq.NEXTVAL, 'Adam', 'Curtis');
```
*Automatically be assigned two*

<br>

Sequences can also be modified

```sql
ALTER SEQUENCE ruunner_id_seq
	INCREMENT BY 1
	MAXVALUE 999999
	NOCACHE
	NOCYCLE;
	
```

<br>

**Important** <br>
You cannot ALTER the START WITH option from a sequence

<br>

**Dropping a sequence  —**  `DROP SEQUENCE runner_id_seq;`