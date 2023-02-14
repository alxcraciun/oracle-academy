# Data Types

- Each column in a relational database can hold only one type of data.
- You cannot mix data types within a column.

<br>

**Character types** 

- `CHAR`  —  fixed size, max. 2000 characters
- `VARCHAR2`  —  variable size, max. 4000 characters
- `CLOB`  —  variable size, maximum 128 terabytes.

<br>

**Number types** 

- `NUMBER`  —  variable size, max. precision 38 digits

<br>

**Date and time types:**

- `DATE`
- `INTERVAL`
- `TIMESTAMP`  —  allows fractions of a second (3 digits)

<br>

**Binary types (also JPG, WAP, MP3 and multimedia files)**

- `RAW`  —  variable size, max. 2000 bytes
- `BLOB`  —  variable size, max. 128 terabytes

<br>

## TIMESTAMP

<br>

Example 1

```sql
create table time_ex1
(exact_time TIMESTAMP);

INSERT INTO time_ex1
values ('10-Jun-2017 10:52:29.123456');

INSERT INTO time_ex1
values (SYSTIMESTAMP);

select *
from time_ex1;
```

<br>

Example 2  —  taking into account different time zones

```sql
create table time_ex2
(time_with_offset TIMESTAMP WITH TIME ZONE);

insert into time_ex2
values (systimestamp);

inset into time_ex2
values ('10-Jun-2017 10:52:29.123456 AM +2:00');

select *
from time_ex2;
```
*You can also use TIMSTAMP WITH LOCAL TIME ZONE to use user’s GMT*

<br>

## INTERVAL

```sql
create table time_ex 
( loan_duration1 INTERVAL YEAR(3) TO MONTH,
	loan_duration2 INTERVAL YEAR(2) TO MONTH
);

INSERT INTO time_ex values 
( interval '120' MONTH(3),
	interval '3-6' YEAR TO MONTH
);

select  sysdate + loan_duration1 as "120 months from now",
				sysdate + loan_duration2 as "3 years 6 months from now"
from time_ex;	
```