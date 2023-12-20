from matplotlib import pyplot as plt
import math

def draw_plot(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.title('Projectile motion of a ball')

def frange(start,end, increment):
    numbers = []
    while start < end:
        numbers.append(start)
        start += increment
    return numbers

def draw_trajectory(u, theta):
    theta = math.radians(theta)
    g = 9.8

    # Time of flight
    t_flight = 2 * u * math.sin(theta) / g

    intervals = frange(0, t_flight, 0.001)

    x = []
    y = []

    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 1/2*g*t**2)

    print("Time of flight: {0}".format(t_flight))
    print('Length: {0}'.format(max(x)))
    print('Hieght: {0}'.format(max(y)))


    draw_plot(x, y)

    return x, y

if __name__ == '__main__':
    trajec_num = int(input('How many trajectories do you want to print? '))
    for i in range(trajec_num):
        try:
            u = float(input('Enter the initial velocity (m/s): '))
            theta = float(input('Enter the angle of projection (degrees): '))
        except ValueError:
            print('You entered an invlaid input. ')
        else:
            draw_trajectory(u, theta)
plt.show()
