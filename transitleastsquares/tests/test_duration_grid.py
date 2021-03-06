from __future__ import division, print_function
import numpy
from transitleastsquares import period_grid, duration_grid

if __name__ == "__main__":
    print("Starting test: duration_grid...", end="")
    periods = period_grid(
        R_star=1,  # R_sun
        M_star=1,  # M_sun
        time_span=20,  # days
        period_min=0,
        period_max=999,
        oversampling_factor=3,
    )
    durations = duration_grid(periods, log_step=1.05, shortest=2)
    numpy.testing.assert_almost_equal(max(durations), 0.12)
    numpy.testing.assert_almost_equal(min(durations), 0.011618569353576557)
    numpy.testing.assert_equal(len(durations), 49)
    print("passed")
