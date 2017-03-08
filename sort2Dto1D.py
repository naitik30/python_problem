



def check_all_Array_complete(cur_pointer_dict):
    for i in range(len(matrix)):
        if cur_pointer_dict[i]!=len(matrix[i]):
            return False
    return True

def convert_to_1D_Array(matrix):
    final_list = list()
    cur_pointer_dict = dict()
    for i in range(len(matrix)):
        cur_pointer_dict[i] = 0
    while (not check_all_Array_complete(cur_pointer_dict)):
        minvalue = 10000
        position = 0
        for i in cur_pointer_dict.keys():
            if cur_pointer_dict[i] < len(matrix[i]):
                if minvalue > matrix[i][cur_pointer_dict[i]]:
                    minvalue = matrix[i][cur_pointer_dict[i]]
                    position = i
        final_list.append(minvalue)
        cur_pointer_dict[position] = cur_pointer_dict[position] + 1
    return final_list

if __name__ =="__main__":

    matrix = [[1,6,7],[2,5,8],[3,4,9]]

    print(convert_to_1D_Array(matrix))
    # output:
    #[1, 2, 3, 4, 5, 6, 7, 8, 9]


