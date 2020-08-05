def bubblesort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
num = int(input('Enter the no to be entered: '))
arr = [int(input()) for i in range(num)]
bubblesort(arr)
n = len(arr)
print('The sorted arr is: ')
for i in range(n):
    print('%d'%arr[i])