# Synonyms

- a word or expression that is an acceped substitude for another word
- used to simplify access to objects by creating another name for the object
- especially useful with lengthy object names, such as views

<br>

**How to create a synonym**

```sql
CREATE [PUBLIC] SYNONYM synonym_name
FOR object_name;
```

<br>

How to delete a synonym <br>
`DROP PUBLIC SYNONYM synonym_name;`

<br>

How to check all synonyms <br>
`select * from USER_SYNONYMS;`