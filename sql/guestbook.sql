-- scheme
desc guestbook;

-- insert
insert into guestbook values(null, '안대혁', '1234', 'ㅎㅇ!!', now());

-- select 
select no,
	   name,
       message,
       date_format(reg_date, '%Y-%m-%d %p %h:%i:%s') as reg_date
  from guestbook
order by reg_date desc;

-- delete
delete 
 from guestbook
where no = 2
	and password = '1234';