# Programming Lab

A collection of practical exercises, sample datasets, and small projects for exploring programming fundamentals. The repository combines Python, SQL, JavaScript, HTML, and a few lower-level examples.

All classroom-style material, records, exercises, and scores in this repository are synthetic demonstration content. No real school, teacher, or student is represented.

## What is here

- **src/lab/** — reusable Python implementations of small algorithms and data structures.
- **examples/** — short runnable examples and programming puzzles.
- **mini_projects/** — command-line applications built from the exercises.
- **web/** — an offline, browser-only assignment board.
- **sql/** — a small normalized SQLite teaching schema and query exercises.
- **data/** — reproducible fixtures for parsing and verification exercises.
- **docs/** — weekly worksheet prompts, scoring rubrics, and reference notes.
- **tests/** — Python standard-library unit tests.

## Running the exercises

Python 3.10 or newer is recommended. No third-party dependencies are needed for the core exercises.

Run tests from the repository root:

    python -m unittest discover -s tests -v

Run a few examples:

    python examples/algorithms.py
    python mini_projects/gradebook/main.py data/scores.csv
    python mini_projects/task_tracker/app.py list

Open web/index.html in a browser to explore a static task board.

## Practice notes

Each section focuses on one concept, with small self-contained inputs and expected outputs. Datasets are fabricated for reproducibility and should not be interpreted as personal or institutional records.

Contributions should include a small test or a documented example showing the intended behavior.
