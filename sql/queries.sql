-- Query A: assignments and the corresponding course.
SELECT a.title AS assignment, c.title AS course
FROM assignments AS a
JOIN courses AS c ON a.course_id=c.course_id
ORDER BY c.title, a.title;

-- Query B: average observed score per assignment.
SELECT a.title, COUNT(s.sample_id) AS submissions,
       ROUND(AVG(s.points), 1) AS average_points
FROM assignments AS a
LEFT JOIN submissions AS s ON s.assignment_id=a.assignment_id
GROUP BY a.assignment_id, a.title
ORDER BY a.assignment_id;

-- Query C: assignments without any submissions.
SELECT a.title
FROM assignments AS a
LEFT JOIN submissions AS s ON s.assignment_id=a.assignment_id
WHERE s.assignment_id IS NULL;
