import random
import matplotlib.pyplot as plt


def monte_carlo_pi(num_points):
    inside_circle = 0
    for _ in range(num_points):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    return 4 * inside_circle / num_points


def visualize_monte_carlo(num_points):
    inside_x, inside_y = [], []
    outside_x, outside_y = [], []
    for _ in range(num_points):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_x.append(x)
            inside_y.append(y)
        else:
            outside_x.append(x)
            outside_y.append(y)
    plt.figure(figsize=(6, 6))
    plt.scatter(inside_x, inside_y, color="blue", s=1, label="Inside Circle")
    plt.scatter(outside_x, outside_y, color="red", s=1, label="Outside Circle")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend(loc="upper right")
    plt.title(f"Monte Carlo Pi Approximation with {num_points} Points")
    plt.show()


num_points = int(input("Enter the number of points to use for the approximation: "))
pi_estimate = monte_carlo_pi(num_points)
print(f"Approximation of Pi with {num_points} points: {pi_estimate}")
# Uncomment below to visualize
# visualize_monte_carlo(num_points)
