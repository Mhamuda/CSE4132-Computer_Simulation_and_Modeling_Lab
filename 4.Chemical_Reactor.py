import matplotlib.pyplot as plt

def chemical_reactor(A, B, C, k1, k2, end_time, dt):
    time = 0
    substance_A = []
    substance_B = []
    substance_C = []
    time_points = []

    while (time <= end_time):
        substance_A.append(A)
        substance_B.append(B)
        substance_C.append(C)
        time_points.append(time)
        time += dt

        A += (k2 * C - k1 * A * B) * dt
        B += (k2 * C - k1 * A * B) * dt
        C += (2 * k1 * A *B - 2 * k2 * C) * dt

        plt.clf()
        plt.title("Simulation of Chemical Reactor")
        plt.xlabel("Time (s)")
        plt.ylabel("Quantity (gm)")
        plt.xlim(0, end_time)
        plt.plot(time_points, substance_A, label = "Substance A")
        plt.plot(time_points, substance_B, label = "Substance B")
        plt.plot(time_points, substance_C, label = "Substance C")
        plt.legend()
        plt.grid()
        plt.pause(0.001)
    
    plt.show()

def main():
    #initial quantities of substance
    a, b, c = 100, 50, 0

    #rate constant
    k1, k2 = 0.008, 0.002
    dt = 0.1
    end_time = 10

    chemical_reactor(a, b, c, k1, k2, end_time, dt)

if __name__ == "__main__": #
    main()