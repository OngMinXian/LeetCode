class Solution:
    def threeSum(self, nums):
        positives_count = {}
        negatives_count = {}
        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1
            elif num > 0:
                positives_count[num] = positives_count.get(num, 0) + 1
            elif num < 0:
                negatives_count[num] = negatives_count.get(num, 0) + 1
        
        res = []

        # Handle zeros
        if zeros >= 3:
            res.append([0, 0, 0])
        if zeros > 0:
            for i in positives_count.keys():
                if -i in negatives_count:
                    res.append([-i, 0, i])
        
        # Handle 2 positives and 1 negative
        for k, v in positives_count.items():
            if v >= 2:
                if -(k*2) in negatives_count:
                    res.append([k, k, -(k*2)])
                    
        positives = list(positives_count.keys())
        for i in range(len(positives)):
            for j in range(i+1, len(positives)):
                if -(positives[i] + positives[j]) in negatives_count:
                    res.append([positives[i], positives[j], -(positives[i] + positives[j])])

        # Handle 2 negatives and 1 positive
        for k, v in negatives_count.items():
            if v >= 2:
                if -(k*2) in positives_count:
                    res.append([k, k, -(k*2)])
                    
        negatives = list(negatives_count.keys())
        for i in range(len(negatives)):
            for j in range(i+1, len(negatives)):
                if -(negatives[i] + negatives[j]) in positives_count:
                    res.append([negatives[i], negatives[j], -(negatives[i] + negatives[j])])

        return res

solution = Solution()
# ans = solution.threeSum([-1,0,1,2,-1,-4]); assert sorted(list(map(lambda x: sorted(x), ans))) == sorted(list(map(lambda x: sorted(x), [[-1,-1,2],[-1,0,1]]))), ans
# ans = solution.threeSum([0,1,1]); assert ans == [], ans
# ans = solution.threeSum([0,0,0]); assert ans == [[0,0,0]], ans
# ans = solution.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]); assert sorted(list(map(lambda x: sorted(x), ans))) == sorted(list(map(lambda x: sorted(x), [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]))), ans
ans = solution.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]); assert sorted(list(map(lambda x: sorted(x), ans))) == sorted(list(map(lambda x: sorted(x), [[-5,1,4],[-4,0,4],[-4,1,3],[-2,-2,4],[-2,1,1],[0,0,0]]))), ans
