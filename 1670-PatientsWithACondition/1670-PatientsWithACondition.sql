-- Last updated: 8/11/2026, 6:37:22 PM
# Write your MySQL query statement below

select patient_id,patient_name,conditions from Patients
where conditions like 'DIAB1%'  or  conditions like '% DIAB1%' ;