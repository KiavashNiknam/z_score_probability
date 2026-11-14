
import math

# Given values
mean = 1019
std = 209
score = 820

# Calculate Z-score
z = (score - mean) / std

# Calculate cumulative probability
probability = 0.5 * (1 + math.erf(z / math.sqrt(2)))

# Convert probability to percentage
percent = probability * 100

# Display results
print("Z Score:", z)
print("Probability:", probability)
print("Percentage:", percent, "%")
