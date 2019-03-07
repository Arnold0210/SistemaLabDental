from Modelo.Modelos import *
from reportlab.pdfgen import canvas

class ControladorConexion:
    Conexion = ModeloConexion()
    def Consultar(self,Tabla):
        Palabra = []
        Columnas = self.Conexion.Columnas(Tabla)
        if(Columnas == None ):
            return None
        for i in Columnas:
            Palabra.append(i)
        Consulta = self.Conexion.Select(Tabla,Palabra)
        return Consulta

class ControladorProducto:
    Producto = ModeloProducto()
    def InsertarProducto(self,Nombre,Precio):
        Query = "INSERT INTO labdental.producto (`nombrePR`,`Valor_Producto`) VALUES (%s,%s)"
        args = (Nombre.upper(), Precio)
        execute = self.Producto.InsertarProducto(Query,args)
        return execute
    def ModificarProducto(self,Nombre,Precio,id):
        args = SQL = ""
        if Precio != "" and Nombre == "":
            SQL = "UPDATE `labdental`.`producto` SET `Valor_Producto`=%s WHERE `idPRODUCTO`=%s;"
            args = (Precio, id)
        elif Nombre != "" and Precio == "":
            SQL = "UPDATE `labdental`.`producto` SET `nombrePR`=%s WHERE `idPRODUCTO`=%s;"
            args = (Nombre.upper(), id)
        elif Nombre != "" and Precio != "":
            SQL = "UPDATE `labdental`.`producto` SET `nombrePR`=%s,Valor_Producto`=%s  WHERE `idPRODUCTO`=%s;"
            args = (Nombre.upper(), Precio, id)
        execute = self.Producto.ModificarProducto(SQL,args)
        return execute
    def VisualizarProducto(self):
        # Palabra= []
        # Palabra = self.Conection.Columnas("producto")
        SQL = 'SELECT idPRODUCTO ,nombrePR , Valor_Producto FROM `labdental`.`producto`;'
        Resultado = self.Producto.VisualizarProducto(SQL)
        Consulta = []
        for i in Resultado:
            Consulta.append(i)
        return Consulta

class ControladorInsumo:
    Insumo = ModeloInsumo()
    def InsertarInsumo(self,Nombre,Cantidad):
        Query = "INSERT INTO labdental.insumo (`Nombre_Insumo`,`Cantidad_Insumo_Disponible`) VALUES (%s,%s)"
        args = (Nombre.upper(), Cantidad)
        execute = self.Insumo.InsertarInsumo(Query,args)
        return execute
    def ModificarInsumo(self,Nombre,Cantidad,id):
        args = SQL = ""
        if Nombre != ""  and Cantidad != "":
            SQL = "UPDATE `labdental`.`insumo` SET `Nombre_Insumo`=%s,`Cantidad_Insumo_Disponible`=%s WHERE `idInsumo`=%s;"
            args = (Nombre.upper(),Cantidad,id)

        elif Nombre == ""  and Cantidad != "":
            SQL = "UPDATE `labdental`.`insumo` SET `Cantidad_Insumo_Disponible`=%s WHERE `idInsumo`=%s;"
            args = (Cantidad,id)

        elif Nombre != "" and Cantidad == "":
            SQL = "UPDATE `labdental`.`insumo` SET `Nombre_Insumo`=%s WHERE `idInsumo`=%s;"
            args = (Nombre.upper() , Cantidad,id)
        execute = self.Insumo.ModificarInsumo(SQL,args)
        return execute
    def VisualizarInsumo(self):
        SQL = 'SELECT idInsumo,Nombre_Insumo,Cantidad_Insumo_disponible FROM `labdental`.`insumo`;'
        Resultado = self.Insumo.VisualizarInsumo(SQL)
        Consulta = []
        for i in Resultado:
            Consulta.append(i)
        return Consulta

class ControladorActividad:
    Actividad = ModeloActividad()
    def InsertarActividad(self,Costo,IdInsumo,IdProducto,Usuario_cedula):
        SQL = "INSERT INTO labdental.actividad (`CostoActividad`,`INSUMO_idInsumo`,`PRODUCTO_idPRODUCTO`,`USUARIO_Cedula`) VALUES(%s,%s,%s,%s)"
        args = (Costo, IdInsumo, IdProducto,Usuario_cedula)
        execute = self.Actividad.InsertarActividad(SQL,args)
        return execute
    def ModificarActividad(self,Costo,IdInsumo,IdProducto,Usuario_cedula,id):
        SQL=args=""
        if  Costo != "" and IdProducto != "" and IdInsumo != "" and Usuario_cedula != "":
            SQL = "UPDATE `labdental`.`actividad` SET `CostoActividad` = %s, `INSUMO_idInsumo` = %s,`PRODUCTO_idPRODUCTO` = %s, `USUARIO_Cedula`= $s where `idACTIVIDAD` = %s;"
            args = (Costo,IdInsumo,IdProducto,Usuario_cedula,id)

        elif Costo == "" and IdProducto != "" and IdInsumo != "" and Usuario_cedula != "":
            SQL = "UPDATE `labdental`.`actividad` set `INSUMO_idInsumo` = %s,`PRODUCTO_idPRODUCTO` = %s, `USUARIO_Cedula`= $s where `idACTIVIDAD` = %s;"
            args = (IdInsumo,IdProducto,Usuario_cedula,id)

        elif Costo != "" and IdProducto == "" and IdInsumo != "" and Usuario_cedula != "":
            SQL = "UPDATE`labdental`.`actividad` set `CostoActividad` = %s,`INSUMO_idINSUMO` = %s, `USUARIO_Cedula`= $s where `idACTIVIDAD` = %s;"
            args = (Costo,IdInsumo,Usuario_cedula,id)

        elif  Costo != "" and IdProducto != "" and IdInsumo == "" and Usuario_cedula != "":
            SQL = "UPDATE `labdental`.`actividad` SET `CostoActividad` = %s,`PRODUCTO_idPRODUCTO` = %s, `USUARIO_Cedula`= $s where `idACTIVIDAD` = %s;"
            args = (Costo,IdProducto,Usuario_cedula,id)

        elif  Costo != "" and IdProducto != "" and IdInsumo != "" and Usuario_cedula == "":
            SQL = "UPDATE `labdental`.`actividad` SET `CostoActividad` = %s, `INSUMO_idInsumo` = %s,`PRODUCTO_idPRODUCTO` = %s where `idACTIVIDAD` = %s;"
            args = (Costo,IdInsumo,IdProducto,id)

        elif  Costo == "" and IdProducto == "" and IdInsumo != "" and Usuario_cedula != "":
            SQL = "UPDATE `labdental`.`actividad` SET  `INSUMO_idInsumo` = %s, `USUARIO_Cedula`= $s where `idACTIVIDAD` = %s;"
            args = (IdInsumo,Usuario_cedula,id)

        elif  Costo == "" and IdProducto != "" and IdInsumo == "" and Usuario_cedula != "":
            SQL = "UPDATE `labdental`.`actividad` SET `PRODUCTO_idPRODUCTO` = %s, `USUARIO_Cedula`= $s where `idACTIVIDAD` = %s;"
            args = (IdProducto,Usuario_cedula,id)

        elif  Costo == "" and IdProducto != "" and IdInsumo != "" and Usuario_cedula == "":
            SQL = "UPDATE `labdental`.`actividad` SET  `INSUMO_idInsumo` = %s,`PRODUCTO_idPRODUCTO` = %s where `idACTIVIDAD` = %s;"
            args = (IdInsumo,IdProducto,id)

        elif  Costo != "" and IdProducto == "" and IdInsumo == "" and Usuario_cedula != "":
            SQL = "UPDATE `labdental`.`actividad` SET `CostoActividad` = %s, `USUARIO_Cedula`= $s where `idACTIVIDAD` = %s;"
            args = (Costo,Usuario_cedula,id)

        elif  Costo != "" and IdProducto == "" and IdInsumo != "" and Usuario_cedula == "":
            SQL = "UPDATE `labdental`.`actividad` SET `CostoActividad` = %s, `INSUMO_idInsumo` = %s,  where `idACTIVIDAD` = %s;"
            args = (Costo,IdInsumo,id)

        elif  Costo != "" and IdProducto != "" and IdInsumo == "" and Usuario_cedula == "":
            SQL = "UPDATE `labdental`.`actividad` SET `CostoActividad` = %s,`PRODUCTO_idPRODUCTO` = %s where `idACTIVIDAD` = %s;"
            args = (Costo,IdProducto,id)

        elif  Costo != "" and IdProducto == "" and IdInsumo == "" and Usuario_cedula == "":
            SQL = "UPDATE `labdental`.`actividad` SET `CostoActividad` = %s where `idACTIVIDAD` = %s;"
            args = (Costo,id)

        elif  Costo == "" and IdProducto != "" and IdInsumo == "" and Usuario_cedula == "":
            SQL = "UPDATE `labdental`.`actividad` SET `PRODUCTO_idPRODUCTO` = %s where `idACTIVIDAD` = %s;"
            args = (IdProducto,id)

        elif  Costo == "" and IdProducto == "" and IdInsumo == "" and Usuario_cedula != "":
            SQL = "UPDATE `labdental`.`actividad` SET `USUARIO_Cedula`= $s where `idACTIVIDAD` = %s;"
            args = (Usuario_cedula,id)

        elif  Costo == "" and IdProducto == "" and IdInsumo != "" and Usuario_cedula == "":
            SQL = "UPDATE `labdental`.`actividad` SET `INSUMO_idInsumo` = %s,  where `idACTIVIDAD` = %s;"
            args = (IdInsumo,id)

        execute = self.Actividad.ModificarActividad(SQL,args)
        return execute
    def VisualizarActividad(self):
        SQL = "SELECT idActividad,CostoActividad,nombrePr,Nombre_Insumo,Nombre FROM `labdental`.`actividad`,`labdental`.`producto`,`labdental`.`insumo`,`labdental`.`usuario` where `actividad`.`PRODUCTO_idPRODUCTO`=`producto`.`idPRODUCTO`  and `actividad`.`INSUMO_idInsumo` = `insumo`.`idInsumo` and `actividad`.`USUARIO_Cedula` = `usuario`.`Cedula`;"
        Resultado = self.Actividad.VisualizarActividad(SQL)
        Consulta = []
        for i in Resultado:
            Consulta.append(i)
        return Resultado

class ControladorUsuario:
    Usuario = ModeloUsuario()
    def InsertarUsuario(self,Cedula,Nombre,Apellido,Fecha_nac):
        SQL = "INSERT INTO `labdental`.`usuario` (`Cedula`, `Nombre`, `Apellido`, `Fecha_nac`) VALUES (%s, %s, %s, %s);"
        args = (Cedula,Nombre,Apellido,Fecha_nac)
        resultado = self.Usuario.InsertarUsuario(SQL,args)
        return resultado

    def ModificarUsuario(self,Cedula,Nombre,Apellido,Fecha_nac):
        SQL = args = ""
        if  Nombre != "" and Apellido != "" and Fecha_nac !="":
            SQL = "UPDATE `labdental`.`usuario` SET Nombre = %s, Apellido = %s , Fecha_nac = %s WHERE  Cedula = %s"
            args =(Nombre,Apellido,Fecha_nac,Cedula)
        elif  Nombre == "" and Apellido != "" and Fecha_nac !="":
            SQL = "UPDATE `labdental`.`usuario` SET  Apellido = %s , Fecha_nac = %s WHERE  Cedula = %s"
            args = (Apellido, Fecha_nac, Cedula)
        elif  Nombre != "" and Apellido == "" and Fecha_nac !="":
            SQL = "UPDATE `labdental`.`usuario` SET  Nombre = %s , Fecha_nac = %s WHERE  Cedula = %s"
            args = (Nombre, Fecha_nac, Cedula)
        elif Nombre == "" and Apellido == "" and Fecha_nac != "":
            SQL = "UPDATE `labdental`.`usuario` SET   Fecha_nac = %s WHERE  Cedula = %s"
            args = ( Fecha_nac, Cedula)
        elif Nombre == "" and Apellido != "" and Fecha_nac == "":
            SQL = "UPDATE `labdental`.`usuario` SET  Apellido = %s WHERE  Cedula = %s"
            args = (Apellido, Cedula)
        elif Nombre != "" and Apellido == "" and Fecha_nac == "":
            SQL = "UPDATE `labdental`.`usuario` SET  Nombre = %s WHERE  Cedula = %s"
            args = (Nombre, Cedula)
        resultado = self.Usuario.ModificarUsuario(SQL,args)
        return resultado

    def VisualizarUsuario(self):
        SQL = "SELECT Cedula,Nombre,Apellido,Fecha_nac FROM usuario;"
        Resultado = self.Usuario.VisualizarUsuario(SQL)

        Consulta = []
        for i in Resultado:
            Consulta.append(i)
        return Consulta

class ControladorSimplex:
    Simplex = ModeloSimplex()
    def CalcularZ(self):
        res = self.Simplex.GenerarSimplex()
        Z,pdf = res.x
        return Z
    def CalcularValorObjetivo(self):
        res,pdf = self.Simplex.GenerarSimplex()
        Optimo = res.fun*-1
        return Optimo
    def PDF(self):
        res,pdf = self.Simplex.GenerarSimplex()
        reporte = canvas.Canvas("Reporte.pdf")
        reporte.drawString(100, 800, "Reporte de Resultados  Laboratorio Dental ")
        reporte.drawString(100,775,"Arnold Julian Herrera Quiñones - 625569")
        reporte.drawString(100, 750, "Cristhian Camilo Arce García - 625577")
        reporte.drawString(100, 725, "Materia Investigacion de Operaciones")
        reporte.drawString(100,700,"El valor de la ganancia obtenida es: "+str(res.fun*-1))
        reporte.drawString(100, 675, "Para obtener este valor de ganancias se necesita : ")
        linea = 650
        if( res == None):
            reporte.drawString(100, linea, "No se ha podido hacer una Optimizacion correspondiente")
        else:
            for i in range(0,len(pdf)):
                print(res.x[i])
                a = res.x[i]
                b = pdf[i]
                reporte.drawString(100, linea, str(b) + " = " + str(a))
                linea = linea - 25
        reporte.save()

