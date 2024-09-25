import pandas as pd

def exportar_a_excel(empresa, nombre_archivo):
    # Crear un objeto ExcelWriter
    with pd.ExcelWriter(nombre_archivo, engine='openpyxl') as writer:
        # Iterar sobre los grupos de proyectos
        for nombre_grupo, grupo in empresa.grupos.items():
            # Crear una lista para almacenar datos de cada proyecto
            datos_proyectos = []

            # Iterar sobre cada proyecto en el grupo
            for proyecto in grupo.proyectos:
                # Crear un diccionario con los datos del proyecto
                datos_proyecto = {
                    'Nombre': proyecto.nombre,
                    'Desembolso Inicial': proyecto.desembolso_inicial,
                    'Coste Capital': proyecto.coste_capital,
                    'VAN': proyecto.van,
                }
                
                # Agregar flujos de caja al diccionario
                for i, flujo in enumerate(proyecto.flujos_de_caja):
                    datos_proyecto[f'Flujo {i + 1}'] = flujo

                # Agregar el diccionario a la lista de datos
                datos_proyectos.append(datos_proyecto)

            # Convertir la lista de datos a un DataFrame de pandas
            df = pd.DataFrame(datos_proyectos)
            
            # Guardar el DataFrame en una hoja de Excel
            df.to_excel(writer, sheet_name=nombre_grupo, index=False)

    print(f"Datos exportados a {nombre_archivo} con éxito.")
