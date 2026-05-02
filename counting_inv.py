def count_inv(arr):
  if len(arr)<=1:
    return arr, 0
  mid = len(arr)//2
  left = arr[:mid]
  right = arr[mid:]

  left_sorted, left_inv = count_inv(left)
  right_sorted, right_inv = count_inv(right)
  merge, split_inv = merge_and_count(left_sorted, right_sorted)
  total_inv = left_inv + right_inv + split_inv

  return merge, total_inv

def merge_and_count(left, right):
  i = j = inv_count = 0
  merged = []
  while i<len(left) and j<len(right):
    if left[i] <= right[j]:
      merged.append(left[i])
      i+=1
    else:
      merged.append(right[j])
      inv_count+= len(left) - i
      j+=1
  merged.extend(left[i:])
  merged.extend(right[j:])

  return merged, inv_count
