import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return np.array([[mandelbrot(complex(r, i), max_iter) for r in r1] for i in r2])

def display(xmin, xmax, ymin, ymax, width=800, height=800, max_iter=100):
    mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
    plt.figure(figsize=(10, 10))
    plt.imshow(mandelbrot_image, extent=(xmin, xmax, ymin, ymax), cmap='inferno')
    plt.colorbar(label='Iterations to escape')
    plt.title("Mandelbrot Set")
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.show()

# Example usage
display(-2.0, 1.0, -1.5, 1.5)
