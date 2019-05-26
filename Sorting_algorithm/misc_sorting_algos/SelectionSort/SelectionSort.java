package com.cse.ds.sort;

import com.cse.ds.Comparator;
import com.cse.ds.Sorting;

/**
 * 
 * @author Tomoya Tokunaga (mailto: ttokunag@ucsd.edu)
 *
 * This file implements Selection sort algorithm
 */
public class SelectionSort<T> implements Sorting<T> {
	
	private Comparator<T> comparator;
	
	/*
    * SelectionSort class requires one parameter, Comparator<T>
    */
	public SelectionSort(Comparator<T> comparator) {
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
		for (int i = 0; i < array.length-1; i++) {
			int indexSwapped = i;
			for (int j = i+1; j < array.length; j++) {
				if (!this.comparator.comparison(array[indexSwapped], array[j], ascending)) {
					indexSwapped = j;
				}
			}
			swap(array, i, indexSwapped);
		}
	}

}
