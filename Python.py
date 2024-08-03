import numpy as np
import matplotlib.pyplot as plt
import threading
import time

# Constants
q = 1.0  # Charge of the particle
m = 1.0  # Mass of the particle
Bz = 1.0  # Magnetic field in the z-direction

# Time parameters
t0 = 0.0  # Initial time
tf = 10.0  # Final time
dt = 0.001  # Time step
num_steps = int((tf - t0) / dt)  # Number of time steps

def lorentz_force(v, B):
    return q * np.cross(v, B)

def rk4_step(r, v, dt):
    B = np.array([0, 0, Bz])
    k1_r = v
    k1_v = lorentz_force(v, B) / m

    k2_r = v + 0.5 * dt * k1_v
    k2_v = lorentz_force(v + 0.5 * dt * k1_v, B) / m

    k3_r = v + 0.5 * dt * k2_v
    k3_v = lorentz_force(v + 0.5 * dt * k2_v, B) / m

    k4_r = v + dt * k3_v
    k4_v = lorentz_force(v + dt * k3_v, B) / m

    r_next = r + (dt / 6) * (k1_r + 2*k2_r + 2*k3_r + k4_r)
    v_next = v + (dt / 6) * (k1_v + 2*k2_v + 2*k3_v + k4_v)

    return r_next, v_next

def simulate_particle(index, r0, v0, positions_all, velocities_all):
    r = r0
    v = v0
    positions = np.zeros((num_steps, 3))
    velocities = np.zeros((num_steps, 3))
    
    for i in range(num_steps):
        positions[i] = r
        velocities[i] = v

        r, v = rk4_step(r, v, dt)
    
    positions_all[index] = positions
    velocities_all[index] = velocities

# Function to measure execution time for a given number of particles
def measure_execution_time(num_particles):
    positions_all = np.zeros((num_particles, num_steps, 3))
    velocities_all = np.zeros((num_particles, num_steps, 3))

    # Generate unique initial conditions for each particle
    initial_conditions = [(np.array([1.0, 0.0, 0.0]) + 0.1*np.random.randn(3),
                           np.array([0.0, 1.0, 0.0]) + 0.1*np.random.randn(3)) for _ in range(num_particles)]

    # Measure start time
    start_time = time.time()

    # Create threads for each particle
    threads = []
    for i in range(num_particles):
        r0, v0 = initial_conditions[i]
        thread = threading.Thread(target=simulate_particle, args=(i, r0, v0, positions_all, velocities_all))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Measure end time
    end_time = time.time()

    # Calculate and return the execution time
    execution_time = end_time - start_time
    return execution_time

# Number of particles to test
num_particles_list = [1, 10, 100, 1000, 10000]
execution_times = []

# Measure execution time for each number of particles
for num_particles in num_particles_list:
    execution_time = measure_execution_time(num_particles)
    execution_times.append(execution_time)
    print(f"Execution Time for {num_particles} particles: {execution_time:.2f} seconds")

# Plotting the results
plt.figure(figsize=(10, 5))
plt.plot(num_particles_list, execution_times, marker='o')
plt.xlabel('Number of Particles')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time vs Number of Particles')
plt.grid(True)
plt.show()
