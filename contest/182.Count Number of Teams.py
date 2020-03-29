class Solution:
    def numTeams(self, arr) -> int:
        length = len(arr)
        if length < 3:
            return 0
        if length == 3:
            if arr[0] > arr[1] > arr[2] or arr[0] < arr[1] < arr[2]:
                return 1
            else:
                return 0

        count = 0
        for i in range(length):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            for j in range(i + 1, length):
                r = length - 1
                while j < r:
                    if arr[i] > arr[j] > arr[r] or arr[i] < arr[j] < arr[r]:
                        count += 1
                    r -= 1

                    
        return count
                
            

            
        
def main():

    arr = [2,5,3,4,1]


    ret = Solution().numTeams(arr)
    out = (ret);
    print(out)


if __name__ == '__main__':
    main()
