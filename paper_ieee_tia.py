'''PAPER IEEE TIA 2025
AUTHOR: ARTHUR GOMES DE SOUZA
ADVISOR: WELLINGTON MAYCON SANTOS BERNARDES.


SYSTEMS USED: 
    1 - Circuit from *Ferreira et al.*;
    2 - IEEE 34-Bus System;
    3 - Feeder ULAE714 -  FEATURED CONSUMERS: Rice processing plant and a carbonated beverage factory; and
    4 - Feeder ULAU13 -  FEATURED CONSUMERS: Large-scale photovoltaic farm and the municipal wastewater treatment plant'''

import py_dss_interface
import pandas as pd 
import time 
import os


start_time = time.time()  # Start time

feeder = 'ULAU13'  #Feeder name: Adrian, 34Bus, ULAE714 and ULAU13

os.makedirs(rf"C:\aie\{feeder}\results", exist_ok=True)


df = pd.DataFrame(columns=[' Case ', ' Transformer Connection ', ' Fault Type ', ' V2/V1 Primary % ', ' V2/V1 Secondary % ', ' Unbalance Ratio ', ' Attribution '])  # DataFrame for data storage

dss = py_dss_interface.DSS()  # Create an instance of the dss class

if feeder == 'Adrian':
    dss_file = rf'C:\aie\{feeder}\Circuit_{feeder}.dss'  # Path to the DSS file circuit case 1
if feeder == '34Bus':
    dss_file = rf'C:\aie\{feeder}\{feeder}.dss'  # Path to the DSS file circuit case 2
if feeder == 'ULAE714' or feeder == 'ULAU13':
    dss_file = rf'C:\aie\{feeder}\Master_{feeder}_DU.dss'  # Path to the DSS file feeders case 3 and 4

# Create a list of faults with case definitions
case_1 = ('New Fault.case_1 phases=1 bus1=b1.1 r=0', 'FT primary Z = 0 Ω')  # Case 1 - 1 phase to ground primary
case_2 = ('New Fault.case_2 phases=1 bus1=b1.1 r=5', 'FT primary Z = 5 Ω')  # Case 2 - 1 phase to ground primary
case_3 = ('New Fault.case_3 phases=1 bus1=b1.1 r=10', 'FT primary Z = 10 Ω')  # Case 3 - 1 phase to ground primary
case_4 = ('New Fault.case_4 phases=1 bus1=b1.1 r=20', 'FT primary Z = 20 Ω')  # Case 4 - 1 phase to ground primary
case_5 = ('New Fault.case_5 phases=1 bus1=b2.1 r=0', 'FT secundary Z = 0 Ω')  # Case 5 - 1 phase to ground secondary
case_6 = ('New Fault.case_6 phases=1 bus1=b2.1 r=5', 'FT secundary Z = 5 Ω')  # Case 6 - 1 phase to ground secondary
case_7 = ('New Fault.case_7 phases=1 bus1=b2.1 r=10', 'FT secundary Z = 10 Ω')  # Case 7 - 1 phase to ground secondary
case_8 = ('New Fault.case_8 phases=1 bus1=b2.1 r=20', 'FT secundary Z = 20 Ω')  # Case 8 - 1 phase to ground secondary
case_9 = ('New Fault.case_9 phases=2 bus1=b1.1.2 r=0', 'FFT primary Z = 0 Ω')  # Case 5 - 2 phase to ground primary
case_10= ('New Fault.case_10 phases=2 bus1=b1.1.2 r=5', 'FFT primary Z = 5 Ω')  # Case 6 - 2 phase to ground primary
case_11 = ('New Fault.case_11 phases=2 bus1=b1.1.2 r=10', 'FFT primary Z = 10 Ω')  # Case 7 - 2 phase to ground primary
case_12 = ('New Fault.case_12 phases=2 bus1=b1.1.2 r=20', 'FFT primary Z = 20 Ω')  # Case 8 - 2 phase to ground primary
case_13 = ('New Fault.case_13 phases=2 bus1=b2.1.2 r=0', 'FFT secundary Z = 0 Ω')  # Case 7 - 2 phase to ground secondary
case_14 = ('New Fault.case_14 phases=2 bus1=b2.1.2 r=5', 'FFT secundary Z = 5 Ω')  # Case 8 - 2 phase to ground secondary
case_15 = ('New Fault.case_15 phases=2 bus1=b2.1.2 r=10', 'FFT secundary Z = 10 Ω')  # Case 9 - 2 phase to ground secondary
case_16 = ('New Fault.case_16 phases=2 bus1=b2.1.2 r=20', 'FFT secundary Z = 20 Ω')  # Case 10 - 2 phase to ground secondary
case_17 = ('New Fault.case_17 phases=2 bus1=b1.1.2 bus2=bn.4.4 r=0', 'FF primary Z = 0 Ω')  # Case 9 - phase to phase primary
case_18 = ('New Fault.case_18 phases=2 bus1=b1.1.2 bus2=bn.4.4 r=5', 'FF primary Z = 5 Ω')  # Case 10 - phase to phase primary
case_19 = ('New Fault.case_19 phases=2 bus1=b1.1.2 bus2=bn.4.4 r=10', 'FF primary Z = 10 Ω')  # Case 11 - phase to phase primary
case_20 = ('New Fault.case_20 phases=2 bus1=b1.1.2 bus2=bn.4.4 r=20', 'FF primary Z = 20 Ω')  # Case 12 - phase to phase primary
case_21 = ('New Fault.case_21 phases=2 bus1=b2.1.2 bus2=bn.4.4 r=0', 'FF secundary Z = 0 Ω')  # Case 11 - phase to phase secondary
case_22 = ('New Fault.case_22 phases=2 bus1=b2.1.2 bus2=bn.4.4 r=5', 'FF secundary Z = 5 Ω')  # Case 12 - phase to phase secondary
case_23 = ('New Fault.case_23 phases=2 bus1=b2.1.2 bus2=bn.4.4 r=10', 'FF secundary Z = 10 Ω')  # Case 13 - phase to phase secondary
case_24 = ('New Fault.case_24 phases=2 bus1=b2.1.2 bus2=bn.4.4 r=20', 'FF secundary Z = 20 Ω')  # Case 14 - phase to phase secondary

cases = [case_1, case_2, case_3, case_4, case_5, case_6, case_7, case_8, case_9, case_10, case_11, case_12, 
         case_13, case_14, case_15, case_16, case_17, case_18, case_19, case_20, case_21, case_22, case_23, case_24]  # List of fault cases

n_case = 1

# List with transformer connection options
connection = ['Delta', 'Wye']


# Loop to test all combinations of transformer connection
for lig1 in connection:
        for lig2 in connection:
            if feeder == '34Bus' or feeder == 'ULAU13': lig2 = 'Wye'  # For the 34Bus feeder, the secondary connection is always Wye
            n_case = 1  
            df = pd.DataFrame(columns=[' Case ', ' Transformer Connection ', ' Fault Type ', ' V2/V1 Primary % ', ' V2/V1 Secondary % ', ' Unbalance Ratio ', ' Attribution '])  # DataFrame for data storage

            for case, description in cases:
                # Compila o arquivo DSS
                dss.text(f'compile [{dss_file}]')
                dss.text('set time = 12') 

                # Defines the parameters of the transformer case 1
                if feeder == 'Adrian':
                    dss.text(f'New Transformer.T1 Phases=3 Windings=2 Xhl=3')
                    dss.text(f'~ wdg=1 bus=b1.1.2.3 conn={lig1} kv=34.5 kva=7500 %r=0.5')
                    dss.text(f'~ wdg=2 bus=b2.1.2.3 conn={lig2} kv=13.8 kva=7500 %r=0.5')

                # Defines the parameters of the transformer case 2
                if feeder == '34Bus':
                    dss.text(f'New Transformer.SubXF Phases=3 Windings=2 Xhl=0.01')
                    dss.text(f'~ wdg=1 bus=b1 conn={lig1} kv=69    kva=25000   %r=0.0005')  #b1=sourcebus
                    dss.text(f'~ wdg=2 bus=b2 conn= {lig2}   kv=24.9  kva=25000   %r=0.0005')  #b2=loadbus

                # Defines the parameters of the transformer cases 3 and 4
                if feeder == 'ULAE714' or feeder == 'ULAU13':
                    dss.text('New Transformer.trafo_se_uber7 phases=3 windings=2 %loadloss=0.72214 %noloadloss=0.100679 xhl=10.0')
                    dss.text(f'~ wdg=1 bus=b1.1.2.3 kv=138 kva=25000 conn={lig1}')
                    dss.text(f'~ wdg=2 bus=b2.1.2.3 kv=13.8 kva=25000 conn={lig2}')

                    


                dss.text(f"{case}")
                dss.solution.solve()
                
                dss.circuit.set_active_bus('b1')
                seq_voltage_b1 = dss.bus.seq_voltages
                v2_v1_prim = seq_voltage_b1[2] / seq_voltage_b1[1]

                dss.circuit.set_active_bus('b2')
                seq_voltage_b2 = dss.bus.seq_voltages
                v2_v1_sec = seq_voltage_b2[2] / seq_voltage_b2[1]

                ds = v2_v1_prim / v2_v1_sec
                atrib = "Consumer" if ds < 0.95 else "Supplies"

                df = pd.concat([df, pd.DataFrame([{
                    ' Case ': n_case, 
                    ' Transformer Connection ': f'{lig1} - {lig2}', 
                    ' Fault Type ': description, 
                    ' V2/V1 Primary % ': v2_v1_prim, 
                    ' V2/V1 Secondary % ': v2_v1_sec, 
                    ' Unbalance Ratio ': ds, 
                    ' Attribution ': atrib
                }])], ignore_index=True)

                n_case += 1
                dss.text('Clear')  

            path_file = fr'C:\aie\{feeder}\results\{feeder}_{lig1}_{lig2}.csv'
            
            df.to_csv(path_file, index=False, encoding='utf-8-sig', header=True, sep=';', float_format='%.4f')

            print(f"File saved: {path_file}")

end_time = time.time()
print(f"Execution Time: {end_time - start_time:.2f} seconds")

