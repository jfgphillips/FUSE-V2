from SolvayIO import *

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

    def step1(self):
        print_format = ("For the production of: ", self.soda_ash, "g \n",
              uC.solidMass("NaHCO3", self.bicarbonate),
              " g of sodium bicarbonate are required")
        return print_format

    def step2(self):
        print("to produce sodium bicarbonate (", uC.solidMass("NaHCO3", self.bicarbonate), ") g \n",
              "req_reactants are (mol): ", self.solv_req_reactants, '\n',
              "byproducts are (mol): ", self.solv_byproducts)
        return

    def step3(self):
        print("to recycle ammoia (", uC.solidMass("NH4Cl", self.solv_byproducts["NH4Cl"]), ") g NH4Cl \n",
              "req_reactants are (mol): ", self.amm_req_reactants, '\n',
              "byproducts are (mol): ", self.amm_byproducts, "\n",
              "waste are (mol): ", self.waste)
        return

    def step4(self):
        print("to recycle ammonia (", uC.solidMass("Ca(OH)2", self.amm_req_reactants["Ca(OH)2"]),
              ") g Ca(OH)2 \n",
              "req_reactants are (mol): ", self.slaker_req_reactants)
        return

    def step5(self):
        parameters = {"CaO": uC.solidMass("CaO", self.slaker_req_reactants["CaO"]),
                      "CaCO3": uC.solidMass("CaCO3", self.kiln_req_reactants["CaCO3"]),
                      "byproducts": self.kiln_byproducts}
        print_format = f"in order to produce the required mass of calcium oxide ({parameters['CaO']} g) \n" \
                       f"limestone: {parameters['CaCO3']} g\n" \
                       f"the byproducts were: {parameters['byproducts']}"
        return print_format

    def requiredreactants(self):
        parameters = {"soda_ash": uC.tonnes(self.soda_ash),
                      "NaCl": uC.tonnes(uC.solidMass("NaCl", self.solv_req_reactants["NaCl"])),
                      "CaCO3": uC.tonnes(uC.solidMass("CaCO3", self.kiln_req_reactants["CaCO3"])),
                      "CaCl2": uC.tonnes(uC.solidMass("CaCl2", self.waste["CaCl2"]))}

        print_format = f"the total required starting materials to produce {parameters['soda_ash']} tonnes of soda ash\n"\
                       f" sodium chloride: {parameters['NaCl']} Tonnes\n" \
                       f" Limestone: {parameters['CaCO3']} Tonnes\n" \
                       f" waste produced \n" \
                       f" calcium chloride: {parameters['CaCl2']} Tonnes"
        return print_format

