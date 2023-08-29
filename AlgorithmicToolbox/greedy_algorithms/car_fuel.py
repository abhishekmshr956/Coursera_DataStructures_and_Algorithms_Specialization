from sys import stdin

# def optimal_fuel_tank(current_f_index, max_travel, n_fueltanks, fueltanks):
#     fueltank_index = None
#     for i in range(current_f_index, n_fueltanks):
#         if fueltanks[i] <= max_travel:
#             fueltank_index = i
#         else:
#             return fueltank_index
#     return fueltank_index

def optimal_fuel_tank(current_f_index, max_travel, n_fueltanks, fueltanks):
    fueltank_index = current_f_index
    for i in range(current_f_index + 1, n_fueltanks):
        if fueltanks[i] - fueltanks[current_f_index] <= max_travel:
            fueltank_index = i
        else:
            break
    return fueltank_index

def number_refill(distance, tank_capacity, n_fueltanks, fueltanks):
    car_pos = 0
    fueltank_index = -1
    n_refill = 0

    while car_pos < distance:
        max_travel = car_pos + tank_capacity
        optimal_fuel_tank_index = optimal_fuel_tank(fueltank_index, max_travel, n_fueltanks, fueltanks)
        
        if optimal_fuel_tank_index == fueltank_index:
            return -1
        if optimal_fuel_tank_index == n_fueltanks - 1:
            break
        
        car_pos = fueltanks[optimal_fuel_tank_index]
        fueltank_index = optimal_fuel_tank_index
        n_refill += 1
    
    return n_refill


# def number_refill(distance, tank_capacity, n_fueltanks, fueltanks):
#     car_pos = 0
#     fueltank_index = -1
#     n_refill = 0

#     while car_pos < distance:
#         max_travel = car_pos + tank_capacity
#         optimal_fuel_tank_index = optimal_fuel_tank(fueltank_index, max_travel, n_fueltanks, fueltanks)
#         if max_travel >= distance:
#             return n_refill
        
#         if optimal_fuel_tank_index == current_f_index:
#             return -1
#         if optimal_fuel_tank_index == None:
#             return -1
#         car_pos = fueltanks[optimal_fuel_tank_index]
#         current_f_index = optimal_fuel_tank_index
#         n_refill += 1
    

if __name__ == '__main__':
    # print(optimal_fuel_tank(0, 3, 4, [1, 2, 5, 9]))
    # print(optimal_fuel_tank(1, 5, 4, [1, 2, 5, 9]))
    # print(optimal_fuel_tank(2, 8, 4, [1, 2, 5, 9]))

    data = list(map(int, stdin.read().split()))
    distance = data[0]
    tank_capacity = data[1]
    n_fueltanks = data[2]
    fueltanks = data[3:]
    n_refill = number_refill(distance, tank_capacity, n_fueltanks, fueltanks)
    print(int(n_refill))

    # print(distance, tank_capacity, n_fueltanks, fueltanks)