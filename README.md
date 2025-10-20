# Word Break Problem using Dynamic Programming and Trie

## Authors
Agaman Banerjee  
Nirjhar Laskar

---

## Abstract
This project provides an efficient algorithmic solution to the **Word Break Problem**, a classical problem in computer science that determines whether a given string can be segmented into valid English words.  
The solution combines two core algorithmic techniques:  
1. **Dynamic Programming (DP)** – to efficiently manage overlapping subproblems in segmentation, and  
2. **Trie Data Structure** – to perform fast dictionary lookups for substring validation.

The implementation is written in **Python** and includes memory and runtime analysis to evaluate the efficiency of the approach. The project was developed as part of the **Design and Analysis of Algorithms (DAA)** coursework.

---

## Introduction
The Word Break Problem is an important problem in natural language processing and algorithm design.  
Given a non-empty string `s` and a dictionary of valid words, the task is to determine if `s` can be segmented into one or more dictionary words.

For example:
- Input: `iloveindia`  
- Output: `Yes, the string can be segmented into meaningful words.`  
  (because "i", "love", and "india" are valid words)

The project uses a combination of **Trie-based dictionary lookup** and **Dynamic Programming** to optimize both time and space performance.

---

## Problem Statement
Given a string `s` and a dictionary `D` containing valid words, determine whether `s` can be segmented into a sequence of one or more dictionary words.

Formally:
Input: s = "leetcode", D = {"leet", "code"}
Output: True
Explanation: s can be segmented as "leet code".


---

## Objectives
1. To implement an efficient solution for the Word Break Problem using Dynamic Programming.  
2. To construct and use a Trie-based dictionary for fast word lookups.  
3. To evaluate time and memory performance using profiling tools.  
4. To demonstrate the practical application of algorithmic design principles.

---

## Algorithm Overview

### 1. Trie Construction
A **Trie (prefix tree)** is used to store the dictionary words. Each node in the Trie represents a character and contains:
- A dictionary of child nodes.
- A flag indicating whether a word ends at that node.

This structure allows quick lookup for any prefix or complete word in **O(L)** time, where **L** is the word length.

### 2. Dynamic Programming Approach
The Dynamic Programming algorithm determines if the string `s` can be segmented as follows:

Let `dp[i] = True` if the substring `s[0:i]` can be segmented into valid words.

Recurrence relation:

dp[i] = True if there exists j < i such that dp[j] == True and s[j:i] is in dictionary.


The final answer is `dp[len(s)]`.

### 3. Integration
- The Trie is built from `words_alpha.txt`, a large English dictionary file.
- The DP algorithm checks all substrings (up to a small fixed length window) using the Trie for word validation.
- Memory and execution time are recorded using `tracemalloc` and `time.perf_counter()`.

---

## Project Structure

### 1. `new_project.py`
This is the main Python program file that implements the complete algorithm.

#### a) Trie Implementation
- Defines `TrieNode` and `Trie` classes.
- Supports insertion (`insert()`) and word lookup (`search()`).
- Inserts both common words and all words from the dictionary file.

#### b) Dictionary Loading
- Loads `words_alpha.txt` file line by line.
- Inserts words longer than two characters into the Trie.
- Measures memory usage and dictionary construction time.

#### c) Dynamic Programming Segmentation
- Takes a string as input from the user.
- Uses a DP array to check for valid segmentations.
- Each substring is checked against the Trie.
- Reports whether the string can be segmented successfully.

#### d) Performance Analysis
- Displays:
  - Current memory usage
  - Peak memory usage
  - Time to build the dictionary
  - Time to perform segmentation

#### e) Output
Displays clear results in the terminal:

Yes, the string can be segmented into meaningful words.
or
No, the string cannot be segmented into meaningful words.


---

### 2. `words_alpha.txt`
This is the dictionary dataset used to build the Trie. It is a text file containing English words, one per line.

#### Dataset Details
- Approximately 370,000 English words.
- All words are in lowercase.
- Example entries:

a
abandon
ability
about
above
abroad
absence
absolute
accept
access
accident
...


#### Purpose
This dataset acts as the vocabulary base for validating substrings during segmentation.  
It ensures the algorithm can identify a large range of English words, enhancing accuracy.

---

## How the Components Work Together
1. The `words_alpha.txt` dataset is read into the Trie.  
2. The Trie enables quick substring validation during DP computation.  
3. The DP algorithm iteratively checks whether each prefix of the input string can form valid words.  
4. Profiling tools track performance metrics.  
5. The program outputs the segmentation result and runtime statistics.

---

## Time and Space Complexity

| Component | Operation | Complexity |
|------------|------------|-------------|
| Trie Insertion | Insert all words from dataset | O(T), where T = total characters in dataset |
| Trie Search | Lookup for a word | O(L), where L = length of the word |
| DP Computation | Segmentation of input string | O(n²), where n = length of input |
| Space | Memory for Trie and DP array | O(T + n) |

---

## Example Workflow

**Input:**  
iloveindia


**Process:**  
- Trie lookup confirms "i", "love", and "india" exist.  
- Dynamic Programming finds a valid segmentation path.

**Output:**  
Yes, the string can be segmented into meaningful words.

**Performance Output Example:**

Current memory usage: 52.38 MB
Peak memory usage: 89.45 MB
Dictionary build time: 1.7541 seconds
Word segmentation time: 0.0041 seconds


---

## Technologies Used
- **Python 3**
- `time` — for runtime measurement  
- `tracemalloc` — for memory profiling  
- `array` — for efficient dynamic programming array storage  
- **Dataset:** `words_alpha.txt` (English word list)

---

## Experimental Results and Observations
- The Trie-based approach significantly reduces word lookup time compared to simple list-based search.  
- Memory usage grows linearly with the number of words loaded.  
- The DP algorithm efficiently handles input strings up to hundreds of characters.  
- Average segmentation time remains under a few milliseconds for short input strings.  
- The method demonstrates scalability and practicality for real dictionary sizes.

---

## How to Run the Project

### Requirements
- Python 3.x installed on your system
- `words_alpha.txt` file placed in the same directory as `new_project.py`

### Steps
1. Download both files into the same folder.  
2. Open a terminal or command prompt in that folder.  
3. Run the program using:
   ```bash
   python new_project.py
4. When prompted, enter any string (for example: iloveindia).
5. View the segmentation result and performance metrics printed on screen.

## Limitations

1. The program currently assumes the dictionary file fits in system memory; optimization may be required for extremely large datasets.
2. It limits substring checking to the previous 30 characters for performance reasons — configurable for accuracy vs. speed trade-off.

## Conclusion

This project successfully implements an efficient and optimized solution for the Word Break Problem using Dynamic Programming and Trie data structures. It demonstrates key algorithmic design principles, including recursion optimization, data structure choice, and space-time trade-offs. The integration of profiling tools adds analytical depth to performance evaluation, making it a strong submission for the Design and Analysis of Algorithms (DAA) course.

## References

1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. Introduction to Algorithms (MIT Press).
2. GeeksforGeeks, "Word Break Problem using Dynamic Programming."
3. Python Documentation – time and tracemalloc modules.
4. GitHub Repository: dwyl/english-words – Source of words_alpha.txt.


