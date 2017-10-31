def sort(list):
    if len(list)<=2:
		if len(list)<2 or list[0]<=list[1]:
			return list
		else:
			return [list[1], list[0]]
    idx = len(list)/2
    first = sort(list[:idx])
    last = sort(list[idx:])
    return merge(first, last)

def merge(list1, list2):
	#print("merge")
	#print(list1)
	#print(list2)
	idx1, idx2 = 0, 0
	sortedList = []
	while idx1<len(list1) and idx2<len(list2):
		if list1[idx1] <= list2[idx2]:
			sortedList.append(list1[idx1])
			idx1+=1
		else:
			sortedList.append(list2[idx2])
			idx2+=1
	#print(sortedList)
	#print("partially merged")
	if idx1<len(list1):
		sortedList.extend(list1[idx1:])
		return sortedList
	else:
		sortedList.extend(list2[idx2:])
		return sortedList

print(merge([1,23,5],[6,2,1]))
print("derp")
print(sort([]))
print(sort([1]))
print(sort([1,2]))
print(sort([2,1]))
print(sort([3,2,1]))
print(sort([1,3,2]))
print(sort([4,3,2,1]))
print(sort([45,12,99,7,2,4,6,5]))