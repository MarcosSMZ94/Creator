def creator(quant:int, dir:str):
    import os

    userhome = os.path.expanduser('~')     

    local = f"{userhome}/Documents/TarefasDeFup/"
    path = os.path.join(local, dir)
    os.mkdir(path)

    while quant > 0:
        open(f"{userhome}/Documents/TarefasDeFup/{dir}/{quant}.py", "w")
        quant -= 1
    print(f"Arquivos criados em {userhome}/Documents/TarefasDeFup/{dir}/")

    pycharm = str(input("Deseja abrir a pasta no pycharm? (Sim / Não)")).strip().lower()
    if pycharm == "sim":
        os.system(f"pycharm {userhome}/Documents/TarefasDeFup/{dir}")
    else:
        print("Até a próxima")



quant = int(input("Quantos arquivos? "))
dir = str(input("Qual será o nome do diretório? "))
creator(quant, dir)


