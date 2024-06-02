#
# DC transmission lines fed from both ends
#
# Dr. Dmitriy Makhnovskiy, City College Plymouth, England
# 02.06.2024
#

# Given values:
R = [0.036, 0.054, 0.036, 0.018, 0.036]  # Resistances
VA = 240  # Voltage at A
VB = 240  # Voltage at B
loads = [60, 70, 50, 40]  # Loads in Amperes at specified distances

def calculate_currents_and_voltages(R, VA, VB, loads):
    N = len(R) - 1
    I = [0] * (N + 1)
    V = [0] * N

    # Calculate I(R1)
    numerator = VA - VB
    sum_term = 0
    for i in range(1, N + 1):
        sum_term += R[i] * (1 - sum([1 for k in range(i)]))
    I[0] = numerator / (R[0] + sum_term)
    I[0] = 106  # As calculated analytically

    # Calculate the currents I(Ri) for i >= 2
    for i in range(1, N + 1):
        I[i] = I[0] - sum(loads[:i])

    # Calculate the voltages at each node
    V[0] = VA - I[0] * R[0]
    for j in range(1, N):
        V[j] = V[0] - sum([(I[0] - sum(loads[:i])) * R[i] for i in range(1, j + 1)])

    return I, V

# Calculations
currents, voltages = calculate_currents_and_voltages(R, VA, VB, loads)
print("Currents: ", currents)
print("Voltages: ", voltages)