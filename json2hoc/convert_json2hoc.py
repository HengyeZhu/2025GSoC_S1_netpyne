#!/usr/bin/env python3

import os
import sys
import pyneuroml
from pyneuroml.neuron import export_to_neuroml2
from neuron import h



def main(acell):
    """Main runner method.
    :param acell: name of cell
    :returns: None
    """
    loader_hoc_file = f"{acell}_loader.hoc"
    loader_hoc_file_txt = """
    /*load_file("nrngui.hoc")*/
    load_file("stdrun.hoc")
    xopen("L1_DAC_bNAC219_1_cell.hoc")
    objref cell
    cell = new L1_DAC_bNAC219_1_cell()
    """
    with open(loader_hoc_file, 'w') as f:
        print(loader_hoc_file_txt, file=f)
    export_to_neuroml2(loader_hoc_file, f"{acell}.morph.cell.nml",
                       includeBiophysicalProperties=False, validate=False)
    os.remove(loader_hoc_file)
    # Note--a couple of diameters are 0.0, modified to 0.001 to validate the
    # model

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("This script only accepts one argument.")
        sys.exit(1)
    main(sys.argv[1])