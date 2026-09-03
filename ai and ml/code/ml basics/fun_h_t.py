import random
import matplotlib.pyplot as plt

# Ask user for number of flips
n = int(input("Enter number of coin flips: "))

heads_prob = []
tails_prob = []
h_count = 0
t_count = 0

for i in range(1, n+1):
    toss = random.choice(["H", "T"])
    if toss == "H":
        h_count += 1
    else:
        t_count += 1

    heads_prob.append(h_count / i)
    tails_prob.append(t_count / i)

# Plot probabilities
plt.figure()
plt.plot(range(1, n+1), heads_prob, label="Probability of Heads")
plt.plot(range(1, n+1), tails_prob, label="Probability of Tails")
plt.xlabel("Number of Tosses")
plt.ylabel("Probability")
plt.title("Probability of Heads and Tails Over Tosses")
plt.legend()
plt.show()

print("Final Heads:", h_count)
print("Final Tails:", t_count)