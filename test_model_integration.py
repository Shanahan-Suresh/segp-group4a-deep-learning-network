import pandas as pd
import torch

import extract_data as extract
from test_neural_network import load_model


#Function to normalize data between given minimum and maximum in received dataframe
def normalize_data(data):
    normalized_data = (data-data.min()) / (data.max() - data.min())
    return normalized_data

#Function to forward user variables into neural network as a tensor
def set_data(temperature,humidity,windpseed,aluminium_temp,chemical_temp,lauric_acid,stearic_acid,parafin_wax,lac,sac,pwc):

    dataframe = pd.DataFrame()
    dataframe["Temperature,℃\n  "] = [temperature]
    dataframe['Humidity, %'] = [humidity]
    dataframe['Windspeed, km/hr'] = [windpseed]
    dataframe['Aluminium Temperature'] = [aluminium_temp]
    dataframe['Chemical Temperature'] = [chemical_temp]
    dataframe['Lauric Acid'] = [lauric_acid]
    dataframe['Stearic Acid'] = [stearic_acid]
    dataframe['Parafin Wax'] = [parafin_wax]
    dataframe['Parafin Wax Composition'] = [pwc]
    dataframe['Lauric Acid Composition'] = [lac]
    dataframe['Stearic Acid Composition'] = [sac]

    dataframe = dataframe.astype(float)
    df = data.append(dataframe,ignore_index=True)

    normalized_data = normalize_data(df)
    input_data_normalized = normalized_data.iloc[-1]
    input_data_tensor = torch.tensor(input_data_normalized)

    load_model(input_data_tensor)



def main(excel):
    global data
    data,finaldf = extract.main(excel)
    
