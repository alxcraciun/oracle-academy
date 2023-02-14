# GROUP BY & HAVING Clauses

## Group by

- divide the rows from a table into smaller groups

```sql
select department_id, AVG(salary)
from employees
group by department_id
order by department_id
```

<br>

Columns in the `select` clause must either
- be part of a group function,
- be listed in the group by clause

<br>

| DEPARTMENT_ID | AVG(SALARY) |
| ------------- | ----------- |
| 10            | 4400        |
| 20            | 9500        |
| 50            | 3500        |
| 60            | 6400        |
| 80            | 10033.33    |
| 90            | 19333.33    |
| 110           | 10150       |
| -             | 7000        |

<br>

### Where Clause

- used to exclude rows before the remaining rows are formed into groups

```sql
select department_id, max(salary)
from employees
where last_name != 'King'
group by department_id;
```

<br>

### More group by examples

<br>

**Round the average of a whole number**

```sql
select region_id, round(avg(population)) as Population
from wf_countries
group by region_id 
order by region_id;
```

<br>

**Count number of spoken languages for all countries**

```sql
select country_id, count(language_id) as "Number of languages"
from wf_spoken_languages
group by country_id;
```

<br>

### Groups within groups

Shows how many employees are doing each job within each department

```sql
select department_id, job_id, count(*)
from employees
where department_id > 40
group by department_id, job_id
```

<br>

### Guidelines

- You cannot use a column alias in the `group by` clause
- `Where` clause excludes rows before they are divided in groups
- Columns in the `select` clause must either
  - be part of a group function,
  - be listed in the group by clause

<br>

## Having

- `where` clause  —  restricts the rows selected
- `having` clause  —  restricts the groups selected

<br>

When using `group by` and `having`: <br>
1. the rows are grouped, 
2. group functions are applied,
3. only those groups matching the having clause are displayed.

<br>

**Example 1**

```sql
select department_id, max(salary)
from employees
group by department_id
HAVING count(*) > 1
order by department_id;
```

| DEPARTMENT_ID | MAX(SALARY) |
| ------------- | ----------- |
| 20            | 13000       |
| 50            | 5800        |
| 60            | 9000        |
| 80            | 11000       |
| 90            | 24000       |
| 110           | 12000       |

<br>

**Example 2**

```sql
select region_id, round(avg(population)) as Population
from wf_countries
group by region_id 
HAVING MIN(population) > 300 000
order by region_id;
```

| REGION_ID | POPULATION  |
| --------- | ----------- |
| 14        | 27 037 687  |
| 17        | 18 729 285  |
| 30        | 193 332 379 |
| 34        | 173 268 273 |

<br>

## Order of keywords

1. `select`
2. `from`
3. `where`
4. `group by`
5. `having`
6. `order by`