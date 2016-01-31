/*
Given a string, find the length of the longest substring without repeating characters.
For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
For "bbbbb" the longest substring is "b", with the length of 1.
*/

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int* dict = new int[256];
        memset(dict, -1, sizeof(int) * 256);
        int start = -1, maxLen = 0;
        for (int i = 0; i < s.length(); ++i) {
            if (dict[s[i]] > start) {
                start = dict[s[i]];
            }
            dict[s[i]] = i;
            maxLen = max(maxLen, i - start);
        }
        delete[] dict;
        dict = nullptr;
        return maxLen;
    }
};
