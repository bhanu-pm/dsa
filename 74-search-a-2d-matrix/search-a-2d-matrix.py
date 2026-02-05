# 2d mat
# m rows, n cols
# each row is in increasing order
# everything in increasing order, but just arranged like a 2d mat
# return true if target in mat, else false


# m = len(matrix) # rows
# n = len(matrix[0]) # cols
# while True
    # curridx = int(left+right/2)
    # conversion to 2d idx
        # which row = int(curridx/cols) # quotient
        # which col = curridx%cols # remainder
    # if target == nums[convertedidx]
        # return True
    # if this is the last remaining element
        # break
    # if target < nums[convertedidx]:
        # right=curridx
    # elif target > nums[convertedidx]:
        # left = curridx+1
# return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        m = len(matrix) # rows
        n = len(matrix[0]) # cols
        right = m*n - 1

        while True:
            idx = int((left+right)/2)
            convertedidx = self.convert(idx, n)

            if target == matrix[convertedidx[0]][convertedidx[1]]:
                return True
            if left == right:
                break
            if target < matrix[convertedidx[0]][convertedidx[1]]:
                right = idx
            elif target > matrix[convertedidx[0]][convertedidx[1]]:
                left = idx+1
        return False
    
    def convert(self, idx, n):
        row = int(idx/n)
        col = idx % n
        return (row, col)