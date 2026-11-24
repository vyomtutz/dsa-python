# dsa-python
# LeetCode Solutions (Python)

My solutions to the [NeetCode 150](https://neetcode.io/roadmap) problem list, written in Python and organized by pattern. I'm a data engineer (PySpark, Kafka, Airflow, Databricks) building up data structures and algorithms alongside machine learning engineering.

Every solution is my own, with a short note on the approach and its complexity, so the reasoning is easy to follow.

## Progress

Last updated: 2026-11-23

| Pattern | Folder | Solved |
|---|---|---|
| Arrays & Hashing | [`arrays-hashing/`](arrays-hashing/) | 1 |
| Two Pointers | [`two-pointers/`](two-pointers/) | 0 |
| Sliding Window | [`sliding-window/`](sliding-window/) | 0 |
| Stack | [`stack/`](stack/) | 0 |
| Binary Search | [`binary-search/`](binary-search/) | 0 |
| Linked List | [`linked-list/`](linked-list/) | 0 |
| Trees | [`trees/`](trees/) | 0 |
| Heap / Priority Queue | [`heap/`](heap/) | 0 |
| Backtracking | [`backtracking/`](backtracking/) | 0 |
| Graphs | [`graphs/`](graphs/) | 0 |
| 1-D Dynamic Programming | [`dp-1d/`](dp-1d/) | 0 |
| 2-D Dynamic Programming | [`dp-2d/`](dp-2d/) | 0 |
| Intervals | [`intervals/`](intervals/) | 0 |
| **Total** | | **0** |



- Folders are named by pattern, following the NeetCode roadmap.
- Files are named `<LeetCode number>-<problem-name>.py`, in lowercase with hyphens, so they sort cleanly.

## Solution format

Each file starts with a short header, then the solution:

```python
"""
1. Two Sum
https://leetcode.com/problems/two-sum/

Pattern: Arrays & Hashing
Approach: Store each number's index in a hash map. For each number, check
          whether (target - number) was already seen.
Time:     O(n)
Space:    O(n)
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index
        for i, n in enumerate(nums):
            if target - n in seen:
                return [seen[target - n], i]
            seen[n] = i
```


