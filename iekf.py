import numpy as np
import math as m


def state_dot(u: np.array):
    return (np.array([[1, 0, 0],
                      [0, 1, 0],
                      [0, 0, 1],
                      [0, 0, 0]]) @ u).reshape(4, 1)


def output(state: np.array):
    return np.array([[m.atan2(state[2], state[0]) * (1 + state[3])],
                     [m.atan2(state[1], m.sqrt(state[0] ** 2 + state[2] ** 2))],
                     [m.sqrt(state[0] ** 2 + state[1] ** 2 + state[2] ** 2)], ])


def output_diff(state: np.array, d_state: np.array):
    return (np.array([[-state[2] * (state[3] + 1) / (state[0] ** 2 + state[2] ** 2), 0,
                       state[0] * (state[3] + 1) / (state[0] ** 2 + state[2] ** 2), m.atan2(state[2], state[0])],
                      [-state[0] * state[1] / (m.sqrt(state[0] ** 2 + state[2] ** 2) * (
                              state[0] ** 2 + state[1] ** 2 + state[2] ** 2)),
                       m.sqrt(state[0] ** 2 + state[2] ** 2) / (state[0] ** 2 + state[1] ** 2 + state[2] ** 2),
                       -state[1] * state[2] / (m.sqrt(state[0] ** 2 + state[2] ** 2) * (
                               state[0] ** 2 + state[1] ** 2 + state[2] ** 2)), 0],
                      [state[0] / m.sqrt(state[0] ** 2 + state[1] ** 2 + state[2] ** 2),
                       state[1] / m.sqrt(state[0] ** 2 + state[1] ** 2 + state[2] ** 2),
                       state[2] / m.sqrt(state[0] ** 2 + state[1] ** 2 + state[2] ** 2), 0]
                      ]) @ d_state).reshape(3, 1)


print(output_diff(np.array([1, 1, 1, 1]), np.array([1, 1, 1, 1])))
