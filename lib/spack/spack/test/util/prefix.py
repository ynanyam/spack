##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
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
"""Tests various features of :py:class:`spack.util.prefix.Prefix`"""

from spack.util.prefix import Prefix


def test_prefix_attributes():
    """Test normal prefix attributes like ``prefix.bin``"""
    prefix = Prefix('/usr')

    assert prefix.bin     == '/usr/bin'
    assert prefix.lib     == '/usr/lib'
    assert prefix.include == '/usr/include'


def test_multilevel_attributes():
    """Test attributes of attributes, like ``prefix.share.man``"""
    prefix = Prefix('/usr/')

    assert prefix.share.man   == '/usr/share/man'
    assert prefix.man.man8    == '/usr/man/man8'
    assert prefix.foo.bar.baz == '/usr/foo/bar/baz'

    share = prefix.share

    assert isinstance(share, Prefix)
    assert share.man == '/usr/share/man'


def test_string_like_behavior():
    """Test string-like behavior of the prefix object"""
    prefix = Prefix('/usr')

    assert prefix == '/usr'
    assert isinstance(prefix, str)

    assert prefix + '/bin' == '/usr/bin'
    assert '--prefix=%s' % prefix == '--prefix=/usr'
    assert '--prefix={0}'.format(prefix) == '--prefix=/usr'

    assert prefix.find('u', 1)
    assert prefix.upper() == '/USR'
    assert prefix.lstrip('/') == 'usr'
