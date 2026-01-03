import numpy as np
import matplotlib.pyplot as plt
import scipy.io as scio

def ReadCharge(path, atomNum:int, specAtom=None):
    dataFile = f'{path}'
    data = scio.loadmat(dataFile)['data'][0][0]
    name_array = ['Index', 
                'totalCharge', 
                'Polarized_r', 
                'Polarized_theta',
                'Polarized_phi', 
                'MagneticMoment',
                ]
    Index_array = [i for i in range(atomNum)]
    if specAtom==None:
        print()
        print(f"{name_array[0]:^5}   {name_array[1]:>11}   {name_array[2]:>11}   {name_array[3]:>15}   {name_array[4]:>13}   {name_array[5]:>14}")
        print("-----")
        for i in range(len(data[6][0])):
            print(f"{Index_array[i]+1:^5}   {data[0][i][0]:>11.6f}  {data[1][i][0]:>11.6f}  {data[2][i][0]:>15.6f}   {data[3][i][0]:>13.6f}   {data[4][i][0]:>14.6f}")
        print("-----")
        print(f"{name_array[0]:^5}   {name_array[1]:>11}   {name_array[2]:>11}   {name_array[3]:>15}   {name_array[4]:>13}   {name_array[5]:>14}")
        print()
        print('~~~~! Charge OUTPUT FINISH !~~~~')
        print()
    else:
        i = specAtom-1
        print()
        print(f"{name_array[0]:^5}   {name_array[1]:>11}   {name_array[2]:>11}   {name_array[3]:>15}   {name_array[4]:>13}   {name_array[5]:>14}")
        print("-----")
        print(f"{Index_array[i]+1:^5}   {data[0][i][0]:>11.6f}  {data[1][i][0]:>11.6f}  {data[2][i][0]:>15.6f}   {data[3][i][0]:>13.6f}   {data[4][i][0]:>14.6f}")