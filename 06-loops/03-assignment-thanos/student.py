# write your code here
def thanos(queue_size, target_size):
    count = 0
    while queue_size > target_size:
        if (queue_size % 2) != 0:
            queue_size -= int(queue_size / 2)
        else:
            queue_size = queue_size / 2
        count +=1
        
    return count

