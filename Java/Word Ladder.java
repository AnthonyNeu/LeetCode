/*
Given two words (beginWord and endWord), and a dictionary, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
*/

public class Solution {
    public int ladderLength(String beginWord, String endWord, Set<String> wordDict) {
        Queue<String> queue = new LinkedList<>();
        queue.offer(beginWord);
        wordDict.add(endWord);
        int result = 1;
        while(!queue.isEmpty()) {
            int size = queue.size();
            for(int i = 0 ; i < size ; i ++) {
                String str = queue.poll();
                if(str.equals(endWord)) return result;
                int length = str.length();
                for(int j = 0 ; j < length ; j ++) {
                    for(char c = 'a'; c <= 'z'; c++) {
                        String candidate = str.substring(0, j) + c + str.substring(j + 1);
                        if(wordDict.contains(candidate)) {
                            queue.offer(candidate);
                            wordDict.remove(candidate);
                        }
                    }
                }
            }
            result ++;
        }
        return 0;
    }
}
