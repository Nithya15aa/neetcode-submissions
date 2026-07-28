from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mapp = defaultdict(int)

        left = 0
        max_count = 0
        res = 0

        for right in range(len(s)):
            mapp[s[right]] += 1
            max_count = max(max_count, mapp[s[right]])

           
            while (right - left + 1) - max_count > k:
                mapp[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res


        