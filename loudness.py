import os
import soundfile as sf
import pyloudnorm as pyln
import extrair

barulho = 20.0

PATH = f'{extrair.OUTPUT_PATH}\\sounds\\'
arrayAdicionados = []

with open(f"{PATH}adicionados.txt", "r") as txt:
    linhas = txt.readlines()
    for l in linhas:
        arrayAdicionados.append(l.replace("\n", ""))

    for root, subdirs, files in os.walk(PATH):
        for file in files:
            paths = os.path.join(root, file)
            if not os.path.normpath(paths).endswith('.txt'):
                if file not in arrayAdicionados:
                    data, rate = sf.read(os.path.normpath(paths))
                    try:
                        meter = pyln.Meter(rate)
                        loudness = meter.integrated_loudness(data)
                        loudness_normalized_audio = pyln.normalize.loudness(data, loudness, +barulho)
                        sf.write(os.path.normpath(paths), loudness_normalized_audio, rate)
                    except:
                        erro = open(f"{PATH}erros.txt", "a")
                        erro.write(f"{file}\n")
                        erro.close()
                        os.remove(f"{os.path.normpath(paths)}")
                    finally:
                        adc = open(f"{PATH}adicionados.txt", "a")
                        adc.write(f"{file}\n")
                        adc.close()
                        print(os.path.normpath(paths))