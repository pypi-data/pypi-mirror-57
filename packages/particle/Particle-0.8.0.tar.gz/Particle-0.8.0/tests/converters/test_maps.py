# Copyright (c) 2018-2019, Eduardo Rodrigues and Henry Schreiner.
#
# Distributed under the 3-clause BSD license, see accompanying file LICENSE
# or https://github.com/scikit-hep/particle for details.

import pytest

from particle.converters.bimap import BiMap
from particle.converters.bimap import DirectionalMaps

from particle.pdgid import PDGID
from particle.pythia import PythiaID

from particle.exceptions import MatchingIDNotFound

from particle import data


def test_BiMap():
    bimap = BiMap(PDGID, PythiaID)

    assert len(bimap) == 538
    assert "BiMap(PDGID-PythiaID)" in str(bimap)

    with pytest.raises(MatchingIDNotFound):
        pyid = bimap[PDGID(9000221)]


def test_DirectionalMaps():
    filename = data.open_text(data, "pdgid_to_pythiaid.csv")
    PDG2PyIDMap, Py2PDGIDMap = DirectionalMaps(
        "PDGID", "PythiaID", filename=filename, converters=(int, int)
    )

    assert len(PDG2PyIDMap) == 538
    assert len(Py2PDGIDMap) == 538

    assert "DirectionalMap(PDGID->PYTHIAID)" in str(PDG2PyIDMap)
    assert "DirectionalMap(PYTHIAID->PDGID)" in str(Py2PDGIDMap)

    with pytest.raises(MatchingIDNotFound):
        pyid = PDG2PyIDMap[PDGID(9000221)]
    with pytest.raises(MatchingIDNotFound):
        pdgid = Py2PDGIDMap[PythiaID(9000221)]
