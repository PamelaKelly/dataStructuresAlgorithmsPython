class BinarySearch:
    
    @staticmethod
    def binary_search(lst, element):
        """
        Function which implements a binary search for an element
        on a given list. 
        @type lst: list
        @param lst: list of elements to search
        @type element: integer or float
        @param element: the element to search for
        
        @rtype: integer
        @return: return True if found, false otherwise 
        """
        midpoint = len(lst) // 2
        if len(lst) == 1:
            if lst[0] == element:
                # we found it at midpoint
                return True
            else:
                return False
        else:
            if element < lst[midpoint]:
                return BinarySearch.binary_search(lst[:midpoint], element)
            else:
                return BinarySearch.binary_search(lst[midpoint:], element)
        
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print("When element is not present: ", BinarySearch.binary_search(my_list, 20))
print("When element is present: ", BinarySearch.binary_search(my_list, 5))
