import matplotlib.pyplot as plt

# Data for Pure CUDA
particles_cuda = [10, 100, 1000, 10000, 50000, 100000, 200000, 500000, 800000]
time_cuda = [1311.72, 1216.87, 1284.31, 1713.44, 5082.04, 8604.86, 16529, 39150.9, 59583.4]

# Data for Thrust
particles_thrust = [10, 100, 1000, 10000, 50000, 100000, 200000, 500000, 800000]
time_thrust = [1321.67, 1202.45, 2330.96, 2690.48, 5477.41, 10795.2, 19267.7, 45110.1, 67188.4]

# Data for Python
particles_python = [1, 10, 100, 1000]
time_python = [540, 5620, 55090, 567600]

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(particles_cuda, time_cuda, marker='o', label='Pure CUDA')
plt.plot(particles_thrust, time_thrust, marker='s', label='Thrust')
plt.plot(particles_python, time_python, marker='^', label='Python')

# Adding labels and title
plt.xlabel('Number of Particles')
plt.ylabel('Execution Time (ms)')
plt.title('Execution Time vs Number of Particles for Different Programs')
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.grid(True, which="both", ls="--")
plt.show()
