import numpy as np
import numba
import time


@numba.guvectorize(["void(float64[:], float64[:], float64[:])"], "(n),(n)->()", target='parallel')
def fast_cosine_gufunc(u, v, result):
    m = u.shape[0]
    udotv = 0
    u_norm = 0
    v_norm = 0
    for i in range(m):
        if (np.isnan(u[i])) or (np.isnan(v[i])):
            continue

        udotv += u[i] * v[i]
        u_norm += u[i] * u[i]
        v_norm += v[i] * v[i]

    u_norm = np.sqrt(u_norm)
    v_norm = np.sqrt(v_norm)

    if (u_norm == 0) or (v_norm == 0):
        ratio = 1.0
    else:
        ratio = udotv / (u_norm * v_norm)
    result[:] = ratio


if __name__ == '__main__':
    start = time.time()
    vec = np.random.rand(300)
    matrix = np.random.rand(3000, 300)

    data = fast_cosine_gufunc(vec, matrix)
    print(data)

    end = time.time()
    print(f'running time {end-start}')
