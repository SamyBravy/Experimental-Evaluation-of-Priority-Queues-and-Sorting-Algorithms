# 🧪 Experimental Evaluation of Algorithms

![Language](https://img.shields.io/badge/Language-Python%20%7C%20Jupyter-blue)
![Topic](https://img.shields.io/badge/Topic-Algorithms%20%26%20Data%20Structures-green)

## Overview

This repository contains an experimental analysis of fundamental algorithms and data structures, focusing on performance benchmarking and theoretical comparison.

The project is divided into two main studies:
1.  **Priority Queues**: Comparative analysis of three implementations:
    -   **Max Heap**
    -   **Unsorted Linked List**
    -   **Sorted Linked List**
2.  **Sorting Algorithms**: Comparative analysis of Insertion Sort and Bucket Sort.

> 📄 **Note**: A detailed experimental report is available in **[PriorityQueue Relazione.pdf](Priority%20Queues/PriorityQueue%20Relazione.pdf)** (LaTeX source included).

## 📂 Contents

### 1. Priority Queues
Located in `Priority Queues/`.

-   **Implementation**: `PriorityQueue.py` implements:
    -   `MaxHeap` (O(log n) insert/extract)
    -   `UnsortedLinkedList` (O(1) insert, O(n) extract)
    -   `SortedLinkedList` (O(n) insert, O(1) extract)
-   **Benchmarking**: Performance tests for operations like `insert`, `maximum`, `extract_max`, and `increase_key`.
-   **Analysis**: Detailed report available in `PriorityQueue Relazione.pdf`.
-   **Results**: Visualized in `benchmark_*.png` plots.

### 2. Sorting Algorithms
Located in `Sorting Algorithms/`.

-   **Analysis**: `Insertion Sort vs Bucket Sort.ipynb`
-   **Content**: A Jupyter Notebook comparing the time complexity and performance of Insertion Sort (O(n²)) versus Bucket Sort (O(n+k)) under various data distributions.

## 🛠️ Usage

### Prerequisites
-   Python 3.x
-   Jupyter Notebook (for the sorting analysis)
-   Matplotlib (for generating plots)

### Running the Code

**Priority Queues:**
```bash
cd "Priority Queues"
python3 PriorityQueue.py
```

**Sorting Analysis:**
```bash
cd "Sorting Algorithms"
jupyter notebook "Insertion Sort vs Bucket Sort.ipynb"
```

## 📊 Results

The experiments demonstrate the theoretical time complexities in practice:
-   **Priority Queues**: Logarithmic time O(log n) for heap operations.
-   **Sorting**: Bucket Sort outperforms Insertion Sort on uniformly distributed data, achieving linear time O(n) on average.
