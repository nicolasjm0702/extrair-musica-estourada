import subprocess, extrair, os, shutil, pathlib
from zipfile import ZipFile, ZIP_DEFLATED

extrair.extrairTextura()
subprocess.run(['py', '.\loudness.py'])
ultimaAdicao = 'som.ogg'


def gerar():
    global ultimaAdicao
    runCode = subprocess.run(['py', '.\loudness.py'], capture_output=True)
    print(runCode.stdout.decode())
    atual = open(extrair.OUTPUT_PATH + 'sounds\\adicionados.txt').readlines()[-1]

    if (ultimaAdicao != atual):
        ultimaAdicao = atual
        print('Gerando...')
        gerar()
    else:
        arquivar()


def arquivar():
    try:
        os.mkdir(extrair.OUTPUT_PATH + 'zip')
        os.mkdir(extrair.OUTPUT_PATH + 'zip\\assets')
        os.mkdir(extrair.OUTPUT_PATH + 'zip\\assets\\minecraft\\')
    except:
        print('Erro ao criar diretório /zip/')

    p = open(extrair.OUTPUT_PATH + 'zip\\pack.mcmeta', 'w')
    p.write('{\n\t"pack": {\n\t\t"pack-format":0,\n\t\t"description":[{"text":"Made by nikao","color":"light_purple"},{"text":"\\nNão usem jogos pirata!","color":"red"}]\n\t}\n}')
    p.close()
    try:
        shutil.move(extrair.OUTPUT_PATH + 'sounds', extrair.OUTPUT_PATH + 'zip\\assets\\minecraft\\')
    except:
        print('Erro ao mover arquivo /sounds/')

    directory = pathlib.Path("zip/")

    with ZipFile("loudnesspy.zip", "w", ZIP_DEFLATED, compresslevel=9) as archive:
        for file_path in directory.rglob("*"):
            archive.write(file_path, arcname=file_path.relative_to(directory))

    try:
        shutil.rmtree('zip')
        shutil.rmtree('sounds')
    except:
        print('Erro ao remover arquivo /zip/ e /sounds/')

    print('Tudo pronto, seu ensurdecedor foi gerado!')


gerar()