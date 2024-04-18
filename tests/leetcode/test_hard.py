from typing import List, Literal
import pytest

from leetcode.hard import SolutionHard

@pytest.fixture
def hard_class_obj():
    return SolutionHard()

# 80. Remove Duplicates from Sorted Array II
@pytest.mark.parametrize("s, words, expected_result", [
    ("a", ["a"], [0]),
    ("aaa", ["a"], [0,1,2]),
    ("barfoothefoobarman", ["foo","bar"], [0,9]),
    ("wordgoodgoodgoodbestword", ["word","good","best","word"], []),
    ("barfoofoobarthefoobarman", ["bar","foo","the"], [6,9,12]),
    ("wordgoodgoodgoodbestword", ["word","good","best","good"], [8])
])
def test_removeDuplicates(hard_class_obj: SolutionHard, s: str, words: List[str], expected_result: List[int]):
    assert hard_class_obj.findSubstring(s, words) == expected_result

# 76. Minimum Window Substring
@pytest.mark.parametrize("s, t, expected_result", [
    ("ADOBECODEBANC", "ABC", "BANC"),
    ("a", "a", "a"),
    ("a", "aa", ""),
    ("abc", "aa", ""),
    ("aaaabbbbccbbbcabc", "acbc", "cabc")
])
def test_minWindow(hard_class_obj: SolutionHard, s: str, t: str, expected_result: str):
    assert hard_class_obj.minWindow(s, t) == expected_result

# 1216. Valid Palindrome III
@pytest.mark.skip("TODO")
#@pytest.mark.parametrize("s, k, expected_result", [
#    ('abcdeca', 2, True),
#    ('abbababa', 1, True)
#])
def test_isValidPalindrome(hard_class_obj: SolutionHard, s: str, k: int, expected_result: bool):
    assert hard_class_obj.isValidPalindrome(s, k) == expected_result

# 527. Word Abbreviation
@pytest.mark.skip("TODO")
#@pytest.mark.parametrize("words, expected_result", [
#    (["like","god","internal","me","internet","interval","intension","face","intrusion"],
#     ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]),
#    (["aa","aaa"], ["aa","aaa"])
#])
def test_wordsAbbreviation(hard_class_obj: SolutionHard, words: List[str], expected_result: List[str]):
    assert hard_class_obj.wordsAbbreviation(words) == expected_result