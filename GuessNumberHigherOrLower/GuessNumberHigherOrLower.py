class Solution:
    def guessNumber(self, n: int) -> int:
        
        low = 1
        high = n
        while True:
            mid = (low + high) >> 1
            current_res = guess(mid)
            
            # Guess is higher
            if current_res == -1:
                high = mid - 1

            # Guess is lower
            elif current_res == 1:
                low = mid + 1

            elif current_res == 0:
                return mid
