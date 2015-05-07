/*
Given an array of integers, every element appears twice except for one. Find that single one.
*/

public int singleNumber(int[] A) {
   	Set<Integer> set = new HashSet<>();
   	for (int x : A) {
      	if (set.contains(x)) {
         	set.remove(x);
      	} else {
         	set.add(x);
		} 
	}
   	return set.iterator().next();
}


public int singleNumber(int[] A) {
   	int num = 0;
   	for (int x : A)	{
	num ^= x; 
	}
	return num; 
}
