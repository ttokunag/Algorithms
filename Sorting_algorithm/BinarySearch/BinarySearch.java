

public class BinarySearch {

  public BinarySearch() {}

  /*
   *  a method to find the given target in the given array. if the
   *  target is found, then return the index of it. Otherwise None
   *  @param arr: an array to be searched
   *  @param target: an element the program looks for
   */
  public static int find(int[] arr, int target) {
    // set the cursor of the leftmost and rightmost bounds
      int left = 0;
      int right = arr.length - 1;

      while (left <= right) {

        median = (left + right) / 2;
        // the case finds the exact position
        if (target == arr[median]) {
          return median;
        }
        // if the target is smaller
        else if (target < arr[median]) {
          right = median - 1;
        }
        // if the target is larger
        else {
          left = median + 1
        }
    
      }

      // if the target is not found, return -1
      return -1;
  
    }

}
