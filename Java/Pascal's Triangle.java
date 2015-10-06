/*
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
*/

public class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<>();
        
        if (numRows == 0) return result;
        
        List<Integer> first = new ArrayList<>();
        first.add(1);
        result.add(first);
        
        for (int i = 2 ; i <= numRows ; i ++) {
            List<Integer> cur = new ArrayList<>();
            List<Integer> prev = result.get(result.size() - 1);
            cur.add(1);
            
            for (int j = 1 ; j < i - 1 ; j ++) {
                cur.add(prev.get(j - 1) + prev.get(j));
            }
            
            cur.add(1);
            result.add(cur);
        }
        
        return result;
        
    }
}
