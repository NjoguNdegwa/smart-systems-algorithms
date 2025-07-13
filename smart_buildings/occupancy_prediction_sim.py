# smart_buildings/occupancy_prediction_sim.py

import numpy as np
import matplotlib.pyplot as plt

def generate_occupancy_data(hours=24):
    return [
        int(5 + 10 * np.sin(np.pi * hour / 12) + np.random.randint(0, 3))
        for hour in range(hours)
    ]

def simulate_energy_usage(occupancy):
    base_load = np.random.uniform(5, 10, len(occupancy))
    return [base + occ * 1.2 for base, occ in zip(base_load, occupancy)]

if __name__ == '__main__':
    occupancy = generate_occupancy_data()
    energy = simulate_energy_usage(occupancy)

    plt.plot(occupancy, label='Occupancy')
    plt.plot(energy, label='Energy Usage')
    plt.legend()
    plt.title("Simulated Smart Building: Occupancy vs. Energy Usage")
    plt.xlabel("Hour of Day")
    plt.ylabel("Value")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
