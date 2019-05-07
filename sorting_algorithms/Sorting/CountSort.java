package com.cse.ds.sort;

import com.cse.ds.Sorting;

/**
 * 
 * @author Tomoya Tokunaga (mailto: ttokunag@ucsd.edu)
 *
 * This file implements Count sort algorithm
 */
public class CountSort<T> implements Sorting<T> {
	
	private T[] order;
	
	/*
	* CountSort class requires one parameter, T[] order
	* order contains unique elements in an array to be sorted in sorted order
    */
	public CountSort(T[] order) {
		this.order = order;
	}
	
	/*
    * description: sorts an array based on data type
	* @param: array, an array to be sorted
	* @param: ascending, true if an array to be sorted in the ascending order
    * return: void
    */
	@Override
	public void sort(T[] array, boolean ascending) {
		int[] count = new int[this.order.length];

		for (int i = 0; i < array.length; i++) {
			for (int j = 0; j < this.order.length; j++) {
				if (array[i].equals(this.order[j])) {
					count[j]++;
					break;
				}
			}
		}

		if (ascending) {
			int curIndex = 0;
			for (int i = 0; i < count.length; i++) {
				for (int j = 0; j < count[i]; j++) {
					array[curIndex] = this.order[i];
					curIndex++;
				}
			}
		}

		else {
			int curIndex = 0;
			for (int i = count.length - 1; i >= 0; i--) {
				for (int j = 0; j < count[i]; j++) {
					array[curIndex] = this.order[i];
					curIndex++;
				}
			}
		}
	}
}
