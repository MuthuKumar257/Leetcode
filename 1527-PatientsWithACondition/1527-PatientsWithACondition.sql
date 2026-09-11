-- Last updated: 9/11/2026, 9:33:34 AM
# Write your MySQL query statement below

select patient_id,patient_name,conditions from Patients
where conditions like 'DIAB1%'  or  conditions like '% DIAB1%' ;