arr = [1,2,3,4,5,6,4,12,9,3,2,1,9]
def slidingwindow(arr, k):
    total = sum(arr[:k])
    max_total = total
    for i in range(len(arr)-k):
        total-=arr[i]
        total+=arr[i+k]
        max_total = max(max_total, total)

    return max_total

print(slidingwindow(arr, 4))