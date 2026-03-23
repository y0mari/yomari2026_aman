import math

class TyreModel:
    def __init__(self):
        pass

    def compute_force(self, slip_value=0.0, coeffs=None, vertical_load=0.0):
        if coeffs is None:
            raise ValueError("Coeffs dictionary is required")

        peak_d = coeffs["a1"] * vertical_load**2 + coeffs["a2"] * vertical_load
        shape_c = coeffs["C"]
        stiffness_b = (
            coeffs["a3"] * math.sin(coeffs["a4"] * math.atan(coeffs["a5"] * vertical_load))
        ) / (shape_c * peak_d)
        curvature_e = coeffs["a6"] * vertical_load**2 + coeffs["a7"] * vertical_load + coeffs["a8"]

        phi_value = (1.0 - curvature_e) * slip_value + (curvature_e / stiffness_b) * math.atan(stiffness_b * slip_value)
        force_value = peak_d * math.sin(shape_c * math.atan(stiffness_b * phi_value))

        return force_value
