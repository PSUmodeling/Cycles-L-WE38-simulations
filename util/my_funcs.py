#!/usr/bin/env python3

import numpy as np
from pihm import read_mesh

def nse(obs, sim):
    obs = np.array(obs)
    sim = np.array(sim)

    return 1.0 - (((obs - sim)**2).sum()) / (((obs - obs.mean())**2).sum())

def read_cycles(simulation):
    with open(f'../input/{simulation}/sim/{simulation}.cycles') as f:
        strs = [line.strip() for line in f if line.strip() and line.strip()[0] != '#']

    num_elem, _, _, _, _, _, _ = read_mesh('..', simulation)

    mgmt = []
    for line in strs[1:1 + num_elem]:
        mgmt.append(int(line.split()[1]))

    return num_elem, np.array(mgmt)
