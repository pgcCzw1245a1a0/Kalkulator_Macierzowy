from Savefunctions import *


def memory_recall(operation_number):
    if not os.path.exists("./memory"):  # checking if memory folder exists
        print("There is no memory folder")
    else:
        if not os.listdir("./memory"):  # checking if there are any operations stored in memory
            print("There are no operations stored in memory")
        else:
            operation_dictionary = load_operation(operation_number)  # converting JSON to a normal Python dictionary
            answer = np.array(operation_dictionary['res'])  # converting a list of lists into a matrix
            return answer

#test output of matrix
#matrix=[[1,2,3],[4,5,6],[7,8,9]]
#print(matrix)
#print(np.array(matrix))
