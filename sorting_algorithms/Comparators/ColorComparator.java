package com.cse.ds.comparator;

import com.cse.ds.Comparator;

/**
 * 
 * @author Tomoya Tokunaga (mailto: ttokunag@ucsd.edu)
 * 
 * this file is about ColorComparator class which implements Comparator interface
 * ColorComparator class is about how we sort Color arrays
 */
public class ColorComparator implements Comparator<String> {

	@Override
	public boolean comparison(String x, String y, boolean ascending) {
		//ascending order
		if (ascending) {
			if (y.equalsIgnoreCase("red")) {
				return true;
			}
			else if (y.equalsIgnoreCase("white")) {
				if (x.equalsIgnoreCase("red")) return false;
				else return true;
			}
			else {
				if (x.equalsIgnoreCase("blue")) return true;
				else return false;
			}
		}
		//descending order
		else {
			if (y.equalsIgnoreCase("blue")) {
				return true;
			}
			else if (y.equalsIgnoreCase("white")) {
				if (x.equalsIgnoreCase("blue")) return false;
				else return true;
			}
			else {
				if (x.equalsIgnoreCase("red")) return true;
				else return false;
			}
		}
	}
}
