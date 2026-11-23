-- SQLite practice schema; all records are synthetic.
PRAGMA foreign_keys = ON;

CREATE TABLE courses (
  course_id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  hours_per_week INTEGER NOT NULL CHECK (hours_per_week BETWEEN 1 AND 30)
);

CREATE TABLE assignments (
  assignment_id INTEGER PRIMARY KEY,
  course_id INTEGER NOT NULL REFERENCES courses(course_id),
  title TEXT NOT NULL,
  max_points INTEGER NOT NULL CHECK (max_points > 0)
);

CREATE TABLE submissions (
  assignment_id INTEGER NOT NULL REFERENCES assignments(assignment_id),
  sample_id TEXT NOT NULL,
  points INTEGER NOT NULL CHECK (points >= 0),
  PRIMARY KEY (assignment_id, sample_id)
);
