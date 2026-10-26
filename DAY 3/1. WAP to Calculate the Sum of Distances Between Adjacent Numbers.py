def sum_of_distances(arr):
    total_distance = 0

    for i in range(len(arr) - 1):
        total_distance += abs(arr[i] - arr[i + 1])

    return total_distance

print(sum_of_distances([10, 11, 7, 12, 14]))