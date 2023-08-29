def optimal_fuel_tank(current_f_index, max_travel, n_fueltanks, fueltanks):
    fueltank_index = current_f_index
    for i in range(current_f_index + 1, n_fueltanks):
        if fueltanks[i] - fueltanks[current_f_index] <= max_travel:
            fueltank_index = i
        else:
            break
    return fueltank_index

def min_refills(distance, tank_capacity, fueltanks):
    n_fueltanks = len(fueltanks)
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

if __name__ == '__main__':
    from sys import stdin
    
    d, m, _, *stops = map(int, stdin.read().split())
    result = min_refills(d, m, stops)
    print(result)
