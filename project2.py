
def merge_sorted_arrays(nums1, nums2):
    i, j = 0, 0
    result = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1


    while i < len(nums1):
        result.append(nums1[i])
        i += 1


    while j < len(nums2):
        result.append(nums2[j])
        j += 1
    
    return result


nums1 = [1, 2, 3,7,8,10,12]
nums2 = [2, 5, 6,213,1231,32132131]
print(merge_sorted_arrays(nums1, nums2)) 




