from functional_group_enumerator import Cocktail
from peptide_builder import PeptideMolecule

if __name__ == '__main__':
    peptide_backbone = PeptideMolecule(
        2,
        include_proline = True
    )
    print(peptide_backbone)
    cocktail = Cocktail(
        peptide_backbone,
        include_amino_acids = True,
        ligand_library = ['Br', 'I'],
    )

    print (cocktail.shake())
    print(cocktail.enumerate(enumeration_complexity='high'))