import argparse
import random
from itertools import product

N_COMPANY = 50
L_FIELD = 10000
Q_MAX = 10**8


def get_args() -> argparse.Namespace:
    # Define aguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--seed', type=int, default=2021)
    args = parser.parse_args()
    return args


def main(args: argparse.Namespace):
    # set_seed
    random.seed(args.seed)
    n = int(N_COMPANY * 4**random.random())
    n = 200

    xy_cand = list(product(range(L_FIELD), range(L_FIELD)))
    xy = random.sample(xy_cand, n)
    q_cand = list(range(1, Q_MAX))
    q = [0] + sorted(random.sample(q_cand, n)) + [Q_MAX]

    print(n)
    for i, (xi, yi) in enumerate(xy):
        ri = q[i + 1] - q[i]
        print(xi, yi, ri)


if __name__ == '__main__':
    args = get_args()
    main(args)
