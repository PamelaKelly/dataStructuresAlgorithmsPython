class SelectionSort:
    """ Class for implementing Selection Sort. """
    
    @staticmethod
    def sort_ascending(lst):
        """
        A function which implement ascending Selection Sort
        on a given list of numbers. 
        
        @type lst: list
        @param lst: an unsorted list of numbers
        
        @rtype: list
        @return: list is now sorted (in place) in ascending order
        """
        for i in range(len(lst)):
            # get the minimum in the rest of the list
            min_num = min(lst[i:])
            
            # get the index of the minimum to do swap later
            min_index = lst.index(min_num)
            
            # store the value at current index in temp variable
            temp = lst[i]
            
            # swap the values
            lst[i] = min_num
            lst[min_index] = temp
            
        return lst
            
my_list = [2, 4, 1, 9, 8, 10, 6]
print("Before Sorting: ", my_list)
print("After Sorting: ", SelectionSort.sort_ascending(my_list))
