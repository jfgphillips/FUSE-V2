from SolvayIO import *

myBrine = brine.brine_att()
myAmmonia = ammonia.ammonia_att()
myLimestone = limestone.limestone_att()
myWater = 100

if __name__ == '__main__':  # TODO: implement this for all the machines, find an emissions and a way to save the process
    saturated_soln = ammoniaSaturator.reaction(myBrine.NaCl_mol, myAmmonia.NH3_mol)
    print(saturated_soln)
    kiln_products = limeKiln.reaction(myLimestone.CaCO3_mol)
    print(kiln_products)
    solvayTower_products = solvayTower.reaction(saturated_soln, kiln_products["kiln_CO_2"])
    print(solvayTower_products)
    ammonium_chloride, sodium_bicarbonate = filter.reaction(solvayTower_products)
    calciner_products = calciner.reaction(sodium_bicarbonate)
    print(calciner_products)
    slacked_lime = slacker.reaction(kiln_products["CaO"], myWater)
    ammoniaRecoveryTower_products = ammoniaRecoveryTower.reaction(slacked_lime["Ca(OH)2"], ammonium_chloride)
    print(ammoniaRecoveryTower_products)










