-- Query to identify top IP addresses with suspicious failed login spikes
SELECT 
    source_ip,
    COUNT(event_id) AS total_failed_attempts,
    MIN(timestamp) AS first_attempt,
    MAX(timestamp) AS last_attempt
FROM 
    authentication_logs
WHERE 
    status = 'FAILED'
    AND timestamp >= NOW() - INTERVAL '24 HOURS'
GROUP BY 
    source_ip
HAVING 
    COUNT(event_id) >= 5
ORDER BY 
    total_failed_attempts DESC;
