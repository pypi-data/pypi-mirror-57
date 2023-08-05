# Copyright (c) 2018-2019, Eduardo Rodrigues and Henry Schreiner.
#
# Distributed under the 3-clause BSD license, see accompanying file LICENSE
# or https://github.com/scikit-hep/particle for details.

from __future__ import absolute_import

from collections import Mapping

import csv

from .. import data
from ..exceptions import MatchingIDNotFound


class BiMap(object):
    def __init__(self, class_A, class_B, converters=(int, int), filename=None):
        """
        Bi-bidirectional map class.

        Parameters
        ----------
        class_A, class_B: class types
            Input class types.
        converters: tuple, optional, default=(int,int)
            Converter functions applied on each entry (row) of the file
            providing the class_a-class_B matches.
            The order of the list elements must agree with that of the classes
            passed in in the constructor.
            By default, data on the file is assumed to be integers,
            which is the typical case for PDG IDs and alike.
        filename: string or file object, optional,
                  default='<class_B_name>_to_<class_A_name>.csv',
                  where the names are taken as lowercase.
            Specify a file from which to read all class_a-class_B matches.
            It does not matter whether the file contains the input as
            val_A,val_B or val_B,val_A.

        Examples
        --------
        >>> from particle import PDGID, PythiaID

        Basic/standard usage:
        >>> bimap = BiMap(PDGID, PythiaID)

        >>> bimap[PDGID(9010221)]
        <PythiaID: 10221>
        >>> bimap[PythiaID(10221)]
        <PDGID: 9010221>

        Advanced usage:
        >>> # Either pass a file name or a file object
        >>> from particle import data
        >>> filename = data.open_text(data, 'pdgid_to_pythiaid.csv')
        >>> bimap = BiMap(PDGID, PythiaID, filename=filename)
        """

        self.class_A = class_A
        self.class_B = class_B

        name_A = self.class_A.__name__.upper()
        name_B = self.class_B.__name__.upper()

        if filename is None:
            filename = "{a}_to_{b}.csv".format(a=name_A.lower(), b=name_B.lower())
            filename = data.open_text(data, filename)
        elif not hasattr(filename, "read"):
            # Conversion to handle pathlib on Python < 3.6:
            filename = str(filename)
            filename = open(filename)

        with filename as _f:
            self._to_map = {
                converters[1](v[name_B]): converters[0](v[name_A])
                for v in csv.DictReader(l for l in _f if not l.startswith("#"))
            }
            _f.seek(0)
            self._from_map = {
                converters[0](v[name_A]): converters[1](v[name_B])
                for v in csv.DictReader(l for l in _f if not l.startswith("#"))
            }

    def __getitem__(self, value):
        if isinstance(value, self.class_B):
            try:
                return self.class_A(self._to_map[value])
            except KeyError:
                pass
        elif isinstance(value, self.class_A):
            try:
                return self.class_B(self._from_map[value])
            except KeyError:
                pass
        msg = "Matching {a}-{b} for input {v} not found !".format(
            a=self.class_A.__name__, b=self.class_B.__name__, v=value
        )
        raise MatchingIDNotFound(msg)

    def __repr__(self):
        return "<{self.__class__.__name__}({a}-{b}): {n} matches>".format(
            self=self,
            a=self.class_A.__name__,
            b=self.class_B.__name__,
            n=self.__len__(),
        )

    def __str__(self):
        return repr(self)

    def __len__(self):
        """Returns the number of matches."""
        return len(self._to_map)


def DirectionalMaps(name_A, name_B, converters=(str, str), filename=None):
    """
        Directional map class providing a to and from mapping.

        Parameters
        ----------
        name_A, name_B: str
            Input names of information to be mapped.
        converters: tuple, optional, default=(str,str)
            Converter functions applied on each entry (row) of the file
            providing the name_a-name_B matches.
            The order of the list elements must agree with that of the
            object names passed in in the constructor.
            By default, data on the file is assumed to be strings,
            which is the typical case for particle names.
        filename: string or file object, optional, default='particle/data/conversions.csv'.
            Specify a file from which to read all name_a-name_B matches.
            It is assumed that the order of items in the file matches the order
            of arguments specified in the class constructor, hence val_A,val_B.

        Examples
        --------

        >>> from particle import data  # doctest: +SKIP
        >>> filename = data.open_text(data, 'a_to_b.csv')  # doctest: +SKIP
        >>> A2BMap, B2AMap = DirectionalMaps('A', 'B', filename=filename)  # doctest: +SKIP
        """

    name_A = name_A.upper()
    name_B = name_B.upper()

    fieldnames = None
    skipinitialspace = True

    if filename is None:
        filename = data.open_text(data, "conversions.csv")
    elif not hasattr(filename, "read"):
        # Conversion to handle pathlib on Python < 3.6:
        filename = str(filename)
        filename = open(filename)

    with filename as _f:
        to_map = {
            converters[1](v[name_B]): converters[0](v[name_A])
            for v in csv.DictReader(
                (l for l in _f if not l.startswith("#")),
                fieldnames=fieldnames,
                skipinitialspace=skipinitialspace,
            )
        }
        _f.seek(0)
        from_map = {
            converters[0](v[name_A]): converters[1](v[name_B])
            for v in csv.DictReader(
                (l for l in _f if not l.startswith("#")),
                fieldnames=fieldnames,
                skipinitialspace=skipinitialspace,
            )
        }

    return (
        DirectionalMap(name_A, name_B, from_map),
        DirectionalMap(name_B, name_A, to_map),
    )


class DirectionalMap(Mapping):
    def __init__(self, name_A, name_B, map):
        """
        Directional map class providing a A -> B mapping.

        Parameters
        ----------
        name_A, name_B: str
            Input names of information to be mapped.
        map: dict
            Input mapping as a dictionary.
        """

        self.name_A = name_A.upper()
        self.name_B = name_B.upper()

        self._map = map

    def __getitem__(self, value):
        try:
            return self._map[value]
        except KeyError:
            msg = "Matching {a}->{b} for input {v} not found !".format(
                a=self.name_A, b=self.name_B, v=value
            )
            raise MatchingIDNotFound(msg)

    def __iter__(self):
        return iter(self._map)

    def __repr__(self):
        return "<{self.__class__.__name__}({a}->{b}): {n} matches>".format(
            self=self, a=self.name_A, b=self.name_B, n=self.__len__()
        )

    def __str__(self):
        return repr(self)

    def __len__(self):
        """Returns the number of matches."""
        return len(self._map)
