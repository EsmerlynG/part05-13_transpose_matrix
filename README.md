# Matrix Transpose Function

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Course](https://img.shields.io/badge/MOOC.fi-Python%20Programming-lightgrey)

A Python function that transposes a square matrix in-place by swapping rows and columns across the diagonal. This solution demonstrates advanced 2D array manipulation, algorithmic optimization, and the critical insight of processing only the upper triangular portion of a matrix.

---

## 📖 Problem Description

Write a function `transpose(matrix: list)` that transposes a square matrix in-place. Transposing flips the matrix over its diagonal - columns become rows and rows become columns.

### Requirements
- Transpose a square matrix (equal rows and columns)
- Modify the matrix directly (no return value)
- Swap elements across the main diagonal
- Handle any n×n square matrix

### Example Transformation
**Original Matrix:**
```
1 2 3
4 5 6
7 8 9
```

**Transposed Matrix:**
```
1 4 7
2 5 8
3 6 9
```

---

## 💻 Code Implementation

```python
def print_matrix(matrix: list):
    for r in matrix:
        for num in r:
            print(f"{num} ", end="")
        print()

def transpose(matrix: list):
    length_of_matrix = len(matrix)
    for row in range(length_of_matrix):
        for column in range(row, length_of_matrix):
            
            number = matrix[row][column]
            matrix[row][column] = matrix[column][row]
            matrix[column][row] = number

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print_matrix(matrix)
    transpose(matrix)
    print()
    print_matrix(matrix)
```

**Output:**
```
1 2 3 
4 5 6 
7 8 9 

1 4 7 
2 5 8 
3 6 9 
```

---

## 🧠 Algorithm Explanation

### **The Upper Triangle Strategy**
```python
for row in range(length_of_matrix):
    for column in range(row, length_of_matrix):  # Start from 'row', not 0
        # Swap matrix[row][column] with matrix[column][row]
```

**Key Insight**: Only process the upper triangular portion of the matrix to avoid double-swapping!

1. **Outer Loop**: Iterate through each row
2. **Inner Loop**: Start from current row index (not 0) to avoid revisiting swapped pairs
3. **Swap Elements**: Exchange `matrix[row][column]` with `matrix[column][row]`
4. **Diagonal Elements**: Elements on the diagonal swap with themselves (no effect)

**Time Complexity:** O(n²/2) ≈ O(n²) - Process roughly half the matrix elements  
**Space Complexity:** O(1) - In-place swapping with only temporary variable

---

## 🛠 How to Run

Clone the repo and run:

```bash
python3 matrix_transpose.py
```

Or import the function in your own code:

```python
from matrix_transpose import transpose, print_matrix

# Create a 4x4 matrix
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

print("Original:")
print_matrix(matrix)

transpose(matrix)

print("\nTransposed:")
print_matrix(matrix)
```

---

## 🧪 Test Cases

```python
# Test case 1: 3x3 matrix
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Original 3x3:")
print_matrix(matrix1)
transpose(matrix1)
print("Transposed 3x3:")
print_matrix(matrix1)

# Test case 2: 2x2 matrix
matrix2 = [[1, 2], [3, 4]]
print("\nOriginal 2x2:")
print_matrix(matrix2)
transpose(matrix2)
print("Transposed 2x2:")
print_matrix(matrix2)

# Test case 3: 1x1 matrix
matrix3 = [[42]]
print("\nOriginal 1x1:")
print_matrix(matrix3)
transpose(matrix3)
print("Transposed 1x1:")
print_matrix(matrix3)

# Test case 4: 4x4 matrix with different values
matrix4 = [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]
print("\nOriginal 4x4:")
print_matrix(matrix4)
transpose(matrix4)
print("Transposed 4x4:")
print_matrix(matrix4)

# Test case 5: Double transpose (should return to original)
matrix5 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
original = [row[:] for row in matrix5]  # Save original
transpose(matrix5)
transpose(matrix5)  # Transpose twice
print("\nAfter double transpose:")
print_matrix(matrix5)
print("Matches original:", matrix5 == original)
```

---

## ✨ Key Learning Highlights

This problem was a masterclass in **algorithmic thinking** and **matrix manipulation optimization**:

### **The Double-Swap Problem**
```python
# WRONG - Visits every position, causing double swaps
for row in range(length_of_matrix):
    for column in range(length_of_matrix):  # Starts from 0 every time
        # When we swap [0][1] with [1][0], 
        # we'll later swap [1][0] back with [0][1]!
```

### **The Upper Triangle Solution**
```python
# CORRECT - Only visit upper triangle
for row in range(length_of_matrix):
    for column in range(row, length_of_matrix):  # Start from current row
        # Each pair is swapped exactly once!
```

### **Visual Understanding**
For a 3×3 matrix, we only process these positions:
```
✓ ✓ ✓    (Row 0: columns 0,1,2)
  ✓ ✓    (Row 1: columns 1,2)
    ✓    (Row 2: column 2)
```

This ensures each off-diagonal pair is swapped exactly once, while diagonal elements are processed but remain unchanged.

---

## 🎯 Design Philosophy

### **Why This Approach?**
1. **Efficiency**: Process only necessary elements (upper triangle)
2. **In-Place Operation**: No additional memory needed for copying
3. **Mathematical Elegance**: Leverages the symmetry of transpose operations
4. **Avoids Edge Cases**: No special handling needed for diagonal elements

### **Clean Code Principles Applied**
- **Clear Variable Names**: `length_of_matrix`, `row`, `column` show intent
- **Minimal Complexity**: Simple nested loops with clear bounds
- **Single Responsibility**: Function does one thing - transpose the matrix

---

## 🔄 Problem-Solving Evolution

### **Initial Naive Approach**
```python
# Attempted simple swap - caused duplicates and overwrites
for row in range(len(matrix)):
    for col in range(len(matrix)):
        # This visits every position and double-swaps!
```

### **Failed Optimization Attempts**
- **Modulo Logic**: Tried using divisibility checks to control swapping
- **Copy and Compare**: Attempted to copy matrix and compare values (overly complex)
- **Various Counter Methods**: Multiple attempts to track visited positions

### **Breakthrough with AI Assistance**
> *"You're visiting every position in the matrix. When you swap [0][1] with [1][0], and then later visit [1][0], you'll swap it back. You need to only visit each pair once. Consider what part of the matrix you should iterate through."*

### **First Working Solution (Counter-Based)**
```python
def transpose(matrix: list):
    count = 0
    for r in range(len(matrix)):
        for n in range(len(matrix[r])):
            if n + count < len(matrix[r]):
                # Swap logic with counter-based bounds
        count += 1
```

### **Final Optimized Solution**
```python
def transpose(matrix: list):
    length_of_matrix = len(matrix)
    for row in range(length_of_matrix):
        for column in range(row, length_of_matrix):
            # Clean range-based upper triangle iteration
```

---

## 🎓 Learning Outcomes

* **Matrix Algorithm Design**: Understanding how to efficiently process 2D arrays
* **Optimization Thinking**: Moving from brute force to mathematically elegant solutions
* **Debugging Complex Logic**: Working through algorithmic mistakes and edge cases
* **Range Function Mastery**: Using `range(start, end)` for controlled iteration
* **In-Place Operations**: Modifying data structures without additional memory
* **Problem Decomposition**: Breaking complex matrix operations into manageable pieces
* **Seeking Help Effectively**: Learning to ask for hints rather than complete solutions

---

## 💡 Developer Reflection

> *"This was a very difficult challenge for me because it really pushed the boundaries of my imagination and my ability to work with matrices. At first, I thought a simple swap would be okay, but I quickly realized that would not work, as it was swapping everything in the matrix and leading to duplicate numerical values.*
> 
> *I kept trying to find a solution in every way I could. I attempted to use modulo to check if numbers divisible by 2 could be subtracted by a certain amount to simulate a swap, but that did not work. I also tried copying the matrix and comparing the values in the designated spots to confirm a proper swap, but that became overly complicated very quickly.*
> 
> *After two hours, I decided to use Claude.ai to assist me by giving vague hints about where I should be looking in my code. The hint was: 'You're visiting every position in the matrix. Think about it: when you swap [0][1] with [1][0], and then later visit [1][0], you'll swap it back with [0][1]. You need to only visit each pair of positions once. Consider what part of the matrix you should iterate through.'*
> 
> *This got me thinking, and I realized I should only be checking the top triangular half of the matrix since I was flipping it over the diagonal axis. My first version used a counter variable, but I wanted to make it more readable and modular. So, instead of using a counter variable, I used the `range` function to search the column from the current row number to the length of the matrix, resulting in a cleaner version of the code.*
> 
> *This was definitely the most challenging problem I have faced so far, as it pushed me to think more deeply about how what I am learning actually functions."*

### **Key Takeaways**
1. **Matrix algorithms require deep thinking** - Simple approaches often fail in subtle ways
2. **Seeking help strategically** - Asking for hints rather than complete solutions promotes learning
3. **Upper triangle insight** - Many matrix operations only need to process half the elements
4. **Code evolution** - Moving from working solutions to cleaner, more readable implementations
5. **Persistence pays off** - Complex problems require multiple attempts and approaches
6. **Mathematical thinking** - Understanding the underlying mathematics improves algorithmic solutions

---

## 📚 Course

This project was completed as part of the **MOOC.fi Python Programming course**.
