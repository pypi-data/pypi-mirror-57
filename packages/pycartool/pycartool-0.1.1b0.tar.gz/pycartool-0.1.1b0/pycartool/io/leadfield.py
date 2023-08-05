# -*- coding: utf-8 -*-
# Authors: Victor Férat <victor.ferat@live.fr>
#
# License: BSD (3-clause)
import struct
import numpy as np


def read_lf(filename):
    """Read Cartool leadfield matrix.

    Parameters
    ----------
    filename : str or file-like
        The leadfield file (.lf) to read.

    Returns
    -------
    leadfield_matrix : numpy.ndarray, shape (n_channels, n_sources, 3)
        the leadfield matrix.

    """
    with open(filename, 'rb') as f:
        byte = f.read(4)
        number_of_electrodes = struct.unpack('i', byte)[0]
        byte = f.read(4)
        number_of_solution_points = struct.unpack('i', byte)[0]
        buf = f.read(number_of_electrodes * number_of_solution_points*8)
        data = np.frombuffer(buf, dtype=np.double)
    number_of_points = int(number_of_solution_points/3)
    leadfield_matrix = data.reshape(number_of_electrodes, number_of_points, 3)
    return(leadfield_matrix)
