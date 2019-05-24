package com.cse.ds.comparator;

import com.cse.ds.Comparator;

/**
 * 
 * @author Tomoya Tokunaga (mailto: ttokunag@ucsd.edu)
 * A custom comparator for comparing String in reverse order.
 * Ex: ABBZ > ZBA
 */
public class StringComparatorReverse implements Comparator<String> {

	@Override
	public boolean comparison(String x1, String y1, boolean ascending) {
		String revX = "";
		String revY = "";
		for (int i = x1.length() - 1; i > 0; i--) {
			revX += x1.charAt(i);
		}
		for (int i = y1.length() - 1; i > 0; i--) {
			revY += y1.charAt(i);
		}
		//ascending order
		if (ascending) {
			if (revX.compareTo(revY) <= 0) return true;
			else return false;
		}
		//descending order
		else {
			if (revX.compareTo(revY) >= 0) return true;
			else return false;
		}
	}
}
