'''
Practice following questions

42. Trapping Rain Water
68. Text Justification
135. Candy
913. Cat and Mouse
381, insert Delete GetRandom O1) - Duplicates allowed

'''

from collections import Counter
from typing import List


class SolutionHard:
    # 30. Substring with Concatenation of All Words
    # Runtime: O(n*n)
    # Space: O(n)
    # More challenges:
    #   [E] 2287. Rearrange Characters to Make Target String
    #   [M] 1676. Lowest Common Ancestor of a Binary Tree IV
    #   [M] 556. Next Greater Element III
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0: return []
        step = len(words[0])
        if len(s) < len(words) * step: return []

        result = []
        target = {}
        for word in words:
            if word not in target:
                target[word] = 1
            else:
                target[word] = target[word] + 1
        for i in range(len(s) - (len(words) * step) + 1):
            word = s[i:i+step]
            if word not in target: continue

            seen = {word: 1}
            count = 1
            if count == len(words):
                result.append(i)
                continue

            start = i + step
            while start < len(s):
                word = s[start:start+step]
                if word not in target: break

                if word not in seen: seen[word] = 0
                seen[word] = seen[word] + 1

                if seen[word] > target[word]: break

                count += 1
                start += step
                if count == len(words):
                    result.append(i)
                    break
        return result
    
    # 76. Minimum Window Substring
    # Runtime: O(2 * len(filtered_s) + len(s) + len(t))
    # Space: O(len(t) + len(s))
    # More challenges:
    #   [H] 239. Sliding Window Maximum
    #   [M] 567. Permutation in String
    #   [H] 632. Smallest Range Covering Elements from K Lists
    def minWindow(self, s: str, t: str) -> str:
        if len(s) == 0 or len(t) == 0 or len(t) > len(s): return ''

        # {char:count}
        target = Counter(t)
        
        # filter out unrelated chars and keep the target char and its index 
        filtered_s = [i for i in range(len(s)) if s[i] in target]

        count = 0   # number of char's found 
        seen = {}   # keep track of {char:count}
        result = [] # default to not found, should containt start and end indices
        left, right = 0, 0
        for right in range(len(filtered_s)):
            end = filtered_s[right] 
            key = s[end]
            seen[key] = seen.get(key, 0) + 1

            if seen[key] == target[key]:
                count += 1

            while left <= right and count == len(target):
                # found all chars in the current window
                start = filtered_s[left]
                if not result or result[1] - result[0] > end - start:
                    result = [start, end]

                # remove the current left most char and try the window again
                key = s[start]
                seen[key] = seen[key] - 1
                if seen[key] < target[key]:
                    count -= 1
                left += 1 

        return '' if not result else s[result[0]:result[1]+1]

    # 527. Word Abbreviation
    # https://leetcode.com/problems/word-abbreviation/
    # Constraints:
    #   words[i] consists of lowercase English letters. All words are unique.
    # Runtime:
    # Space:
    # More challenge:
    #
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        # TODO
        pass

    # 1216. Valid Palindrome III
    # https://leetcode.com/problems/valid-palindrome-iii/description/
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # TODO
        pass

    # 220. Contains Duplicate III
    # https://leetcode.com/problems/contains-duplicate-iii/description/
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        # TODO 
        pass



if __name__ == '__main__':
    obj = SolutionHard()

    print(obj.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))