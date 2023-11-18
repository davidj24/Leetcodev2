class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
#        if len(strs) == 1:
#            return strs[0]
#        i = 0

#        strs_len = [len(word) for word in strs]
#        i = 0

#        common = ""
#        while i < min(strs_len):
#            j = 1
#            true_for = 0
#            while j < len(strs):
#                if strs[0][:i+1] == strs[j][:i+1] and i+1 <= len(strs[j]):
#                    true_for += 1
#                    j += 1
#                else:
#                    j += 1
#            if true_for == len(strs)-1:
#                common = strs[0][:i+1]
#            i += 1
#        return common

        if not strs:
            return ""
        prefix = strs[0]
        for word in strs[1:]:
            while word.find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix