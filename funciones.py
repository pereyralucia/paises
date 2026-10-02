dominio=input("Indica el dominio que quéres conocer ")
def obtener_pais():
    paises={"ar":"Argentina","br":"Brasil","uy":"Uruguay","cl":"Chile","es":"España"}
    paises={"mx":"Mexico","ec":"Ecuador","fr":"Francia","py":"Paraguay"}
    print(paises[dominio])
obtener_pais()