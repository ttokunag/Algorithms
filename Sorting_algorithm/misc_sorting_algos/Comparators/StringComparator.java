package com.cse.ds.comparator;

import com.cse.ds.Comparator;

/**
 * 
 * @author Tomoya Tokunaga (mailto: ttokunag@ucsd.edu)
 *
 * this file is about StringComparator class which implements Comparator interface
 * StringComparator class is about how we sort String arrays
 */
public class StringComparator implements Comparator<String> {

	@Override
	public boolean comparison(String x, String y, boolean ascending) {
		//ascending order
		if (ascending) {
			if (x.compareTo(y) <= 0) return true;
			else return false;
		}
		//descending order
		else {
			if (x.compareTo(y) >= 0) return true;
			else return false;
		}
	}
}
