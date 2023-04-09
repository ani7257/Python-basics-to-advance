#Problem3
child_id = (10, 20, 30, 40, 50)
chocolates_received = [12, 5, 3, 4, 6]

def calculate_total_chocolates():
    total_chocolates = sum(chocolates_received)
    return total_chocolates

def reward_child(child_id_rewarded, extra_chocolates):
    if extra_chocolates < 1:
        print("Error: Extra chocolates is less than 1")
        return
    
    if child_id_rewarded not in child_id:
        print("Error: Child ID is invalid")
        return
    
    child_index = child_id.index(child_id_rewarded)
    chocolates_received[child_index] += extra_chocolates
    print(chocolates_received)
    
total_chocolates = calculate_total_chocolates()
print("Total number of chocolates received:", total_chocolates)
reward_child(20, 3)  

