import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def load_positions(filename, num_particles, num_timesteps):
    positions = np.fromfile(filename, dtype=np.float32)
    positions = positions.reshape((num_timesteps, num_particles, 3))
    return positions

def plot_trajectories(positions):
    num_timesteps, num_particles, _ = positions.shape
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for i in range(num_particles):
        ax.plot(positions[:, i, 0], positions[:, i, 1], positions[:, i, 2], label=f'Particle {i+1}')

    ax.set_xlabel('X position')
    ax.set_ylabel('Y position')
    ax.set_zlabel('Z position')
    ax.set_title('Charged Particles Trajectory in a Uniform Magnetic Field')
    ax.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    num_particles = 10
    num_timesteps = 10000

    positions = load_positions('particle_positions.bin', num_particles, num_timesteps)
    plot_trajectories(positions)
