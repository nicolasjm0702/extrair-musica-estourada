import json, os, platform, shutil

# OUTPUT_PATH = os.path.normpath(os.path.expandvars(os.path.expanduser(f"~/Desktop/")))
OUTPUT_PATH = './'

def extrairTextura():
    if platform.system() == "Windows":
        MC_ASSETS = os.path.expandvars(r"%APPDATA%/.minecraft/assets")
    else:
        MC_ASSETS = os.path.expanduser(r"~/.minecraft/assets")

    MC_VERSION = input("Versão do minecraft? Ex. 1.18, 1.5, 1.7\n") + ".json"
    print("A versão selecionada foi a " + MC_VERSION[:-5] + "\n")


    MC_OBJECT_INDEX = f"{MC_ASSETS}/indexes/{MC_VERSION}"
    MC_OBJECTS_PATH = f"{MC_ASSETS}/objects"
    MC_SOUNDS = r"minecraft/sounds/"

    with open(MC_OBJECT_INDEX, "r") as read_file:
        data = json.load(read_file)

        sounds = {k[len(MC_SOUNDS):] : v["hash"] for (k, v) in data["objects"].items() if k.startswith(MC_SOUNDS)}

        print("Extranindo arquivo:")

        for fpath, fhash in sounds.items():
            src_fpath = os.path.normpath(f"{MC_OBJECTS_PATH}/{fhash[:2]}/{fhash}")
            dest_fpath = os.path.normpath(f"{OUTPUT_PATH}/sounds/{fpath}")

            print(fpath)

            os.makedirs(os.path.dirname(dest_fpath), exist_ok=True)

            shutil.copyfile(src_fpath, dest_fpath)

    txt = open(f"{OUTPUT_PATH}\\sounds\\adicionados.txt", "w")
    txt.close()
    txt2 = open(f"{OUTPUT_PATH}\\sounds\\erros.txt", "w")
    txt2.close()