class BubbleSort:
    """ Class for implementing Bubble Sort"""
    
    @staticmethod
    def bubble_sort(lst):
        """
        Function which implements ascending Bubble Sort 
        on a given list of numbers.
        
        @type lst: list
        @param list: an unsorted list of numbers
        
        @rtype: list
        @return: list is now sorted (in place) in ascending order
        """
        for i in range(len(lst) - 1):
            for j in range(len(lst) - 1 - i):
                if lst[j] > lst[j + 1]:
                    temp = lst[j]
                    lst[j] = lst[j + 1]
                    lst[j + 1] = temp
        return lst
    
    @staticmethod
    def bubble_sort_optimised(lst):
        """
        Function which implements ascending Bubble Sort
        on a given list of numbers, using an optimised approach
        
        @type lst: list
        @param lst: list of numbers
        
        @rtype: list
        @return: list is now sorted (in place) in ascending order
        """
        swapped = True
        for i in range(len(lst) - 1):
            if not swapped:
                break
            for j in range(len(lst) - 1 - i):
                swapped = False
                if lst[j] > lst[j + 1]:
                    temp = lst[j]
                    lst[j] = lst[j + 1]
                    lst[j + 1] = temp
                    swapped = True
        return lst
                
            
        
        
my_list = [9, 5, 7, 3, 6, 2, 1]
print("Before Sorted: ", my_list)
print("After Sorting (Method 1): ", BubbleSort.bubble_sort(my_list))
my_list = [1, 2, 3, 7, 4, 5, 9]
print("After Sorting (Method 2): ", BubbleSort.bubble_sort_optimised(my_list))