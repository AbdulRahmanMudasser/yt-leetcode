class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # unique_number = set()

        # for num in nums:
        #     if num in unique_number:
        #         unique_number.remove(num)
        #     else:
        #         unique_number.add(num)

        # return unique_number.pop()

        result = 0

        for num in nums:
            result = result ^ num

        return result