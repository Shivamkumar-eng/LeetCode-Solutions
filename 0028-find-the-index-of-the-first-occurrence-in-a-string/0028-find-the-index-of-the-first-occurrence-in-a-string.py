class Solution:

  def strStr(self, haystack: str, needle: str) -> int:
    if not needle:
      return 0

    n = len(needle)
    m = len(haystack)

    # 1. Build LPS array for needle
    lps = [0] * n
    length = 0
    i = 1

    while i < n:
      if needle[i] == needle[length]:
        length += 1
        lps[i] = length
        i += 1
      else:
        if length != 0:
          length = lps[length - 1]
        else:
          lps[i] = 0
          i += 1

    # 2. Search haystack using left (needle pointer) and right (haystack pointer)
    left = 0
    right = 0

    while right < m:
      if needle[left] == haystack[right]:
        left += 1
        right += 1

        # Found full match
        if left == n:
          return right - n
      else:
        if left != 0:
          left = lps[left - 1]
        else:
          right += 1

    return -1
