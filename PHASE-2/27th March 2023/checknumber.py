def check_numbers(number_queue):
    solution_queue1=Queue(5)
    while(not number_queue.is_empty()):
        status=0
        element=num_queue.dequeue()
        for i in range(1,11):
            if element%i!=0:
                status=1
                break
        if status==0:
            solution_queue1.enqueue(element)
    return solution_queue1
