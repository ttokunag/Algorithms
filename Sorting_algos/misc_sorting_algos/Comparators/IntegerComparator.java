package com.cse.ds.comparator;

import com.cse.ds.Comparator;

/**
 * 
 * @author Tomoya Tokunaga (mailto: ttokunag@ucsd.edu)
 * 
 * this file is about IntegerComparator class which implements Comparator interface
 * IntegerComparator class is about how we sort Integer arrays
 */
public class IntegerComparator implements Comparator<Integer> {

	@Override
	public boolean comparison(Integer x, Integer y, boolean ascending) {
		if (ascending) {
			if (x < y) return true;
			else return false;
		}
		else {
			if (x < y) return false;
			else return true;
		}
	}
}
