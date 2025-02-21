### URI

- is basically the path to your data
- can't be airflow itself
- it is case sesitive
- has to be ascii compliant

### Subdags and Grouping dags

- to group dags, the arguments must be the same between subdags and parent dags.
- special notation with a `.`

```python
f"{parent_dag_id}.{child_dag_id}"
```

### General

- Deploying airflow through docker requires you to configure it not from theconf file but instead from the docker-compose file inside the environment variablaes there.
-
