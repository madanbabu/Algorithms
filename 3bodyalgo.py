import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


class Body:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = np.array(position)
        self.velocity = np.array(velocity)


def gravitational_force(bodies):
    # Get positions as a single array
    positions = np.array([body.position for body in bodies])

    # Calculate pairwise distances in one go
    distances = np.linalg.norm(positions[:, None] - positions[None], axis=-1)

    # Avoid division by zero for self-acceleration
    distances[np.diag_indices_from(distances)] = 1.0

    # Calculate forces using vectorized operations
    forces = np.sum(-bodies[:, None].mass * (positions[:, None] - positions[None]) / (distances**3), axis=1)
    return forces


def simulate(bodies, dt, steps):
    def deriv(state, t):
        # Unpack state
        positions, velocities = state.reshape(-1, 3, 2)
        # Calculate accelerations
        accelerations = gravitational_force(Body(*zip(*row))) for row in positions
        return np.vstack((velocities, accelerations))

    # Initial state as combined positions and velocities
    state0 = np.vstack([body.position for body in bodies] + [body.velocity for body in bodies])
    t = np.linspace(0, dt * steps, steps + 1)

    # Solve ODE using Runge-Kutta method
    state = odeint(deriv, state0, t)

    # Separate positions and velocities from the solution
    positions, velocities = state.T[:3], state.T[3:]
    return positions, velocities


def main():
    # Define initial conditions (modify as needed)
    bodies = [
        Body(10, [-10, 10, -11], [-3, 0, 0]),
        Body(20, [0, 0, 0], [0, 0, 0]),
        Body(30, [10, 10, 12], [3, 0, 0]),
    ]
    dt = 0.01  # Time step
    steps = 10000  # Number of steps

    positions, velocities = simulate(bodies, dt, steps)

    # Plot the trajectories of the first 1000 positions for clarity
    plt.figure(figsize=(10, 6))
    for i in range(3):
        plt.plot(positions[:1000, i], label=f"Body {i+1}")
