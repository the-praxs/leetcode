# [LeetCode](https://leetcode.com/problemset/all/)

![Language](https://img.shields.io/badge/language-Python-orange.svg) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE.md) ![Update](https://img.shields.io/badge/update-weekly-green.svg)
[![LeetCode user the-praxs](https://img.shields.io/badge/dynamic/json?style=flat-square&labelColor=black&color=%23ffa116&label=Solved&query=solvedOverTotal&url=https%3A%2F%2Fleetcode-badge.vercel.app%2Fapi%2Fusers%2Fthe-praxs&logo=leetcode&logoColor=yellow)](https://leetcode.com/the-praxs/) ![](https://badges.peiyuan.ch/leetcode/the-praxs/submission?accepted=true&difficulty=all) ![](https://badges.peiyuan.ch/leetcode/the-praxs/submission?accepted=true&difficulty=easy) ![](https://badges.peiyuan.ch/leetcode/the-praxs/submission?accepted=true&difficulty=medium) ![](https://badges.peiyuan.ch/leetcode/the-praxs/submission?accepted=true&difficulty=hard)

* Solution to all the problems as listed on [Grind 169](https://www.techinterviewhandbook.org/grind75?order=all_rounded&weeks=6&hours=25&grouping=topics).
* "🔒" means [LeetCode premium membership](https://leetcode.com/subscribe/) is required for reading the question.

## Algorithms

* [Array](https://github.com/the-praxs/leetcode#array)
* [Binary Search](https://github.com/the-praxs/leetcode#binary-search)
* [Binary Search Tree](https://github.com/the-praxs/leetcode#binary-search-tree)
* [Binary Tree](https://github.com/the-praxs/leetcode#binary-tree)
* [Dynamic Programming]([https://](https://github.com/the-praxs/leetcode#dynamic-programming))
* [Graph](https://github.com/the-praxs/leetcode#graph)
* [Linked List](https://github.com/the-praxs/leetcode#linked-list)
* [Stack](https://github.com/the-praxs/leetcode#stack)
* [String](https://github.com/the-praxs/leetcode#string)

## Reference

* C++
    * [STL Time Complexity (Detailed)](http://www.cplusplus.com/reference/stl/)
    * [STL Time Complexity (Summary)](http://john-ahlgren.blogspot.com/2013/10/stl-container-performance.html)
    * [Data Structure and Algorithms Cheat Sheet](https://github.com/gibsjose/cpp-cheat-sheet/blob/master/Data%20Structures%20and%20Algorithms.md)
* Python
    * [Time Complexity](https://wiki.python.org/moin/TimeComplexity)
* Algorithms
    * [Rosetta Code](https://rosettacode.org)
    * [CP-Algorithms](https://cp-algorithms.com)
    * [KACTL](https://github.com/kth-competitive-programming/kactl)
    * [Codeforces](https://codeforces.com/)
* Math
    * [Stack Exchange](https://math.stackexchange.com)     
* Visualization
    * [VisuAlgo](https://visualgo.net/en)
    * [Data Structure Visualizations](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html)
    * [Algorithm Visualizer](https://algorithm-visualizer.org/)
 * Handy Table
    * [Thinking Techniques](https://sites.google.com/site/mostafasibrahim/programming-competitions/thinking-techniques) as follows:

| n | Complexity | Possible Algorithms & Techniques |
| - | - | - |
| 10<sup>18</sup>+ | _O(1)_ | Math |
| 10<sup>18</sup> | _O(logn)_ | Binary & Ternary Search / Matrix Power / Cycle Tricks / Big Simulation Steps / Values Reranking / Math |
| 10<sup>16</sup> | _O(n<sup>1/2</sup>)_ | Math |
| 10<sup>8</sup> | _O(n)_ | Greedy / Ad-hoc / DP |
| 4×10<sup>7</sup> | _O(nlogn)_ | Linear # Calls to Binary & Ternary Search / Pre-processing & Querying / Divide and Conquer |
| 10<sup>4</sup> | _O(n<sup>2</sup>)_ | Ad-hoc / DP / Greedy / Divide and Conquer / Branch and Bound |
| 500 | _O(n<sup>3</sup>)_ | Ad-hoc / DP / Greedy / Divide and Conquer / Branch and Bound  |
| 90 | _O(n<sup>4</sup>)_ | Ad-hoc / DP / Greedy / Divide and Conquer / Branch and Bound |
| 50 | _O(n<sup>5</sup>)_ | Branch and Bound |
| 40 | _O(n×2<sup>n/2</sup>)_ | 	Meet in the Middle |
| 20 | _O(n×2<sup>n</sup>)_ | Backtracking / Generating 2<sup>n</sup> Subsets / Bitmask Technique |
| 11 | _O(n!)_ | Factorial / Permutation / Combination Algorithm |

## Array
| #   | Title | Solution | Time | Space | Difficulty | Note |
| --- | ----- | -------- | ---- | ----- | ---------- | --- |
|1    |[Two Sum](https://leetcode.com/problems/two-sum/)       | [Python](./Python/1-two-sum.py)         |__O(n)__      |__O(n)__       |Easy | Use HashMap as {array value: array index}. |
|121  | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | [Python](./Python/121-best-time-to-buy-and-sell-stock.py) | __O(n)__ | __O(1)__ | Easy | Use two variables to keep track of the minimum buy and sell price. |
|57  | [Insert Interval](https://leetcode.com/problems/insert-interval/) | [Python](./Python/57-insert-interval.py) | __O(n)__ | __O(n)__ | Medium | Check new interval before every interval then update new interval.|
|15  | [3Sum](https://leetcode.com/problems/3sum/) | [Python](./Python/15-3sum.py) | __O(n^2)__ | __O(1)__ | Medium | Sort the array and use one number as target then solve as [Two Sum](https://leetcode.com/problems/two-sum/)/[Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) problem. |
|238  | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | [Python](./Python/238-product-of-array-except-self.py) | __O(n)__ | __O(1)__ | Medium | Use prefix and postfix to save product of previous numbers and product of previous numbers from right, respectively |

<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>

## Binary Search
| #   | Title | Solution | Time | Space | Difficulty | Note |
| --- | ----- | -------- | ---- | ----- | ---------- | --- |
|704  | [Binary Search](https://leetcode.com/problems/binary-search/) | [Python](./Python/704-binary-search.py) | __O(logn)__ | __O(1)__ | Easy | Use left and right pointers to keep track of middle point. |

<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>

## Binary Search Tree
| #   | Title | Solution | Time | Space | Difficulty | Note |
| --- | ----- | -------- | ---- | ----- | ---------- | --- |
|235  | [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | [Python](./Python/110-balanced-binary-tree.py) | __O(logn)__ | __O(1)__ | Medium |   |

<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>

## Binary Tree
| #   | Title | Solution | Time | Space | Difficulty | Note |
| --- | ----- | -------- | ---- | ----- | ---------- | --- |
|226  |[Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | [Python](./Python/226-invert-binary-tree.py) |__O(n)__ |__O(n)__ | Easy | Use BFS to traverse the tree. |

<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>

## Dynamic Programming
| #   | Title | Solution | Time | Space | Difficulty | Note |
| --- | ----- | -------- | ---- | ----- | ---------- | --- |
|53  | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | [Python](./Python/53-maximum-subarray.py) | __O(n)__ | __O(1)__ | Easy | Use two variables to keep track of the maximum subarray sum and the current subarray sum. |

<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>

## Graph
| #   | Title | Solution | Time | Space | Difficulty | Note |
| --- | ----- | -------- | ---- | ----- | ---------- | --- |
|733  | [Flood Fill](https://leetcode.com/problems/flood-fill/) | [Python](./Python/733-flood-fill.py) | __O(n)__ | __O(n)__ | Easy | Use DFS to traverse the image. |

<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>

## Linked List
| #   | Title | Solution | Time | Space | Difficulty | Note |
| --- | ----- | -------- | ---- | ----- | ---------- | --- |
|21   | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | [Python](./Python/21-merge-two-sorted-lists.py) | __O(n+m)__ | __O(1)__ | Easy | Use extra ListNode to work the problem. |

<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>

## Stack
| #   | Title | Solution | Time | Space | Difficulty | Note |
| --- | ----- | -------- | ---- | ----- | ---------- | --- |
|20 |[Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) |[Python](./Python/20-valid-parentheses.py) |__O(n)__ |__O(n)__ |Easy |Use Stack and HashMap to check bracket order |

<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>

## String
| #   | Title | Solution | Time | Space | Difficulty | Note |
| --- | ----- | -------- | ---- | ----- | ---------- | --- |
|5    |[Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | [Python](./Python/5-valid-palindrome.py) |__O(n)__ |__O(1)__ | Easy | Use two pointers to check characters on each side. |
|242  |[Valid Anagram](https://leetcode.com/problems/valid-anagram/) | [Python](./Python/242-valid-anagram.py) |__O(n)__ |__O(1)__ | Easy | Use HashMap to count characters. |

<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>