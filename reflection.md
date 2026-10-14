# Lab 5: Static Code Analysis — Reflection

## 1. What is static code analysis?

Static code analysis is the process of checking source code without executing the program. It helps identify coding errors, security vulnerabilities, and style problems before the software is used.

## 2. What are the purposes of Pylint, Bandit, and Flake8?

- **Pylint:** Checks code quality, naming conventions, missing docstrings, and unused variables or arguments.
- **Bandit:** Identifies potential security problems in Python code.
- **Flake8:** Checks code formatting, indentation, whitespace, and Python style guidelines.

## 3. What issues did you identify and fix in the program?

I identified several issues in the School Bus Transport Register program. These included SQL injection risks, unsafe shell execution, a bare exception handler, improper file handling, incorrect function naming, and missing docstrings. I fixed these issues by using parameterized SQL queries, removing unnecessary shell execution, improving exception handling, using a file context manager, following naming conventions, and adding docstrings.

## 4. How does static code analysis improve software quality?

Static code analysis improves software quality by identifying potential problems early. It helps developers write secure, readable, maintainable, and reliable code. Using Pylint, Bandit, and Flake8 also helps developers follow coding standards and reduce common programming mistakes.

## Conclusion

In this lab, I learned how to use Pylint, Bandit, and Flake8 to analyze Python code. I understood how to identify and fix code quality, security, and style issues. This practical exercise helped me improve my Python programming skills and understand the importance of static code analysis.