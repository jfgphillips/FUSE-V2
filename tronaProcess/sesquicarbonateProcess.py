import pandas as pd


class sequesqicarbonateProcess:
    def __init__(self):
        self.df = pd.read_excel(r'../data/trona_attributes.xlsx',
                                sheet_name='sequesquicarbonate method',
                                skiprows=1)
        self.initiate_process_package = {"crusher": self.df['value'].loc['crusher'],
                                         "dry calciner": self.df['value'].loc['dry calciner'],
                                         "dissolving vessel": self.df['value'].loc['dissolving vessel'],
                                         "clarifier": self.df['value'].loc['clarifier'],
                                         "crystallisation vessel": self.df['value'].loc['crystallisation vessel'],
                                         "centrifuge": self.df['value'].loc['centrifuge'],
                                         "calciner": self.df['value'].loc['dehydration']}


        return
