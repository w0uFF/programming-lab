"""Simple stack and bounded queue implementations for study."""
from collections import deque
from typing import Generic, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("stack is empty")
        return self._items.pop()

    def __len__(self) -> int:
        return len(self._items)


class BoundedQueue(Generic[T]):
    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self._items: deque[T] = deque()

    def enqueue(self, item: T) -> None:
        if len(self._items) >= self.capacity:
            raise OverflowError("queue is full")
        self._items.append(item)

    def dequeue(self) -> T:
        if not self._items:
            raise IndexError("queue is empty")
        return self._items.popleft()
