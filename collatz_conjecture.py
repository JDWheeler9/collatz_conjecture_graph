# Import
import matplotlib.pyplot as plt


# Finds the number of loops it takes to complete the Collatz Conjecture
def collatz_finder(x):
    loopNumbers = 0
    while x != 1 and x != 0:
        if x % 2 == 0:
            x = int(x / 2)
        else:
            x = int(3 * x + 1)
        loopNumbers += 1
    return loopNumbers

# Main Function
x_list = []
y_list = []
for collatzNum in range(1, 100000):
    x_list.append(collatzNum)
    y_list.append(collatz_finder(collatzNum))

# Plotting the numbers
plt.scatter(x_list, y_list)
plt.title('Numbers vs Their Collatz Conjecture Loops')
plt.ylabel('Number of Loops')
plt.xlabel('Collatz Number')
plt.axis([1, 100000, 0, 500])
plt.show()
