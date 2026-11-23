INSERT INTO courses(course_id,title,hours_per_week) VALUES
  (1,'Programming fundamentals',5),
  (2,'Database basics',3),
  (3,'Web development',4);

INSERT INTO assignments(assignment_id,course_id,title,max_points) VALUES
  (11,1,'Loops and functions',100),
  (12,1,'Collections',100),
  (21,2,'Simple joins',50),
  (31,3,'Semantic HTML',50);

INSERT INTO submissions(assignment_id,sample_id,points) VALUES
  (11,'demo-001',88),
  (11,'demo-002',72),
  (12,'demo-001',91),
  (12,'demo-002',78),
  (21,'demo-001',42);
