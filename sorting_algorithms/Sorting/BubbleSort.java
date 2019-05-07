package com.cse.ds.sort;

import com.cse.ds.Comparator;
import com.cse.ds.Sorting;

/**
 * @author Tomoya Tokunaga (mailto: ttokunag@ucsd.edu)
 * 
 * This file implements Bubble sort algorithm
 */
public class BubbleSort<T> implements Sorting<T> {
	
	private Comparator<T> comparator;
	
	/*
    * BubbleSort class requires one parameter, Comparator<T>
    */
	public BubbleSort(Comparator<T> comparator) {
		this.comparator = comparator;
	}
	
	/*
    * description: sorts an array based on data type
	* @param: array, an array to be sorted
	* @param: ascending, true if an array to be sorted in the ascending order
    * return: void
    */
	@Override
	public void sort(T[] array, boolean ascending) {
		int n = array.length;
		for (int i = 0; i < n-1; i++) {
			for (int j = 0; j < n-i-1; j++) {
				if (!this.comparator.comparison(array[j], array[j+1], ascending)) {
					swap(array, j, j+1);
				}
			}
		}
	}

}
