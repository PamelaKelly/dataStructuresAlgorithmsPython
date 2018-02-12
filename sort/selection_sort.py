class SelectionSort:
    
    def __init__(self, unsorted_list):
        self.__list = unsorted_list
        self.__length = len(unsorted_list)
    
    def sort_ascending(self):
        for i in range(self.__length):
            # get the minimum in the rest of the list
            min_num = min(self.__list[i:])
            
            # get the index of the minimum to do swap later
            min_index = self.__list.index(min_num)
            
            # store the value at current index in temp variable
            temp = self.__list[i]
            
            # swap the values
            self.__list[i] = min_num
            self.__list[min_index] = temp
            
        return self.__list
            
my_list = [2, 4, 1, 9, 8, 10, 6]
sorter = SelectionSort(my_list)
print(sorter.sort_ascending())
print(my_list)
        