#  - stopping conditions
#     - if we reach the end of the row or column
#     - if we reach a row or column we already went through
#  - clockwise spiral
#     - row 0 co min row
#     - col n co max col
#     - row m ro max row
#     - col 0 ro min col

#     - row 1     co
#     - col n-1   co
#     - row m-1   ro
#     - col 1     ro

#  - are all the numbers in matrix unique?
#     - I want to check if we already added that number
#     - didn't mention anything, so that is not the direction

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        if len(matrix) == 1:
            return matrix[0]

        # check = {"min_row":False, "max_col":False, "max_row":False, "min_col":False}
        seen = set() # set of tuple ( i, j )
        output = []
        total_len = len(matrix[0]) * len(matrix)
        direction = 0 # it will indicate when we have to change the direction we are moving in
        i, j = 0, 0
        while True:
            if len(output) == total_len:
                break

            # continue doing our thing
            if direction % 4 == 0:
                # moving right
                # only increment j
                output.append(matrix[i][j])
                seen.add((i, j))
                if j+1 < len(matrix[0]) and ((i, j+1) not in seen):
                    j+=1
                else:
                    direction += 1
                    i+=1
            elif direction % 4 == 1:
                # moving down
                # only increment i
                output.append(matrix[i][j])
                seen.add((i, j))
                if i+1 < len(matrix) and ((i+1, j) not in seen):
                    i+=1
                else:
                    direction += 1
                    j-=1
            elif direction % 4 == 2:
                # moving left
                # only decrement j
                output.append(matrix[i][j])
                seen.add((i, j))
                next_i, next_j = i, j-1
                if j-1 >= 0 and ((i, j-1) not in seen):
                    j-=1
                else:
                    direction += 1
                    i-=1
            elif direction %4 == 3:
                # moving up
                # only decrement i
                output.append(matrix[i][j])
                seen.add((i, j))
                next_i, next_j = i-1, j
                if i-1 >= 0 and ((i-1, j) not in seen):
                    i-=1
                else:
                    direction += 1
                    j+=1
            
        return output