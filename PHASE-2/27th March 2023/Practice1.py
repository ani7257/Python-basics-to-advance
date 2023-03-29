#Practice1
def num(queue):
    div_q= []
    for num in queue:
        if all(num %i == 0 for i in range(1,11)):
            div_q.append(num)
    return div_q
input_queue=[13983, 10080, 7113, 2520, 2500]
output_queue=num(input_queue)
print(output_queue)



