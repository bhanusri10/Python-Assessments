--Creatiing Table called employee

create table employee (
    id int,
    name varchar(10),
    salary int,
    department varchar(20)
);

--Inserting values into the created table

insert into employee (id, name, salary, department) values
(1, 'a', 10, 'IT'),
(2, 'b', 20, 'HR'),
(3, 'c', 30, 'Finance'),
(4, 'd', 40, 'IT'),
(5, 'e', 50, 'HR'),
(6, 'f', 60, 'Marketing');

-- 1. give me the departments having employees more than HR department count.

SELECT department
FROM employee
GROUP BY department
HAVING COUNT(*) > (
    SELECT COUNT(*)
    FROM employee
    WHERE department = 'HR'
);

-- 2. Find  Departments whose salary is more than 25.

SELECT DISTINCT department
FROM employee
WHERE salary > 25;

-- 3. give me all employees who are having highest salary in a company.

SELECT *
FROM employee
WHERE salary = (SELECT MAX(salary) FROM employee);

-- 4. employees who are having salary more than average salary of their department.

SELECT e1.* 
FROM employee e1 
WHERE e1.salary > (
    SELECT AVG(e2.salary) 
    FROM employee e2 
    WHERE e2.department = e1.department
);

-- 5. employees who earn same salary as others.

SELECT *
FROM employee
WHERE salary IN (
    SELECT salary
    FROM employee
    GROUP BY salary
    HAVING COUNT(*) > 1
);

-- 6. list of employees from departments with more than 2 employees.

SELECT *
FROM employee
WHERE department IN (
    SELECT department
    FROM employee
    GROUP BY department
    HAVING COUNT(*) > 2
);

-- 7. find the second highest salary from employee table.

SELECT DISTINCT salary
FROM employee
ORDER BY salary DESC
LIMIT 1 OFFSET 1;

-- 8. find the departmetns where total slaary > total salary of IT department.

SELECT department
FROM employee
GROUP BY department
HAVING SUM(salary) > (
    SELECT SUM(salary)
    FROM employee
    WHERE department = 'IT'
);








 