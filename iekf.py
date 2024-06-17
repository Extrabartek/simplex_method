import sympy as sp


class KalmanEquations:
    states: dict[str, sp.Symbol]
    measurements: dict[str, sp.Symbol]
    inputs: dict[str, sp.Symbol]

    state_equations: list
    measurement_equations: list

    states = {}
    measurements = {}
    inputs = {}

    state_equations = []
    measurement_equations = []
    input_equations = []

    def __init__(self, states, measurements, inputs):
        for state in states:
            self.states[state] = sp.Symbol(state)
        for measurement in measurements:
            self.measurements[measurement] = sp.Symbol(measurement)
        for INPUT in inputs:
            self.inputs[INPUT] = sp.Symbol(INPUT)

        self.state_equations = []
        self.measurement_equations = []

    def define_state_equations(self):
        self.state_equations = [self.inputs['u_dot'],
                                self.inputs['v_dot'],
                                self.inputs['w_dot'],
                                0.0]

    def define_output_equations(self):
        self.measurement_equations = [self.measurements['alpha_m'] / (
                sp.atan2(self.states['w'], self.states['u']) * (1 + self.states['C_alpha_up'])),
                                      sp.atan2(self.states['v'],
                                               (sp.sqrt(self.states['u'] ** 2 + self.states['w'] ** 2))),
                                      sp.sqrt(self.states['u'] ** 2 + self.states['v'] ** 2 + self.states['w'] ** 2)]


class IeKF:
    base_equations: KalmanEquations

    nominal_state: list
    nominal_output: list

    def __init__(self, base_equations):
        self.base_equations = base_equations
        self.nominal_state = []
        self.nominal_output = []

    def nominal_state(self, state_vector: dict[str, float]):
        for i in range(len(self.base_equations.state_equations)):
            self.nominal_state.append(self.base_equations.state_equations[i].evalf(subs=state_vector))
            self.nominal_output.append(self.base_equations.measurement_equations[i].evalf(subs=state_vector))


kalman_eqs = KalmanEquations(['u', 'v', 'w', 'C_alpha_up'],
                             ['alpha_m', 'beta_m', 'V_m'],
                             ['u_dot', 'v_dot', 'w_dot'])

kalman_eqs.define_state_equations()
kalman_eqs.define_output_equations()

print(kalman_eqs.state_equations)
print(kalman_eqs.measurement_equations)
