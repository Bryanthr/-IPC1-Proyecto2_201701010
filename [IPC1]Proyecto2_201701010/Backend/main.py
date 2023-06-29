#SE INSTALARON LAS LIBRERÍAS
    #en cmd: pip install flask; pip install flask_cors

#IMPORTAR ARCHIVOS IMPORTANTES PARA CORRER EL SERVIDOR
from flask import Flask, request
#Flask: sirve para crear la aplicación servidor
#jsonify: sirve para mostrar la salida del JSON más ordenada
#request: sirve para obtener el body de la petición HTTP

from flask_cors import CORS
#no sé para que es pero creo que es para no tener errores de seguridad :v
#CORS: sirve para habilitar los orígenes cruzados, es decir un origen diferente

#Importar JSON ya que los puntos de entrada y salida son de tipo JSON
#import json

#Importar las clases creadas
from Clases.Usuario import Usuario
from Clases.Comentario import Comentario

#Importar los metodos creados
from Metodos.Administrador import *
from Metodos.Inicial import *
from Metodos.Usuario import * 


usuarios = []
usuarioEnSesion = -1
peliculas = []
comentarios = []

#Para administrador: Tipo 1
usuarios.append(Usuario('Usuario', 'Administrador', 'admin', 'admin', '1').toDict())

#Para usuarios: Tipo 2
usuarios.append(Usuario('Bryant', 'Herrera', 'BHRubio', '1234', '2').toDict())

#Comentarios de ejemplo
comentarios.append(Comentario('Spider-man: Spiderverse', 'BHRubio', 'La mejor animación que he visto').toDict())
comentarios.append(Comentario('Spider-man: Spiderverse', 'RandomUser', 'Buenísma pero, no me gusto el final').toDict())
comentarios.append(Comentario('La Sirenita 2023', 'BHRubio', 'Prefiero la version animada de 1989').toDict())
comentarios.append(Comentario('La Sirenita 2023', 'RandomUser', 'Horrible').toDict())

app = Flask(__name__)
CORS(app)

@app.route ('/', methods=['GET'])
def rutaInicial():
    return("No funciona")

#------------------------INICIO--------------------------
@app.route('/registrarUsuario', methods=['POST'])
def registrarUsuario():
    respuesta = RegistrarUsuario(request.json, usuarios)
    return respuesta

@app.route('/recuperarContrasenia', methods=['POST'])
def recuperarContrasenia():
    respuesta = RecuperarContrasenia(request.json, usuarios)
    return respuesta

@app.route('/iniciarSesion', methods=['POST'])
def iniciarSesion():
    respuesta = IniciarSesion(request.json, usuarios)
    global usuarioEnSesion
    
    usuarioEnSesion = respuesta['usuarioEnSesion']
    print(usuarioEnSesion)
    return respuesta
    


#------------------------USUARIOS------------------------
@app.route('/getUsuarioEnSesion', methods=['GET'])
def getUsuarioEnSesion():
    respuesta = GetUsuarioEnSesion(usuarios, usuarioEnSesion)
    return respuesta

@app.route('/modificarPerfil', methods=['POST'])
def modificarPerfil():
    global usuarios
    respuesta = ModificarPerfil(request.json, usuarios, usuarioEnSesion)
    usuarios = respuesta['data']
    return {'data':'OK', 'status': respuesta['status']}


#-------------------------ADMINISTRADOR------------------
@app.route('/cargarPeliculas', methods=['POST'])
def cargarPeliculas():
    respuesta = CargarPeliculas(request.json)
    global peliculas
    peliculas = respuesta['data']
    return respuesta

@app.route('/getPeliculas', methods=['GET'])
def getPeliculas():
    respuesta = {'data': peliculas, 'status': 200}
    return respuesta

@app.route('/getPelicula', methods=['POST'])
def getPelicula():
    respuesta = GetPelicula(request.json, peliculas)
    return respuesta

@app.route('/editarPelicula', methods=['POST'])
def editarPelicula():
    global peliculas
    respuesta = EditarPelicula(request.json, peliculas)
    peliculas = respuesta['data']
    return {'data':'OK', 'status': respuesta['status']}

@app.route('/eliminarPelicula', methods=['POST'])
def eliminarPelicula():
    global peliculas
    respuesta = EliminarPelicula(request.json, peliculas)
    peliculas = respuesta['data']
    return {'data':'OK', 'status': respuesta['status']}

@app.route('/getComentarios', methods=['POST'])
def getComentarios():
    respuesta = GetComentarios(request.json, comentarios)
    return respuesta

@app.route('/getUsuarios', methods=['GET'])
def getUsuarios():
    respuesta = {'data': usuarios, 'status': 200}
    return respuesta

@app.route('/eliminarUsuario', methods=['POST'])
def eliminarUsuario():
    global usuarios
    respuesta = EliminarUsuario(request.json, usuarios)
    usuarios = respuesta['data']
    return {'data':'OK', 'status': respuesta['status']}

#




if __name__ == "__main__":
    app.run(host = "0.0.0.0", port= 3000, debug=True)