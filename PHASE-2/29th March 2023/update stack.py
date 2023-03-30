def update_stack(stack):
    smallest = min(stack)
    updated_stack = []
    for val in stack:
        if val != smallest:
            updated_stack.append(val)
    for i in range(stack.count(smallest)):
        updated_stack.append(smallest)
    stack[:] = updated_stack[::-1]

stack = [5, 66, 587]
update_stack(stack)
print(stack)  
