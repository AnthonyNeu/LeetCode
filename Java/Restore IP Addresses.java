/*
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
*/

public class Solution {
    public List<String> restoreIpAddresses(String s) {
        List<String> result = new ArrayList<>();
        String ip = "";
        dfs(s, result, ip, 0, 0);
        return result;
    }
    
    private void dfs(String s, List<String> result, String ip, int start, int length) {
        if(start == s.length() && length == 4) {
            result.add(ip.substring(0, ip.length() - 1));
            return;
        }
        
        /* last one is more digit than 3*/
        if((s.length() - start) > 3 * (4 - length)) return;
        /* all the remaining digits cannot be mapped to an ip */
        if((s.length() - start) < (4 - length)) return;
        
        int num = 0;
        for(int i = start ; i < Math.min(start + 3, s.length()) ; i ++) {
            num = (s.charAt(i) - '0') + num * 10;
            
            if(num <= 255) {
                ip += s.charAt(i);
                dfs(s, result, ip + '.', i + 1, length + 1);
            }
            /* can not have 0 as first digit of a number */
            if(num == 0) break;
        }
    }
}