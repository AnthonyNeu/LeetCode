"""
Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
"""

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        dict.add(start)
        dict.add(end)
        
        #If A->C and B->C, then traces[C] contains A and B.
        #This is used for recovering the paths.
        result,current,found,trace,visited = [],[start],False,{word:[] for word in dict},set([start])
        
        while current and not found:
            for word in current:
                visited.add(word)
                
            next = set([])    
            for word in current:
                for i in xrange(len(word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + char + word[i+1:]
                        if candidate in dict and candidate not in visited:
                            if candidate == end:
                                found = True
                            next.add(candidate)
                            trace[candidate].append(word)
            
            current = next
        
        if found:
            self.buildresult(result,trace,[],end)
            
        return result
        
    def buildresult(self,result,trace,path,word):
        if not trace[word]:
            result.append([word] + path)
        else:
            for prev in trace[word]:
                self.buildresult(result, trace, [word] + path, prev)
