# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):

	largest = i # Initialize largest as root
	l = 2 * i + 1	 # left = 2*i + 1
	r = 2 * i + 2	 # right = 2*i + 2

	# See if left child of root exists and is
	# greater than root
	if l < n and arr[i] < arr[l]:
		largest = l

	# See if right child of root exists and is
	# greater than root
	if r < n and arr[largest] < arr[r]:
		largest = r

	# Change root, if needed
	if largest != i:
		arr[i],arr[largest] = arr[largest],arr[i] # swap

		# Heapify the root.
		heapify(arr, n, largest)

# The main function to sort an array of given size
def heapSort(arr):
	n = len(arr)

	# Build a maxheap.
	for i in range((n//2) - 1, -1, -1):
		heapify(arr, n, i)

	# One by one extract elements
	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] # swap
		heapify(arr, i, 0)

# Driver code to test above
arr = [ 5, 6, 7,12,3]
heapSort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n):
	print (arr[i],end=" "),
# This code is contributed by Mohit Kumra

# def heapSortDriver(arr,n,newarr):
#     # print("Main function arr",arr," n is ",n)
#     # print("N is-------------------- ", n)
#     if n<1:
#         return arr
#     # print("test")
#     arr=heapSort2(arr,n)
#     newarr[n-1]=arr[n-1]
#     # arr=arr[:n-1]
#     #
#     final= heapSortDriver(arr[:n-1],n-1,newarr)
#     return newarr
#     # print("Final Array",arr)
#
#
# def heapSort2(arr,n):
#
#     for i in range ((n//2)-1,-1,-1):
#         # print("i is ",i)
#         # print("array before calling the heapify",arr)
#         arr= heapify(arr,n,i)
#         # print("count")
#     arr[0], arr[-1] = arr[-1], arr[0]
#     # print("array in heapsort", arr)
#     return arr
#
# def heapify(arr,n,i):
#     parent=arr[i]
#     leftindex=2 * i + 1
#     rightindex=2*i+2
#     # print("left index",leftindex)
#     # print("Right index",rightindex)
#     # # print("test1")
#
#     if leftindex <n and rightindex<n:
#         # print("Both If statements")
#         rightChild = arr[2 * i + 2]
#         leftChild = arr[(2 * i) + 1]
#
#         if rightChild>leftChild:
#             max=rightChild
#             index=2*i+2
#         else:
#             max=leftChild
#             index = 2 * i + 1
#         if max>parent:
#             arr[index],arr[i]=arr[i],arr[index]
#         # print("new arr in heapify",arr)
#         # return arr
#     elif leftindex <n:
#         # print("Only Left If")
#         leftChild = arr[(2 * i) + 1]
#         if leftChild>parent:
#             # print("testing")
#             arr[leftindex],arr[i]=arr[i],arr[leftindex]
#             # print("executed")
#     else:
#         # print("Only Right if")
#         rightChild = arr[2 * i + 2]
#         if rightChild>parent:
#             arr[rightindex], arr[parent] = arr[parent], arr[rightindex]
#     return arr
#
#
#
# # arr=[4,10,3,5,1,6,8]
# arr=[4,10,3,5,1,6,15,14,13,17,16,29,12,46]
# # print("left",arr[13])
# # print("Parent",arr[6])
# # arr=[2,1]
# n=len(arr)
# newarr=[0]*n
# print(heapSortDriver(arr,n,newarr))