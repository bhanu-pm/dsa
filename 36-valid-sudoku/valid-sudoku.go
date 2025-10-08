func isValidSudoku(board [][]byte) bool {
    for _, i := range board {
        isrow := isValid(i)
        if isrow == false {
            return false
        }
    }
    for i:=0; i<9; i++ {
        columnSlice := colToRow(board, i)
        iscol := isValid(columnSlice)
        if iscol == false {
            return false
        }
    }
    for i := 0; i < 9; i += 3 {
        for j := 0; j < 9; j += 3 {
            boxSlice := make([]byte, 0, 9)
            for row := i; row < i+3; row++ {
                for col := j; col < j+3; col++ {
                    boxSlice = append(boxSlice, board[row][col])
                }
            }
            if !isValid(boxSlice) {
                return false
            }
        }
    }
    return true
}

func isValid(nums []byte) bool {
    rowdict := make(map[byte]bool)
    for _, num := range nums {
        if rowdict[num] {
            return false
        }
        if num != '.' {
            rowdict[num] = true
        }
    }
    return true
}

func colToRow(board [][]byte, col int) []byte {
    colslice := make([]byte, 0, 9)
    for i:=0; i<9; i++ {
        colslice = append(colslice, board[i][col])
    }
    return colslice
}