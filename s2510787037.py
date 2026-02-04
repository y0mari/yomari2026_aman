import argparse
import numpy as np
from scipy.constants import g 
from tyre_model import TyreModel
from constants import SIDE_FORCE_COEFFS, BRAKE_FORCE_COEFFS
from plotter import plot_forces

def compute_vertical_load(vechile_mass=1500.0):
    return(vechile_mass*g)/ 4.0
def main():
    arg_parse_ = argparse.ArgumentParser(
        description="Magic formula Tyre simulation"
    )
    arg_parse_.add_argument(
        "weight",
        type=float,
        required=True,
        help="Vechile mass in kg"
    )
    args_ = arg_parse_.parse_args()
    tyre_model = TyreModel()
    vertical_load = compute_vertical_load(args_.weight)
    slip_range = np.linspace(0.0, 100.00, 100)
    side_force_value =[]
    brake_force_values =[]
    for slip_value in slip_range:
        fx = tyre_model.compute_force(
            slip_range/ 100.0,
            BRAKE_FORCE_COEFFS,
            vertical_load
        )
        fy = tyre_model.compute_force(
            args_.slip,
            SIDE_FORCE_COEFFS,
            vertical_load
        )
        brake_force_values.append(fx * args_.mu)
        side_force_value.append(fy * args_.mu)
        plot_forces(
        slip_range,
        side_force_value,
        args_.slip
        
    
        )
        if __name__ =="__main__":
            main()
