def print_matrix( matrix ):
    for i in range(len(matrix)):    #how many rows is ther in this case 3
        row = matrix[i]             #goes through every row 
        for j in range(len(row)):   
            elt = matrix[i][j]      #elt is element. elt is equal to a value on the matrix 
            if j > 0:               #check if this is the first value in the matrix (first colum) 
                print(f" {elt}",end="")
            else:
                print(f"{elt}",end="")
        print()




def main():
    # making a 3x4 matrix of 0s 
    num_row = 3 
    num_col = 4
    matrix = []
    for i in range(num_row):
        row = []
        for j in range(num_col):
            row.append(0)
        matrix.append(row)
    print_matrix(matrix)

if __name__ == "__main__":
    main()
