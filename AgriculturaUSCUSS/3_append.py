import pandas as pd


data_output1 = './2_Model/BAU/data_land_BAU_Output.csv'
data_output2 = './2_Model/PLANDEACCION/data_land_PLANDEACCION_Output.csv'
data_output3 = './2_Model/DDP50/data_land_DDP50_Output.csv'

df1 = pd.read_csv(data_output1)
df2 = pd.read_csv(data_output2)
df3 = pd.read_csv(data_output3)

dff2 = df1._append(df2)
dff3 = dff2._append(df3)

    
dff3['Capex2023'] = dff3['CapitalInvestment']
dff3['FixedOpex2023'] = dff3['AnnualFixedOperatingCost']
dff3['VarOpex2023'] = dff3['AnnualVariableOperatingCost']
dff3['Opex2023'] = dff3['OperatingCost']
dff3['Externalities2023'] = dff3['AnnualTechnologyEmissionPenaltyByEmission']


dff3.to_csv( './2_Model/f0_OSMOSYS_ECU_Output.csv', index = None, header=True)