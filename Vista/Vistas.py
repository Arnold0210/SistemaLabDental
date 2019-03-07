from Controlador.Controladores import *
from GUI.SILD import *
from PyQt4 import QtSql, QtGui, uic,QtCore
#import reportlab
import mysql.connector
import sys
from Modelo.Modelos import ModeloConexion
class root(QtGui.QDialog):
    Producto = ControladorProducto()
    Insumo = ControladorInsumo()
    Usuario = ControladorUsuario()
    Actividad = ControladorActividad()
    Conexion = ControladorConexion()
    Modelo = ModeloConexion()
    Simplex = ControladorSimplex()

    def __init__(self,parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.Ui = Ui_Dialog()
        self.Ui.setupUi(self)
        QtCore.QObject.connect(self.Ui.pushButton_GuardarProducto,QtCore.SIGNAL("clicked()"),self.AgregarProducto)
        QtCore.QObject.connect(self.Ui.pushButton_ActualizarProducto,QtCore.SIGNAL("clicked()"),self.ModificarProducto)
        QtCore.QObject.connect(self.Ui.pushButton_MostrarCrear,QtCore.SIGNAL("clicked()"),self.MostrarCrear)
        QtCore.QObject.connect(self.Ui.pushButton_MostrarActualizar, QtCore.SIGNAL("clicked()"), self.MostrarActualizar)
        QtCore.QObject.connect(self.Ui.pushButtonGuardarUsuario, QtCore.SIGNAL("clicked()"), self.AgregarUsuario)
        QtCore.QObject.connect(self.Ui.pushButton_GuardarInusmo, QtCore.SIGNAL("clicked()"), self.AgregarInsumo)
        QtCore.QObject.connect(self.Ui.pushButtonGuardarActividad,QtCore.SIGNAL("clicked()"),self.AgregarActividad)
        QtCore.QObject.connect(self.Ui.pushButtonGuardarActividad_2, QtCore.SIGNAL("clicked()"), self.ModificarActividad)
        QtCore.QObject.connect(self.Ui.pushButton_ActualizarInsumo, QtCore.SIGNAL("clicked()"), self.ModificarInsumo)
        QtCore.QObject.connect(self.Ui.pushButton_ActualizarProducto, QtCore.SIGNAL("clicked()"), self.ModificarProducto)
        QtCore.QObject.connect(self.Ui.pushButton_ActualizarUsuario, QtCore.SIGNAL("clicked()"), self.Modificarusuario)
        QtCore.QObject.connect(self.Ui.pushButton_MostrarAllProducts, QtCore.SIGNAL("clicked()"), self.MostrarAllProductos)
        QtCore.QObject.connect(self.Ui.pushButton_ShowAllInsumos, QtCore.SIGNAL("clicked()"), self.MostrarAllInsumos)
        QtCore.QObject.connect(self.Ui.pushButton_ShowAllUsers, QtCore.SIGNAL("clicked()"), self.MostrarAllUsuarios)
        QtCore.QObject.connect(self.Ui.pushButton_5, QtCore.SIGNAL("clicked()"), self.MostrarAllActividades)
        QtCore.QObject.connect(self.Ui.pushButton_7, QtCore.SIGNAL("clicked()"), self.Ganancia)
        #QtCore.QObject.connect(self.Ui.pushButton_7, QtCore.SIGNAL("clicked()"), self.)

    def MostrarCrear(self):
        self.Ui.tableWidget__MostrarCrear.setColumnCount(6)
        self.Ui.tableWidget__MostrarCrear.setHorizontalHeaderLabels(["Id Producto","Nombre Producto","Id Insumo","Nombre Insumo","Cedula Usuario","Nombre Usuario"])
        DB = self.Modelo.Conexion()
        Cursor = DB.cursor()
        consulta1 = []
        consulta2 = []
        consulta3 = []
        SQL = "SELECT idPRODUCTO,nombrePR FROM `labdental`.`producto`;"
        Cursor.execute(SQL)
        for i in Cursor:
            consulta1.append(i)
        SQL2 = "SELECT idInsumo,Nombre_Insumo FROM `labdental`.`insumo`;"
        Cursor.execute(SQL2)
        for i in Cursor:
            consulta2.append(i)
        SQL3 = "SELECT cedula,Nombre FROM `labdental`.`usuario`;"
        Cursor.execute(SQL3)
        for i in Cursor:
            consulta3.append(i)
        row = 0
        for i in range(0,len(consulta1)):
            self.Ui.tableWidget__MostrarCrear.insertRow(row)
            idproducto = str(consulta1[i][0])
            nombreproducto = str(consulta1[i][1])
            self.Ui.tableWidget__MostrarCrear.setItem(row, 0, QtGui.QTableWidgetItem(idproducto))
            self.Ui.tableWidget__MostrarCrear.setItem(row, 1, QtGui.QTableWidgetItem(nombreproducto))
            row = row + 1
        row1 = 0
        for i in range(0,len(consulta2)):
            self.Ui.tableWidget__MostrarCrear.insertRow(row)
            idinsumo = str(consulta2[i][0])
            nombreinsumo = str(consulta2[i][1])
            self.Ui.tableWidget__MostrarCrear.setItem(row1, 2, QtGui.QTableWidgetItem(idinsumo))
            self.Ui.tableWidget__MostrarCrear.setItem(row1, 3, QtGui.QTableWidgetItem(nombreinsumo))
            row1 = row1 + 1
        row2 = 0
        for i  in range(0,len(consulta3)):
            self.Ui.tableWidget__MostrarCrear.insertRow(row)
            cedula = str(consulta3[i][0])
            nombre = str(consulta3[i][1])
            self.Ui.tableWidget__MostrarCrear.setItem(row2,4, QtGui.QTableWidgetItem(cedula))
            self.Ui.tableWidget__MostrarCrear.setItem(row2,5, QtGui.QTableWidgetItem(nombre))
            row2 = row2 + 1
        Cursor.close()
        DB.close()

    def MostrarActualizar(self):
        self.Ui.tableWidget_MostrarDatos.setColumnCount(6)
        self.Ui.tableWidget_MostrarDatos.setHorizontalHeaderLabels(["Id Producto","Nombre Producto","Id Insumo "," Nombre Insumo ","Cedula Usuario","Nombre Usuario"])
        DB = self.Modelo.Conexion()
        Cursor = DB.cursor()
        consulta1 = []
        consulta2 = []
        consulta3 = []
        SQL = "SELECT idPRODUCTO,nombrePR FROM `labdental`.`producto`;"
        Cursor.execute(SQL)
        for i in Cursor:
            consulta1.append(i)
        SQL2 = "SELECT idInsumo,Nombre_Insumo FROM `labdental`.`insumo`;"
        Cursor.execute(SQL2)
        for i in Cursor:
            consulta2.append(i)
        SQL3 = "SELECT cedula,Nombre FROM `labdental`.`usuario`;"
        Cursor.execute(SQL3)
        for i in Cursor:
            consulta3.append(i)
        row = 0
        for i in range(0, len(consulta1)):
            self.Ui.tableWidget_MostrarDatos.insertRow(row)
            idproducto = str(consulta1[i][0])
            nombreproducto = str(consulta1[i][1])
            self.Ui.tableWidget_MostrarDatos.setItem(row, 0, QtGui.QTableWidgetItem(idproducto))
            self.Ui.tableWidget_MostrarDatos.setItem(row, 1, QtGui.QTableWidgetItem(nombreproducto))
            row = row + 1
        row1 = 0
        for i in range(0, len(consulta2)):
            self.Ui.tableWidget_MostrarDatos.insertRow(row)
            idinsumo = str(consulta2[i][0])
            nombreinsumo = str(consulta2[i][1])
            self.Ui.tableWidget_MostrarDatos.setItem(row1, 2, QtGui.QTableWidgetItem(idinsumo))
            self.Ui.tableWidget_MostrarDatos.setItem(row1, 3, QtGui.QTableWidgetItem(nombreinsumo))
            row1 = row1 + 1
        row2 = 0
        for i in range(0, len(consulta3)):
            self.Ui.tableWidget_MostrarDatos.insertRow(row)
            cedula = str(consulta3[i][0])
            nombre = str(consulta3[i][1])
            self.Ui.tableWidget_MostrarDatos.setItem(row2, 4, QtGui.QTableWidgetItem(cedula))
            self.Ui.tableWidget_MostrarDatos.setItem(row2, 5, QtGui.QTableWidgetItem(nombre))
            row2 = row2 + 1
        Cursor.close()
        DB.close()

    def MostrarAllProductos(self):
        self.Ui.tableWidget.setColumnCount(3)
        self.Ui.tableWidget.setHorizontalHeaderLabels(["Id Producto","Nombre Producto","Valor producto"])
        resultado = self.Producto.VisualizarProducto()
        row = 0
        for i in range(0,len(resultado)):
            self.Ui.tableWidget.insertRow(row)
            idp = str(resultado[i][0])
            nombre = str(resultado[i][1])
            valor = str(resultado[i][2])
            self.Ui.tableWidget.setItem(row,0,QtGui.QTableWidgetItem(idp))
            self.Ui.tableWidget.setItem(row, 1, QtGui.QTableWidgetItem(nombre))
            self.Ui.tableWidget.setItem(row, 2, QtGui.QTableWidgetItem(valor))
            row = row + 1

    def MostrarAllActividades(self):
        self.Ui.tableWidget.setColumnCount(5)
        self.Ui.tableWidget.setHorizontalHeaderLabels(["Id Actividad", "Costo Actividad", "Nombre Producto","Nombre Insumo", "Nombre Usuario"])
        resultado = self.Actividad.VisualizarActividad()
        row = 0
        for i in range(0, len(resultado)):
            self.Ui.tableWidget.insertRow(row)
            ida = str(resultado[i][0])
            costo = str(resultado[i][1])
            nombrep = str(resultado[i][2])
            nombrei = str(resultado[i][3])
            nombreu = str(resultado[i][4])
            self.Ui.tableWidget.setItem(row, 0, QtGui.QTableWidgetItem(ida))
            self.Ui.tableWidget.setItem(row, 1, QtGui.QTableWidgetItem(costo))
            self.Ui.tableWidget.setItem(row, 2, QtGui.QTableWidgetItem(nombrep))
            self.Ui.tableWidget.setItem(row, 3, QtGui.QTableWidgetItem(nombrei))
            self.Ui.tableWidget.setItem(row, 4, QtGui.QTableWidgetItem(nombreu))
            row = row + 1

    def MostrarAllUsuarios(self):
        self.Ui.tableWidget.setColumnCount(4)
        self.Ui.tableWidget.setHorizontalHeaderLabels([" Cedula", " Nombre", " Apellido"," Fecha de Nacimiento"])
        resultado = self.Usuario.VisualizarUsuario()
        row = 0
        for i in range(0, len(resultado)):
            self.Ui.tableWidget.insertRow(row)
            cedula = str(resultado[i][0])
            nombre = str(resultado[i][1])
            apellido = str(resultado[i][2])
            fecha = str(resultado[i][3])
            self.Ui.tableWidget.setItem(row, 0, QtGui.QTableWidgetItem(cedula))
            self.Ui.tableWidget.setItem(row, 1, QtGui.QTableWidgetItem(nombre))
            self.Ui.tableWidget.setItem(row, 2, QtGui.QTableWidgetItem(apellido))
            self.Ui.tableWidget.setItem(row, 3, QtGui.QTableWidgetItem(fecha))
            row = row + 1


    def MostrarAllInsumos(self):
        self.Ui.tableWidget.setColumnCount(3)
        self.Ui.tableWidget.setHorizontalHeaderLabels(["Id Insumo", "Nombre Insumo", "Horas Disponibles"])
        resultado = self.Insumo.VisualizarInsumo()
        row = 0
        for i in range(0, len(resultado)):
            self.Ui.tableWidget.insertRow(row)
            idi = str(resultado[i][0])
            nombre = str(resultado[i][1])
            horas = str(resultado[i][2])
            self.Ui.tableWidget.setItem(row, 0, QtGui.QTableWidgetItem(idi))
            self.Ui.tableWidget.setItem(row, 1, QtGui.QTableWidgetItem(nombre))
            self.Ui.tableWidget.setItem(row, 2, QtGui.QTableWidgetItem(horas))
            row= row + 1

    def AgregarProducto(self):
        Nombre =  str(self.Ui.lineEditGuardarNombreProducto.text().upper())
        Precio = str(self.Ui.lineEditGuardarValorProductoo.text().upper())
        resultado = self.Producto.InsertarProducto(Nombre,Precio)
        if resultado:
            self.Ui.crearProducto.setText("El producto ha sido registrado satisfactoriamente")
        else:
            self.Ui.crearProducto.setText("No se pudo registrar el producto correctamente, "+str(resultado))

    def AgregarInsumo(self):
        Nombre = str(self.Ui.lineEditGuardarNombreInsumo.text().upper())
        Cantidad = str(self.Ui.lineEditGuardarHorasInsumo.text().upper())
        resultado = self.Insumo.InsertarInsumo(Nombre,Cantidad)
        if(resultado ==True):
            self.Ui.CrearActividad.setText("Se ha ingresado el Insumo Exitosamente")
        else:
            self.Ui.CrearActividad.setText("No Se ha ingresado el Insumo Correctamente, "+str(resultado))

    def AgregarActividad(self):
        costo = str(self.Ui.lineEditAgregarActividad.text())
        idinsumo =str(self.Ui.lineEdit.text())
        idproducto = str(self.Ui.lineEdit_2.text())
        cedula =str(self.Ui.lineEdit_7.text())
        execute = self.Actividad.InsertarActividad(costo,idinsumo,idproducto,cedula)
        if len(cedula) >10 :
            self.Ui.CrearActividad.setText("No se ha modificado exitosamente la actividad, La longitud de la cedula no puede ser mayor a 10")
        else:
            if execute == True:
                self.Ui.CrearActividad.setText("Se ha ingresado la actividad Exitosamente")
            else:
                self.Ui.CrearActividad.setText("No ha ingresado la actividad Correctamente "+execute)

    def AgregarUsuario(self):
        Nombre = str(self.Ui.lineEditGuardarNombreUsuario.text().upper())
        Apellido = str(self.Ui.lineEditGuardarApellidoUsuario.text().upper())
        Cedula = str(self.Ui.lineEdit_6.text().upper())
        fech_nac = str(self.Ui.dateEditFEchaNacimientoUsuario.text().upper())

        if(len(Cedula)>10):
            self.Ui.Crearusuario.setText("No se ha podido Ingresar el Usuario Correctamente, La longitud de la cédula no puede ser mayor a 10")
        else:
            resultado = self.Usuario.InsertarUsuario(Cedula, Nombre, Apellido, fech_nac)
            if(resultado == True):
                self.Ui.Crearusuario.setText("Se ha ingresado el Usuario Exitosamente")
            else:
                self.Ui.Crearusuario.setText("No se ha podido Ingresar el Usuario Correctamente, "+str(resultado))

    def ModificarProducto(self):
        Nombre = str(self.Ui.lineEditActualizarNombreProducto.text().upper())
        Precio = str(self.Ui.lineEditActualizarValorProducto.text().upper())
        Id = str(self.Ui.lineEdit_IDActualizarProducto.text())

        resultado = self.Producto.ModificarProducto(Nombre,Precio,Id)
        if (resultado == True):
            self.Ui.ModificarProducto.setText("Se ha  modificado el producto Correctamente")
        else:
            self.Ui.ModificarProducto.setText("No se ha  modificado el producto Correctamente, "+str(resultado))

    def ModificarInsumo(self):
        nombreinsumo = str(self.Ui.lineEditActualizarNombreInsumo.text().upper())
        horasinsumo =str(self.Ui.lineEditActualizarHorasInsumo.text())
        idinsumo =str(self.Ui.lineEdit_IDACtualizarInsumo.text())
        resultado = self.Insumo.ModificarInsumo(nombreinsumo,horasinsumo,idinsumo)
        if resultado == True:
            self.Ui.ModificarInsumo.setText("Se ha modificado exitosamente el Insumo")
        else:
            self.Ui.ModificarInsumo.setText("No se ha modificado exitosamente el Insumo, "+str(resultado))

    def ModificarActividad(self):
        costo = str(self.Ui.lineEditAgregarActividad_2.text())
        idinsumo = str(self.Ui.lineEdit_3.text())
        idproducto =str(self.Ui.lineEdit_4.text())
        idusuario = str(self.Ui.lineEdit_5.text())
        idactividad = str(self.Ui.lineEdit_IdActualizarActividad.text())
        resultado = self.Actividad.ModificarActividad(costo,idinsumo,idproducto,idusuario,idactividad)
        if len(idusuario) >10 :
            self.Ui.ActualizarActividad.setText("No se ha modificado exitosamente la actividad, La longitud de la cedula no puede ser mayor a 10")
        else:
            if resultado == True:
                self.Ui.ActualizarActividad.setText("Se ha modificado exitosamente la actividad")
            else:
                self.Ui.ActualizarActividad.setText("No se ha modificado exitosamente la actividad, "+str(resultado))

    def Modificarusuario(self):
        Nombre = str(self.Ui.lineEditActualizarNombreUsuario.text().upper())
        Fecha = str(self.Ui.lineEditActualizarFechaNacUsuario.text().upper())
        Apellido = str(self.Ui.lineEditActualizarApellidoUsuaio.text().upper())
        Cedula = str(self.Ui.lineEdit_idActualizarUsuario.text())
        resultado = self.Usuario.ModificarUsuario(Cedula,Nombre,Apellido,Fecha)
        if len(Cedula)>10:
            self.Ui.ModificarUsuario.setText("No Se ha Modificado Correctamente el usuario, La longitud de cedula no puede ser mayor a 10")
        else:
            if resultado :
                self.Ui.ModificarUsuario.setText("Se ha Modificado Correctamente el usuario")
            else:
                self.Ui.ModificarUsuario.setText("No Se ha Modificado Correctamente el usuario, "+str(resultado))

    def Ganancia(self):

        res = str(self.Simplex.CalcularValorObjetivo())
        resultado = "Ganancia = " + res
        self.Ui.label_33.setText(resultado)
        self.Simplex.PDF()

if __name__ == "__main__":
    Root = QtGui.QApplication(sys.argv)
    rroot = root()
    rroot.show()
    rroot.exec_()
