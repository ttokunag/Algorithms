package com.cse.ds.sort;

import com.cse.ds.Comparator;
import com.cse.ds.Sorting;

/**
 * 
 * @author Tomoya Tokunaga (mailto: ttokunag@ucsd.edu)
 *
 * This file implements Merge sort algorithm
 */
public class MergeSort<T> implements Sorting<T> {

	private Comparator<T> comparator;

	/*
    * MergeSort class requires one parameter, Comparator<T>
    */
	public MergeSort(Comparator<T> comparator) {
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
		if (array.length > 1) {
			int mid = array.length / 2;
			Object[] left = new Object[mid];
			Object[] right = new Object[array.length - mid];
			for (int i = 0; i < mid; i++) {
				left[i] = array[i];
			}
			for (int i = 0; i < array.length - mid; i++) {
				right[i] = array[i + mid];
			}
			
			this.sort((T[])left, ascending);
			this.sort((T[])right, ascending);
			int i = 0;
			int j = 0;
			int k = 0;
			
			while (i < left.length && j < right.length) {
				if (this.comparator.comparison((T)left[i], (T)right[j], ascending)) {
					array[k] = (T)left[i];
					i++;
				}
				else {
					array[k] = (T)right[j];
					j++;
				}
				k++;
			}
			
			while (i < left.length) {
				array[k] = (T)left[i];
				i++;
				k++;
			}
			
			while (j < right.length) {
				array[k] = (T)right[j];
				j++;
				k++;
			}
		}
	}
}
