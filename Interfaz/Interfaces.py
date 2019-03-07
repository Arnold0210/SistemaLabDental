class InterfaceConexion:
    def __init__(self):
        self.config_mysql = {
            'user': 'LabDental',
            'password': 'LabDental123',
            'host': 'localhost',
            'database': 'labdental',
        }

    def Conexion(self):
        ...

    def SQlConsulta(self, Conector, Palabra, Tabla):
        ...

    def Select(self, Tabla, Palabra):
        ...

    def ConsultaColumnas(self,Conector,Tabla):
        ...

    def Columnas(self, Tabla):
        ...


class InterfaceProducto:
    idProducto=""
    nombrePR=""
    Valor_Producto = ""
    def VisualizarProducto(self,SQL):
        ...

    def InsertarProducto(self, Nombre, Precio):
        ...

    def ModificarProducto(self,SQL,args):
        ...

class InterfaceInsumo(InterfaceConexion):
    iddInsumo = ""
    Nombre_Insumo=""
    Cantidad_Insumo_Dispoible=""

    def InsertarInsumo(self, Query,args):
        ...

    def ModificarInsumo(self,SQL,args):
        ...

    def VisualizarInsumo(self,SQL):
        ...

class InterfaceActividad(InterfaceConexion):
    idActividad = ""
    CostoActividad = ""
    INSUMO_idInsumo = ""
    PRODUCTO_idPRODUCTO = ""
    USUARIO_Cedula = ""

    def InsertarActividad(self,SQL,args):
        ...

    def ModificarActividad(self,SQL,args):
        ...

    def VisualizarActividad(self,SQL):
        ...


class InterfaceUsuario(InterfaceConexion):
    idusuario=""
    Nombre=""
    Cedula=""
    Apellido=""
    Fecha_nac=""
    def InsertarUsuario(self,SQL,args):
        ...

    def ModificarUsuario(self,SQL,args):
        ...

    def VisualizarUsuario(self,SQl):
        ...

class InterfaceSimplex(InterfaceConexion):
    idSimplex = ""
    Variable_Fila=""
    Variable_Columna=""
    Valor=""
    def h(kw, **kwg):
        ...
    def GenerarSimplex(self):
        ...

class InterfaceOptimizacion(InterfaceConexion):
    idOptimizacion = ""
    Fecha_Optimizacion = ""
    Simplex_idSimplex = ""
    USUARIO_Cedula = ""
    def InsertarOptimizacion(self):
        ...

    def ModificarOptimizacion(self):
        ...