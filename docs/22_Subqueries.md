# Subqueries

- used to find information you don’t know yet
- executes before the main query / outer query
- a `select` embedded in a clause of another `select`

<br>

**Can be placed in:**

- `from` clause
- `where` clause
- `having` clause

<br>

## Guidelines

- A subquery is enclosed in parentheses.
- A subqueries cannot have its own `order by` clause.
- A subquery is placed on the right side of the condition
- The outer and inner queries can get data from different tables.
- Limit on the number of subqueries depends on the buffer size.

<br>

*Example: Find out all the employees hired after Mr. Vargas*

```sql
select first_name, last_name, hire_date
from employees
where hire_date > (select hire_date from employees where last_name = 'Vargas'
```

<br>

### Subquery and NULL

- If a subquery returns a null value, the outer query takes that result.
- If used in a `where` clause, the outer query will then return no rows.

<br>

**Remember!** <br>
Comparing any value with a null always yields a null.