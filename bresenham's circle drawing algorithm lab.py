import matplotlib.pyplot as plt

def draw_circle(radius):
    x = 0
    y = radius
    p = 1 - radius  # Initial decision parameter

    # Lists to store the x and y coordinates of the circle
    x_values = []
    y_values = []

    # Plot the initial point in all octants
    x_values.extend([x, -x, x, -x])
    y_values.extend([y, y, -y, -y])

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        if x > y:
            break  # To avoid duplicate points

        # Plot points in all octants
        x_values.extend([x, -x, x, -x, y, -y, y, -y])
        y_values.extend([y, y, -y, -y, x, x, -x, -x])

    # Plot the circle using matplotlib
    plt.scatter(x_values, y_values, marker='.')
    plt.axis('equal')
    plt.title('Bresenham Circle Drawing Algorithm')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid()
    plt.show()

# Example usage:
radius = 10
draw_circle(radius)
