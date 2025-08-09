'''ARTIGO AIE 2025
AUTORES ARTHUR GOMES DE SOUZA E LUIZ ARTHUR TARRALO PASSATUTO
ATRIBUIÇÃO DE RESPONSABILIDADE DE VTCD VIA OPENDSS E QGIS
SISTEMAS UTILIZADOS: 
    1 - Feeder ULAE714 -  CONSUMIDORES DESTACADOS: COCAL ALIMENTOS E UBERLÂNDIA REFRESCOS COCA COLA
    2 - Feeder ULAU13 -  CONSUMIDORES DESTACADOS: UFV CAPIM BRANCO II E Estação de Tratamento de Esgoto Uberabinha - DMAE'''

import py_dss_interface
import pandas as pd 
import numpy as np
#import matplotlib.pyplot as plt
import time 

start_time = time.time()  # Start time

feeder = 'ULAE714'  # Feeder name

df = pd.DataFrame(columns=[' Caso ', ' Ligação Trafo ', ' Tipo de Curto ', ' V2/V1 primário % ', ' V2/V1 secundário % ', ' Razão de Desequilíbrio ', ' Atribuição '])  # DataFrame for data storage

dss = py_dss_interface.DSS()  # Create an instance of the dss class

dss_file = rf'C:\arquivos_trabalho_aie\{feeder}\Master_{feeder}_DU .dss'  # Path to the DSS file

# Create a list of faults with case definitions
caso_1 = ('New Fault.caso_1 phases=1 bus1=b1.1 r=0', 'FT primário Z = 0 Ω')  # Case 1 - 1 phase to ground primary
caso_2 = ('New Fault.caso_2 phases=1 bus1=b1.1 r=5', 'FT primário Z = 5 Ω')  # Case 2 - 1 phase to ground primary
caso_3 = ('New Fault.caso_3 phases=1 bus1=b1.1 r=10', 'FT primário Z = 10 Ω')  # Case 3 - 1 phase to ground primary
caso_4 = ('New Fault.caso_4 phases=1 bus1=b1.1 r=20', 'FT primário Z = 20 Ω')  # Case 4 - 1 phase to ground primary
caso_5 = ('New Fault.caso_5 phases=1 bus1=b2.1 r=0', 'FT secundário Z = 0 Ω')  # Case 5 - 1 phase to ground secondary
caso_6 = ('New Fault.caso_6 phases=1 bus1=b2.1 r=5', 'FT secundário Z = 5 Ω')  # Case 6 - 1 phase to ground secondary
caso_7 = ('New Fault.caso_7 phases=1 bus1=b2.1 r=10', 'FT secundário Z = 10 Ω')  # Case 7 - 1 phase to ground secondary
caso_8 = ('New Fault.caso_8 phases=1 bus1=b2.1 r=20', 'FT secundário Z = 20 Ω')  # Case 8 - 1 phase to ground secondary
caso_9 = ('New Fault.caso_9 phases=2 bus1=b1.1.2 r=0', 'FFT primário Z = 0 Ω')  # Case 5 - 2 phase to ground primary
caso_10= ('New Fault.caso_10 phases=2 bus1=b1.1.2 r=5', 'FFT primário Z = 5 Ω')  # Case 6 - 2 phase to ground primary
caso_11 = ('New Fault.caso_11 phases=2 bus1=b1.1.2 r=10', 'FFT primário Z = 10 Ω')  # Case 7 - 2 phase to ground primary
caso_12 = ('New Fault.caso_12 phases=2 bus1=b1.1.2 r=20', 'FFT primário Z = 20 Ω')  # Case 8 - 2 phase to ground primary
caso_13 = ('New Fault.caso_13 phases=2 bus1=b2.1.2 r=0', 'FFT secundário Z = 0 Ω')  # Case 7 - 2 phase to ground secondary
caso_14 = ('New Fault.caso_14 phases=2 bus1=b2.1.2 r=5', 'FFT secundário Z = 5 Ω')  # Case 8 - 2 phase to ground secondary
caso_15 = ('New Fault.caso_15 phases=2 bus1=b2.1.2 r=10', 'FFT secundário Z = 10 Ω')  # Case 9 - 2 phase to ground secondary
caso_16 = ('New Fault.caso_16 phases=2 bus1=b2.1.2 r=20', 'FFT secundário Z = 20 Ω')  # Case 10 - 2 phase to ground secondary
caso_17 = ('New Fault.caso_17 phases=2 bus1=b1.1.2 bus2=bn.4.4 r=0', 'FF primário Z = 0 Ω')  # Case 9 - phase to phase primary
caso_18 = ('New Fault.caso_18 phases=2 bus1=b1.1.2 bus2=bn.4.4 r=5', 'FF primário Z = 5 Ω')  # Case 10 - phase to phase primary
caso_19 = ('New Fault.caso_19 phases=2 bus1=b1.1.2 bus2=bn.4.4 r=10', 'FF primário Z = 10 Ω')  # Case 11 - phase to phase primary
caso_20 = ('New Fault.caso_20 phases=2 bus1=b1.1.2 bus2=bn.4.4 r=20', 'FF primário Z = 20 Ω')  # Case 12 - phase to phase primary
caso_21 = ('New Fault.caso_21 phases=2 bus1=b2.1.2 bus2=bn.4.4 r=0', 'FF secundário Z = 0 Ω')  # Case 11 - phase to phase secondary
caso_22 = ('New Fault.caso_22 phases=2 bus1=b2.1.2 bus2=bn.4.4 r=5', 'FF secundário Z = 5 Ω')  # Case 12 - phase to phase secondary
caso_23 = ('New Fault.caso_23 phases=2 bus1=b2.1.2 bus2=bn.4.4 r=10', 'FF secundário Z = 10 Ω')  # Case 13 - phase to phase secondary
caso_24 = ('New Fault.caso_24 phases=2 bus1=b2.1.2 bus2=bn.4.4 r=20', 'FF secundário Z = 20 Ω')  # Case 14 - phase to phase secondary

casos = [caso_1, caso_2, caso_3, caso_4, caso_5, caso_6, caso_7, caso_8, caso_9, caso_10, caso_11, caso_12, 
         caso_13, caso_14, caso_15, caso_16, caso_17, caso_18, caso_19, caso_20, caso_21, caso_22, caso_23, caso_24]  # List of fault cases

num_caso = 1

# Lista com as opções de ligação do transformador
ligacoes = ['Delta', 'Wye']

# Loop para testar todas as combinações de ligação do transformador
for lig1 in ligacoes:
        for lig2 in ligacoes:
            num_caso = 1  # Reinicia a contagem de casos
            df = pd.DataFrame(columns=[' Caso ', ' Ligação Trafo ', ' Tipo de Curto ', ' V2/V1 primário % ', ' V2/V1 secundário % ', ' Razão de Desequilíbrio ', ' Atribuição '])  # DataFrame para cada combinação

            # Loop pelos casos de curto
            for caso, descricao in casos:
                # Compila o arquivo DSS
                dss.text(f'compile [{dss_file}]')
                dss.text('set time = 12')  # Define o tempo da simulação

                # Define os parâmetros do transformador
                #dss.text('New Transformer.trafo_se_uber7 phases=3 windings=2 %loadloss=0.72214 %noloadloss=0.100679 xhl=10.0')
                #dss.text(f'~ wdg=1 bus=b1.1.2.3 kv=138 kva=25000 conn={lig1}')
                #dss.text(f'~ wdg=2 bus=b2.1.2.3 kv=13.8 kva=25000 conn={lig2}')
                
                dss.text(f'New Transformer.T1 Phases=3 Windings=2 Xhl=3')
                dss.text(f'~ wdg=1 bus=b1.1.2.3 conn={lig1} kv=34.5 kva=7500 %r=0.5')
                dss.text(f'~ wdg=2 bus=b2.1.2.3 conn={lig2} kv=13.8 kva=7500 %r=0.5')

                # Aplica a falha
                dss.text(f"{caso}")
                dss.solution.solve()
                
                # Obtém tensões do primário
                dss.circuit.set_active_bus('b1')
                seq_voltage_b1 = dss.bus.seq_voltages
                v2_v1_prim = seq_voltage_b1[2] / seq_voltage_b1[1]

                # Obtém tensões do secundário
                dss.circuit.set_active_bus('b2')
                seq_voltage_b2 = dss.bus.seq_voltages
                v2_v1_sec = seq_voltage_b2[2] / seq_voltage_b2[1]

                # Calcula a razão de desequilíbrio
                ds = v2_v1_prim / v2_v1_sec
                atrib = "Consumidor" if ds < 0.95 else "Supridor"

                # Armazena os resultados no DataFrame
                df = pd.concat([df, pd.DataFrame([{
                    ' Caso ': num_caso, 
                    ' Ligação Trafo ': f'{lig1} - {lig2}', 
                    ' Tipo de Curto ': descricao, 
                    ' V2/V1 primário % ': v2_v1_prim, 
                    ' V2/V1 secundário % ': v2_v1_sec, 
                    ' Razão de Desequilíbrio ': ds, 
                    ' Atribuição ': atrib
                }])], ignore_index=True)

                num_caso += 1
                dss.text('Clear')  # Limpa o circuito antes da próxima iteração

            # Salva os resultados em um CSV nomeado de acordo com a conexão do trafo
            caminho_arquivo = fr'C:\arquivos_trabalho_aie\resultados\{feeder}_{lig1}_{lig2}_v2.csv'
            df.to_csv(caminho_arquivo, index=False, encoding='utf-8-sig', header=True, sep=';', float_format='%.4f')

            print(f"Arquivo salvo: {caminho_arquivo}")

# Tempo total de execução
end_time = time.time()
print(f"Execution Time: {end_time - start_time:.2f} seconds")
