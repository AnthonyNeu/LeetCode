/*
Given a sorted integer array where the range of elements are [0, 99] inclusive, return its missing ranges.
For example, given [0, 1, 3, 50, 75], return [“2”, “4->49”, “51->74”, “76->99”]
*/

public List<String> findMissingRanges(int[] vals, int start, int end) {
   	List<String> ranges = new ArrayList<>();
   	int prev = start - 1;
   	for (int i = 0; i <= vals.length; i++) {
      	int curr = (i == vals.length) ? end + 1 : vals[i];
      	if (curr - prev >= 2) {
         	ranges.add(getRange(prev + 1, curr - 1));
      	}
	prev = curr; }
   	return ranges;
}

private String getRange(int from, int to) {
	return (from == to) ? String.valueOf(from) : from + "->" + to;
}