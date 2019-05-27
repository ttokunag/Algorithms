# Algorithms
### Tomoya Tokunaga (mailto: ttokunag@ucsd.edu)

This repository contains all the files about Algorithms which is from very well-known ones such as Binary Search and Merge Sort to ones not so well-known but I think useful through development. I would like you to let me know if there exists some issues or room for implovement on my codes!

## Table of Contents
### `Algorithms Comparison`
This IPython notebook is about the experiment of timing performances of well-known sorting algorithms such as Insertion sort, Heap sort, Merge sort, and Quick sort. I was so curious about why algorithms performances differ even though their Big O notations are the same that I do this experiment.

I timed every algorithm performance and create a dataframe using `pandas` python library, and at the end I visualized the performance difference by plotting the data on a graph. The followings are the actual graphs I've created in the notebook.<br>
<img src="https://github.com/ttokunag/Algorithms/blob/master/Algorithm_Comparison/pictures/runtime_analysis1.png" width="550">

I made analysis from my viewpoint, so I would be happy if you read the notebook if you get interested in by accident. I'm look forward to your feedbacks!

### `graph_algos`
This directory is intended to implement well-know graph algorithms such as path-finding algorithm using Depth-First search and  Breadth-First search, and Dijkstra's algorithm.<br><br>
It also contains IPython notebook which compares algorithms time complexity if an algorithm can be implemented in several ways such as BFS & DFS.

### `Sorting Algorithms`
This directory contains files implements well-known sorting algorithms such as Merge Sort, Quick Sort, Heap sort, and so on.
It's very interesting to see how well each sorting algorithm in terms of time complexity, so I conducted complexity analysis of algorithms whose Big O notation is the same. The notebook is stored in [`Algorithm Comparison`](https://github.com/ttokunag/Algorithms/tree/master/Algorithm_Comparison) directory.

### `Searching Algorithms`
This directory contains files implements well-know sorting algorithms such as Binary search.
