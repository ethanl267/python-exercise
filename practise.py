list1 = [3, 6, 9, 12, 15, 18, 21]                                                   # make your first list 
list2 = [4, 8, 12, 16, 20, 24, 28]                                                  # make your second list 
list3 = []                                                                          # make a list that has no  values

odd_index = list1 [1::2]                                                            # allow your first list to extract odd elements 
print("elements of odd-index from list1")                                           # print a statement that tells you to extract elements from your first list
print(odd_index)                                                                    # print odd_index


even_index = list2 [0::2]                                                           # allow your second list to extract even elements
print("elements of even_index from list2")                                          # print a statement that tells you to extract elements from your second list
print(even_index)                                                                   # print even_index  

list3 = [odd_index + even_index]                                                    # add your odd and even index into your list3
print(list3)                                                                        # print list3


list =  [34, 54, 67, 89, 11, 43, 94]

no_index = list.pop(4)
print("list after removing index 4")
print(list)
print("\n")

list.insert(2 , 11)
print("List after Adding element at index 2")
print(list)
print("\n")

list.append(11)
print("List after Adding element at last")
print(list)
print("\n")


list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
chunk_1 = [11 , 45 , 8]
print(chunk_1[::-1])
print("\n")

Chunk_2 = [23, 14, 12]
print(Chunk_2[::-1])
print("\n")


Chunk_3 = [78, 45, 89]
print(Chunk_3[::-1])
print("\n")



list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

list_dict = dict()
for i in list:
  if(i in list_dict):
    list_dict[i] += 1
  else:
    list_dict[i] = 1
  
print("Printing count of each item  ",list_dict)
print("\n")


First_List = [2, 3, 4, 5, 6, 7, 8]
Second_List = [4, 9, 16, 25, 36, 49, 64]

output = [[a, b] for a in First_List 
          for b in Second_List if a != b] 
print(output)
print("\n")


 nums1 = [65, 42, 78, 83, 23, 57, 29]
 nums2 = [67, 73, 43, 48, 83, 57, 29]

def intersection(nums2, nums2):
  return set([i for i in nums2 if i in set(nums1)])

  print(intersection(nums1, nums2))






firstSet  = {57, 83, 29}
secondSet = {57, 83, 29, 67, 73, 43, 48}

print("First Set ", firstSet)
print("Second Set ", secondSet)

print("First set is subset of second set -", firstSet.issubset(secondSet))
print("Second set is subset of First set - ", secondSet.issubset(firstSet))

print("First set is Super set of second set - ", firstSet.issuperset(secondSet))
print("Second set is Super set of First set - ", secondSet.issuperset(firstSet))

if(firstSet.issubset(secondSet)):
  firstSet.clear()
  
if(secondSet.issubset(firstSet)):
  secondSet.clear()

print("First Set ", firstSet)
print("Second Set ", secondSet)
print("\n")



selectnum = [47, 64, 69, 37, 76, 83, 95, 97]
Dict ={'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

print("List -", selectnum)
print("Dictionary - ", Dict)

selectnum[[:] = [item for item in selectnum if item in Dict.values()]
print("after removing unwanted elemnts from list ", selectnum)












