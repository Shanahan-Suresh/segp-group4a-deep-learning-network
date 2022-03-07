import pandas as pd
import torch

from test_neural_network import load_model

import extract_data as extract
import numpy as np
def normalize_data(data):
    normalized_data = (data-data.min()) / (data.max() - data.min())
    return  normalized_data

def set_data(temperature,humidity,windpseed,srfile,aluminium_temp,chemical_temp,lauric_acid,stearic_acid,parafin_wax,lac,sac,pwc):

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

    #print(dataframe)
    #print(dataframe.dtypes)
    #print(dataframe)
    #print(dataframe)
    '''
    dataframe.append(temperature)
    dataframe.append(humidity)
    dataframe.append(windpseed)
    #dataframe.append(srfile)
    dataframe.append(aluminium_temp)
    dataframe.append(chemical_temp)
    dataframe.append(lauric_acid)
    dataframe.append(stearic_acid)
    dataframe.append(parafin_wax)
    dataframe.append(lac)
    dataframe.append(sac)
    dataframe.append(pwc)
    finalArray = np.asarray(dataframe, dtype = np.float64)
    print(data_min)


    data_min,data_max = get_max_min()
    #print(type(data_min))
    data_min = data_min.to_frame()
    data_min = data_min.transpose()
    data_min.
    #print(data_min)
    print(dataframe)
    print("hi")
    print(data_min)
    print("hi")
    print(dataframe-data_min)
    #dataframe = (dataframe-data_min) / (data_max - data_min)

    #print(dataframe)'''





def main():
    global data
    data,finaldf = extract.main()
    #normalized_data = dataset_function.create_dataset(data)

