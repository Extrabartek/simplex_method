import numpy as np
import math as m


def state_dot_matrix():
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


dt = 0.01

x_k_k = np.array([1, 1, 1, 1])
uk = np.array([1, 1, 1])
uk1 = np.array([1, 1, 1])
uk2 = np.array([1, 1, 1])
uk3 = np.array([1, 1, 1])

k1 = x_k_k @ uk
k2 = (x_k_k + k1 * dt / 2) @ uk1
k3 = (x_k_k + k2 * dt / 2) @ uk2
k4 = (x_k_k + k3 * dt) @ uk3

x_k_k1 = x_k_k + (k1 + 2 * k2 + 2 * k3 + k4) * dt / 6
