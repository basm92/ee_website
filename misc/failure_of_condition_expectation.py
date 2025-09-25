import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style for better aesthetics
sns.set_style("whitegrid")

# --- 1. Simulation Setup ---
# For reproducibility
np.random.seed(42) 

# Number of observations
n = 5000 

# Generate X from a standard normal distribution (mean=0, variance=1)
X = np.random.randn(n)

# Construct the error term u = X^2 - E[X^2]
# Since X is standard normal, E[X^2] = Var(X) + (E[X])^2 = 1 + 0^2 = 1
u = X**2 - 1


# --- 2. Verify the Conditions ---

# Condition 1: Is E[u] = 0?
mean_u = np.mean(u)
print(f"Sample Mean of u (approximates E[u]): {mean_u:.4f}")
print("This is very close to the theoretical value of 0.")
print("-" * 50)


# Condition 2: Is E[uX] = 0? (i.e., are they uncorrelated?)
# Since E[u] is approx 0, Cov(u, X) = E[(u - E[u])(X - E[X])] ≈ E[uX]
mean_uX = np.mean(u * X) 
# An even better way is to calculate the sample covariance directly
covariance_uX = np.cov(u, X)[0, 1]

print(f"Sample Mean of u*X (approximates E[uX]): {mean_uX:.4f}")
print(f"Sample Covariance of u and X: {covariance_uX:.4f}")
print("Both are very close to the theoretical value of 0, showing they are uncorrelated.")
print("-" * 50)


# --- 3. Visualize the Failure of E[u|X] = 0 ---

print("Now, let's visualize the relationship between u and X.")
print("If E[u|X]=0 were true, the scatter plot should show no discernible pattern.")

# Create the plot
plt.figure(figsize=(10, 6))

# Scatter plot of X vs u
plt.scatter(X, u, alpha=0.3, label='Sample data points (X, u)')

# Plot the theoretical conditional mean: E[u|X] = X^2 - 1
x_vals = np.linspace(X.min(), X.max(), 100)
y_vals_conditional_mean = x_vals**2 - 1
plt.plot(x_vals, y_vals_conditional_mean, color='red', linewidth=3, label='True Conditional Mean: $E[u|X] = X^2 - 1$')

# Add a horizontal line at y=0 for reference
plt.axhline(0, color='black', linestyle='--', label='If $E[u|X]=0$ were true')

# Add labels and title
plt.title('Demonstration: $E[u]=0$ and $E[uX]=0$ does NOT imply $E[u|X]=0$', fontsize=14)
plt.xlabel('X', fontsize=12)
plt.ylabel('u', fontsize=12)
plt.legend()
plt.ylim(-2, 8) # Adjust y-axis for better visibility
plt.show()