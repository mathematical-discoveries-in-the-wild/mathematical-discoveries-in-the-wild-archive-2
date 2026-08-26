"""Finite Fourier checks for the two periodic-profile counterexamples."""

import numpy as np


def cross_spectrum(w, h_of_w, psi_plus, psi_minus):
    n = w.size
    c = np.fft.fft(w) / n
    a = np.fft.fft(h_of_w) / n
    freqs = np.fft.fftfreq(n) * n
    total = 0.0j
    for idx, k in enumerate(freqs.astype(int)):
        if k > 0:
            total += a[idx] * np.conj(psi_plus * c[idx])
        elif k < 0:
            total += a[idx] * np.conj(psi_minus * c[idx])
    return total


def source_prediction(w, h_of_w, psi_plus, psi_minus):
    mean = np.mean(w)
    return np.mean(h_of_w * np.conj((psi_plus + psi_minus) * (w - mean)))


n = 4096
s = np.arange(n) / n

square = np.where(s < 0.5, 1.0, -1.0).astype(complex)
print("square corrected:", cross_spectrum(square, square, 1.0, 1.0))
print("square source:   ", source_prediction(square, square, 1.0, 1.0))

positive_wave = np.exp(2j * np.pi * s)
print("one-sided corrected:", cross_spectrum(positive_wave, positive_wave, 0.0, 1.0))
print("one-sided source:   ", source_prediction(positive_wave, positive_wave, 0.0, 1.0))
