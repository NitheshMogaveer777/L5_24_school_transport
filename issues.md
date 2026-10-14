# Static Code Analysis Issues

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| SQL injection risk | Security | 9 | SQL query uses an f-string to insert student data directly. | Use parameterized SQL queries with placeholders. |
| Unsafe shell execution | Security | 24 | `subprocess.run()` uses `shell=True`. | Remove shell execution and print the dispatch message directly. |
| Bare exception | Bug / Quality | 30 | A bare `except:` catches all exceptions. | Remove the unnecessary handler or catch a specific exception. |
| File handling | Quality | 18–21 | File is opened and closed manually without specifying encoding. | Use `with open(path, "w", encoding="utf-8")`. |
| Function naming | Style | 8, 13, 17, 23, 27 | Function names use camelCase instead of snake_case. | Rename functions using lowercase words separated by underscores. |
| Unused argument | Quality | 13 | The `driver` argument is not used. | Remove the argument if it is not required. |
| Missing docstrings | Quality | Multiple | Functions do not explain their purpose. | Add short docstrings to functions. |