-- 1
SELECT stu_homeroom, stu_first_name, stu_last_name, stu_gender
FROM students
where stu_grade_level = 1 AND stu_status = 'Active'
ORDER BY stu_homeroom desc, stu_last_name, stu_first_name
;

-- 2
SELECT skl_name, stu_homeroom, stu_first_name, stu_last_name, stu_gender
FROM students
JOIN schools ON stu_skl_id = skl_id
where stu_grade_level = 1 AND stu_status = 'Active'
ORDER BY skl_name, stu_homeroom desc, stu_last_name, stu_first_name
;

-- 3
SELECT count(*)
FROM students
JOIN schools ON skl_id = stu_skl_id
WHERE skl_name = 'Hancock Elementary School'
AND stu_status = 'Active'
AND stu_homeroom = 04
;

-- 4
SELECT tch_first_name, tch_last_name
FROM teachers
JOIN schools ON skl_id = tch_skl_id
WHERE skl_name = 'Hancock Elementary School'
AND tch_homeroom = 04
;

-- 5
SELECT stu_counselor, stu_grade_level, stu_first_name, stu_last_name
FROM students
JOIN schools ON stu_skl_id = skl_id
WHERE skl_name = 'Washington High School'
AND stu_status = 'Active'
AND stu_counselor IN ('McDonnell, Kristen','Giordano, Laura')
ORDER BY stu_counselor, stu_grade_level, stu_last_name, stu_first_name
;

-- 6
SELECT trn_school_year, trn_course, trn_final,trn_credit
FROM transcripts 
JOIN students ON stu_id = trn_stu_id
WHERE stu_first_name = 'Grace'
AND stu_last_name = 'Brewer'
AND trn_school_year >= 2016
ORDER BY trn_school_year, trn_course
;

-- 7 
SELECT cls_course, cls_section, cls_meeting_times, cls_room
FROM classes
JOIN teachers ON cls_tch_id = tch_id
WHERE tch_first_name = 'Catherine'
AND tch_last_name = 'Bennett'
AND cls_course != 'DST'
ORDER BY cls_meeting_times
;

-- Bonus
SELECT cls_course, cls_section, stu_first_name, stu_last_name
FROM classes
JOIN schedules ON ssc_stu_id = cls_id
JOIN students ON ssc_stu_id = stu_id
JOIN teachers ON cls_tch_id = tch_id
WHERE tch_first_name = 'Catherine'
AND tch_last_name = 'Bennett'
AND cls_course <> 'DST'
ORDER BY cls_course, cls_section, stu_first_name, stu_last_name
;

SELECT *
from teachers
where tch_first_name = 'Catherine'
and tch_last_name = 'Bennett'
;
 
 update teachers
 set tch_last_name = 'Polk'
 where tch_last_name = 'Bennett'
 and tch_first_name = 'Catherine'
 ;
 
 select * 
 from schools
 
 ;
 
 update schools
 set skl_level = 'k-4'
 where skl_level = 'Elementary'
 ;
 
 
