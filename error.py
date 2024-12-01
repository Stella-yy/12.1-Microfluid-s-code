import pandas as pd
import numpy as np

# Provided data
data_dict = {
    "Height_px": [751, 58, 313, 246, 536, 999, 1288, 811, 902, 1240, 1053, 1323, 560, 1295, 1017, 753, 110, 692, 352, 650, 1109, 991, 259, 975, 22, 1293, 1083, 95, 655, 732, 254, 936, 1241],
    "Length_px": [190, 55, 148, 83, 166, 150, 61, 135, 122, 63, 125, 51, 159, 45, 118, 141, 67, 175, 127, 184, 107, 98, 122, 134, 43, 67, 118, 79, 241, 144, 161, 127, 109],
    "Height_um": [326.52, 25.22, 136.09, 106.96, 233.04, 434.35, 560.00, 352.61, 392.17, 539.13, 457.83, 575.22, 243.48, 563.04, 442.17, 327.39, 47.83, 300.87, 153.04, 282.61, 482.17, 430.87, 112.61, 423.91, 9.57, 562.17, 470.87, 41.30, 284.78, 318.26, 110.43, 406.96, 539.57],
    "Length_um": [82.61, 23.91, 64.35, 36.09, 72.17, 65.22, 26.52, 58.70, 53.04, 27.39, 54.35, 22.17, 69.13, 19.57, 51.30, 61.30, 29.13, 76.09, 55.22, 80.00, 46.52, 42.61, 53.04, 58.26, 18.70, 29.13, 51.30, 34.35, 104.78, 62.61, 70.00, 55.22, 47.39],
    "Velocity_mm_s": [1.49, 0.43, 1.16, 0.65, 1.31, 1.18, 0.48, 1.06, 0.96, 0.50, 0.98, 0.40, 1.25, 0.35, 0.93, 1.11, 0.53, 1.38, 1.00, 1.45, 0.84, 0.77, 0.96, 1.05, 0.34, 0.53, 0.93, 0.62, 1.89, 1.13, 1.27, 1.00, 0.86],
}

# Constants for scale and uncertainty
scale_px = 460
scale_um = 200
delta_scale_px = 1  # Uncertainty in scale (px)
delta_scale_um = 1  # Uncertainty in scale (um)
delta_time = 0.1  # Uncertainty in time (s)
delta_length_px = 1  # Measurement error in length (px)
delta_height_px = 1  # Measurement error in height (px)

# Calculate uncertainties
heights_px = np.array(data_dict["Height_px"])
lengths_px = np.array(data_dict["Length_px"])
heights_um = np.array(data_dict["Height_um"])
lengths_um = np.array(data_dict["Length_um"])
velocities_mm_s = np.array(data_dict["Velocity_mm_s"])

# Uncertainty in height (um)
delta_height_um = heights_um * (
    (delta_scale_px / scale_px) + (delta_scale_um / scale_um)
)

# Uncertainty in length (um)
delta_length_um = lengths_um * (
    (delta_length_px / lengths_px) + (delta_scale_um / scale_um)
)

# Uncertainty in velocity (mm/s)
delta_velocity = velocities_mm_s * (
    (delta_length_um / lengths_um) + (delta_time / 1)  # Assuming 1s measurement time
)

# Compile results
error_data = {
    "Height_px": heights_px,
    "Height_um": heights_um,
    "Delta_Height_um": delta_height_um,
    "Length_px": lengths_px,
    "Length_um": lengths_um,
    "Delta_Length_um": delta_length_um,
    "Velocity_mm_s": velocities_mm_s,
    "Delta_Velocity_mm_s": delta_velocity,
}

error_df = pd.DataFrame(error_data)

# Save the results to an Excel file
error_file_path = "Users/yueyu/Downloads/errors.xlsx"
error_df.to_excel(error_file_path, index=False)

error_file_path