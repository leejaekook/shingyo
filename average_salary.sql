select
d.dept_name,
avg(s.salary) as average_salary
from salaries s
join dept_emp de
on s.emp_no = de.emp_no
join departments d
on de.dept_no = d.dept_no
where s.to_date='9999-01-01'
and de.to_date = '9999-01-01'
group by d.dept_name
order by average_salary desc;
