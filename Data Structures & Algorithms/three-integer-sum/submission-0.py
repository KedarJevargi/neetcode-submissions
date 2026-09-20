class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        from collections import Counter
        hashmap = Counter(nums)   # frequency map
        ans = set()
        n = len(nums)

        for i in range(n - 1):
            hashmap[nums[i]] -= 1   # use nums[i]

            for j in range(i + 1, n):
                if hashmap[nums[j]] <= 0:
                    continue

                hashmap[nums[j]] -= 1   # use nums[j]

                target = -(nums[i] + nums[j])
                if hashmap.get(target, 0) > 0:
                    triplet = tuple(sorted((nums[i], nums[j], target)))
                    ans.add(triplet)

                hashmap[nums[j]] += 1   # restore

            hashmap[nums[i]] += 1       # restore

        return [list(t) for t in ans]
