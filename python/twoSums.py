class Solution:
    def twoSums(self, num, target):
        processed = {}
        for i in range(0, len(num)):
            if target-num[i] in processed:
                return [Processed[target-num[i]]+1, i+1]
            processed[num[i]]=i

