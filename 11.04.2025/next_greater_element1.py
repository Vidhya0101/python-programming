class Solution:
    def nextGreaterElement(self, nums1, nums2):

        stack = []
        ans = [-1] * len(nums2)

        map = {}
        last = []

        for num in nums1:
            map[num] = None

        for i in range(len(nums2)):

            if nums2[i] in map:
                map[nums2[i]] = i

            while stack and nums2[stack[-1]] < nums2[i]:
                index = stack.pop()
                ans[index] = nums2[i]

            stack.append(i)

        for num in nums1:
            last.append(ans[map.get(num)])

        return last
