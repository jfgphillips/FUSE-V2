import matplotlib.pyplot as plt
from undergroundMining.roomAndPillarMethod import roomAndPillarMethod as rpm

class plot:
    def __init__(self):
        self.all_data = rpm()
        self.emissions_data = self.all_data.total_emissions_df
    def emissions_boxplot(self):
        fields = ['miner_emissions','support_emissions', 'transportation_emissions']
        colours = ['red', 'green', 'blue', 'orange']
        labels = ['miner', 'support','transportation']
        fig, ax = plt.subplots(1, figsize=(12,10))
        print(plt.bar(self.emissions_data.index))


        #for idx, name in enumerate(fields):




if __name__ == '__main__':
    test = plot()