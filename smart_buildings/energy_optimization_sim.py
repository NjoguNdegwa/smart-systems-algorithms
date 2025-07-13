import numpy as np

def simulate(building_temp, outside_temp, target_temp, iterations=10):
    energy_cost = 0
    for _ in range(iterations):
        delta = target_temp - building_temp
        building_temp += 0.1 * delta + 0.05 * (outside_temp - building_temp)
        energy_cost += abs(delta) * 0.5
    return building_temp, energy_cost

if __name__ == "__main__":
    final_temp, cost = simulate(building_temp=18, outside_temp=10, target_temp=22)
    print(f"Final temp: {final_temp:.2f}°C | Energy cost: {cost:.2f}")
