import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Constants for uncertainties
delta_L_px = 1  # Uncertainty in pixel length
delta_Scale_px = 1  # Uncertainty in Scale_px
delta_Scale_um = 1  # Uncertainty in Scale_um
delta_t_ms = 0.1  # Uncertainty in time (ms)

# Scale values (constants for the dataset)
Scale_px = 460  # Scale in pixels
Scale_um = 200  # Scale in micrometers

# Dataset (Height and Velocity Information)
data = {
    "t_ms": [53.1] * 34,  # Time in milliseconds
    "height_px": [
        751, 58, 313, 246, 536, 999, 1288, 811, 902, 1240, 1053, 1323, 560, 1295, 1017, 753, 110, 692, 352, 650,
        1109, 991, 259, 975, 22, 1293, 1083, 95, 655, 732, 254, 936, 1241
    ],
    "length_px": [
        190, 55, 148, 83, 166, 150, 61, 135, 122, 63, 125, 51, 159, 45, 118, 141, 67, 175, 127, 184, 107, 98,
        122, 134, 43, 67, 118, 79, 241, 144, 161, 127, 109
    ],
    "height_um": [
        326.5217391, 25.2173913, 136.0869565, 106.9565217, 233.0434783, 434.3478261, 560, 352.6086957, 392.173913,
        539.1304348, 457.826087, 575.2173913, 243.4782609, 563.0434783, 442.173913, 327.3913043, 47.82608696,
        300.8695652, 153.0434783, 282.6086957, 482.173913, 430.8695652, 112.6086957, 423.9130435, 9.565217391,
        562.173913, 470.8695652, 41.30434783, 284.7826087, 318.2608696, 110.4347826, 406.9565217, 539.5652174
    ],
    "length_um": [
        82.60869565, 23.91304348, 64.34782609, 36.08695652, 72.17391304, 65.2173913, 26.52173913, 58.69565217,
        53.04347826, 27.39130435, 54.34782609, 22.17391304, 69.13043478, 19.56521739, 51.30434783, 61.30434783,
        29.13043478, 76.08695652, 55.2173913, 80, 46.52173913, 42.60869565, 53.04347826, 58.26086957, 18.69565217,
        29.13043478, 51.30434783, 34.34782609, 104.7826087, 62.60869565, 70, 55.2173913, 47.39130435
    ],
    "velocity_mm_s": [
        1.555719315, 0.450339802, 1.211823467, 0.679603701, 1.359207402, 1.22819946, 0.49946778, 1.105379514,
        0.99893556, 0.515843773, 1.02349955, 0.417587816, 1.301891427, 0.368459838, 0.966183575, 1.154507492,
        0.548595759, 1.43289937, 1.039875542, 1.506591337, 0.876115615, 0.802423647, 0.99893556, 1.097191517,
        0.352083845, 0.548595759, 0.966183575, 0.646851715, 1.973307132, 1.179071481, 1.31826742, 1.039875542,
        0.892491607
    ]
}

# Convert data into arrays
height_px = np.array(data["height_px"])
height_um = np.array(data["height_um"])
length_px = np.array(data["length_px"])
length_um = np.array(data["length_um"])
velocity_mm_s = np.array(data["velocity_mm_s"])
t_ms = np.array(data["t_ms"])

# Partial derivatives for height uncertainty
dH_dHpx = Scale_um / Scale_px
dH_dScalePx = -(Scale_um * height_px) / (Scale_px**2)
dH_dScaleUm = height_px / Scale_px

# Height uncertainty calculation
delta_height_um = np.sqrt(
    (dH_dHpx * delta_L_px)**2 +
    (dH_dScalePx * delta_Scale_px)**2 +
    (dH_dScaleUm * delta_Scale_um)**2
)

# Partial derivatives for velocity uncertainty
dv_dL = 1 / t_ms  # Use time directly in milliseconds
dv_dt = -length_um / (t_ms**2)

# Velocity uncertainty calculation
delta_velocity_mm_s = np.sqrt(
    (dv_dL * delta_height_um[:len(velocity_mm_s)])**2 +
    (dv_dt * delta_t_ms)**2
)

# Plotting Velocity vs. Height with Error Bars
plt.figure(figsize=(10, 6))
plt.errorbar(
    height_um, velocity_mm_s, xerr=delta_height_um[:len(velocity_mm_s)],
    yerr=delta_velocity_mm_s, fmt='o', ecolor='orange', capsize=3, label='Data with Error Bars'
)
plt.title("Velocity vs Height with Error Bar for Syringe at 80mm Height")
plt.xlabel("Height (µm)")
plt.ylabel("Velocity (mm/s)")
plt.legend()
plt.grid(True)
plt.show()
