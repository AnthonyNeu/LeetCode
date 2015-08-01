/*
Given an array of strings, return all groups of strings that are anagrams.

Note: All inputs will be in lower-case.
*/


public class Solution {
    public List<String> anagrams(String[] strs) {
        Map<String, ArrayList<String>> map = new HashMap<>();
        
        for(String str : strs){
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            
            String sorted = new String(chars);
            
            if(!map.containsKey(sorted)){
                map.put(sorted, new ArrayList<>());
            }
            
            map.get(sorted).add(str);
        }
        
        List<String> result = new ArrayList<String>();
        
        for (ArrayList<String> tmp : map.values()) {
            if (tmp.size() > 1) {
                result.addAll(tmp);
            }
        }
        
        return result;
    }
}