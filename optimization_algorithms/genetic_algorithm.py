import random

def fitness(x):
    return -(x**2) + 10  # Max at x=0

def mutate(x):
    return x + random.uniform(-1, 1)

def genetic_algorithm(generations=50, population_size=10):
    population = [random.uniform(-10, 10) for _ in range(population_size)]
    for _ in range(generations):
        population.sort(key=fitness, reverse=True)
        best = population[:2]
        population = best + [mutate(random.choice(best)) for _ in range(population_size - 2)]
    return population[0]

if __name__ == "__main__":
    solution = genetic_algorithm()
    print(f"Best solution: x = {solution}, fitness = {fitness(solution)}")
