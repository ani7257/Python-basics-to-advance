#Practice3
def merge_queues(queue1, queue2):
    len1 = len(queue1)
    len2 = len(queue2)
    merged_queue = []
    for i in range(min(len1, len2)):
        merged_queue.append(queue1[i])
        merged_queue.append(queue2[i])
    if len1 > len2:
        merged_queue += queue1[len2:]
    elif len2 > len1:
        merged_queue += queue2[len1:]
    return merged_queue
queue1 = [3, 6, 8]
queue2 = ['b', 'y', 'u', 't', 'r', 'o']
merged_queue = merge_queues(queue1, queue2)
print(merged_queue)  # Output: [3, 'b', 6, 'y', 8, 'u', 't', 'r', 'o']'''


                    
