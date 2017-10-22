#!/usr/bin/env python
import sys
import numpy as np
import slmgen

# try:
#     import slmgen
# except ImportError:
#     from os.path import dirname, join
#     from os import pardir
#     sys.path.append(join(dirname(__file__), pardir))
#     import slmgen


def main():
    binary, sample, annulus = slmgen.linear_bessel_array(pattern_only=False)
    assert np.allclose(0.081422659413112178, binary.std())
    assert np.allclose(0.99332580566406248, binary.mean())
    assert np.allclose(263242524012.73526, sample.std())
    assert np.allclose(24425585968.797722, sample.mean())
    assert np.allclose(1080564.3878853747, annulus.std())
    assert np.allclose(14884.92777634431, annulus.mean())

    binary, sample, annulus = slmgen.hex_lattice(pattern_only=False)
    assert np.allclose(0.14246046093792242, binary.std())
    assert np.allclose(0.97927551269531254, binary.mean())
    assert np.allclose(158283805034.7933, sample.std())
    assert np.allclose(24141289655.596405, sample.mean())
    assert np.allclose(1654057.3464906327, annulus.std())
    assert np.allclose(22978.027036855601, annulus.mean())
    print("Tests passed")


if __name__ == "__main__":
    sys.exit(main())
