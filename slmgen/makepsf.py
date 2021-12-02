from scipy import special
from math import sqrt
import numpy as np


def tuplecheck(val):
    """ for all things that require design and experimental value...   """

    # if it's a single number, exp/design are the same, return 2-tuple
    if isinstance(val, (float, int)):
        return (val, val)
    # otherwise it's a tuple with len == 1 | 2
    elif isinstance(val, tuple):
        # exp/design are the same, return 2-tuple
        if len(val) == 1:
            return (val[0], val[0])
        elif len(val) == 2:
            return val
    raise ValueError("Must be either int, float, or tuple of length 1/2: %s" % val)


def makePSF(
    wavelength=0.525,
    NA=1.4,
    nx=257,
    nz=257,
    dx=0.02,
    dz=0.02,
    RI=1.33,
    immRI=1.5,
    csRI=1.515,
    csthick=170,
    workingdistance=150,
    particledistance=0,
    num_basis=200,
    num_samples=1000,
    oversampling=1,
):
    # dx/dz are output pixel sizes in microns
    # RI is refractive index of sample
    # workingdistance in microns, working distance (immersion medium thickness) design value
    # particledistance in microns, particle distance from coverslip
    # Size of the PSF array, pixels

    ny = nx  # square ... not really necessary until this becomes 3D again

    ni, ni0 = tuplecheck(immRI)  # immersion medium RI experimental value, design value
    ng, ng0 = tuplecheck(csRI)  # coverslip RI experimental value, design value
    tg, tg0 = tuplecheck(
        csthick
    )  # coverslip thickness experimental value, design value

    # Precision control
    # num_basis    = 100      # Number of rescaled Bessels that approximate the phase function
    # num_samples  = 1000     # Number of pupil samples along radial direction
    # oversampling = 2        # Defines the upsampling ratio on the image space grid for computations

    # Scaling factors for the Fourier-Bessel series expansion
    min_wavelength = 0.436  # microns
    scaling_factor = (
        NA * (3 * np.arange(1, num_basis + 1) - 2) * min_wavelength / wavelength
    )

    # Place the origin at the center of the final PSF array
    x0 = (nx - 1) / 2
    y0 = (ny - 1) / 2

    # Find the maximum possible radius coordinate of the PSF array by finding the distance
    # from the center of the array to a corner
    max_radius = round(sqrt((nx - x0) * (nx - x0) + (ny - y0) * (ny - y0))) + 1

    # Radial coordinates, image space
    r = dx * np.arange(0, oversampling * max_radius) / oversampling

    # Radial coordinates, pupil space
    a = min([NA, RI, ni, ni0, ng, ng0]) / NA
    rho = np.linspace(0, a, num_samples)

    # Stage displacements away from best focus
    z = dz * np.arange(-nz / 2, nz / 2) + dz / 2

    # Define the wavefront aberration
    NArho2 = NA ** 2 * rho ** 2
    OPDs = particledistance * np.sqrt(RI ** 2 - NArho2)  # OPD in the sample
    OPDi = (z.reshape(-1, 1) + workingdistance) * np.sqrt(
        ni ** 2 - NArho2
    ) - workingdistance * np.sqrt(
        ni0 ** 2 - NArho2
    )  # OPD in the immersion medium
    OPDg = tg * np.sqrt(ng ** 2 - NArho2) - tg0 * np.sqrt(
        ng0 ** 2 - NArho2
    )  # OPD in the coverslip
    W = 2 * np.pi / wavelength * (OPDs + OPDi + OPDg)

    # Sample the phase
    # Shape is (number of z samples by number of rho samples)
    phase = np.cos(W) + 1j * np.sin(W)

    # Define the basis of Bessel functions
    # Shape is (number of basis functions by number of rho samples)
    J = special.jv(0, scaling_factor.reshape(-1, 1) * rho)

    # Compute the approximation to the sampled pupil phase by finding the least squares
    # solution to the complex coefficients of the Fourier-Bessel expansion.
    # Shape of C is (number of basis functions by number of z samples).
    # Note the matrix transposes to get the dimensions correct.
    C, residuals, _, _ = np.linalg.lstsq(J.T, phase.T, rcond=None)

    # Which z-plane to compute
    # z0 = 24

    # The Fourier-Bessel approximation
    # est = J.T.dot(C[:, z0])

    b = 2 * np.pi * r.reshape(-1, 1) * NA / wavelength

    def J0(x):
        return special.jv(0, x)

    def J1(x):
        return special.jv(1, x)

    # See equation 5 in Li, Xue, and Blu
    denom = scaling_factor * scaling_factor - b * b
    R = (
        scaling_factor * J1(scaling_factor * a) * J0(b * a) * a
        - b * J0(scaling_factor * a) * J1(b * a) * a
    )
    R /= denom

    # The transpose places the axial direction along the first dimension of the array, i.e. rows
    # This is only for convenience.
    PSF_rz = (np.abs(R.dot(C)) ** 2).T

    # Normalize to the maximum value
    PSF_rz /= np.max(PSF_rz)

    return PSF_rz
