import numpy as np
import math as m


def state_dot_matrix(u: np.array):
    return np.array([[1, 0, 0],
                      [0, 1, 0],
                      [0, 0, 1],
                      [0, 0, 0]])


def output_matrix(state: np.array):
    return np.array([[m.atan2(state[2], state[0]) * (1 + state[3])],
                     [m.atan2(state[1], m.sqrt(state[0] ** 2 + state[2] ** 2))],
                     [m.sqrt(state[0] ** 2 + state[1] ** 2 + state[2] ** 2)], ])


def output_diff_matrix(state: np.array):
    return np.array([[-state[2] * (state[3] + 1) / (state[0] ** 2 + state[2] ** 2), 0,
                       state[0] * (state[3] + 1) / (state[0] ** 2 + state[2] ** 2), m.atan2(state[2], state[0])],
                      [-state[0] * state[1] / (m.sqrt(state[0] ** 2 + state[2] ** 2) * (
                              state[0] ** 2 + state[1] ** 2 + state[2] ** 2)),
                       m.sqrt(state[0] ** 2 + state[2] ** 2) / (state[0] ** 2 + state[1] ** 2 + state[2] ** 2),
                       -state[1] * state[2] / (m.sqrt(state[0] ** 2 + state[2] ** 2) * (
                               state[0] ** 2 + state[1] ** 2 + state[2] ** 2)), 0],
                      [state[0] / m.sqrt(state[0] ** 2 + state[1] ** 2 + state[2] ** 2),
                       state[1] / m.sqrt(state[0] ** 2 + state[1] ** 2 + state[2] ** 2),
                       state[2] / m.sqrt(state[0] ** 2 + state[1] ** 2 + state[2] ** 2), 0]
                      ])


print(output_diff_matrix(np.array([1, 1, 1, 1])))
