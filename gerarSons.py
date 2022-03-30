import subprocess, extrair

extrair.extrairTextura()
subprocess.run(['py', '.\loudness.py'])

def gerar():
    runCode = subprocess.run(['py', '.\loudness.py'], capture_output=True)
    print(runCode.stdout.decode())
    if runCode.stdout.decode() != "":
        gerar()

gerar()