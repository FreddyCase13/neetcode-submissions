class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        bottle = -1
        temp = 0

        for i in range(len(arr) -1, -1, -1):
            temp = arr[i]
            arr[i] = bottle
            bottle = max(temp, bottle)
        return arr
            
