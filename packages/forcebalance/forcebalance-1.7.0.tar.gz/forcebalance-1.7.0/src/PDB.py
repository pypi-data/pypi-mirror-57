""" PDB parsing class

    This module parses PDBs in accordance to PDB Format Description Version 2.2
    (1996); it is not very forgiving.   Each class in this module corresponds
    to a record in the PDB Format Description.  Much of the documentation for
    the classes is taken directly from the above PDB Format Description.

    ----------------------------

    PDB2PQR -- An automated pipeline for the setup, execution, and analysis of
    Poisson-Boltzmann electrostatics calculations

	Copyright (c) 2002-2007, Jens Erik Nielsen, University College Dublin;
	Nathan A. Baker, Washington University in St. Louis; Paul Czodrowski &
	Gerhard Klebe, University of Marburg

	All rights reserved.

	Redistribution and use in source and binary forms, with or without modification,
	are permitted provided that the following conditions are met:

		* Redistributions of source code must retain the above copyright notice,
		  this list of conditions and the following disclaimer.
		* Redistributions in binary form must reproduce the above copyright notice,
		  this list of conditions and the following disclaimer in the documentation
		  and/or other materials provided with the distribution.
		* Neither the names of University College Dublin, Washington University in
		  St. Louis, or University of Marburg nor the names of its contributors may
		  be used to endorse or promote products derived from this software without
		  specific prior written permission.

	THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
	ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
	WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
	IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
	INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
	BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
	DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
	LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
	OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
	OF THE POSSIBILITY OF SUCH DAMAGE.

    ----------------------------
    Modified by KA Beauchamp for inclusion in MSMBuilder.
    Adapted by Lee-Ping Wang for inclusion in ForceBalance.
"""

from builtins import hex
from builtins import range
from builtins import object
__date__ = "4 August 2008"
__author__ = "Todd Dolinsky, Yong Huang"

import string, sys
import copy  ### PC
import numpy as np

try:
    import forcebalance
    from forcebalance.output import *
    logger = getLogger(__name__)
except:
    import logging as logger

class END(object):
    """ END class

        The END records are paired with MODEL records to group individual
        structures found in a coordinate entry.
    """

    def __init__(self, line):
        """
            Initialize by parsing line (nothing to do)
        """
        pass

def toInt(strin):
    try:
        return int(strin)
    except:
        return int(strin,16)

# def toStr(intin):
#     if intin >= 100000:
#         return

class MASTER(object):
    """ MASTER class

        The MASTER record is a control record for bookkeeping. It lists the
        number of lines in the coordinate entry or file for selected record
        types.
    """

    def __init__(self, line):
        """
            Initialize by parsing line

            COLUMNS  TYPE   FIELD     DEFINITION
            -------------------------------------------------
            11-15    int    numRemark Number of REMARK records
            21-25    int    numHet    Number of HET records
            26-30    int    numHelix  Number of HELIX records
            31-35    int    numSheet  Number of SHEET records
            36-40    int    numTurn   Number of TURN records
            41-45    int    numSite   Number of SITE records
            46-50    int    numXform  Number of coordinate transformation
                                      records (ORIGX+SCALE+MTRIX)
            51-55    int    numCoord  Number of atomic coordinate records
                                      (ATOM+HETATM)
            56-60    int    numTer    Number of TER records
            61-65    int    numConect Number of CONECT records
            66-70    int    numSeq    Number of SEQRES records
        """
        record = line[0:6].strip()
        if record == "MASTER":
            self.numRemark = toInt(line[10:15].strip())
            self.numHet = toInt(line[20:25].strip())
            self.numHelix = toInt(line[25:30].strip())
            self.numSheet = toInt(line[30:35].strip())
            self.numTurn = toInt(line[35:40].strip())
            self.numSite = toInt(line[40:45].strip())
            self.numXform = toInt(line[45:50].strip())
            self.numCoord = toInt(line[50:55].strip())
            self.numTer = toInt(line[55:60].strip())
            self.numConect = toInt(line[60:65].strip())
            self.numSeq = toInt(line[65:70].strip())
        else:  logger.error(record+'\n') ; raise ValueError


class CONECT(object):
    """ CONECT class

        The CONECT records specify connectivity between atoms for which
        coordinates are supplied. The connectivity is described using the atom
        serial number as found in the entry. CONECT records are mandatory for
        HET groups (excluding water) and for other bonds not specified in the
        standard residue connectivity table which involve atoms in standard
        residues (see Appendix 4 for the list of standard residues). These
        records are generated by the PDB.
    """

    def __init__(self, line):
        """
            Initialize by parsing line

            COLUMNS  TYPE   FIELD    DEFINITION
            --------------------------------------------
             7-11    int    serial   Atom serial number
            12-16    int    serial1  Serial number of bonded atom
            17-21    int    serial2  Serial number of bonded atom
            22-26    int    serial3  Serial number of bonded atom
            27-31    int    serial4  Serial number of bonded atom
            32-36    int    serial5  Serial number of hydrogen bonded atom
            37-41    int    serial6  Serial number of hydrogen bonded atom
            42-46    int    serial7  Serial number of salt bridged    atom
            47-51    int    serial8  Serial number of hydrogen bonded atom
            52-56    int    serial9  Serial number of hydrogen bonded atom
            57-61    int    serial10 Serial number of salt bridged    atom
        """
        record = line[0:6].strip()
        if record == "CONECT":
            self.serial = toInt(line[6:11].strip())
            try:  self.serial1 = toInt(line[11:16].strip())
            except ValueError:  self.serial1 = None
            try:  self.serial2 = toInt(line[16:21].strip())
            except ValueError:  self.serial2 = None
            try:  self.serial3 = toInt(line[21:26].strip())
            except ValueError:  self.serial3 = None
            try:  self.serial4 = toInt(line[26:31].strip())
            except ValueError:  self.serial4 = None
            try:  self.serial5 = toInt(line[31:36].strip())
            except ValueError:  self.serial5 = None
            try:  self.serial6 = toInt(line[36:41].strip())
            except ValueError:  self.serial6 = None
            try:  self.serial7 = toInt(line[41:46].strip())
            except ValueError:  self.serial7 = None
            try:  self.serial8 = toInt(line[46:51].strip())
            except ValueError:  self.serial8 = None
            try:  self.serial9 = toInt(line[51:56].strip())
            except ValueError:  self.serial9 = None
            try:  self.serial10 = toInt(line[56:61].strip())
            except ValueError:  self.serial10 = None
        else:  logger.error(record+'\n') ; raise ValueError

class ENDMDL(object):
    """ ENDMDL class

        The ENDMDL records are paired with MODEL records to group individual
        structures found in a coordinate entry.
    """

    def __init__(self, line):
        """
            Initialize by parsing line (nothing to do)
        """
        pass

class TER(object):
    """ TER class

        The TER record indicates the end of a list of ATOM/HETATM records for a
        chain.
    """

    def __init__(self, line):
        """ Initialize by parsing line:

            COLUMNS  TYPE   FIELD   DEFINITION
            -------------------------------------------
             7-11    int    serial  Serial number.
            18-20    string resName Residue name.
            22       string chainID Chain identifier.
            23-26    int    resSeq  Residue sequence number.
            27       string iCode   Insertion code.
        """
        record = line[0:6].strip()
        if record == "TER":
            try: # Not really needed
                self.serial = toInt(line[6:11].strip())
                self.resName = line[17:20].strip()
                self.chainID = line[21].strip()
                self.resSeq = toInt(line[22:26].strip())
                self.iCode = line[26].strip()
            except (IndexError, ValueError):
                self.serial = None
                self.resName = None
                self.chainID = None
                self.resSeq = None
                self.iCode = None
        else:  logger.error(record+'\n') ; raise ValueError

class SIGUIJ(object):
    """ SIGUIJ class

        The SIGUIJ records present the anisotropic temperature factors.
    """

    def __init__(self, line):
        """
            Initialize by parsing line:

              COLUMNS  TYPE   FIELD   DEFINITION
              ------------------------------------------------------
               7-11    int    serial  Atom serial number.
              13-16    string name    Atom name.
              17       string altLoc  Alternate location indicator.
              18-20    string resName Residue name.
              22       string chainID Chain identifier.
              23-26    int    resSeq  Residue sequence number.
              27       string iCode   Insertion code.
              29-35    int    sig11   Sigma U(1,1)
              36-42    int    sig22   Sigma U(2,2)
              43-49    int    sig33   Sigma U(3,3)
              50-56    int    sig12   Sigma U(1,2)
              57-63    int    sig13   Sigma U(1,3)
              64-70    int    sig23   Sigma U(2,3)
              73-76    string segID   Segment identifier, left-justified.
              77-78    string element Element symbol, right-justified.
              79-80    string charge  Charge on the atom.
        """
        record = line[0:6].strip()
        if record == "SIGUIJ":
            self.serial = toInt(line[6:11].strip())
            self.name = line[12:16].strip()
            self.altLoc = line[16].strip()
            self.resName = line[17:20].strip()
            self.chainID = line[21].strip()
            self.resSeq = toInt(line[22:26].strip())
            self.iCode = line[26].strip()
            self.sig11 = toInt(line[28:35].strip())
            self.sig22 = toInt(line[35:42].strip())
            self.sig33 = toInt(line[42:49].strip())
            self.sig12 = toInt(line[49:56].strip())
            self.sig13 = toInt(line[56:63].strip())
            self.sig23 = toInt(line[63:70].strip())
            self.segID = line[72:76].strip()
            self.element = line[76:78].strip()
            self.charge = line[78:80].strip()
        else: logger.error(record+'\n') ; raise ValueError


class ANISOU(object):
    """ ANISOU class

        The ANISOU records present the anisotropic temperature factors.
    """

    def __init__(self, line):
        """
            Initialize by parsing line:

              COLUMNS  TYPE   FIELD   DEFINITION
              ------------------------------------------------------
               7-11    int    serial  Atom serial number.
              13-16    string name    Atom name.
              17       string altLoc  Alternate location indicator.
              18-20    string resName Residue name.
              22       string chainID Chain identifier.
              23-26    int    resSeq  Residue sequence number.
              27       string iCode   Insertion code.
              29-35    int    u00     U(1,1)
              36-42    int    u11     U(2,2)
              43-49    int    u22     U(3,3)
              50-56    int    u01     U(1,2)
              57-63    int    u02     U(1,3)
              64-70    int    u12     U(2,3)
              73-76    string segID   Segment identifier, left-justified.
              77-78    string element Element symbol, right-justified.
              79-80    string charge  Charge on the atom.
        """
        record = line[0:6].strip()
        if record == "ANISOU":
            self.serial = toInt(line[6:11].strip())
            self.name = line[12:16].strip()
            self.altLoc = line[16].strip()
            self.resName = line[17:20].strip()
            self.chainID = line[21].strip()
            self.resSeq = toInt(line[22:26].strip())
            self.iCode = line[26].strip()
            self.u00 = toInt(line[28:35].strip())
            self.u11 = toInt(line[35:42].strip())
            self.u22 = toInt(line[42:49].strip())
            self.u01 = toInt(line[49:56].strip())
            self.u02 = toInt(line[56:63].strip())
            self.u12 = toInt(line[63:70].strip())
            self.segID = line[72:76].strip()
            self.element = line[76:78].strip()
            self.charge = line[78:80].strip()
        else: logger.error(record+'\n') ; raise ValueError

class SIGATM(object):
    """ SIGATM class

        The SIGATM records present the standard deviation of atomic parameters
        as they appear in ATOM and HETATM records.
    """

    def __init__(self, line):
        """
            Initialize by parsing line

            COLUMNS  TYPE   FIELD    DEFINITION
            ---------------------------------------------
            7-11      int   serial   Atom serial number.
            13-16     string name    Atom name.
            17        string altLoc  Alternate location indicator.
            18-20     string resName Residue name.
            22        string chainID Chain identifier.
            23-26     int    resSeq  Residue sequence number.
            27        string iCode   Code for insertion of residues.
            31-38     float  sigX    Standard devition of orthogonal
                                     coordinates for X in Angstroms.
            39-46     float  sigY    Standard devition of orthogonal
                                     coordinates for Y in Angstroms.
            47-54     float  sigZ    Standard devition of orthogonal
                                     coordinates for Z in Angstroms.
            55-60     float  sigOcc  Standard devition of occupancy.
            61-66     float  sigTemp Standard devition of temperature factor.
            73-76     string segID   Segment identifier, left-justified.
            77-78     string element Element symbol, right-justified.
            79-80     string charge  Charge on the atom.
        """
        record = line[0:6].strip()
        if record == "HETATM":
            self.serial = toInt(line[6:11].strip())
            self.name = line[12:16].strip()
            self.altLoc = line[16].strip()
            self.resName = line[17:20].strip()
            self.chainID = line[21].strip()
            self.resSeq = toInt(line[22:26].strip())
            self.iCode = line[26].strip()
            self.sigX = float(line[30:38].strip())
            self.sigY = float(line[38:46].strip())
            self.sigZ = float(line[46:54].strip())
            self.sigOcc = float(line[54:60].strip())
            self.sigTemp = float(line[60:66].strip())
            self.segID = line[72:76].strip()
            self.element = line[76:78].strip()
            self.charge = line[78:80].strip()
        else: logger.error(record+'\n') ; raise ValueError

class HETATM(object):
    """ HETATM class

        The HETATM records present the atomic coordinate records for atoms
        within "non-standard" groups. These records are used for water
        molecules and atoms presented in HET groups.
    """

    def __init__(self,line,sybylType="A.aaa",lBonds=[],lBondedAtoms=[]): ### PC
        """
            Initialize by parsing line

            COLUMNS  TYPE   FIELD  DEFINITION
            ---------------------------------------------
            7-11      int   serial        Atom serial number.
            13-16     string name          Atom name.
            17        string altLoc        Alternate location indicator.
            18-20     string resName       Residue name.
            22        string chainID       Chain identifier.
            23-26     int    resSeq        Residue sequence number.
            27        string iCode         Code for insertion of residues.
            31-38     float  x             Orthogonal coordinates for X in
                                           Angstroms.
            39-46     float  y             Orthogonal coordinates for Y in
                                           Angstroms.
            47-54     float  z             Orthogonal coordinates for Z in
                                           Angstroms.
            55-60     float  occupancy     Occupancy.
            61-66     float  tempFactor    Temperature factor.
            73-76     string segID         Segment identifier, left-justified.
            77-78     string element       Element symbol, right-justified.
            79-80     string charge        Charge on the atom.
        """
        record = line[0:6].strip()
        if record == "HETATM":
            self.serial = toInt(line[6:11].strip())
            self.name = line[12:16].strip()
            self.altLoc = line[16].strip()
            try:
                self.resName = line[17:20].strip()
                self.chainID = line[21].strip()
                self.resSeq = toInt(line[22:26].strip())
                self.iCode = line[26].strip()
            except:
                raise ValueError('Residue name must be less than 4 characters!')
            self.x = float(line[30:38].strip())
            self.y = float(line[38:46].strip())
            self.z = float(line[46:54].strip())
            ### PC
#            self.lAtoms = lAtoms
            self.sybylType = sybylType
            self.lBondedAtoms = lBondedAtoms
            self.lBonds = lBonds
            self.radius = 1.0
            ###
            try:
                self.occupancy = float(line[54:60].strip())
                self.tempFactor = float(line[60:66].strip())
                self.segID = line[72:76].strip()
                self.element = line[76:78].strip()
                self.charge = line[78:80].strip()
            except ValueError as IndexError:
                self.occupancy = 0.00
                self.tempFactor = 0.00
                self.segID = ""
                self.element = ""
                self.charge = ""
        else: logger.error(record+'\n') ; raise ValueError

    def __str__(self):
        """
            Print object as string

            COLUMNS  TYPE   FIELD  DEFINITION
            ---------------------------------------------
            7-11      int   serial        Atom serial number.
            13-16     string name          Atom name.
            17        string altLoc        Alternate location indicator.
            18-20     string resName       Residue name.
            22        string chainID       Chain identifier.
            23-26     int    resSeq        Residue sequence number.
            27        string iCode         Code for insertion of residues.
            31-38     float  x             Orthogonal coordinates for X in
                                           Angstroms.
            39-46     float  y             Orthogonal coordinates for Y in
                                           Angstroms.
            47-54     float  z             Orthogonal coordinates for Z in
                                           Angstroms.
            55-60     float  occupancy     Occupancy.
            61-66     float  tempFactor    Temperature factor.
            73-76     string segID         Segment identifier, left-justified.
            77-78     string element       Element symbol, right-justified.
            79-80     string charge        Charge on the atom.
        """
        str = ""
        tstr = "HETATM"
        str = str + string.ljust(tstr, 6)[:6]
        if self.serial < 100000:
            tstr = "%d" % self.serial
        else:
            tstr = hex(self.serial)[2:]
        str = str + string.rjust(tstr, 5)[:5]
        str = str + " "
        tstr = self.name
        if len(tstr) == 4:
            str = str + string.ljust(tstr, 4)[:4]
        else:
            str = str + " " + string.ljust(tstr, 3)[:3]
        tstr = self.altLoc
        str = str + string.ljust(tstr, 1)[:1]
        tstr = self.resName
        str = str + string.ljust(tstr, 3)[:3]
        str = str + " "
        tstr = self.chainID
        str = str + string.ljust(tstr, 1)[:1]
        if self.resSeq < 100000:
            tstr = "%d" % self.resSeq
        else:
            tstr = hex(self.resSeq)[2:]
        str = str + string.rjust(tstr, 4)[:4]
        tstr = self.iCode
        str = str + string.ljust(tstr, 1)[:1]
        str = str + "   "
        tstr = "%8.3f" % self.x
        str = str + string.ljust(tstr, 8)[:8]
        tstr = "%8.3f" % self.y
        str = str + string.ljust(tstr, 8)[:8]
        tstr = "%8.3f" % self.z
        str = str + string.ljust(tstr, 8)[:8]
        tstr = "%6.2f" % self.occupancy
        str = str + string.ljust(tstr, 6)[:6]
        tstr = "%6.2f" % self.tempFactor
        str = str + string.rjust(tstr, 6)[:6]
        tstr = self.segID
        str = str + string.ljust(tstr, 4)[:4]
        tstr = self.element
        str = str + string.ljust(tstr, 2)[:2]
        tstr = self.charge
        str = str + string.ljust(tstr, 2)[:2]
        return str

### PC
# to do:  - parse SUBSTRUCTURE
#         - avoid/detect blanks in @<TRIPOS>BOND
#         - what happens, if no SUBSTRUCTURE present?
#         - different order of SUBSTRUCTURE/MOLECULE
#         - readlines instead of read -> blanks are avoided (you get a list)
#         - (maybe) flag for parsing each RTI

class MOL2BOND(object):
    """
    Bonding of MOL2 files
    """
    def __init__(self, frm, to, type, id=0):
        self.to   = to     # bond to this atom
        self.frm  = frm    # bond from atom
        self.type = type   # 1=single, 2=double, ar=aromatic
        self.id   = id     # bond_id

class MOL2MOLECULE(object):
    """
    Tripos MOL2 molecule
    For further information look at (web page exists: 25 August 2005):
    http://www.tripos.com/index.php?family=modules,SimplePage,,,&page=sup_mol2&s=0
    """
    def __init__(self):
        self.lAtoms         = []       # all atoms of class <ATOM>
        self.lBonds         = []       # all bonds of class <BOND>
        self.lPDBAtoms      = []       # PDB-like list of all atoms

    def read(self,file):
        """
        Routines for reading MOL2 file
        """
        #self.filename = filename
        #data = open(self.filename).read()

        data = file.read()
        data = data.replace("\r\n", "\n")
        data = data.replace("\r", "\n")

        # ATOM section
        start = data.find("@<TRIPOS>ATOM")
        stop = data.find("@<TRIPOS>BOND")

        # Do some error checking
        if start == -1:
            logger.error("Unable to find '@<TRIPOS>ATOM' in MOL2 file!\n")
            raise RuntimeError
        elif stop == -1:
            logger.error("Unable to find '@<TRIPOS>BOND' in MOL2 file!\n")
            raise RuntimeError

        atoms = data[start+14:stop-2].split("\n")
        # BOND section
        start = data.find("@<TRIPOS>BOND")
        stop = data.find("@<TRIPOS>SUBSTRUCTURE")

        # More error checking
        if stop == -1:
            logger.error("Unable to find '@<TRIPOS>SUBSTRUCTURE' in MOL2 file!\n")
            raise RuntimeError

        bonds = data[start+14:stop-1].split("\n")
        self.parseAtoms(atoms)
        self.parseBonds(bonds)
        self.createlBondedAtoms()
        #self.createPDBlineFromMOL2(atoms)

    def parseAtoms(self,AtomList):
        """
        for parsing @<TRIPOS>ATOM
        """
        for AtomLine in AtomList:
            SeparatedAtomLine = AtomLine.split()

            # Error checking
            if len(SeparatedAtomLine) < 8:
                logger.error("Bad atom entry in MOL2 file: %s\n" % AtomLine)
                raise RuntimeError

            fakeRecord = "HETATM"
            fakeChain = " L"
            try:
                mol2pdb = '%s%5i%5s%4s%2s%4i    %8.3f%8.3f%8.3f' %\
                   (fakeRecord,toInt(SeparatedAtomLine[0]),
                    SeparatedAtomLine[1],SeparatedAtomLine[7],
                    fakeChain,toInt(SeparatedAtomLine[6]),
                    float(SeparatedAtomLine[2]),float(SeparatedAtomLine[3]),
                    float(SeparatedAtomLine[4]))
            except ValueError:
                logger.error("Bad atom entry in MOL2 file: %s\n" % AtomLine)
                raise RuntimeError

            thisAtom = HETATM(mol2pdb, SeparatedAtomLine[5],[],[])
            self.lPDBAtoms.append(mol2pdb)
            self.lAtoms.append(thisAtom)

    def parseBonds(self,BondList):
        """
        for parsing @<TRIPOS>BOND
        """
        for BondLine in BondList:
            SeparatedBondLine = BondLine.split()
            if len(SeparatedBondLine) < 4:
                logger.error("Bad bond entry in MOL2 file: %s\n" % BondLine)
                raise RuntimeError
            try:
                thisBond = MOL2BOND(
                    toInt(SeparatedBondLine[1]), # bond frm
                    toInt(SeparatedBondLine[2]), # bond to
                    SeparatedBondLine[3],      # bond type
                    toInt(SeparatedBondLine[0])  # bond id
                    )
            except ValueError:
                logger.error("Bad bond entry in MOL2 file: %s\n" % BondLine)
                raise RuntimeError
            self.lBonds.append(thisBond)

    def createlBondedAtoms(self):
        """
        Creates for each atom a list of the bonded Atoms

        This becomes one attribute of MOL2ATOM!
        """
        for bond in self.lBonds:
            self.lAtoms[bond.frm-1].lBondedAtoms.append(
                self.lAtoms[bond.to-1])

            self.lAtoms[bond.to-1].lBondedAtoms.append(
                self.lAtoms[bond.frm-1])

            atbond = copy.deepcopy(bond)
            atbond.other_atom=self.lAtoms[bond.to-1]
            self.lAtoms[bond.frm-1].lBonds.append(atbond)

            atbond = copy.deepcopy(bond)
            atbond.other_atom=self.lAtoms[bond.frm-1]
            self.lAtoms[bond.to-1].lBonds.append(atbond)
        return


    def createPDBlineFromMOL2(self):
        FakeType = "HETATM"
        return ('%s%5i%5s%4s%2s%5s   %8.3f%8.3f%8.3f\n' %
                (FakeType,            self.serial,   self.name,
                 self.resName, ' L',          self.resSeq,
                 self.x,self.y, self.z))
### PC

class ATOM(object):
    """ ATOM class

        The ATOM records present the atomic coordinates for standard residues.
        They also present the occupancy and temperature factor for each atom.
        Heterogen coordinates use the HETATM record type. The element symbol is
        always present on each ATOM record; segment identifier and charge are
        optional.
    """

    def __init__(self, line):
        """
            Initialize by parsing line

            COLUMNS  TYPE   FIELD  DEFINITION
            ---------------------------------------------
            7-11      int   serial        Atom serial number.
            13-16     string name          Atom name.
            17        string altLoc        Alternate location indicator.
            18-20     string resName       Residue name.
            22        string chainID       Chain identifier.
            23-26     int    resSeq        Residue sequence number.
            27        string iCode         Code for insertion of residues.
            31-38     float  x             Orthogonal coordinates for X in
                                           Angstroms.
            39-46     float  y             Orthogonal coordinates for Y in
                                           Angstroms.
            47-54     float  z             Orthogonal coordinates for Z in
                                           Angstroms.
            55-60     float  occupancy     Occupancy.
            61-66     float  tempFactor    Temperature factor.
            73-76     string segID         Segment identifier, left-justified.
            77-78     string element       Element symbol, right-justified.
            79-80     string charge        Charge on the atom.
        """
        record = line[0:6].strip()
        if record == "ATOM":
            self.serial = toInt(line[6:11].strip())
            self.name = line[12:16].strip()
            self.altLoc = line[16].strip()
            self.resName = line[17:20].strip()
            self.chainID = line[21].strip()
            self.resSeq = toInt(line[22:26].strip())
            self.iCode = line[26].strip()
            self.x = float(line[30:38].strip())
            self.y = float(line[38:46].strip())
            self.z = float(line[46:54].strip())
            try:
                self.occupancy = float(line[54:60].strip())
                self.tempFactor = float(line[60:66].strip())
                self.segID = line[72:76].strip()
                self.charge = line[78:80].strip()
            except ValueError as IndexError:
                self.occupancy = 0.00
                self.tempFactor = 0.00
                self.segID = ""
                self.charge = ""
            # QYD: separate trial on reading element
            try:
                self.element = line[76:78].strip()
            except ValueError as IndexError:
                self.element = ""
        else:
            logger.error(record+'\n') ; raise ValueError

    def __str__(self):
        """
            Print object as string

            COLUMNS  TYPE   FIELD  DEFINITION
            ---------------------------------------------
            7-11      int   serial        Atom serial number.
            13-16     string name          Atom name.
            17        string altLoc        Alternate location indicator.
            18-20     string resName       Residue name.
            22        string chainID       Chain identifier.
            23-26     int    resSeq        Residue sequence number.
            27        string iCode         Code for insertion of residues.
            31-38     float  x             Orthogonal coordinates for X in
                                           Angstroms.
            39-46     float  y             Orthogonal coordinates for Y in
                                           Angstroms.
            47-54     float  z             Orthogonal coordinates for Z in
                                           Angstroms.
            55-60     float  occupancy     Occupancy.
            61-66     float  tempFactor    Temperature factor.
            73-76     string segID         Segment identifier, left-justified.
            77-78     string element       Element symbol, right-justified.
            79-80     string charge        Charge on the atom.
        """
        str = ""
        tstr = "ATOM"
        str = str + string.ljust(tstr, 6)[:6]
        if self.serial < 100000:
            tstr = "%d" % self.serial
        else:
            tstr = hex(self.serial)[2:]
        str = str + string.rjust(tstr, 5)[:5]
        str = str + " "
        tstr = self.name
        if len(tstr) == 4:
            str = str + string.ljust(tstr, 4)[:4]
        else:
            str = str + " " + string.ljust(tstr, 3)[:3]
        tstr = self.altLoc
        str = str + string.ljust(tstr, 1)[:1]
        tstr = self.resName
        str = str + string.ljust(tstr, 3)[:3]
        str = str + " "
        tstr = self.chainID
        str = str + string.ljust(tstr, 1)[:1]
        if self.resSeq < 100000:
            tstr = "%d" % self.resSeq
        else:
            tstr = hex(self.resSeq)[2:]
        str = str + string.rjust(tstr, 4)[:4]
        tstr = self.iCode
        str = str + string.ljust(tstr, 1)[:1]
        str = str + "   "
        tstr = "%8.3f" % self.x
        str = str + string.ljust(tstr, 8)[:8]
        tstr = "%8.3f" % self.y
        str = str + string.ljust(tstr, 8)[:8]
        tstr = "%8.3f" % self.z
        str = str + string.ljust(tstr, 8)[:8]
        tstr = "%6.2f" % self.occupancy
        str = str + string.ljust(tstr, 6)[:6]
        tstr = "%6.2f" % self.tempFactor
        str = str + string.ljust(tstr, 6)[:6]
        tstr = self.segID
        str = str + string.ljust(tstr, 4)[:4]
        tstr = self.element
        str = str + string.ljust(tstr, 2)[:2]
        tstr = self.charge
        str = str + string.ljust(tstr, 2)[:2]
        return str

class MODEL(object):
    """ MODEL class

        The MODEL record specifies the model serial number when multiple
        structures are presented in a single coordinate entry, as is often the
        case with structures determined by NMR.
    """

    def __init__(self, line):
        """
           Initialize by parsing line

           COLUMNS  TYPE   FIELD  DEFINITION
           -----------------------------------------------------
           11-14    int    serial Model serial number.
        """
        record = line[0:6].strip()
        if record == "MODEL":
            self.serial = toInt(line[10:14].strip())
        else:  logger.error(record+'\n') ; raise ValueError

class TVECT(object):
    """ TVECT class

        The TVECT records present the translation vector for infinite
        covalently connected structures.
    """

    def __init__(self, line):
        """
            Initialize by parsing line

            COLUMNS  TYPE   FIELD  DEFINITION
            ---------------------------------
             8-10    int    serial Serial number
            11-20    float  t1     Components of translation vector
            21-30    float  t2     Components of translation vector
            31-40    float  t2     Components of translation vector
            41-70    string text   Comments
        """
        record = line[0:6].strip()
        if record == "TVECT":
            self.serial = toInt(line[7:10].strip())
            self.t1 = float(line[10:20].strip())
            self.t2 = float(line[20:30].strip())
            self.t3 = float(line[30:40].strip())
            self.text = line[40:70].strip()
        else:  logger.error(record+'\n') ; raise ValueError

class MTRIX3(object):
    """ MTRIX3 class

        The MTRIX3 (n = 1, 2, or 3) records present transformations expressing
        non-crystallographic symmetry.
    """

    def __init__(self, line):
        """
            Initialize by parsing line

            COLUMNS  TYPE   FIELD  DEFINITION
            ---------------------------------
             8-10    int    serial Serial number
            11-20    float  mn1    M31
            21-30    float  mn2    M32
            31-40    float  mn3    M33
            46-55    float  vn     V3
            60       int    iGiven 1 if coordinates for the representations
                            which are approximately related by the
                            transformations of the molecule are contained in
                            the entry.  Otherwise, blank.
        """
        record = line[0:6].strip()
        if record == "MTRIX3":
            self.serial = toInt(line[7:10].strip())
            self.mn1 = float(line[10:20].strip())
            self.mn2 = float(line[20:30].strip())
            self.mn3 = float(line[30:40].strip())
            self.vn = float(line[45:55].strip())
            self.iGiven = toInt(line[59].strip())
        else:  logger.error(record+'\n') ; raise ValueError

class MTRIX2(object):
    """ MTRIX2 class

        The MTRIXn (n = 1, 2, or 3) records present transformations expressing
        non-crystallographic symmetry.
    """

    def __init__(self, line):
        """
            Initialize by parsing line

            COLUMNS  TYPE   FIELD  DEFINITION
            ---------------------------------
             8-10    int    serial Serial number
            11-20    float  mn1    M21
            21-30    float  mn2    M22
            31-40    float  mn3    M23
            46-55    float  vn     V2
            60       int    iGiven 1 if coordinates for the representations
                            which are approximately related by the
                            transformations of the molecule are contained in
                            the entry.  Otherwise, blank.
        """
        record = line[0:6].strip()
        if record == "MTRIX2":
            self.serial = toInt(line[7:10].strip())
            self.mn1 = float(line[10:20].strip())
            self.mn2 = float(line[20:30].strip())
            self.mn3 = float(line[30:40].strip())
            self.vn = float(line[45:55].strip())
            self.iGiven = toInt(line[59].strip())
        else:  logger.error(record+'\n') ; raise ValueError

class MTRIX1(object):
    """ MTRIX1 class

        The MTRIXn (n = 1, 2, or 3) records present transformations expressing
        non-crystallographic symmetry.
    """

    def __init__(self, line):
        """
            Initialize by parsing line

            COLUMNS  TYPE   FIELD  DEFINITION
            ---------------------------------
             8-10    int    serial Serial number
            11-20    float  mn1    M11
            21-30    float  mn2    M12
            31-40    float  mn3    M13
            46-55    float  vn     V1
            60       int    iGiven 1 if coordinates for the representations
                            which are approximately related by the
                            transformations of the molecule are contained in
                            the entry.  Otherwise, blank.
        """
        record = line[0:6].strip()
        if record == "MTRIX1":
            self.serial = toInt(line[7:10].strip())
            self.mn1 = float(line[10:20].strip())
            self.mn2 = float(line[20:30].strip())
            self.mn3 = float(line[30:40].strip())
            self.vn = float(line[45:55].strip())
            try:  self.iGiven = toInt(line[45:55].strip())
            except ValueError:  self.iGiven = None
            except IndexError:  self.iGiven = None
        else:  logger.error(record+'\n') ; raise ValueError

class SCALE3(object):
    """ SCALE3 class

        The SCALEn (n = 1, 2, or 3) records present the transformation from the
        orthogonal coordinates as contained in the entry to fractional
        crystallographic coordinates. Non-standard coordinate systems should be
        explained in the remarks.
    """

    def __init__(self, line):
        """
            Initialize by parsing line

            COLUMNS  TYPE   FIELD  DEFINITION
            ---------------------------------
            11-20    float  sn1    S31
            21-30    float  sn2    S32
            31-40    float  sn3    S33
            46-55    float  un     U3
        """
        record = line[0:6].strip()
        if record == "SCALE3":
            self.sn1 = float(line[10:20].strip())
            self.sn2 = float(line[20:30].strip())
            self.sn3 = float(line[30:40].strip())
            self.un = float(line[45:55].strip())
        else:  logger.error(record+'\n') ; raise ValueError

class SCALE2(object):
    """ SCALE2 class

        The SCALEn (n = 1, 2, or 3) records present the transformation from the
        orthogonal coordinates as contained in the entry to fractional
        crystallographic coordinates. Non-standard coordinate systems should be
        explained in the remarks.
    """

    def __init__(self, line):
        """
            Initialize by parsing line

            COLUMNS  TYPE   FIELD  DEFINITION
            ---------------------------------
            11-20    float  sn1    S21
            21-30    float  sn2    S22
            31-40    float  sn3    S23
            46-55    float  un     U2
        """
        record = line[0:6].strip()
        if record == "SCALE2":
            self.sn1 = float(line[10:20].strip())
            self.sn2 = float(line[20:30].strip())
            self.sn3 = float(line[30:40].strip())
            self.un = float(line[45:55].strip())
        else:  logger.error(record+'\n') ; raise ValueError

class SCALE1(object):
    """ SCALE1 class

        The SCALEn (n = 1, 2, or 3) records present the transformation from the
        orthogonal coordinates as contained in the entry to fractional
        crystallographic coordinates. Non-standard coordinate systems should be
        explained in the remarks.
    """

    def __init__(self, line):
        """
            Initialize by parsing line

            COLUMNS  TYPE   FIELD  DEFINITION
            ---------------------------------
            11-20    float  sn1    S11
            21-30    float  sn2    S12
            31-40    float  sn3    S13
            46-55    float  un     U1
        """
        record = line[0:6].strip()
        if record == "SCALE1":
            self.sn1 = float(line[10:20].strip())
            self.sn2 = float(line[20:30].strip())
            self.sn3 = float(line[30:40].strip())
            self.un = float(line[45:55].strip())
        else:  logger.error(record+'\n') ; raise ValueError

class ORIGX2(object):
    """ ORIGX2 class

        The ORIGXn (n = 1, 2, or 3) records present the transformation from the
        orthogonal coordinates contained in the entry to the submitted
        coordinates.
    """

    def __init__(self, line):
        """
            Initialize by parsing line

            COLUMNS  TYPE   FIELD  DEFINITION
            ---------------------------------
            11-20    float  on1    O21
            21-30    float  on2    O22
            31-40    float  on3    O23
            46-55    float  tn     T2
        """
        record = line[0:6].strip()
        if record == "ORIGX2":
            self.on1 = float(line[10:20].strip())
            self.on2 = float(line[20:30].strip())
            self.on3 = float(line[30:40].strip())
            self.tn = float(line[45:55].strip())
        else:  logger.error(record+'\n') ; raise ValueError

class ORIGX3(object):
    """ ORIGX3 class

        The ORIGXn (n = 1, 2, or 3) records present the transformation from the
        orthogonal coordinates contained in the entry to the submitted
        coordinates.
    """

    def __init__(self, line):
        """
            Initialize by parsing line

            COLUMNS  TYPE   FIELD  DEFINITION
            ---------------------------------
            11-20    float  on1    O31
            21-30    float  on2    O32
            31-40    float  on3    O33
            46-55    float  tn     T3
        """
        record = line[0:6].strip()
        if record == "ORIGX3":
            self.on1 = float(line[10:20].strip())
            self.on2 = float(line[20:30].strip())
            self.on3 = float(line[30:40].strip())
            self.tn = float(line[45:55].strip())
        else:  logger.error(record+'\n') ; raise ValueError

class ORIGX1(object):
    """ ORIGX1 class

        The ORIGXn (n = 1, 2, or 3) records present the transformation from the
        orthogonal coordinates contained in the entry to the submitted
        coordinates.
    """

    def __init__(self, line):
        """
            Initialize by parsing line

            COLUMNS  TYPE   FIELD  DEFINITION
            ---------------------------------
            11-20    float  on1    O11
            21-30    float  on2    O12
            31-40    float  on3    O13
            46-55    float  tn     T1
        """
        record = line[0:6].strip()
        if record == "ORIGX1":
            self.on1 = float(line[10:20].strip())
            self.on2 = float(line[20:30].strip())
            self.on3 = float(line[30:40].strip())
            self.tn = float(line[45:55].strip())
        else:  logger.error(record+'\n') ; raise ValueError

class CRYST1(object):
    """ CRYST1 class

        The CRYST1 record presents the unit cell parameters, space group, and Z
        value. If the structure was not determined by crystallographic means,
        CRYST1 simply defines a unit cube.
    """

    def __init__(self, line):
        """
           Initialize by parsing line

           COLUMNS  TYPE   FIELD  DEFINITION
           ---------------------------------------
            7-15    float  a      a (Angstroms).
           16-24    float  b      b (Angstroms).
           25-33    float  c      c (Angstroms).
           34-40    float  alpha  alpha (degrees).
           41-47    float  beta   beta (degrees).
           48-54    float  gamma  gamma (degrees).
           56-66    string sGroup Space group.
           67-70    int    z      Z value.
        """
        record = line[0:6].strip()
        if record == "CRYST1":
            self.a = float(line[6:15].strip())
            self.b = float(line[15:24].strip())
            self.c = float(line[24:33].strip())
            self.alpha = float(line[33:40].strip())
            self.beta = float(line[40:47].strip())
            self.gamma = float(line[47:54].strip())
            self.sGroup = line[55:65].strip()
            self.z = toInt(line[66:70].strip())
        else:  logger.error(record+'\n') ; raise ValueError


class SITE(object):
    """ SITE class

        The SITE records supply the identification of groups comprising
        important sites in the macromolecule.
    """

    def __init__(self, line):
        """
            Initialize by parsing the line

            COLUMNS  TYPE   FIELD    DEFINITION
            --------------------------------------------------------------
             8-10    int    seqNum   Sequence number.
            12-14    string siteID   Site name.
            16-17    int    numRes   Number of residues comprising site.
            19-21    string resName1 Residue name for first residue
                                     comprising site.
            23       string chainID1 Chain identifier for first residue
                                     comprising site.
            24-27    int    seq1     Residue sequence number for first
                                     residue comprising site.
            28       string iCode1   Insertion code for first residue
                                     comprising site.
            30-32    string resName2 Residue name for second residue
                                     comprising site.
            34       string chainID2 Chain identifier for second residue
                                     comprising site.
            35-38    int    seq2     Residue sequence number for second
                                     residue comprising site.
            39       string iCode2   Insertion code for second residue
                                     comprising site.
            41-43    string resName3 Residue name for third residue
                                     comprising site.
            45       string chainID3 Chain identifier for third residue
                                     comprising site.
            46-49    int    seq3     Residue sequence number for third
                                     residue comprising site.
            50       string iCode3   Insertion code for third residue
                                     comprising site.
            52-54    string resName4 Residue name for fourth residue
                                     comprising site.
            56       string chainID4 Chain identifier for fourth residue
                                     comprising site.
            57-60    int    seq4     Residue sequence number for fourth
                                     residue comprising site.
            61       string iCode4   Insertion code for fourth residue
                                     comprising site.
        """
        record = line[0:6].strip()
        if record == "SITE":
            self.seqNum = toInt(line[7:10].strip())
            self.siteID = line[11:14].strip()
            self.numRes = toInt(line[15:17].strip())
            self.resName1 = line[18:21].strip()
            self.chainID1 = line[22].strip()
            self.seq1 = toInt(line[23:27].strip())
            self.iCode1 = line[27].strip()
            self.resName2 = line[29:32].strip()
            self.chainID2 = line[33].strip()
            self.seq2 = toInt(line[34:38].strip())
            self.iCode2 = line[38].strip()
            self.resName3 = line[40:43].strip()
            self.chainID3 = line[44].strip()
            self.seq3 = toInt(line[45:49].strip())
            self.iCode3 = line[49].strip()
            self.resName4 = line[51:54].strip()
            self.chainID4 = line[55].strip()
            self.seq4 = toInt(line[56:60].strip())
            try:  self.iCode4 = line[60].strip()
            except IndexError:  self.iCode4 = None
        else:  logger.error(record+'\n') ; raise ValueError

class CISPEP(object):
    """ CISPEP field

        CISPEP records specify the prolines and other peptides found to be in
        the cis conformation. This record replaces the use of footnote records
        to list cis peptides.
    """

    def __init__(self, line):
        """
            Initialize by parsing line

            COLUMNS  TYPE   FIELD    DEFINITION
            -----------------------------------------------------------
            8-10     int    serNum   Record serial number.
            12-14    string pep1     Residue name.
            16       string chainID1 Chain identifier.
            18-21    int    seqNum1  Residue sequence number.
            22       string icode1   Insertion code.
            26-28    string pep2     Residue name.
            30       string chainID2 Chain identifier.
            32-35    int    seqNum2  Residue sequence number.
            36       string icode2   Insertion code.
            44-46    int    modNum   Identifies the specific model.
            54-59    float  measure  Measure of the angle in degrees.
        """
        record = line[0:6].strip()
        if record == "CISPEP":
            self.serNum = toInt(line[7:10].strip())
            self.pep1 = line[11:14].strip()
            self.chainID1 = line[15].strip()
            self.seqNum1 = toInt(line[17:21].strip())
            self.icode1 = line[21].strip()
            self.pep2 = line[25:28].strip()
            self.chainID2 = line[29].strip()
            self.seqNum2 = toInt(line[31:35].strip())
            self.icode2 = line[35].strip()
            self.modNum = toInt(line[43:46].strip())
            self.measure = float(line[53:59].strip())
        else:  logger.error(record+'\n') ; raise ValueError

class SLTBRG(object):
    """ SLTBRG field

        The SLTBRG records specify salt bridges in the entry.
        records and is provided here for convenience in searching.
    """

    def __init__(self, line):
        """
            Initialize by parsing line

            COLUMNS  TYPE   FIELD     DEFINITION
            -----------------------------------------------------
            13-16    string name1     Atom name.
            17       string altLoc1   Alternate location indicator.
            18-20    string resName1  Residue name.
            22       string chainID1  Chain identifier.
            23-26    int    resSeq1   Residue sequence number.
            27       string iCode1    Insertion code.
            43-46    string name2     Atom name.
            47       string altLoc2   Alternate location indicator.
            48-50    string resName2  Residue name.
            52       string chainID2  Chain identifier.
            53-56    int    resSeq2   Residue sequence number.
            57       string iCode2    Insertion code.
            60-65    string sym1      Symmetry operator for 1st atom.
            67-72    string sym2      Symmetry operator for 2nd atom.
        """
        record = line[0:6].strip()
        if record == "SLTBRG":
            self.name1 = line[12:16].strip()
            self.altLoc1 = line[16].strip()
            self.resName1 = line[17:20].strip()
            self.chainID1 = line[21].strip()
            self.resSeq1 = toInt(line[22:26].strip())
            self.iCode1 = line[26].strip()
            self.name2 = line[42:46].strip()
            self.altLoc2 = line[46].strip()
            self.resName2 = line[47:50].strip()
            self.chainID2 = line[51].strip()
            self.resSeq2 = toInt(line[52:56].strip())
            self.iCode2 = line[56].strip()
            self.sym1 = line[59:65].strip()
            self.sym2 = line[66:72].strip()
        else:  logger.error(record+'\n') ; raise ValueError

class HYDBND(object):
    """ HYDBND field

        The HYDBND records specify hydrogen bonds in the entry.
    """

    def __init__(self, line):
        """
            Initialize by parsing line

            COLUMNS  TYPE   FIELD  DEFINITION
            -----------------------------------------------------------
            13-16    string name1          Atom name.
            17       string altLoc1        Alternate location indicator.
            18-20    string resName1       Residue name.
            22       string Chain1         Chain identifier.
            23-27    int    resSeq1        Residue sequence number.
            28       string ICode1         Insertion code.
            30-33    string nameH          Hydrogen atom name.
            34       string altLocH        Alternate location indicator.
            36       string ChainH         Chain identifier.
            37-41    int    resSeqH        Residue sequence number.
            42       string iCodeH         Insertion code.
            44-47    string name2          Atom name.
            48       string altLoc2        Alternate location indicator.
            49-51    string resName2       Residue name.
            53       string chainID2       Chain identifier.
            54-58    int    resSeq2        Residue sequence number.
            59       string iCode2         Insertion code.
            60-65    string sym1           Symmetry operator for 1st
                                                          non-hydrogen atom.
            67-72    string sym2           Symmetry operator for 2nd
                                              non-hydrogen atom.
        """
        record = line[0:6].strip()
        if record == "HYDBND":
            self.name1 = line[12:16].strip()
            self.altLoc1 = line[16].strip()
            self.resName1 = line[17:20].strip()
            self.Chain1 = line[21].strip()
            self.resSeq1 = line[22:27].strip()
            self.ICode1 = line[27].strip()
            self.nameH = line[29:33].strip()
            self.altLocH = line[33].strip()
            self.ChainH = line[35].strip()
            self.resSeqH = line[36:41].strip()
            self.ICodeH = line[41].strip()
            self.name2 = line[43:47].strip()
            self.altLoc2 = line[47].strip()
            self.resName2 = line[48:51].strip()
            self.Chain2 = line[52].strip()
            self.resSeq2 = line[53:58].strip()
            self.ICode2 = line[58].strip()
            self.sym1 = line[59:65].strip()
            self.sym2 = line[66:72].strip()
        else:  logger.error(record+'\n') ; raise ValueError

class LINK(object):
    """ LINK field

        The LINK records specify connectivity between residues that is not
        implied by the primary structure. Connectivity is expressed in terms of
        the atom names. This record supplements information given in CONECT
        records and is provided here for convenience in searching.
    """

    def __init__(self, line):
        """
            Initialize by parsing line

            COLUMNS  TYPE   FIELD     DEFINITION
            -----------------------------------------------------
            13-16    string name1     Atom name.
            17       string altLoc1   Alternate location indicator.
            18-20    string resName1  Residue name.
            22       string chainID1  Chain identifier.
            23-26    int    resSeq1   Residue sequence number.
            27       string iCode1    Insertion code.
            43-46    string name2     Atom name.
            47       string altLoc2   Alternate location indicator.
            48-50    string resName2  Residue name.
            52       string chainID2  Chain identifier.
            53-56    int    resSeq2   Residue sequence number.
            57       string iCode2    Insertion code.
            60-65    string sym1      Symmetry operator for 1st atom.
            67-72    string sym2      Symmetry operator for 2nd atom.
        """
        record = line[0:6].strip()
        if record == "LINK":
            self.name1 = line[12:16].strip()
            self.altLoc1 = line[16].strip()
            self.resName1 = line[17:20].strip()
            self.chainID1 = line[21].strip()
            self.resSeq1 = toInt(line[22:26].strip())
            self.iCode1 = line[26].strip()
            self.name2 = line[42:46].strip()
            self.altLoc2 = line[46].strip()
            self.resName2 = line[47:50].strip()
            self.chainID2 = line[51].strip()
            self.resSeq2 = toInt(line[52:56].strip())
            self.iCode2 = line[56].strip()
            self.sym1 = line[59:65].strip()
            self.sym2 = line[66:72].strip()
        else:  logger.error(record+'\n') ; raise ValueError


class SSBOND(object):
    """ SSBOND field

        The SSBOND record identifies each disulfide bond in protein and
        polypeptide structures by identifying the two residues involved in the
        bond.
    """

    def __init__(self, line):
        """
            Initialize by parsing line

            COLUMNS  TYPE   FIELD  DEFINITION
            -----------------------------------------------------
             8 - 10  int    serNum         Serial number.
            16       string chainID1       Chain identifier.
            18 - 21  int    seqNum1        Residue sequence number.
            22       string icode1         Insertion code.
            30       string chainID2       Chain identifier.
            32 - 35  int    seqNum2        Residue sequence number.
            36       string icode2         Insertion code.
            60 - 65  string sym1           Symmetry operator for 1st residue.
            67 - 72  string sym2           Symmetry operator for 2nd residue.
        """
        record = line[0:6].strip()
        if record == "SSBOND":
            self.serNum = toInt(line[7:10].strip())
            self.chainID1 = line[15].strip()
            self.seqNum1 = toInt(line[17:21].strip())
            self.icode1 = line[21].strip()
            self.chainID2 = line[29].strip()
            self.seqNum2 = toInt(line[31:35].strip())
            self.icode2 = line[35].strip()
            self.sym1 = line[59:65].strip()
            self.sym2 = line[66:72].strip()
        else:  logger.error(record+'\n') ; raise ValueError

class TURN(object):
    """ TURN field

        The TURN records identify turns and other short loop turns which
        normally connect other secondary structure segments.
    """

    def __init__(self, line):
        """
            Initialize by parsing line

            COLUMNS  TYPE   FIELD       DEFINITION
            ---------------------------------------------------------
            8-10     int    seq         Turn number; starts with 1 and
                                        increments by one.
            12-14    string turnId      Turn identifier
            16-18    string initResName Residue name of initial residue in
                                        turn.
            20       string initChainId Chain identifier for the chain
                                        containing this turn.
            21-24    int    initSeqNum  Sequence number of initial residue in
                                        turn.
            25       string initICode   Insertion code of initial residue in
                                        turn.
            27-29    string endResName  Residue name of terminal residue of
                                        turn.
            31       string endChainId  Chain identifier for the chain
                                        containing this turn.
            32-35    int    endSeqNum   Sequence number of terminal residue of
                                        turn.
            36       string endICode    Insertion code of terminal residue of
                                        turn.
            41-70    string comment     Associated comment.
        """
        record = line[0:6].strip()
        if record == "TURN":
            self.seq = toInt(line[7:10].strip())
            self.turnId = line[11:14].strip()
            self.initResName = line[15:18].strip()
            self.initChainId = line[19].strip()
            self.initSeqNum = toInt(line[20:24].strip())
            self.initICode = line[24].strip()
            self.endResName = line[26:29].strip()
            self.endChainId = line[30].strip()
            self.endSeqNum = toInt(line[31:35].strip())
            self.endICode = line[35].strip()
            self.comment = line[40:70].strip()
        else:  logger.error(record+'\n') ; raise ValueError

class SHEET(object):
    """ SHEET field

        SHEET records are used to identify the position of sheets in the
        molecule. Sheets are both named and numbered. The residues where the
        sheet begins and ends are noted.
    """

    def __init__(self, line):
        """
            Initialize by parsing line

            COLUMNS  TYPE   FIELD       DEFINITION
            -------------------------------------------------
             8 - 10  int    strand      Strand number which starts at 1 for
                                        each strand within a sheet and
                                        increases by one.
            12 - 14  string sheetID     Sheet identifier.
            15 - 16  int    numStrands  Number of strands in sheet.
            18 - 20  string initResName Residue name of initial residue.
            22       string initChainID Chain identifier of initial residue in
                                        strand.
            23 - 26  int    initSeqNum  Sequence number of initial residue in
                                        strand.
            27       string initICode   Insertion code of initial residue in
                                        strand.
            29 - 31  string endResName  Residue name of terminal residue.
            33       string endChainID  Chain identifier of terminal residue.
            34 - 37  int    endSeqNum   Sequence number of terminal residue.
            38       string endICode    Insertion code of terminal residue.
            39 - 40  int    sense       Sense of strand with respect to
                                        previous strand in the sheet. 0 if
                                        first strand, 1 if parallel, -1 if
                                        anti-parallel.
            42 - 45  string curAtom     Registration. Atom name in current
                                        strand.
            46 - 48  string curResName  Registration. Residue name in current
                                        strand.
            50       string curChainId  Registration. Chain identifier in
                                        current strand.
            51 - 54  int    curResSeq   Registration. Residue sequence number
                                        in current strand.
            55       string curICode    Registration. Insertion code in current
                                        strand.
            57 - 60  string prevAtom    Registration. Atom name in previous
                                        strand.
            61 - 63  string prevResName Registration. Residue name in previous
                                        strand.
            65       string prevChainId Registration. Chain identifier in
                                        previous strand.
            66 - 69  int    prevResSeq  Registration. Residue sequence number
                                        in previous strand.
            70       string prevICode   Registration. Insertion code in
                                        previous strand.
        """
        record = line[0:6].strip()
        if record == "SHEET":
            self.strand = toInt(line[7:10].strip())
            self.sheetID = line[11:14].strip()
            self.numStrands = toInt(line[14:16].strip())
            self.initResName = line[17:20].strip()
            self.initChainID = line[21].strip()
            self.initSeqNum = toInt(line[22:26].strip())
            self.initICode = line[26].strip()
            self.endResName = line[28:31].strip()
            self.endChainID = line[32].strip()
            self.endSeqNum = toInt(line[33:37].strip())
            self.endICode = line[37].strip()
            self.sense = toInt(line[38:40].strip())
            try:
                self.curAtom = line[41:45].strip()
                self.curResName = line[45:48].strip()
                self.curChainID = line[49].strip()
                try:  self.curResSeq = toInt(line[50:54].strip())
                except ValueError:  self.curResSeq = None
                self.curICode = line[54].strip()
                self.prevAtom = line[56:60].strip()
                self.prevResName = line[60:63].strip()
                self.prevChainID = line[64].strip()
                try:  self.prevResSeq = toInt(line[65:69].strip())
                except ValueError:  self.prevResSeq = None
                self.prevICode = line[69].strip()
            except IndexError:
                self.curAtom = None
                self.curResName = None
                self.curChainID = None
                self.curResSeq = None
                self.curICode = None
                self.prevAtom = None
                self.prevResName = None
                self.prevChainID = None
                self.prevResSeq = None
                self.prevICode = None
        else:  logger.error(record+'\n') ; raise ValueError

class HELIX(object):
    """ HELIX field

        HELIX records are used to identify the position of helices in the
        molecule. Helices are both named and numbered. The residues where the
        helix begins and ends are noted, as well as the total length.
    """

    def __init__(self, line):
        """
            Initialize by parsing line

            COLUMNS  TYPE   FIELD  DEFINITION
            ------------------------------------------------------
            8-10     int    serNum      Serial number of the helix.  This
                                        starts at 1 and increases
                                        incrementally.
            12-14    string helixID     Helix identifier.  In addition to a
                                        serial number, each helix is given an
                                        alphanumeric character helix identifier.
            16-18    string initResName Name of the initial residue.
            20       string initChainID Chain identifier for the chain
                                        containing this helix.
            22-25    int    initSeqNum  Sequence number of the initial residue.
            26       string initICode   Insertion code of the initial residue.
            28-30    string endResName  Name of the terminal residue of
                                        the helix.
            32       string endChainID  Chain identifier for the chain
                                        containing this helix.
            34-37    int    endSeqNum   Sequence number of the terminal residue.
            38       string endICode    Insertion code of the terminal residue.
            39-40    int    helixClass  Helix class (see below).
            41-70    string comment     Comment about this helix.
            72-76    int    length      Length of this helix.
        """
        record = line[0:6].strip()
        if record == "HELIX":
            self.serNum = toInt(line[7:10].strip())
            self.helixID = line[11:14].strip()
            self.initResName = line[15:18].strip()
            self.initChainID = line[19].strip()
            self.initSeqNum = toInt(line[21:25].strip())
            self.initICode = line[25].strip()
            self.endResName = line[27:30].strip()
            self.endChainID = line[31].strip()
            self.endSeqNum = toInt(line[33:37].strip())
            self.endICode = line[37].strip()
            try:  self.helixClass = toInt(line[38:40].strip())
            except ValueError:  self.helixClass = None
            self.comment = line[40:70].strip()
            try:  self.length = toInt(line[71:76].strip())
            except ValueError:  self.length = None
        else:  logger.error(record+'\n') ; raise ValueError

class FORMUL(object):
    """ FORMUL field

        The FORMUL record presents the chemical formula and charge of a
        non-standard group.
    """

    def __init__(self, line):
        """
            Initialize by parsing line

            COLUMNS  TYPE   FIELD    DEFINITION
            -----------------------------------------------------
            9-10     int    compNum  Component number
            13-15    string hetID    Het identifier
            19       string asterisk * for water
            20-70    string text     Chemical formula
        """
        record = line[0:6].strip()
        if record == "FORMUL":
            self.compNum = toInt(line[8:10].strip())
            self.hetID = line[12:15].strip()
            self.asterisk = line[19].strip()
            self.text = line[19:70].strip()
        else:  logger.error(record+'\n') ; raise ValueError

class HETSYN(object):
    """ HETSYN field

        This record provides synonyms, if any, for the compound in the
        corresponding (i.e., same hetID) HETNAM record. This is to allow
        greater flexibility in searching for HET groups.
    """

    def __init__(self, line):
        """
            Initialize by parsing line

            COLUMNS  TYPE   FIELD         DEFINITION
            -----------------------------------------------------
            12-14    string hetID         Het identifier, right-justified.
            16-70    string hetSynonyms   List of synonyms
        """
        record = line[0:6].strip()
        if record == "HETSYN":
            self.hetID = line[11:14].strip()
            self.hetSynonyms = line[15:70].strip()
        else:  logger.error(record+'\n') ; raise ValueError

class HETNAM(object):
    """ HETNAM field

        This record gives the chemical name of the compound with the given
        hetID.
    """

    def __init__(self, line):
        """
            Initialize by parsing line

            COLUMNS  TYPE   FIELD  DEFINITION
            -----------------------------------------------------
            12-14    string hetID  Het identifier, right-justified.
            16-70    string text   Chemical name.
        """
        record = line[0:6].strip()
        if record == "HETNAM":
            self.hetID = line[11:14].strip()
            self.text = line[15:70].strip()
        else:  logger.error(record+'\n') ; raise ValueError

class HET(object):
    """ HET field

        HET records are used to describe non-standard residues, such as
        prosthetic groups, inhibitors, solvent molecules, and ions for which
        coordinates are supplied. Groups are considered HET if they are:
         - not one of the standard amino acids, and
         - not one of the nucleic acids (C, G, A, T, U, and I), and
         - not one of the modified versions of nucleic acids (+C, +G, +A, +T,
           +U, and +I), and
         - not an unknown amino acid or nucleic acid where UNK is used to
           indicate the unknown residue name.
        Het records also describe heterogens for which the chemical identity is
        unknown, in which case the group is assigned the hetID UNK.
    """

    def __init__(self, line):
        """
            Initialize by parsing line

            COLUMNS  TYPE   FIELD       DEFINITION
            --------------------------------------------------------
            8-10     string hetID       Het identifier, right-justified.
            13       string ChainID     Chain identifier.
            14-17    int    seqNum      Sequence number.
            18       string iCode       Insertion code.
            21-25    int    numHetAtoms Number of HETATM records for the
            31-70    string text        Text describing Het group.
        """
        record = line[0:6].strip()
        if record == "HET":
            self.hetID = line[7:10].strip()
            self.chainID = line[12].strip()
            try:  self.seqNum = toInt(line[13].strip())
            except ValueError:  self.seqNum = None
            self.iCode = line[17].strip()
            self.numHetAtoms = toInt(line[20:25].strip())
            self.text = line[30:70].strip()
        else:  logger.error(record+'\n') ; raise ValueError

class MODRES(object):
    """ MODRES field

        The MODRES record provides descriptions of modifications (e.g.,
        chemical or post-translational) to protein and nucleic acid residues.
        Included are a mapping between residue names given in a PDB entry and
        standard residues.
    """

    def __init__(self, line):
        """
            Initialize by parsing a line

            COLUMNS  TYPE   FIELD   DEFINITION
            ---------------------------------------
            8-11     string idCode  ID code of this entry.
            13-15    string resName Residue name used in this entry.
            17       string chainID Chain identifier.
            19-22    int    seqNum  Sequence number.
            23       string iCode   Insertion code.
            25-27    string stdRes  Standard residue name.
            30-70    string comment Description of the residue modification.
        """
        record = line[0:6].strip()
        if record == "MODRES":
            string.idCode = line[7:11].strip()
            string.resName = line[12:15].strip()
            string.chainID = line[16].strip()
            string.seqNum = toInt(line[18:22].strip())
            string.iCode = line[22].strip()
            string.stdRes = line[24:27].strip()
            string.comment = line[29:70].strip()
        else:  logger.error(record+'\n') ; raise ValueError

class SEQRES(object):
    """ SEQRES field

        SEQRES records contain the amino acid or nucleic acid sequence of
        residues in each chain of the macromolecule that was studied.
    """

    def __init__(self, line):
        """
            Initialize by parsing a line

            COLUMNS  TYPE   FIELD   DEFINITION
            -----------------------------------------------------
            9-10     int    serNum  Serial number of the SEQRES record for the
                                    current chain.  Starts at 1 and increments
                                    by one each line.  Reset to 1 for each
                                    chain.
            12       string chainID Chain identifier.  This may be any single
                                    legal character, including a blank which is
                                    used if there is only one chain.
            14-17    int    numRes  Number of residues in the chain.  This
                                    value is repeated on every record.
            20-22    string resName Residue name.
            24-26    string resName Residue name.
            28-30    string resName Residue name.
            32-34    string resName Residue name.
            36-38    string resName Residue name.
            40-42    string resName Residue name.
            44-46    string resName Residue name.
            48-50    string resName Residue name.
            52-54    string resName Residue name.
            56-58    string resName Residue name.
            60-62    string resName Residue name.
            64-66    string resName Residue name.
            68-70    string resName Residue name.
        """
        record = line[0:6].strip()
        if record == "SEQRES":
            self.serNum = toInt(line[8:10].strip())
            self.chainID = line[11].strip()
            self.numRes = toInt(line[13:17].strip())
            self.resName = []
            self.resName.append(line[19:22].strip())
            self.resName.append(line[23:26].strip())
            self.resName.append(line[27:30].strip())
            self.resName.append(line[31:34].strip())
            self.resName.append(line[35:38].strip())
            self.resName.append(line[39:42].strip())
            self.resName.append(line[43:46].strip())
            self.resName.append(line[47:50].strip())
            self.resName.append(line[51:54].strip())
            self.resName.append(line[55:58].strip())
            self.resName.append(line[59:62].strip())
            self.resName.append(line[63:66].strip())
            self.resName.append(line[67:70].strip())
        else:  logger.error(record+'\n') ; raise ValueError

class SEQADV(object):
    """ SEQADV field

        The SEQADV record identifies conflicts between sequence information in
        the ATOM records of the PDB entry and the sequence database entry given
        on DBREF. Please note that these records were designed to identify
        differences and not errors. No assumption is made as to which database
        contains the correct data. PDB may include REMARK records in the entry
        that reflect the depositor's view of which database has the correct
        sequence.
    """

    def __init__(self, line):
        """
            Initialize by parsing line

            COLUMNS  TYPE   FIELD    DEFINITION
            -----------------------------------------------------
            8-11     string idCode   ID code of this entry.
            13-15    string resName  Name of the PDB residue in conflict.
            17       string chainID  PDB chain identifier.
            19-22    int    seqNum   PDB sequence number.
            23       string iCode    PDB insertion code.
            25-28    string database Sequence database name.
            30-38    string dbIdCode Sequence database accession
                                     number.
            40-42    string dbRes    Sequence database residue name.
            44-48    int    dbSeq    Sequence database sequence number.
            50-70    string conflict Conflict comment.
        """
        record = line[0:6].strip()
        if record == "SEQADV":
            self.idCode = line[7:11].strip()
            self.resName = line[12:15].strip()
            self.chainID = line[16].strip()
            try:  self.seqNum = toInt(line[19:22].strip())
            except ValueError:  self.seqNum = None
            self.iCode = line[22].strip()
            self.database = line[24:28].strip()
            self.dbIdCode = line[29:38].strip()
            self.dbRes = line[39:42].strip()
            try:  self.dbSeq = toInt(line[43:48].strip())
            except ValueError:  self.dbSeq = None
            self.conflict = line[49:70].strip()
        else:  logger.error(record+'\n') ; raise ValueError

class DBREF(object):
    """ DBREF field

        The DBREF record provides cross-reference links between PDB sequences
        and the corresponding database entry or entries. A cross reference to
        the sequence database is mandatory for each peptide chain with a length
        greater than ten (10) residues. For nucleic acid entries a DBREF record
        pointing to the Nucleic Acid Database (NDB) is mandatory when the
        corresponding entry exists in NDB.
    """

    def __init__(self, line):
        """
             Initialize by parsing a line.

             COLUMNS  TYPE   FIELD       DEFINITION
             ------------------------------------------------------
             8-11     string idCode      ID code of this entry.
             13       string chainID     Chain identifier.
             15-18    int    seqBegin    Initial sequence number of the PDB
                                         sequence segment.
             19       string insertBegin Initial insertion code of the PDB
                                         sequence segment.
             21-24    int    seqEnd      Ending sequence number of the PDB
                                         sequence segment.
             25       string insertEnd   Ending insertion code of the PDB
                                         sequence segment.
             27-32    string database    Sequence database name.  "PDB" when
                                         a corresponding sequence database
                                         entry has not been identified.
             34-41    string dbAccession Sequence database accession code.
                                         For GenBank entries, this is the
                                         NCBI gi number.
             43-54    string dbIdCode    Sequence database identification
                                         code.  For GenBank entries, this is
                                         the accession code.
             56-60    int    dbseqBegin  Initial sequence number of the
                                         database seqment.
             61       string dbinsBeg    Insertion code of initial residue
                                         of the segment, if PDB is the
                                         reference.
             63-67    int    dbseqEnd    Ending sequence number of the
                                         database segment.
             68       string dbinsEnd    Insertion code of the ending
                                         residue of the segment, if PDB is
                                         the reference.
        """
        record = line[0:6].strip()
        if record == "DBREF":
            self.idCode = line[7:11].strip()
            self.chainID = line[12].strip()
            self.seqBegin = toInt(line[14:18].strip())
            self.insertBegin = line[18].strip()
            self.seqEnd = toInt(line[20:24].strip())
            self.insertEnd = line[24].strip()
            self.database = line[26:32].strip()
            self.dbAccession = line[33:41].strip()
            self.dbIdCode = line[42:54].strip()
            self.dbseqBegin = toInt(line[55:60].strip())
            self.dbinsBeg = line[60].strip()
            self.dbseqEnd = toInt(line[62:67].strip())
            try:  self.dbinsEnd = line[67].strip()
            except IndexError:  self.dbinsEnd = None
        else:  logger.error(record+'\n') ; raise ValueError

class REMARK(object):
    """ REMARK field

        REMARK records present experimental details, annotations, comments, and
        information not included in other records. In a number of cases,
        REMARKs are used to expand the contents of other record types. A new
        level of structure is being used for some REMARK records. This is
        expected to facilitate searching and will assist in the conversion to a
        relational database.
    """

    def __init__(self, line):
        """
            Initialize by parsing line
        """
        record = line[0:6].strip()
        if record == "REMARK":
            try:
                self.remarkNum = toInt(line[7:10].strip())
            except ValueError:
                self.remarkNum = None
            self.remarkDict = {}
            remarkText = line[11:70]
            if self.remarkNum == 1:
                subfield = line[11:20].strip()
                if subfield == "REFERENCE":
                    self.remarkDict["refNum"] = toInt(line[21:70].strip())
                elif subfield == "AUTH":
                    self.remarkDict["authorList"] = line[19:70].strip()
                elif subfield == "TITL":
                    self.remarkDict["title"] = line[19:70].strip()
                elif subfield == "EDIT":
                    self.remarkDict["editorList"] = line[19:70].strip()
                elif subfield == "REF":
                    self.remarkDict["ref"] = line[19:66].strip()
                elif subfield == "PUBL":
                    self.remarkDict["pub"] = line[19:70].strip()
                elif subfield == "REFN":
                    self.remarkDict["refn"] = line[19:70].strip()
            elif self.remarkNum == 2:
                restr = line[22:27].strip()
                try:  self.remarkDict["resolution"] = float(restr)
                except ValueError:
                    self.remarkDict["comment"] = line[11:70].strip()
            else:
                self.remarkDict["text"] = line[11:70].strip()


class JRNL(object):
    """ JRNL field

        The JRNL record contains the primary literature citation that describes
        the experiment which resulted in the deposited coordinate set. There is
        at most one JRNL reference per entry. If there is no primary reference,
        then there is no JRNL reference. Other references are given in REMARK
        1.
    """

    def __init__(self, line):
        """
            Initialize by parsing line

            COLUMNS  TYPE   FIELD  DEFINITION
            -----------------------------------------------
            13-70    string text   See Details on web.
        """
        record = line[0:6].strip()
        if record == "JRNL":
            self.text = line[12:70].strip()
        else:  logger.error(record+'\n') ; raise ValueError

class SPRSDE(object):
    """ SPRSDE field

        The SPRSDE records contain a list of the ID codes of entries that were
        made obsolete by the given coordinate entry and withdrawn from the PDB
        release set. One entry may replace many. It is PDB policy that only the
        principal investigator of a structure has the authority to withdraw it.
    """

    def __init__(self, line):
        """
            Initialize by parsing line

            COLUMNS  TYPE   FIELD      DEFINITION
            -----------------------------------------------
            12-20    string sprsdeDate Date this entry superseded the
                                       listed entries.
            22-25    string idCode     ID code of this entry.
            32-35    string sIdCode    ID code of a superseded entry.
            37-40    string sIdCode    ID code of a superseded entry.
            42-45    string sIdCode    ID code of a superseded entry.
            47-50    string sIdCode    ID code of a superseded entry.
            52-55    string sIdCode    ID code of a superseded entry.
            57-60    string sIdCode    ID code of a superseded entry.
            62-65    string sIdCode    ID code of a superseded entry.
            67-70    string sIdCode    ID code of a superseded entry.
        """
        record = line[0:6].strip()
        if record == "SPRSDE":
            self.sprsdeDate = line[11:20].strip()
            self.idCode = line[21:25].strip()
            self.sIdCodes = []
            self.sIdCodes.append(line[31:35].strip())
            self.sIdCodes.append(line[36:40].strip())
            self.sIdCodes.append(line[41:45].strip())
            self.sIdCodes.append(line[46:50].strip())
            self.sIdCodes.append(line[51:55].strip())
            self.sIdCodes.append(line[56:60].strip())
            self.sIdCodes.append(line[61:65].strip())
            self.sIdCodes.append(line[66:70].strip())
        else:  logger.error(record+'\n') ; raise ValueError

class REVDAT(object):
    """ REVDAT field

        REVDAT records contain a history of the modifications made to an entry
        since its release.
    """

    def __init__(self, line):
        """
            Initialize by parsing a line.

            COLUMNS  TYPE   FIELD  DEFINITION
            -------------------------------------------------------
            8-10     int    modNum  Modification number.
            14-22    string modDate Date of modification (or release for
                                    new entries).
            24-28    string modId   Identifies this particular modification.
                                    It links to the archive used internally by
                                    PDB.
            32       int    modType An integer identifying the type of
                                    modification.  In case of revisions
                                    with more than one possible modType,
                                    the highest value applicable will be
                                    assigned.
            40-45    string record  Name of the modified record.
            47-52    string record  Name of the modified record.
            54-59    string record  Name of the modified record.
            61-66    string record  Name of the modified record.
        """
        record = line[0:6].strip()
        if record == "REVDAT":
            self.modNum = toInt(line[7:10].strip())
            self.modDate = line[13:22].strip()
            self.modId = line[23:28].strip()
            self.modType = toInt(line[31].strip())
            self.records = []
            self.records.append(line[39:45].strip())
            self.records.append(line[46:52].strip())
            self.records.append(line[53:59].strip())
            self.records.append(line[60:66].strip())
        else:  logger.error(record+'\n') ; raise ValueError

class AUTHOR(object):
    """ AUTHOR field

        The AUTHOR record contains the names of the people responsible for the
        contents of the entry.
    """

    def __init__(self, line):
        """
            Initialize by parsing a line

            COLUMNS  TYPE   FIELD      DEFINITION
            --------------------------------------------------
            11-70    string authorList List of the author names, separated by
                                       commas
        """
        record = line[0:6].strip()
        if record == "AUTHOR":
            self.authorList = line[10:70].strip()
        else:  logger.error(record+'\n') ; raise ValueError

class EXPDTA(object):
    """ EXPDTA field

        The EXPDTA record identifies the experimental technique used. This may
        refer to the type of radiation and sample, or include the spectroscopic
        or modeling technique. Permitted values include:

        ELECTRON DIFFRACTION
        FIBER DIFFRACTION
        FLUORESCENCE TRANSFER
        NEUTRON DIFFRACTION
        NMR
        THEORETICAL MODEL
        X-RAY DIFFRACTION
    """

    def __init__(self, line):
        """
            Initialize by parsing a line

            COLUMNS  TYPE   FIELD     DEFINITION
            --------------------------------------------------
            11-70    string technique The experimental technique(s) with
                                      optional comment describing the sample
                                      or experiment
        """
        record = line[0:6].strip()
        if record == "EXPDTA":
            self.technique = line[10:70].strip()
        else:  logger.error(record+'\n') ; raise ValueError

class KEYWDS(object):
    """ KEYWDS field

        The KEYWDS record contains a set of terms relevant to the entry. Terms
        in the KEYWDS record provide a simple means of categorizing entries and
        may be used to generate index files. This record addresses some of the
        limitations found in the classification field of the HEADER record. It
        provides the opportunity to add further annotation to the entry in a
        concise and computer-searchable fashion.
    """

    def __init__(self, line):
        """
            Initialize by parsing a line

            COLUMNS  TYPE   FIELD   DEFINITION
            --------------------------------------------------
            11-70    string keywds  Comma-separated list of keywords relevant
                                    to the entry
        """
        record = line[0:6].strip()
        if record == "KEYWDS":
            self.keywds = line[10:70].strip()
        else:  logger.error(record+'\n') ; raise ValueError

class SOURCE(object):
    """ SOURCE field

        The SOURCE record specifies the biological and/or chemical source of
        each biological molecule in the entry. Sources are described by both
        the common name and the scientific name, e.g., genus and species.
        Strain and/or cell-line for immortalized cells are given when they help
        to uniquely identify the biological entity studied.
    """

    def __init__(self, line):
        """
            Initialize by parsing a line

            COLUMNS  TYPE   FIELD   DEFINITION
            --------------------------------------------------
            11-70    string source  Identifies the source of the macromolecule
                                    in a token: value format
        """
        record = line[0:6].strip()
        if record == "SOURCE":
            self.source = line[10:70].strip()
        else:  logger.error(record+'\n') ; raise ValueError


class COMPND(object):
    """ COMPND field

        The COMPND record describes the macromolecular contents of an entry.
        Each macromolecule found in the entry is described by a set of token:
        value pairs, and is referred to as a COMPND record component. Since the
        concept of a molecule is difficult to specify exactly, PDB staff may
        exercise editorial judgment in consultation with depositors in
        assigning these names.

        For each macromolecular component, the molecule name, synonyms, number
        assigned by the Enzyme Commission (EC), and other relevant details are
        specified.
    """

    def __init__(self, line):
        """
            Initialize by parsing a line

            COLUMNS  TYPE   FIELD    DEFINITION
            --------------------------------------------------
            11-70    string compound Description of the molecular list
                                     components.
        """
        record = line[0:6].strip()
        if record == "COMPND":
            self.compound = line[10:70].strip()
        else:  logger.error(record+'\n') ; raise ValueError

class CAVEAT(object):
    """ CAVEAT field

        CAVEAT warns of severe errors in an entry. Use caution when using an
        entry containing this record.
    """

    def __init__(self, line):
        """
            Initialize by parsing line.

            COLUMNS  TYPE   FIELD   DEFINITION
            ----------------------------------------------------
            12-15    string idCode  PDB ID code of this entry.
            20-70    string comment Free text giving the reason for the
                                    CAVEAT.
        """
        record = line[0:6].strip()
        if record == "CAVEAT":
            self.idCode = line[11:15].strip()
            self.comment = line[19:70].strip()
        else:  logger.error(record+'\n') ; raise ValueError

class TITLE(object):
    """ TITLE field

        The TITLE record contains a title for the experiment or analysis that
        is represented in the entry. It should identify an entry in the PDB in
        the same way that a title identifies a paper.
    """

    def __init__(self, line):
        """
            Initialize by parsing a line.

            COLUMNS  TYPE   FIELD  DEFINITION
            ---------------------------------------------
            11-70    string title  Title of the experiment
        """
        record = line[0:6].strip()
        if record == "TITLE":
            self.title = line[10:70].strip()
        else:  logger.error(record+'\n') ; raise ValueError

class OBSLTE(object):
    """ OBSLTE field

        This record acts as a flag in an entry which has been withdrawn from
        the PDB's full release. It indicates which, if any, new entries have
        replaced the withdrawn entry.

        The format allows for the case of multiple new entries replacing one
        existing entry.
    """

    def __init__(self, line):
        """
           Initialize by parsing a line.

           COLUMNS  TYPE   FIELD    DEFINITION
           -----------------------------------------------
           12-20    string repDate  Date that this entry was replaced.
           22-25    string idCode   ID code of this entry.
           32-35    string rIdCode  ID code of entry that replaced
                                    this one.
           37-40    string rIdCode  ID code of entry that replaced
                                    this one.
           42-45    string rIdCode  ID code of entry that replaced
                                    this one.
           47-50    string rIdCode  ID code of entry that replaced
                                    this one.
           52-55    string rIdCode  ID code of entry that replaced
                                    this one.
           57-60    string rIdCode  ID code of entry that replaced
                                    this one.
           62-65    string rIdCode  ID code of entry that replaced
                                    this one.
           67-70    string rIdCode  ID code of entry that replaced
                                    this one.
        """
        record = line[0:6].strip()
        if record == "OBSLTE":
            self.repDate = line[11:20].strip()
            self.idCode = line[21:25].strip()
            self.rIdCodes = []
            self.rIdCodes.append(line[31:35].strip())
            self.rIdCodes.append(line[36:40].strip())
            self.rIdCodes.append(line[41:45].strip())
            self.rIdCodes.append(line[46:50].strip())
            self.rIdCodes.append(line[51:55].strip())
            self.rIdCodes.append(line[56:60].strip())
            self.rIdCodes.append(line[61:65].strip())
            self.rIdCodes.append(line[67:70].strip())
        else:  logger.error(record+'\n') ; raise ValueError

class HEADER(object):
    """ HEADER field

        The HEADER record uniquely identifies a PDB entry through the idCode
        field. This record also provides a classification for the entry.
        Finally, it contains the date the coordinates were deposited at the
        PDB. """

    def __init__(self, line):
        """
           Initialize by parsing a line.

           COLUMNS  TYPE   FIELD          DEFINITION
           ---------------------------------------------------------
           11-50    string classification Classifies the molecule(s)
           51-59    string depDate        Deposition date.  This is the date
                                          the coordinates were received by
                                          the PDB
           63-66    string idCode         This identifier is unique within PDB
        """
        record = line[0:6].strip()
        if record == "HEADER":
            self.classification = line[10:50].strip()
            self.depDate = line[50:59].strip()
            self.IDcode = line[62:66].strip()
        else:  logger.error(record+'\n') ; raise ValueError

def readAtom(line):
    """
        If the ATOM/HETATM is not column-formatted, try to get some
        information by parsing whitespace from the right.  Look for
        five floating point numbers followed by the residue number.

        Parameters
            line:  The line to parse(string)
       if record == ATOM:
            self.serial = toInt(line[6:11].strip())
            self.name = line[12:16].strip()
            self.altLoc = line[16].strip()
            self.resName = line[17:20].strip()
            self.chainID = line[21].strip()
            self.resSeq = toInt(line[22:26].strip())
            self.iCode = line[26].strip()
            self.x = float(line[30:38].strip())
            self.y = float(line[38:46].strip())
            self.z = float(line[46:54].strip())
            try:
                self.occupancy = float(line[54:60].strip())
                self.tempFactor = float(line[60:66].strip())
                self.segID = line[72:76].strip()
                self.element = line[76:78].strip()
                self.charge = line[78:80].strip()
            except ValueError, IndexError:
                self.occupancy = 0.00
                self.tempFactor = 0.00
                self.segID = 0
                self.element = 0
                self.charge = 0
        else: logger.error(record+'\n') ; raise ValueError
    """

    # Try to find 5 consecutive floats
    words = string.split(line)
    size = len(words) - 1
    consec = 0
    for i in range(size):
        entry = words[size - i]
        try:
            val = float(entry)
            consec = consec + 1
            if consec == 5:
                break
        except ValueError:
            consec = 0

    record = line[0:6].strip()
    newline = line[0:22]
    newline = newline + string.rjust(words[size-i-1],4)
    newline = newline + string.rjust("",3)
    newline = newline + string.rjust(words[size-i],8)
    newline = newline + string.rjust(words[size-i+1],8)
    newline = newline + string.rjust(words[size-i+2],8)
    newline = newline + string.rjust(words[size-i+3],6)
    newline = newline + string.rjust(words[size-i+4],6)
    cmdstr = "%s(newline)" % record
    obj = eval(cmdstr)
    return obj

def readPDB(file):
    """ Parse PDB-format data into array of Atom objects.
        Parameters
          file:  open file object
        Returns (dict, errlist)
          dict:  a dictionary indexed by PDB record names
          errlist:  a list of record names that couldn't be parsed
    """

    pdblist = []  # Array of parsed lines (as objects)
    errlist = []  # List of records we can't parse

    while 1:
        line = file.readline().strip()
        if line == '':  break

        # We assume we have a method for each PDB record and can therefore
        # parse them automatically
        try:
            record = line[0:6].strip()
            if record not in errlist:
                cmdstr = "%s(line)" % record
                obj = eval(cmdstr)
                pdblist.append(obj)
        except NameError as details:
            errlist.append(record)
        except Exception as details:
            if record == "ATOM" or record == "HETATM":
               try:
                   obj = readAtom(line)
                   pdblist.append(obj)
               except Exception as details:
                   sys.stderr.write("Error parsing line: %s\n" % details)
                   sys.stderr.write("<%s>\n" % line.strip())
            elif record == "SITE" or record == "TURN":
                pass
            elif record == "SSBOND" or record == "LINK":
                sys.stderr.write("Warning -- ignoring record: \n")
                sys.stderr.write("<%s>\n" % line.strip())
            else:
                sys.stderr.write("Error parsing line: %s\n" % details)
                sys.stderr.write("<%s>\n" % line.strip())

    return pdblist, errlist

def getRandom():
    """ Download a random PDB and return the path name.
        Returns
          path name of downloaded file
    """

    import os, random

    URL = "ftp://ftp.rcsb.org/pub/pdb/data/structures/all/pdb/"
    pdblines = os.popen("ncftpls %s" % URL).readlines()
    pdbline = string.join(pdblines)
    pdbline = string.replace(pdbline, "\n", "")
    pdbline = string.replace(pdbline, "@", "")
    pdbline = pdbline.strip()
    pdblist = string.split(pdbline)
    pdbZ = random.choice(pdblist)
    os.popen("ncftpget %s/%s" % (URL, pdbZ))
    os.popen("uncompress %s" % pdbZ)
    return pdbZ[:-2]

def main():
    """ Main driver for testing.  Parses set number of random PDBs """

    npdb = 1
    sys.stdout.write("Testing %d PDBs...\n" % npdb)
    for i in range(0, npdb):
        sys.stdout.write("Getting random PDB...\n")
        path = getRandom()
        sys.stdout.write("Parsing %s...\n" % path)
        pdbdict, errlist = readPDB(open(path, "rU"))
        if len(errlist) > 0:  sys.stdout.write("\tSkipped records: %s\n" % errlist)
        sys.stdout.write("\tNo skipped records.\n")

if __name__ == "__main__":  main()
