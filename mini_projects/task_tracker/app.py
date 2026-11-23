#!/usr/bin/env python3
"""In-memory task manager; data resets after every invocation."""
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple task list exercise")
    parser.add_argument("action", choices=["list", "add", "complete"])
    parser.add_argument("task", nargs="?", default="")
    args = parser.parse_args()
    tasks = [
        {"title": "Read worksheet 02", "done": True},
        {"title": "Implement queue", "done": False},
        {"title": "Write two unit tests", "done": False},
    ]
    if args.action == "add":
        if not args.task:
            parser.error("add requires a task title")
        tasks.append({"title": args.task, "done": False})
    elif args.action == "complete":
        if not args.task:
            parser.error("complete requires a task title")
        for task in tasks:
            if task["title"] == args.task:
                task["done"] = True
    for task in tasks:
        mark = "x" if task["done"] else " "
        print(f"[{mark}] {task['title']}")


if __name__ == "__main__":
    main()
