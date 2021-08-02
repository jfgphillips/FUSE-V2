from SolvayIO import *
import pprint

import calculators.unitConversions as uC

class revReactionFlow:
    def __init__(self, soda_ash):
        self.soda_ash = soda_ash
        self.bicarbonate = calciner.revReaction(uC.solidMol("Na2CO3", self.soda_ash))
        self.solv_req_reactants, self.solv_byproducts = solvayTower.revReaction(self.bicarbonate)
        self.amm_req_reactants, self.amm_byproducts, self.waste = ammoniaRecoveryTower.revReaction(
            self.solv_byproducts["NH4Cl"])
        self.slaker_req_reactants = slacker.revReaction(self.amm_req_reactants["Ca(OH)2"])
        self.kiln_req_reactants, self.kiln_byproducts = limeKiln.revReaction(self.slaker_req_reactants["CaO"])
        self.p_method()



    def p_method(self):
        print(f'\n\nthis is step 1 \n{self.step1()}\n'
              f'\n\nthis is step 2 \n{self.step2()}\n'
              f'\n\nthis is step 3 \n{self.step3()}\n'
              f'\n\nthis is step 4 \n{self.step4()}\n'
              f'\n\nthis is step 5 \n{self.step5()}\n'
              f'\n\nthese are the required reactants \n\n{self.requiredreactants()}')

    def step1(self):
        print_format = f"For the production of: {self.soda_ash}g soda ash\n" \
                       f"{uC.solidMass('NaHCO3', self.bicarbonate)}g of sodium bicarbonate is required"
        return print_format

    def step2(self):
        print_format = f"to produce sodium bicarbonate {uC.solidMass('NaHCO3', self.bicarbonate)} \n"\
                       f"req_reactants are (mol): \n{pprint.pformat(self.solv_req_reactants)} \n" \
                       f"byproducts are (mol): {pprint.pformat(self.solv_byproducts)}"
        return print_format

    def step3(self):
        print_format = f"to recycle ammoia ({uC.solidMass('NH4Cl', self.solv_byproducts['NH4Cl'])} g) NH4Cl \n" \
                       f"req_reactants are (mol): {pprint.pformat(self.amm_req_reactants)} \n" \
                       f"byproducts are (mol): {pprint.pformat(self.amm_byproducts)} \n" \
                       f"waste was (mol): {pprint.pformat(self.waste)}"
        return print_format

    def step4(self):
        print_format = f"to recycle ammonia ({uC.solidMass('Ca(OH)2', self.amm_req_reactants['Ca(OH)2'])} g) Ca(OH)2 \n" \
                       f"required reactants are (mol): {pprint.pformat(self.slaker_req_reactants)}"
        return print_format

    def step5(self):
        parameters = {"CaO": uC.solidMass("CaO", self.slaker_req_reactants["CaO"]),
                      "CaCO3": uC.solidMass("CaCO3", self.kiln_req_reactants["CaCO3"]),
                      "byproducts": self.kiln_byproducts}
        print_format = f"in order to produce the required mass of calcium oxide ({parameters['CaO']} g) \n" \
                       f"limestone: {parameters['CaCO3']} g\n" \
                       f"the byproducts were (mol): {pprint.pformat(parameters['byproducts'])}"
        return print_format

    def requiredreactants(self):
        parameters = {"soda_ash": uC.tonnes(self.soda_ash),
                      "NaCl": uC.tonnes(uC.solidMass("NaCl", self.solv_req_reactants["NaCl"])),
                      "CaCO3": uC.tonnes(uC.solidMass("CaCO3", self.kiln_req_reactants["CaCO3"])),
                      "CaCl2": uC.tonnes(uC.solidMass("CaCl2", self.waste["CaCl2"]))}

        print_format = f"the total required starting materials to produce {parameters['soda_ash']} tonnes of soda ash\n"\
                       f"sodium chloride: {parameters['NaCl']} Tonnes\n" \
                       f"Limestone: {parameters['CaCO3']} Tonnes\n" \
                       f"waste produced: calcium chloride: {parameters['CaCl2']} Tonnes"
        return print_format

if __name__ == '__main__':
    test = revReactionFlow(1000000)