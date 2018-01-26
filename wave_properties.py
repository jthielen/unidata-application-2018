# Wave Properties Helper Functions

import numpy as np
from datetime import datetime, timedelta


def get_minima_indicies(array):
    return (np.diff(np.sign(np.diff(array))) > 0).nonzero()[0] + 1


def get_maxima_indicies(array):
    return (np.diff(np.sign(np.diff(array))) < 0).nonzero()[0] + 1


def get_increments(previous_extrema, current_extrema):
    # Make sure these are cast as lists
    previous_extrema = list(previous_extrema)
    current_extrema = list(current_extrema)

    # Adjust for overflow
    current_extrema = cycle_adjust(previous_extrema, current_extrema)

    increments = []
    for lon in current_extrema:
        # Find closest extrema in previous, and assume continuation
        prev_lon = min(previous_extrema, key=lambda x:abs(x-lon))
        increments.append(lon - prev_lon)

    return np.array(increments)


def cycle_adjust(previous_extrema, current_extrema):
    # Bump up an overflowed element
    if min(current_extrema) < min(previous_extrema)/2:
        # If the the new lowest element is closer to zero than it is to the previous lowest,
        # assume it is an overflow
        overflowed = current_extrema.pop(0)
        current_extrema.append(overflowed + 360.)
        
    return current_extrema


def reject_outliers(data):
    d = data - np.median(data)
    iqr = np.percentile(d, 75) - np.percentile(d, 25)
    iqr = iqr if iqr > 0 else 1.

    return data[np.abs(d) < 1.5 * iqr]


def fraction_of_day(td):
    return td / np.timedelta64(1, 'D')
