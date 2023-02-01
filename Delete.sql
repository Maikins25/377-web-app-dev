select *
from students
where stu_first_name = 'Matthew'
;

SELECT *
FROM students
where stu_id = 'STD0000003QhS1'
;

delete
from students
where stu_id = 'STD0000003QhS1'
;

select *
from attendance
where att_stu_id = 'STD0000003QhS1'
;


delete 
from attendance
where att_stu_id = 'STD0000003QhS1'
;

select * 
from attendance
where att_stu_id = 'stdX2000001008'
;
delete
from attendance
where att_stu_id = 'stdX2000001008'
;

select * 
from transcripts
where trn_stu_id = 'stdX2000001008'
;

delete
from transcripts
where trn_stu_id = 'stdX2000001008'
;

select *
from schedules
where ssc_stu_id = 'stdX2000001008'
;

-- searching for orphans to eliminate

select *
from attendance 
join students
where stu_id <> att_stu_id
;


select * 
from students 
join attendance on stu_id = att_stu_id
where stu_last_name like 'Le%'
and stu_grade_level = '12'
;

select stu_id, stu_first_name, stu_last_name, count(*)
from students 
join attendance on stu_id = att_stu_id
where stu_last_name like 'Le%'
and stu_grade_level = '12'
group by stu_id, stu_first_name, stu_last_name
;


select stu_id, stu_first_name, stu_last_name, count(*)
from students 
left outer join attendance on stu_id = att_stu_id
where stu_last_name like 'Le%'
and stu_grade_level = '12'
group by stu_id, stu_first_name, stu_last_name
;

select stu_id, stu_first_name, stu_last_name
from students 
left outer join attendance on stu_id = att_stu_id
where stu_last_name like 'Le%'
and stu_grade_level = '12'
and att_stu_id is null
;

select *
from attendance
left outer join students on stu_id = att_stu_id
where stu_id is null

;

delete 
from students
where stu_last_name like 'Z%'
;

-- query should work but it takes too long to execute
delete attendance
from attendance
left outer join students on stu_id = att_stu_id
where stu_id is null
;

select * 
from students 
where stu_grade_level in ('01','02')
;

-- In operator from subselect

select * 
from students
where stu_skl_id IN (select skl_id from schools where skl_name like '%Elementary%')
;


select * 
from students
where stu_skl_id NOT IN (select skl_id from schools where skl_name like '%Elementary%')
;

select *
from attendance
where att_stu_id not in (select stu_id from students)

;

delete
from attendance
where att_stu_id not in (select stu_id from students)

;


