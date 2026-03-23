import argparse
import numpy as np
from scipy.constants import g
from tyre_model import TyreModel
from constant import SIDE_FORCE_COEFFS, BRAKE_FORCE_COEFFS
from plotter import plot_forces


def compute_vertical_load(vehicle_mass=1500.0):
    return (vehicle_mass * g) / 4.0  # per wheel

def main():
    parser = argparse.ArgumentParser(description="Magic Formula Tyre Simulation")
    parser.add_argument("weight", type=float, help="Vehicle mass in kg")
    parser.add_argument("--mu", type=float, default=1.0, help="Friction coefficient")
    parser.add_argument("--slip_angle", type=float, default=0.0, help="Slip angle in degrees")
    args = parser.parse_args()

    tyre_model = TyreModel()
    vertical_load = compute_vertical_load(args.weight)

    slip_range = np.linspace(0, 100, 100) / 100.0  # normalized 0–1
    side_forces = []
    brake_forces = []

    for slip in slip_range:
        fx = tyre_model.compute_force(slip, BRAKE_FORCE_COEFFS, vertical_load)
        fy = tyre_model.compute_force(slip, SIDE_FORCE_COEFFS, vertical_load)

        brake_forces.append(fx * args.mu)
        side_forces.append(fy * args.mu)

    plot_forces(slip_range * 100, side_forces, brake_forces, slip_angle_deg=args.slip_angle)

if __name__ == "__main__":
    main()
