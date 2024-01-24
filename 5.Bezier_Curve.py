import matplotlib.pyplot as plt
import numpy as np

def read_coordinates_from_file(file_name):
    coordinates = np.loadtxt(file_name, unpack=True)
    return coordinates

def factorial(n):
    if(n):
        return n * factorial(n - 1)
    else:
        return 1
    
def nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

def BEZ(k, n, u):
    return nCr(n, k) * u ** k * (1-u) ** (n-k)

def bezier_curve(x_controlPoints, y_controlPoints):
    n = len(x_controlPoints) - 1
    eps = 0.01  # step size
    x_curvePoints = []
    y_curvePoints = []
    u = 0

    while (u < 1 + eps):
        x, y = 0, 0

        for k in range(len(x_controlPoints)):
            bez = BEZ(k, n, u)
            x += x_controlPoints[k] * bez   #
            y += y_controlPoints[k] * bez

        x_curvePoints.append(x)
        y_curvePoints.append(y)
        u += eps

        plt.clf()
        plt.title("Bezier Curve")
        plt.plot(x_controlPoints, y_controlPoints, marker = "o", label = "Control Graph")
        plt.plot(x_curvePoints, y_curvePoints, label = "Bezier Curve")
        plt.legend()
        plt.grid()
        plt.pause(0.01)
    
    plt.show()

def main():
    x_controlPoints, y_controlPoints = read_coordinates_from_file("bezier_curve_input.txt")
    bezier_curve(x_controlPoints, y_controlPoints)

if __name__ == "__main__":
    main()


# P(u) = summation from k = 0 to n (P_k * BEZ (k, n, u)) ; 0<=u<=1
# BEZ(k, n, u) = C(n,k) * u^k * (1-u)^(n-k)