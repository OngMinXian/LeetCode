# LeetCode
This is a personal repository of LeetCode practice in preparation of job interviews.

## Problems & Solutions
| Title | Solution | Time/Space Complexity | Note |
| ------ | ------ | ------ | ------ |
| Merge Strings Alternatively | Use a for loop to iterate through n where n is shorter len and concatenate the remaining string | O(max(n, m))<br/>O(n+m) | Easy |
| Greatest Common Divisor Of Strings | Check if str1 + str2 == str2 + str1 and finding GCD of lengths | O(n+m)<br/>O(n+m) | Easy |
| Kids With The Greatest Number Of Candies | Find current highest and compare with after adding extra | O(n)<br/>O(n) | Easy |
| Can Place Flowers | Compare i and i+1 position, increment and decrement as required | O(n)<br/>O(1) | Easy |
| Reverse Vowels Of A String | Use pointers for left and right of string and swap if required | O(n)<br/>O(n) | Easy |
| Make Zeros | Use 2 pointers, 1 to keep track of most left zero and 1 to iterate through array | O(n)<br/>O(1) | Easy |
| Is Subsequence | 2 pointers, 1 for each string | O(n)<br/>O(1) | Easy |
| Maximum Average Subarray I | Siding window problem | O(n)<br/>O(1) | Easy |
| Find The Highest Altitude | Simple running sum and max problem | O(n)<br/>O(1) | Easy |
| Find Pivot Index | Use 2 running sums, left and right of index sum | O(n)<br/>O(1) | Easy |
| Find the Difference of Two Arrays | Use Python sets and difference of sets | O(n)<br/>O(n) | Easy |
| Unique Occurrances | Hashmap implementation | O(n)<br/>O(n) | Easy |
| Number of Recent Calls | Use a deque from collections | O(n)<br/>O(n) | Easy |
| Reverse Linked List | Classic reverse linked list problem, use prev curr and next variables with while loop | O(n)<br/>O(1) | Easy |
| Maximum Depth of Binary Tree | Uses DFS and returns the maximum depth reached using max operator | O(n)<br/>O(h) | Easy |
| Leaf-Similar Trees | In order traversal problem using DFS | O(n)<br/>O(h) | Easy |
| Search in a Binary Search Tree | Binary search in a binary tree | O(logn)<br/>O(logh) | Easy |
| Guess Number Higher or Lower | Classic binary search problem using low, high and mid | O(logn)<br/>O(logn) | Easy |
| N-th Tribonacci Number | 3 variable question using a for loop or use recursion with memoization | O(n)<br/>O(1) | Easy |
| Min Cost Climbing Stairs | Minimum cost to reach stair n depends on minimum cost of n-1 and n-2, use 1D dynamic programming | O(n)<br/>O(n) | Easy |
| Count bits | Number of 1s in even number is same as half of the number and +1 for odd number | O(n)<br/>O(n) | Easy |
| Single Number | Use XOR operator on all numbers for constant space, or not use hash table for linear space | O(n)<br/>O(1) | Easy |
| Two Sum | Use a hash table | O(n)<br/>O(1) | Easy |
| Valid Parenthesis | Use a stack | O(n)<br/>O(n) | Easy |
| Merge Two Sorted Lists | Use a dummy and current node and compare values of front of each list | O(n)<br/>O(1) | Easy |
| Best Time To Buy And Sell Stock | Keep track of lowest price and highest profit | O(n)<br/>O(n) | Easy |
| Valid Palindrome | Use 2 pointers for front and back | O(n)<br/>O(1) | Easy |
| Invert Binary Tree | Depth first search while swapping left and right children | O(n)<br/>O(h) | Easy |
| Valid Anagram | Use hash maps to keep count | O(n)<br/>O(n) | Easy |
| Binary Search | Classic binary search algorithm | O(logn)<br/>O(1) | Easy |
| Flood Fill | Use DFS to spread only to same as original color | O(n)<br/>O(1) | Easy |
| Lowest Common Ancestor of a Binary Search Tree | Check if current node is in between given range, else visit left/right | O(logn)<br/>O(1) | Easy |
| Balanced Binary Tree | Compare left and right depth at each node | O(n)<br/>O(n) | Easy |
| Linked List Cycle | Use 2 pointer (slow and fast) to check for cycle | O(n)<br/>O(1) | Easy |
| Implement Queue Using Stacks | Use 1 stack as front and another back. To pop, check if back is empty and reverse front else pop from back stack | NA | Easy |
| First Bad Version | Search using binary search algorithm | O(logn)<br/>O(1) | Easy |
| Ransom Note | Use hash map | O(n)<br/>O(n) | Easy |
| Climbing Stairs | Use 1D DP table | O(n)<br/>O(n) | Easy |
| Longest Palindrome | Use hash map and consider even and odd counts | O(n)<br/>O(n) | Easy |
| Majority Element | Moore voting algorithm | O(n)<br/>O(1) | Easy |
| Add Binary | Add binary position by position using carry over strategy | O(n)<br/>O(n) | Easy |
| Diameter Of A Binary Tree | Diameter of a node is max depth of left side + max depth of right side | O(n)<br/>O(n) | Easy |
| Middle Of The Linked List | Slow and faster pointer approach | O(n)<br/>O(1) | Easy |
| Contains Duplicate | Use hashset/map | O(n)<br/>O(n) | Easy |
| Maximum Subarray | Keep maximum sum up to ith position using DP or 2 variables | O(n)<br/>O(1) | Medium |
| Insert Interval | Check if new interval lies within the other intervals and maintain left and right intervals to it | O(n)<br/>O(n) | Medium |
| 01 Matrix | Multiple source BFS | O(mn)<br/>O(mn) | Medium |
| K Closest Points To Origin | Quick select > min/max heap > sorting | O(n)<br/>O(n) | Medium |
| Longest Substring Without Repeating Characters | Use dictionary to maintain last seen index and use a sliding window of left and right | O(n)<br/>O(n) | Medium |
| 3 Sum | Use a positive/negative hash counter and zero counter and consider 2 positives 1 negative / 2 negatives 1 postive | O(n^2)<br/>O(n) | Medium |
| Binary Tree Level Order Traversal | BFS problem | O(n)<br/>O(n) | Medium |
| Clone Graph | BFS problem | O(n)<br/>O(n) | Medium |
| Evaluate Reverse Polish Notation | Use stack and pop 2 numbers when meet operator | O(n)<br/>O(n) | Medium |
| Course Schedule | Topological sort to check if cycle exist and every vertice is visited | O(V+E)<br/>O(V+E) | Medium |
| Implement Trie (Prefix Tree) | Use a tree structure where each node is a character | NA | Medium |
| Coin Change | Dynamic programming and math.inf | O(n)<br/>O(n) | Medium |
| Product Of Array Except Self | Maintain a left and right product and iterate through array twice or use 2 pointers | O(n)<br/>O(n) | Medium |
| Min Stack | Use 1 stack for normal stack another stack to maintain minimum at each push/pop | NA | Medium |
| Validate Binary Search Tree | DFS returning lower and upper bounds or use in order traversal | O(n)<br/>O(h) | Medium |
| Number Of Islands | Multi-source BFS | O(nm)<br/>O(nm) | Medium |
| Rotting Oranges | Multi-source BFS while keeping count of iterations | O(nm)<br/>O(nm) | Medium |
| Search In Rotated Sorted Array | Binary search and consider which half is sorted | O(logn)<br/>O(1) | Medium |
| Combination Sum | DFS/Backtracking algorithm | O(n^c)<br/>O(target/c) | Medium |
| Permutations | Combinatorial search problem using DFS/Backtracking algorithm | O(n!)<br/>O(n!) | Medium |
| Merge Intervals | Sort first before merging and check which end is bigger using max | O(nlogn)<br/>O(n) | Medium |
| Lowest Common Ancestor Of A Binary Tree | DFS to required nodes and return the nodes/none until LCA | O(n)<br/>O(h) | Medium |
| Time Based Key-Value Store | Use binary search as timestamps are strictly increasing and hash maps | O(logn)<br/>O(n) | Medium |
| Sort Colors | Use a 3 pointer approach (partition between 0, 1 and 2 and a current index) | O(n)<br/>O(1) | Medium |
| Word Break | Dynamic programming to check each possible substring | O(nm)<br/>O(n) | Medium |
| Partition Equal Subset Sum | Dynamic programming in knapsack problem | O(nw)<br/>O(w) | Medium |
| String to Integer (atoi) | Consider numerous edge cases | O(n)<br/>O(n) | Medium |
| Spiral Matrix | While loop to keep spiraling till solved | O(n)<br/>O(n) | Medium |
| Subsets | DFS approach to visit all possible subsets | O(n!)<br/>O(n!) | Medium |
| Binary Tree Right Side View | BFS with in order traversal | O(n)<br/>O(n) | Medium |
| Longest Palindromic Substring | Expand around center considering odd and even palindromes | O(n^2)<br/>O(1) | Medium |
| Unique Paths | DP solution | O(mn)<br/>O(mn) | Medium |
| Construct Binary Tree From Preorder and Inorder Traversal | Use a dictionary to index inorder and recursively build tree by popping left from preorder array and separating inorder array | O(n)<br/>O(h) | Medium |
| Container with Most Water | 2 pointer approach to constantly update the lower height | O(n)<br/>O(1) | Medium |
| Letter Combinations Of A Phone Number | Backtracking approach | O(4^n)<br/>O(n) | Medium |
