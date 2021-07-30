import pandas as pd

class tShield_att:
    def __init__(self):
        df = pd.read_excel(r'/Users/john/Documents/University Work/summer internship/FUSE/data/mine_attributes.xlsx', sheet_name="t shield", skiprows=1)

class afc_att:
    def __init__(self):
        df = pd.read_excel(r'/Users/john/Documents/University Work/summer internship/FUSE/data/mine_attributes.xlsx', sheet_name="afc", skiprows=1)

class flatLinkChain_att:
    def __init__(self):
        df = pd.read_excel(r'/Users/john/Documents/University Work/summer internship/FUSE/data/mine_attributes.xlsx', sheet_name="flat link chain", skiprows=1)

class lowProfileChain_att:
    def __init__(self):
        df = pd.read_excel(r'/Users/john/Documents/University Work/summer internship/FUSE/data/mine_attributes.xlsx', sheet_name="low profile chain", skiprows=1)

