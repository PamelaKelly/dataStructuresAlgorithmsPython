class LinearSearch:
    
    def __init__(self):
        pass
    
    @staticmethod
    def search(lst, element):
        """
        Linear search function which returns the index
        at which the element is found, else returns -1. 
        
        @type lst: list
        @param lst: list of elements that is to be searched
        @type element: any type
        @param element: the element to search the list for
        
        @rtype: integer
        @return: index at which the element was found
        """
        for i in range(len(lst)):
            if lst[i] == element:
                return i
        return -1
    