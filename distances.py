from biopython.Bio.PDB import PDBParser

import numpy as np
import sys

parser = PDBParser()

def getSmallestDists(model):
    

    smallestDists = []

    chitosanIds = []



    for chain in model:
        for residue in chain:
            if residue.resname == 'CTS':
                chitosanIds.append(chain.id)

    for r in model.get_residues():
        arr = []
        for id in chitosanIds:
            if r.resname == 'EMO':
                for atom in r:
                    for chitosan in model[id]:
                        for chitosanAtom in chitosan:
                            arr.append(abs(atom - chitosanAtom))
        if len(arr) != 0:
            smallestDists.append(np.amin(arr))

    return smallestDists


modelName = sys.argv[2]
modelFile = sys.argv[1]

print(modelFile)
print(modelName)

structure = parser.get_structure(modelName, modelFile)



#for model in structure:
for i in range(100, 151):
    arr = getSmallestDists(structure[i])
    for element in arr:
        print(element, end =' ')
    print()
