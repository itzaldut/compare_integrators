import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import pandas as pd


def f(x):
    return np.sin(100*x)/x

exact_integral, _ = quad(f, 0.01, 1)

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        total += 2 * f(a + i * h)
    return (h / 2) * total

def simpson_rule(f, a, b, n):
    if n % 2 != 0:
      raise ValueError("n must be even for Simpson's rule, received n = {}".format(n))
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    fx = f(x)
    result = (h / 3) * (fx[0] + 2 * fx[2:n:2].sum() + 4 * fx[1:n:2].sum() + fx[n])
    return result

def gauss_legendre_quad(f, a, b, n):
    nodes, weights = np.polynomial.legendre.leggauss(n)  # roots of Legendre polynomial and weights :contentReference[oaicite:0]{index=0}

    # Map nodes from [-1,1] to [a, b]
    x_mapped = 0.5 * (b - a) * nodes + 0.5 * (b + a)

    # Apply weights and function evaluations
    integral = 0.5 * (b - a) * np.dot(weights, f(x_mapped))
    return integral

# Integration settings
a, b = 0.01, 1.0
I_exact = exact_integral

# List of N values to test
N_values = np.array(np.arange(2,2000, 100))  # 4, 8, 16, ..., 512

errors_trap = []
errors_simp = []
errors_gauss = []

for N in N_values:
    I_trap = trapezoidal_rule(f, a, b, N)
    I_simp = simpson_rule(f, a, b, N)
    I_gauss = gauss_legendre_quad(f, a, b, N)

    errors_trap.append(abs(I_trap - I_exact))
    errors_simp.append(abs(I_simp - I_exact))
    errors_gauss.append(abs(I_gauss - I_exact))

eps_floor = 1e-16
errors_gauss = np.maximum(errors_gauss, eps_floor)
# Plotting
plt.figure(figsize=(8, 6))
plt.loglog(N_values, errors_trap, label='Trapezoidal')
plt.loglog(N_values, errors_simp, label='Simpson')
plt.loglog(N_values, errors_gauss, label = 'Gaussian', nonpositive='clip')


plt.xlabel('Number of intervals $N$ (log scale)')
plt.ylabel('Absolute error (log scale)')
plt.title('Error Convergence: Trapezoidal, Simpson, and Gauss Quadrature')
plt.legend()
plt.grid(True, which='both', ls='--')
plt.savefig('BadErrors.png')
plt.show()
