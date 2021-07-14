from SolvayIO import *
from calculators import unitConversions

soda_ash = 1000000  # grams

if __name__ == '__main__':
    bicarbonate = calciner.revReaction(unitConversions.solidMol("Na2CO3", soda_ash))

    print("For the production of: ", soda_ash, "g \n",
          unitConversions.solidMass("NaHCO3", bicarbonate),
          " g of sodium bicarbonate are required")

    solv_req_reactants, solv_byproducts = solvayTower.revReaction(bicarbonate)

    print("to produce sodium bicarbonate (", unitConversions.solidMass("NaHCO3", bicarbonate), ") g \n",
          "req_reactants are (mol): ", solv_req_reactants, '\n',
          "byproducts are (mol): ", solv_byproducts)

    amm_req_reactants, amm_byproducts, waste = ammoniaRecoveryTower.revReaction(solv_byproducts["NH4Cl"])

    print("to recycle ammoia (", unitConversions.solidMass("NH4Cl", solv_byproducts["NH4Cl"]), ") g NH4Cl \n",
          "req_reactants are (mol): ", amm_req_reactants, '\n',
          "byproducts are (mol): ", amm_byproducts, "\n",
          "waste are (mol): ", waste)

    slaker_req_reactants = slacker.revReaction(amm_req_reactants["Ca(OH)2"])
    print("to recycle ammonia (", unitConversions.solidMass("Ca(OH)2", amm_req_reactants["Ca(OH)2"]), ") g Ca(OH)2 \n",
          "req_reactants are (mol): ", slaker_req_reactants)

    kiln_req_reactants, kiln_byproducts = limeKiln.revReaction(slaker_req_reactants["CaO"])
    print("to produce (", unitConversions.solidMass("CaO", slaker_req_reactants["CaO"]), ") g CaO \n",
          "req_limestone are : ", unitConversions.solidMass("CaCO3", kiln_req_reactants["CaCO3"]), 'g CaCO3\n'
          "byproducts are (mol): ", kiln_byproducts)

    print("\n",
          "TOTAL REQ STARTING MATERIALS TO PRODUCE:", unitConversions.tonnes(soda_ash), "tonnes of soda ash \n",
          "NaCl: ", unitConversions.tonnes(unitConversions.solidMass("NaCl", solv_req_reactants["NaCl"])), "tonnes \n",
          "CaCO3: ", unitConversions.tonnes(unitConversions.solidMass("CaCO3", kiln_req_reactants["CaCO3"])), "tonnes \n",
          "WASTE PRODUCED: ", unitConversions.tonnes(unitConversions.solidMass("CaCl2", waste["CaCl2"])), "tonnes calcium chloride \n")
