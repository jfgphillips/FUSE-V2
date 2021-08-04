from SolvayIO import *
from calculators import unitConversions as uC


class reactantflow:
    def __init__(self):
        myBrine = brine.brine_att()
        myAmmonia = ammonia.ammonia_att()
        myLimestone = limestone.limestone_att()
        myWater = 100
        self.saturated_soln = ammoniaSaturator.reaction(myBrine.NaCl_mol, myAmmonia.NH3_mol)
        self.kiln_products = limeKiln.reaction(myLimestone.CaCO3_mol)
        self.solvayTower_products = solvayTower.reaction(self.saturated_soln, self.kiln_products["CO2"])
        self.ammonium_chloride, self.sodium_bicarbonate = filter.reaction(self.solvayTower_products)
        self.calciner_products = calciner.reaction(self.sodium_bicarbonate['NaHCO3'])
        self.slacked_lime = slacker.reaction(self.kiln_products["CaO"], myWater)
        amm_rec_kwargs = {"CaOH2":self.slacked_lime["Ca(OH)2"],"NH4Cl": self.ammonium_chloride["NH4Cl"]}
        self.ammRecTwr_products, self.ammRecTwr_waste = ammoniaRecoveryTower.reaction(**amm_rec_kwargs)
        #print(self.ammRecTwr_products, self.ammRecTwr_waste)
        self.print_dict = self.concat_print_dict()

    def __repr__(self):
        newline = "\n"
        print_format = f'{newline.join(f"{key}: {uC.solidMass(key, value)} grams" for key, value in self.print_dict.items())} '
        return print_format

    def concat_print_dict(self):
        dict = {**self.kiln_products,
                **self.solvayTower_products,
                **self.ammonium_chloride,
                **self.calciner_products,
                **self.slacked_lime,
                **self.ammRecTwr_products,
                **self.ammRecTwr_waste}
        return dict


if __name__ == '__main__':  # TODO: implement this for all the machines, find an emissions and a way to save the process
    test = reactantflow()
    print(test)
