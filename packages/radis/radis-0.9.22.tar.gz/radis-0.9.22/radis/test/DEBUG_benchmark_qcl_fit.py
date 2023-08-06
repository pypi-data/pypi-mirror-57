# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:39:29 2019

@author: erwan
"""

from radis import Spectrum, experimental_spectrum, SpectrumFactory, plot_diff

#s_exp = experimental_spectrum('benchmark_qcl_fit.txt')
s_exp = Spectrum.from_txt('benchmark_qcl_fit.txt', 'transmittance_noslit', 'cm-1', 'I/I0',
                          delimiter=',')


sf = SpectrumFactory(2252.92, 2254.04,
                     isotope='1,2,3',
                     wstep=0.001,
                     broadening_max_width=0.1,
                     pressure=0.020,  # N/A. Just guessed
                     path_length=7,   # N/A. Just guessed
                     verbose=3,
                     )
sf.load_databank('HITEMP-CO2-DUNHAM')

s = sf.non_eq_spectrum(Trot=605, Tvib=(647, 647, 1085))
plot_diff(s_exp, s)
