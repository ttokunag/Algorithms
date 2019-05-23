package com.cse.ds.sorting;

/**
 * 
 * @author harsh
 *
 * @param <T>
 */
public interface Sorting<T> {
	
	public abstract void sort(T[] array, boolean ascending);
	
	public default void swap(T array[],int i,int j)
	{
		T tmp = array[i];
		array[i] = array[j];
		array[j] = tmp;
	}
	
	public default void print(T array[])
	{
		for(T val:array)
		{
			System.out.print(val.toString()+" ");
		}
		System.out.println();
	}
}
