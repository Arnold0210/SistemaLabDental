from Interfaz.Interfaces import *
from mysql import connector as mysql
from mysql.connector import *
from scipy.optimize import linprog

class ModeloConexion(InterfaceConexion):
    def Conexion(self):
        Conector = None
        try:
            Conector = mysql.connect(**self.config_mysql)
        except Error:
            print(Error)
        finally:
            return Conector
    def SQlConsulta(self, Conector, Palabra, Tabla):
        SQL = "SELECT "
        Consulta = []
        Cursor = Conector.cursor()
        for i in range(0,len(Palabra)):
            if(i == len(Palabra) - 1):
                SQL = SQL + Palabra[i]
            else:
                SQL = SQL + Palabra[i] +","
        SQL = SQL + " FROM " + Tabla +";"
        try:
            if(Cursor==None):
                return None
            else:
                Cursor.execute(SQL)
                for i in Cursor:
                    Consulta.append(i)
        except Error as error:
            print(error)
        finally:
            Cursor.close()
            Conector.close()
            return Consulta
    def Select(self, Tabla, Palabra):
        DB = self.Conexion()
        if(DB == None):
            return None
        else:
            Consultar = self.SQlConsulta(DB,Palabra,Tabla)
            if(Consultar == None):
                return None
            DB.close()
            return Consultar
    def ConsultaColumnas(self,Conector,Tabla):
        Palabra = []
        Cursor = Conector.cursor()
        Columnas = "SELECT COLUMN_NAME FROM information_schema.columns WHERE table_name = '" + Tabla + "';"
        try:
            Cursor.execute(Columnas)
            for i in Cursor:
                Palabra.append(list(i))
        except Error as  error:
            print(error)
        finally:
            Cursor.close()
        return Palabra
    def Columnas(self, Tabla):
        Palabra = []
        DB = self.Conexion()
        if(DB == None):
            return None
        else:
            Columnas = self.ConsultaColumnas(DB, Tabla)
            for i in Columnas:
                for j in range(len(Columnas[0])):
                    Palabra.append(i[j])
            DB.close()
            return Palabra

class ModeloProducto(InterfaceProducto):
    Conection = ModeloConexion()
    def InsertarProducto(self, Query,args):
        DB = self.Conection.Conexion()
        Cursor = DB.cursor()
        try:
            Cursor.execute(Query, args)
            DB.commit()
            return True
        except Error as error:
            return error
        finally:
            Cursor.close()
            DB.close()
    def ModificarProducto(self,SQL,args):
        DB = self.Conection.Conexion()
        Cursor = DB.cursor()
        try:
            Cursor.execute(SQL, args)
            DB.commit()
            return True
        except Error as e:
            return e
        finally:
            Cursor.close()
            DB.close()
    def VisualizarProducto(self,SQL):
        DB = self.Conection.Conexion()
        Cursor = DB.cursor()
        Consulta = []
        try:
            Cursor.execute(SQL)
            for i in Cursor:
                Consulta.append(i)
            return Consulta
        except Error:
            return Error
        finally:
            Cursor.close()
            DB.close()

class ModeloInsumo(InterfaceInsumo):
    Conection = ModeloConexion()
    def InsertarInsumo(self,Query , args):
        DB = self.Conection.Conexion()
        Cursor = DB.cursor()
        try:
            Cursor.execute(Query, args)
            DB.commit()
            return True
        except Error as error:
            return error
        finally:
            Cursor.close()
            DB.close()

    def ModificarInsumo(self,SQL,args):
        DB = self.Conection.Conexion()
        Cursor = DB.cursor()
        try:
            Cursor.execute(SQL, args)
            DB.commit()
            return  True
        except Error as e:
            return e
        finally:
            Cursor.close()
            DB.close()

    def VisualizarInsumo(self, SQL):
        # Palabra= []
        # Palabra = self.Conection.Columnas("producto")
        DB = self.Conection.Conexion()
        Cursor = DB.cursor()
        Consulta = []
        try:
            Cursor.execute(SQL)
            for i in Cursor:
                Consulta.append(i)
            return Consulta
        except Error:
            return Error
        finally:
            Cursor.close()
            DB.close()

class ModeloActividad(InterfaceActividad):
    Conection = ModeloConexion()
    def InsertarActividad(self,SQL,args):
        DB = self.Conection.Conexion()
        Cursor = DB.cursor()
        try:
            Cursor.execute(SQL, args)
            DB.commit()
            return True
        except Error as error:
            return error
        finally:
            Cursor.close()
            DB.close()
    def ModificarActividad(self,SQL,args):
        DB = self.Conection.Conexion()
        Cursor = DB.cursor()
        try:
            Cursor.execute(SQL,args)
            DB.commit()
            return  True
        except Error as e:
            return e
        finally:
            Cursor.close()
            DB.close()
    def VisualizarActividad(self,SQL):
        DB = self.Conection.Conexion()
        Cursor = DB.cursor()
        Consulta = []
        try:
            Cursor.execute(SQL)
            for i in Cursor:
                Consulta.append(i)
            return Consulta
        except Error:
            return Error
        finally:
            Cursor.close()
            DB.close()

class ModeloUsuario(InterfaceUsuario):
    Conection = ModeloConexion()
    def InsertarUsuario(self,SQL,args):
        DB = self.Conection.Conexion()
        Cursor = DB.cursor()
        try:
            Cursor.execute(SQL, args)
            DB.commit()
            return True
        except Error as error:
            return error
        finally:
            Cursor.close()
            DB.close()
    def ModificarUsuario(self,SQL,args):
        DB = self.Conection.Conexion()
        Cursor = DB.cursor()
        try:
            Cursor.execute(SQL, args)
            DB.commit()
            return True
        except Error:
            return Error
        finally:
            Cursor.close()
            DB.close()

    def VisualizarUsuario(self,SQL):
        DB = self.Conection.Conexion()
        Cursor = DB.cursor()
        Consulta = []
        try:
            Cursor.execute(SQL)
            for i in Cursor:
                Consulta.append(i)
            return Consulta
        except Error:
            return Error
        finally:
            Cursor.close()
            DB.close()
class ModeloSimplex(InterfaceSimplex):
    Conexion = ModeloConexion()
    def h(kw, **kwg):
        basicas = kwg['tableau']
        print(basicas)
        return basicas
    def GenerarSimplex(self):
        db = self.Conexion.Conexion()
        Cursor = db.cursor()
        SQL = "SELECT idACTIVIDAD,INSUMO_idInsumo,PRODUCTO_idPRODUCTO,CostoActividad FROM `labdental`.`actividad`;"
        Cursor.execute(SQL)
        T_1 = []
        for i in Cursor:
            T_1.append(i)
        SQL = "SELECT * FROM `labdental`.`producto`;"
        Cursor.execute(SQL)
        T_2 = []
        for i in Cursor:
            T_2.append(i)
        SQL = "SELECT * FROM labdental.insumo;"
        Cursor.execute(SQL)
        T_3 = []
        for i in Cursor:
            T_3.append(i)
        A = []
        B = []
        C = []
        NOMBRES_PROD = []
        ID_PROD = []
        ID_PRODA = []
        ID_ACTIVIDAD = []
        ID_INSUMO = []
        ID_INSUMOB = []
        VALOR = []
        m_1 = []
        m_2 = []
        m_3 = []
        m_4 = []
        matriz1 = []
        matriz2 = []

        for i in range(0, len(T_2)):
            C.append((-1*T_2[i][2]))
            NOMBRES_PROD.append(T_2[i][1])
            ID_PROD.append(T_2[i][0])

        for j in range(0, len(T_3)):
            B.append(T_3[j][2])
            ID_INSUMO.append(T_3[j][0])

        for v in range(0, len(ID_INSUMO)):
            m_1.append(ID_INSUMO[v])
            m_2.append(v)
        matriz1.append(m_1)
        matriz1.append(m_2)

        for v in range(0, len(T_1)):
            ID_INSUMOB.append(T_1[v][1])
            ID_PRODA.append(T_1[v][2])
            VALOR.append(T_1[v][3])

        for v in range(0, len(ID_PROD)):
            m_3.append(ID_PROD[v])
            m_4.append(v)
        matriz2.append(m_3)
        matriz2.append(m_4)

        for f in range(0, len(B)):
            TAB = []
            for c in range(0, len(C)):
                TAB.append(0)
            A.append(TAB)

        for f in range(0, len(ID_INSUMOB)):
            TAB = []
            for c in range(0, len(B)):

                if (ID_INSUMOB[f] == matriz1[0][c]):
                    #print("A",ID_INSUMOB[f],"---",matriz1[0][c])
                    a = matriz1[1][c]
                if (ID_PRODA[f] == matriz2[0][c]):
                    #print("B",ID_PRODA[f],"---",matriz2[0][c])
                    b = matriz2[1][c]
                    V = VALOR[f]
                    #print(V)
                #             print(a, "<--->", b)
            A[a][b] = V
            a = 0
            b = 0
            V = 0
        #print("T_1", T_1)
        #print("C\n",C)
        #print("A \n", A)
        #print("B \n", B)
        res = linprog(C, A_eq=A, b_eq=B, bounds=None)
        a = res.x
        print(type(a))
        if res == None:
            return None,NOMBRES_PROD
        else:
            return res,NOMBRES_PROD



