class Proyecto:
    def __init__(self, nombre, desembolso_inicial, coste_capital, flujos_de_caja):
        self.nombre = nombre
        self.desembolso_inicial = desembolso_inicial
        self.coste_capital = self._parse_coste_capital(coste_capital)
        self.flujos_de_caja = flujos_de_caja
        self.van = None  # Puedes calcularlo más tarde si es necesario
    
    def _parse_coste_capital(self, coste_capital):
        """
        Convierte el coste de capital de porcentaje a decimal.
        Por ejemplo, "10%" -> 0.10
        """
        return float(coste_capital.strip('%')) / 100

    def calcular_van(self):
        """Calcula el VAN basándose en los flujos de caja y el desembolso inicial."""
        if self.van is None:  # Solo calcular si no se ha calculado aún
            self.van = -self.desembolso_inicial
            for i, flujo in enumerate(self.flujos_de_caja):
                self.van += flujo / (1 + self.coste_capital) ** (i + 1)
        return self.van

    def __repr__(self):
        return f"Proyecto({self.nombre}, Desembolso Inicial: {self.desembolso_inicial}, Coste Capital: {self.coste_capital}, Flujos: {self.flujos_de_caja}, VAN: {self.van})"


class GrupoProyectos:
    def __init__(self, nombre_grupo):
        self.nombre_grupo = nombre_grupo
        self.proyectos = []

    def agregar_proyecto(self, proyecto):
        self.proyectos.append(proyecto)

    def __iter__(self):
        return iter(self.proyectos)  # Hacemos que la clase sea iterable

    def __repr__(self):
        return f"GrupoProyectos({self.nombre_grupo}, Proyectos: {self.proyectos})"


class EmpresaProyectos:
    def __init__(self):
        self.grupos = {}

    def agregar_grupo(self, nombre_grupo):
        self.grupos[nombre_grupo] = GrupoProyectos(nombre_grupo)

    def agregar_proyecto_a_grupo(self, nombre_grupo, proyecto):
        if nombre_grupo not in self.grupos:
            self.agregar_grupo(nombre_grupo)
        self.grupos[nombre_grupo].agregar_proyecto(proyecto)

    def __repr__(self):
        return f"EmpresaProyectos(Grupos: {self.grupos})"
