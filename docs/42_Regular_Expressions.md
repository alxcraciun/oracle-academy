# Regular Expressions

- simple and complex patterns for searching and manipulating
- In Oracle, they are an extension of the POSIX
- Can be used on CHAR, CLOB, VARCHAR2
- based on the use of meta characters

<br>

## Meta Characters

Characters that have a special meaning such as:

- wildcard character
- range of characters
- repeating character
- non-matching character

<br>

| Metacharacter | Property                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| . (dot)       | Matches any character in the supported character set, except NULL         |
| ?             | Matches zero or one occurrence                                            |
| *             | Matches zero or more occurrences                                          |
| +             | Matches one or more occurrences                                           |
| ( )           | Grouping expression, treated as a single sub-expression                   |
| \             | Escape character                                                          |
| \|            | Alternation operator for specifying alternative matches                   |
| ^             | Matches the start-of-line                                                 |
| $             | Matches the end-of-line                                                   |
| [ ]           | Matching list matching any one of the expressions represented in the list |

<br>

**Examples of regular expressions**

- Letter ‘a’ followed by any one character followed by ‘c’  →  `‘a.c’`
- Same expression as standard SQL search  →  `WHERE COLUMN LIKE ‘a_c’`

<br>


| Regular Expression Functions | Usecase                                                                                                                                                                   |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| REGEXP_LIKE                  | Similar to the LIKE operator, but performs regular expression matching instead of simple pattern matching                                                                 |
| REGEXP_REPLACE               | Searches for a regular expression pattern and replaces it with a replacementstring                                                                                        |
| REGEXP_INSTR                 | Searches for a given string for a regular expression pattern and returns the position where the match is found                                                            |
| REGEXP_SUBSTR                | Searches for a regular expression pattern within a given string and returns the matched substring                                                                         |
| REGEXP_COUNT                 | Returns the number of times a pattern appears in a string. Can specify the string, the pattern, the start position and the matching options (e.g. c for case sensitivity) |

<br>

## Function Examples

<br>

**Search employees with first name Stephen or Steven**

```sql
select first_name, last_name
from employees
where REGEXP_LIKE(first_name, '^Ste(v|ph)en$');
```

<br>

**Replace every ‘H’ followed by a vowel wth ‘**’**

```sql
select last_name,
REGEXP_REPLACE(last_name, '^H(a|e|i|o|u)', '**') as "Name changed"
from employees;
```

<br>

| LAST_NAME | Name changed |
| --------- | ------------ |
| Abel      | Abel         |
| Davies    | Davies       |
| ......    | ......       |
| Hartstein | **rtstein    |
| Higgins   | **ggins      |
| ......    | ......       |

<br>

**Count the appearences of subexpression ‘ab’**

```sql
select country_name,
REGEXP_COUNT(country_name, '(ab)') as " Count of 'ab' " 
from wf_countries
where REGEXP_COUNT(country_name, '(ab)') > 0;
```

<br>


| COUNTRY_NAME                                  | Count of ‘ab’ |
| --------------------------------------------- | ------------- |
| Republic of Zimbabwe                          | 1             |
| Arab Republic of Egipt                        | 1             |
| Great Socialist Peoples Libyan Arab Jamahirya | 1             |
| Kingdom of Saudi Arabia                       | 1             |
| Syrian Arab Republic                          | 1             |
| Gabonese Republic                             | 1             |
| United Arab Emirates                          | 1             |

<br>

## Advanced use-cases

*Using Regular Expressions in Check Constraints*

<br>

**Ensure that all emails contain a “@” sign**

```sql
ALTER TABLE employees
ADD CONSTRAINT email_addr_chk
CHECK (REGEXP_LIKE(email, '@'));
```

<br>

**Checking a valid email adress**

```sql
CREATE TABLE my_contacts (
	first_name VARCHAR2(15),
	last_name VARCHAR2(15),
	email VARCHAR2(30)  ***CHECK(REGEXP_LIKE(email, '.+@.+\..+'))***
);
```
*An `@` followed by characters, than a `.` follwed by some characters*

<br>

**Syntax Explanation**

`.+`  —  means one or more characters

`@`    —  an @ symbol

`\.`  —  a dot ( \ used as an escape character)