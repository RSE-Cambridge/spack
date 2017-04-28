##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Pmix(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "http://www.example.com"
    url      = "https://raw.githubusercontent.com/pmix/tarballs/master/pmix-1.1.1.tar.bz2"

    version('1.1.1', '6146c15645a9b71314b20c997a0ff6af')

    depends_on('hwloc')
    depends_on('libevent')
    depends_on('munge')

    def configure_args(self):
        args = [
            "--with-hwloc=%s" % self.spec['hwloc'].prefix,
            "--with-libevent=%s" % self.spec['libevent'].prefix,
            "--with-munge=%s" % self.spec['munge'].prefix,
        ]
        return args
