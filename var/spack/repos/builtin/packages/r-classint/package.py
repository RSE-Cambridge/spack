# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RClassint(RPackage):
    """Selected commonly used methods for choosing univariate class intervals
       for mapping or other graphics purposes."""

    homepage = "https://cloud.r-project.org/package=classInt"
    url      = "https://cloud.r-project.org/src/contrib/classInt_0.1-24.tar.gz"
    list_url = "https://cloud.r-project.org/src/contrib/Archive/classInt"

    version('0.4-1', sha256='39c63f8e37b379033d73d57929b5b8ea41b0023626cc1cec648d66bade5d0103')
    version('0.3-3', sha256='a93e685ef9c40d5977bb91d7116505a25303b229897a20544722a94ea1365f30')
    version('0.3-1', sha256='e2e6f857b544dfecb482b99346aa3ecfdc27b4d401c3537ee8fbaf91caca92b9')
    version('0.1-24', '45f1bde3ec7601ce17c99189be5c0fd5')

    depends_on('r@2.2:', type=('build', 'run'))
    depends_on('r-e1071', type=('build', 'run'))
    depends_on('r-class', type=('build', 'run'))
    depends_on('r-kernsmooth', type=('build', 'run'))
