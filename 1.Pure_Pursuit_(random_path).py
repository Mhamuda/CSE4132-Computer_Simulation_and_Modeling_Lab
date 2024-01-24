import matplotlib.pyplot as plt
import numpy as np

def generate_random_path(length) :
    return np.random.uniform(0, 100, length)

def pure_pursuit():
    length = int(input("Enter the length of the path: "))
    x_bomber = generate_random_path(length)
    y_bomber = generate_random_path(length)

    xf =  np.random.uniform(0, 100)
    yf =  np.random.uniform(0, 100)
    fighter_speed = 20

    x_fighter = []
    y_fighter = []
    time = 0
    escape_distance, caught_distance = 900, 10

    while True:
        x_fighter.append(xf)
        y_fighter.append(yf)

        plt.clf()
        plt.title("Simulation of a Pure Pursuit")
        plt.plot(x_fighter, y_fighter, marker = "o", color = "red", label = "Fighter")
        plt.plot(x_bomber[0: time+1], y_bomber[0: time+1], marker = "o", color = "green", label = "Bomber")
        plt.xlim(-100, 200)
        plt.ylim(-100, 100)
        plt.legend()    
        plt.grid()
        plt.pause(1)    # pause the figure 1 second

        distance = ((xf - x_bomber[time])**2 + (yf - y_bomber[time])**2)**0.5

        if distance <= caught_distance:
            print(f"Target caught at time {time} second.")
            break
        
        if distance > escape_distance or time > len(x_bomber):
            print(f"Target escape at time {time} second.")
            break

        sin = (y_bomber[time] - yf) / distance
        cos = (x_bomber[time] - xf) / distance
        time += 1
        xf += fighter_speed * cos
        yf += fighter_speed * sin
    plt.show()

def main():
    pure_pursuit()

if __name__ == "__main__":
    main()