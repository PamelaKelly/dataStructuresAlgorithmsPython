class MergeSort:
    
    @staticmethod
    def merge_sort(lst):
        """
        Function which recursively merge sorts a given list. 
        @type lst: list
        @param lst: list of elements to be sorted
        
        @rtype: list
        @return: lst is sorted using merge sort
        """
        n = len(lst)
        if n < 2:
            return lst
        else:
            if n %2 == 0:
                left_list = lst[:n//2]
                right_list = lst[n//2:]
            else:
                left_list = lst[:n//2]
                right_list = lst[n//2:]
            left = MergeSort.merge_sort(left_list) 
            right = MergeSort.merge_sort(right_list)
            return MergeSort.merge(left, right)
            
    @staticmethod        
    def merge(left, right):
        """
        Helper function which merges the two lists at each step
        @type left: list
        @param left: left hand side list
        @type right: list
        @param right: right hand side list
        
        @rtype: list
        @return: the two given lists merged in the correct order
        """
        left_idx, right_idx = 0, 0
        merged_list = []
        # before we have moved full through either list
        while left_idx < len(left) and right_idx < len(right):
            # find the smaller of the two elements & append it
            if left[left_idx] < right[right_idx]:
                merged_list.append(left[left_idx])
                # increment and move on from elements that have been appended
                left_idx += 1
            else:
                merged_list.append(right[right_idx])
                right_idx += 1
        
        # if the lists are uneven lengths we may have some elements 
        # that haven't been added to the merged list
        if left_idx < len(left):
            merged_list.extend(left[left_idx:])
        elif right_idx < len(right):
            merged_list.extend(right[right_idx:])
        
        return merged_list
                
            

odd_list = [2, 5, 3, 4, 1, 9, 7, 6, 8]
even_list = [8, 5, 1, 3, 7, 2, 6, 4]
print("Before Sorting: ", odd_list)
print("After Sorting: ", MergeSort.merge_sort(odd_list))
print("Before Sorting: ", even_list)
print("After Sorting: ", MergeSort.merge_sort(even_list))
        
        