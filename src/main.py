from models import Proyecto, GrupoProyectos, EmpresaProyectos  # Ahora models.py está en src
from data_processing import load_data
from calculate_van import calculate_van
from project_selection import select_project_by_van
from export_data import exportar_a_excel

def main():
    # Carga de datos desde el archivo JSON
    data = load_data("/Users/luis/develop/proyectos/project_picker/data/proyectos.json")

    # Creación de la instancia de EmpresaProyectos
    cluster_proyectos = EmpresaProyectos()

    # Agregar proyectos del grupo "Proyectos_Reunidos_SA"
    for proyecto in data["Proyectos_Reunidos_SA"]:
        nuevo_proyecto = Proyecto(
            proyecto["proyecto"],
            proyecto["desembolso_inicial"],
            proyecto["coste_capital"],
            proyecto["flujos_de_caja"]
        )
        cluster_proyectos.agregar_proyecto_a_grupo("Proyectos_Reunidos_SA", nuevo_proyecto)

    # Agregar proyectos del grupo "Empresa_Central_Americana_SA"
    for proyecto in data["Empresa_Central_Americana_SA"]:
        nuevo_proyecto = Proyecto(
            proyecto["pais"],
            proyecto["desembolso_inicial"],
            proyecto["coste_capital"],
            proyecto["flujos_de_caja"]
        )
        cluster_proyectos.agregar_proyecto_a_grupo("Empresa_Central_Americana_SA", nuevo_proyecto)

    # Imprimir la representación del objeto Cluster_Proyectos
    print(cluster_proyectos)

    # Calcular el VAN de cada proyecto
    for grupo in cluster_proyectos.grupos:
        for proyecto in cluster_proyectos.grupos[grupo]:
            proyecto.van = calculate_van(proyecto.desembolso_inicial, proyecto.flujos_de_caja,  proyecto.coste_capital)

    print(cluster_proyectos)

    exportar_a_excel(cluster_proyectos, "proyectos.xlsx")



if __name__ == "__main__":
    main()
