# Number

### ROUND

- can be used with both numbers and dates
- arguments: `column`, `decimal_places`

<br>

**More about decimal places:**

- Default: `decimal_places = 0`
- If positive, rounds to right of decimal point
- If negative, rounds to the left of decimal point

```sql
ROUND(45.926) ->  46

ROUND(45.926, 2)  ->  45.93

ROUND(45.926, -1)  ->  50
```

<br>

### TRUNC

- terminates the number at a given point
- can be used with both numbers and dates
- same arguments and properties as `ROUND`

```sql
TRUNC(45.926)  ->  45

TRUNC(45.926, 2)  ->   45.92
```

<br>

### MOD

- finds the remainder after one value is divided by another value

```sql
select country_name, MOD(airports, 2) as "Mod Parity"
from wf_countries;
```