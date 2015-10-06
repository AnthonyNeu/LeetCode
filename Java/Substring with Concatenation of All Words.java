/*
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
*/

public class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> result = new ArrayList<>();
        int wordNum = words.length, wordLength = words[0].length(), i = 0;
        
        if (wordNum * wordLength > s.length()) return result;
        
        Map<String, Integer> map = new HashMap<>();
        
        for (String str : words) {
            if (map.containsKey(str)) map.put(str, map.get(str) + 1);
            else map.put(str, 1);
        }
        
        while (i < s.length() + 1 - wordNum * wordLength) {
            Map<String, List<Integer>> cur = new HashMap<>();
            int j = 0;
            while (j < wordNum) {
                String word = s.substring(i + j * wordLength, i + (j + 1) * wordLength);
                
                if (!map.containsKey(word)) break;
                
                if (!cur.containsKey(word)) {
                    List<Integer> list = new ArrayList<>();
                    list.add(i + j * wordLength);
                    cur.put(word, list);
                } else {
                    cur.get(word).add(i + j * wordLength);
                }
                
                if (cur.get(word).size() > map.get(word)) {
                    break;
                }
                j ++;
            }
            
            if (j == wordNum) result.add(i);
            i ++;
        }
        
        return result;
    }
}
