-- QUERY 1: Calculate the overall no-show rate to establish the baseline metric.
SELECT 
    no_show,
    COUNT(*) as total_appointments,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM appointments), 2) as percentage
FROM appointments
GROUP BY no_show;


-- QUERY 2: Analyze if booking appointments further in advance increases the no-show rate.
SELECT 
    no_show,
    AVG(lead_time_days) as average_days_booked_in_advance
FROM appointments
GROUP BY no_show;


-- QUERY 3: Determine if the time of day impacts patient attendance.
SELECT 
    CASE 
        WHEN appointment_time < '12:00' THEN 'Morning'
        ELSE 'Afternoon'
    END as time_of_day,
    no_show,
    COUNT(*) as count
FROM appointments
GROUP BY time_of_day, no_show
ORDER BY time_of_day;