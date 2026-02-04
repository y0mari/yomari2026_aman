import mathplot.ppylot as plt
def plot_force(
        slip_values,
        slide_forces,
        brake_forces,
        slip_angle_deg
):
 
    plt.figure(figsize=(8,5))
    plt.plot(slip_values, slide_forces, label="slide force Fy")
    plt.plot(slip_values, brake_forces, label="brake force Fx")
    plt.xlabel("Longitudinal slip K [%]")
    plt.xlabel("Force [N]")
    plt.title(f"Tyre Forces at slip angle a = {slip_angle_deg} ")
    plt.legend()
    plt.grind(True)
    plt.tight_layout()
    file_name= f"tyre_forces_alpha{slip_angle_deg}.png"
    plt.savefig(file_name)
    plt.close()