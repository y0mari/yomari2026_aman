import matplotlib.pyplot as plt

def plot_forces(slip_values, side_forces, brake_forces, slip_angle_deg=0):
    plt.figure(figsize=(8, 5))
    plt.plot(slip_values, side_forces, label="Side Force Fy")
    plt.plot(slip_values, brake_forces, label="Brake Force Fx")
    plt.xlabel("Longitudinal Slip [%]")
    plt.ylabel("Force [N]")
    plt.title(f"Tyre Forces at Slip Angle α = {slip_angle_deg}°")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    file_name = f"tyre_forces_alpha{slip_angle_deg}.png"
    plt.savefig(file_name)
    plt.close()
    print(f"Plot saved as {file_name}")
