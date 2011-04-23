#! /usr/bin/python
# -*- coding: utf-8 -*-

import brian

tau = 20 * brian.msecond 
Vt = -50 * brian.mvolt
Vr = -60 * brian.mvolt
El = -60 * brian.mvolt

N = 40

G = brian.NeuronGroup(N=N, model='dV/dt = -(V-El)/tau : volt' , threshold=Vt, reset=Vr)
M = brian.SpikeMonitor(G)

G.V = Vr + 2*(Vt-Vr)*brian.rand(N)

brian.run(1 * brian.second)

print M.nspikes
