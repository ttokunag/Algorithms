package com.cse.ds.comparator;

import com.cse.ds.Comparator;
import com.cse.ds.models.Student;

/**
 * 
 * @author Tomoya Tokunaga (mailto: ttokunag@ucsd.edu)
 *
 * this file is about StudentComparator class which implements Comparator interface
 * StudentComparator class is about how we sort Student arrays
 */
public class StudentComparator implements Comparator<Student> {

	@Override
	public boolean comparison(Student x, Student y, boolean ascending) {
		if (ascending) {
			if (x.getCGPA() < y.getCGPA()) {
				return true;
			}
			else if (x.getCGPA().equals(y.getCGPA())) {
				return Integer.parseInt(x.getPID()) < Integer.parseInt(y.getPID());
			}
			else {
				return false;
			}
		}

		else {
			if (x.getCGPA() > y.getCGPA()) {
				return true;
			}
			else if (x.getCGPA().equals(y.getCGPA())) {
				return Integer.parseInt(x.getPID()) > Integer.parseInt(y.getPID());
			}
			else {
				return false;
			}
		}
	}
}
