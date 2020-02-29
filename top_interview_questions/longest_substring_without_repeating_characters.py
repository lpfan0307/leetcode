class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        max_length, start, char_dict = 0, 0, {}
        for idx, char in enumerate(s, 1):
            if char_dict.get(char, -1) >= start:
                start = char_dict[char]
            char_dict[char] = idx
            max_length = max(max_length, idx - start)
        return max_length

def lengthOfLongestSubstring( s):
    max_length, start, char_dict = 0, 0, {}
    for idx, char in enumerate(s, 1):
        print(idx)
        if char_dict.get(char, -1) >= start:
            start = char_dict[char]
        char_dict[char] = idx
        max_length = max(max_length, idx - start)
    print(max_length)
    return max_length

lengthOfLongestSubstring('adfajfljgadgfgadfalfdjadf')