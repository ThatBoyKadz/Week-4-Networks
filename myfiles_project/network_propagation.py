import random
import time

# -----------------------------
# Network Structure (Graph)
# -----------------------------
# Each computer is a node; edges represent network connections
network = {
    "PC1": ["PC2", "PC3"],
    "PC2": ["PC1", "PC4"],
    "PC3": ["PC1", "PC5"],
    "PC4": ["PC2"],
    "PC5": ["PC3", "PC6"],
    "PC6": ["PC5"]
}

# Starting infected machine
infected = {"PC1"}   # initial infection source

# Infection probability (per neighbor)
INFECTION_CHANCE = 0.4   # 40% chance of spreading to each connected PC per step


def simulate_step(infected_nodes):
    """Simulate one round of network propagation."""
    new_infections = set()

    for node in infected_nodes:
        neighbors = network.get(node, [])
        for neighbor in neighbors:
            if neighbor not in infected_nodes:
                if random.random() < INFECTION_CHANCE:
                    new_infections.add(neighbor)

    return new_infections


print("\n=== Network Propagation Simulation ===\n")
print(f"Initial infected machine: {infected}\n")

step = 1
while True:
    print(f"--- Step {step} ---")
    print(f"Currently infected: {infected}")

    newly_infected = simulate_step(infected)

    if not newly_infected:
        print("\nNo further infections. Propagation stopped.")
        break

    print(f"New infections this step: {newly_infected}\n")

    infected.update(newly_infected)

    time.sleep(1)  # slow down the simulation
    step += 1

print("\nFinal infected machines:", infected)
