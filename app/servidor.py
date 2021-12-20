from flask import Flask, request, render_template,redirect,flash,url_for
from app import autenticacion

app= Flask(__name__, template_folder='templates')
app.secret_key = 'A(!b]k"tQeVUYEISX>i5y|Z`JoW`7c'

nombre = ''
nombre_lista = ''
id_lista = ''
id_receta = ''
nombre_receta = ''
error = None


'''
///////////////////////////////////////////
       rutas para cargado de página 
///////////////////////////////////////////
'''


@app.route('/')
@app.route('/index')
def index_page():
    return render_template('index.html')


@app.route('/signup')
def signup_page():
    return render_template('signup.html')


@app.route('/login')
def login_page():
    if nombre == '':
        return render_template('login.html')
    else:
        return redirect('/mis_listas')




'''
///////////////////////////////////////////
      rutas con los form html- usuario
///////////////////////////////////////////
'''


@app.route('/signup', methods=['GET','POST'])
def crear_usuario():
    error=None
    if request.form['passwd'] != request.form['confirm']:
        error = 'Las contraseñas no coinciden.'
    elif not autenticacion.validar_correo(request.form['correo']):
        error = 'Ingresa un correo válido.'
    else:
        aux=autenticacion.validar_registro(request.form['nombre_usuario'], request.form['correo'], request.form['passwd'])
        if aux == 2:
            flash('Te registraste con éxito, procede a iniciar sesión.')
            return redirect('/login')
        elif aux == 0:
            error ='El usuario ya existe o el correo ya se encuentra registrado.'
        else:
            error = 'Error inesperado'
    return render_template('signup.html', error=error)


@app.route('/login',methods=['POST'])
def validar_login():
    error=None
    global nombre
    nombre = request.form['nombre_usuario']
    nombre_session=nombre
    aux=autenticacion.validar_login(nombre,request.form['passwd'])
    if aux == 0:
        nombre = ''
        error= 'El usuario no existe o la contraseña es incorrecta.'
    elif aux == 1:
        flash('Bienvenido, ', nombre_session)
        return redirect('/mis_listas')
    else:
        nombre = ''
        error = 'Error inesperado'
    return render_template('login.html',error=error, nombre_session=nombre_session)


@app.route('/cambio_correo',methods=['POST'])
def cambiar_correo():
    error=None
    passwd=request.form['passwd']
    correo=request.form['correo']
    if not autenticacion.validar_correo(request.form['correo']):
        error = 'Ingresa un correo válido.'
    else:
        aux = autenticacion.cambiar_correo(nombre, passwd, correo)
        if aux == 2:
            error = 'El correo electrónico ya se encuentra registrado.'
        elif aux == 1:
            flash('Correo electrónico actualizado')
            return redirect('/ajustes')
        elif aux == 0:
            error = 'Contraseña incorrecta.'
        else:
            error = 'Error inesperado'
    return render_template('cambio_correo.html', error=error)


@app.route('/cambio_passwd', methods=['POST'])
def cambiar_passwd():
    error = None
    passwd = request.form['last_passwd']
    new_passwd = request.form['new_passwd']
    aux = autenticacion.cambiar_passwd(nombre, passwd, new_passwd)
    if aux == 2:
        error = 'La contraseña nueva debe ser diferente a la antigua.'
    elif aux == 1:
        flash('Contraseña actualizada')
        return redirect('/ajustes')
    elif aux == 0:
        error = 'Contraseña incorrecta.'
    else:
        error = 'Error inesperado'
    return render_template('cambio_passwd.html', error=error)


@app.route('/borrar_cuenta', methods=['POST'])
def borrar_cuenta():
    error = None
    global nombre
    passwd = request.form['passwd']
    aux_id = autenticacion.get_id(nombre)
    aux = autenticacion.borrar_cuenta(aux_id, nombre, passwd)
    if aux == 0:
        error = 'La cuenta no pudo ser borrada.'
    elif aux == 1:
        flash('Cuenta borrada con éxito')
        nombre = ''
        return redirect('/login')
    else:
        error = 'Error inesperado'
    return render_template('ajustes.html', error=error)


@app.route('/logout')
def logout():
    global nombre
    global nombre_lista
    nombre = ''
    nombre_lista = ''
    flash('La sesión cerró correctamente.')
    return redirect ('/login')


@app.route('/cambio_correo')
def cambio_correo_page():
    if nombre == '':
        return redirect('/login')
    nombre_session = nombre
    return render_template('cambio_correo.html', nombre_session=nombre_session)


@app.route('/cambio_passwd')
def cambio_passwd_page():
    if nombre == '':
        return redirect('/login')
    nombre_session = nombre
    return render_template('cambio_passwd.html', nombre_session=nombre_session)


@app.route('/borrar_cuenta')
def borrar_cuenta_page():
    if nombre == '':
        return redirect('/login')
    return render_template('borrar_cuenta.html', nombre_sesion=nombre)


@app.route('/ajustes')
def settings_page():
    if nombre == '':
        return redirect('/login')
    else:
        aux = autenticacion.get_correo(nombre)
        nombre_session = nombre
        correo_session = aux
    return render_template('ajustes.html', nombre_session=nombre_session, correo_session=correo_session)

'''
///////////////////////////////////////////
    rutas con los form html- productos
///////////////////////////////////////////
'''


@app.route('/registros')
def registros_page():
    if nombre == '':
        return redirect('/login')
    nombre_session = nombre
    return render_template('registros.html', nombre_session=nombre_session)


@app.route('/productos')
def productos_page():
    if nombre == '':
        return redirect('/login')
    nombre_session = nombre
    return render_template('busqueda.html', nombre_session=nombre_session)


@app.route('/productos', methods=['POST'])
def buscar_producto():
    error = None
    global nombre
    aux_id = autenticacion.get_id(nombre)
    busqueda = request.form['busqueda']
    aux = autenticacion.buscar_producto(aux_id, busqueda)
    i = 0
    j = []
    k = []
    while i < len(aux):
        j = aux[i]
        aux_precio = autenticacion.buscar_precio(j[1])
        k = k + aux_precio
        i += 1
    return render_template('busqueda.html', error=error, resultados=aux, precios=k, nombre_session=nombre)


@app.route('/registros', methods=['POST'])
def registrar_productos():
    error = None
    global nombre
    producto_ingresado = request.form['ingresar_producto']
    precio=request.form['ingresar_precio']
    aux_id = autenticacion.get_id(nombre)
    consultar_producto = autenticacion.validar_producto(producto_ingresado, aux_id)
    if consultar_producto == 1:
        autenticacion.crear_producto(producto_ingresado, aux_id)
    aux_id_producto = autenticacion.get_id_producto(aux_id, producto_ingresado)
    aux2=aux_id_producto[0]
    aux = autenticacion.ingresar_precio(precio, aux2[0])

    if aux == 1:
        flash('Precio ingresado!')
    else:
        error = 'Error inesperado'
    return render_template('registros.html', error=error, resultado=producto_ingresado, precio=precio)

'''
///////////////////////////////////////////
      rutas con los form html- listas
///////////////////////////////////////////
'''


@app.route('/nueva_lista')
def nueva_lista_page():
    if nombre == '':
        return redirect('/login')
    nombre_session = nombre
    return render_template('nueva_lista.html', nombre_session=nombre_session)


@app.route('/mis_listas')
def mis_listas_page():
    if nombre == '':
        return redirect('/login')
    nombre_session = nombre
    aux_id = autenticacion.get_id(nombre)
    id_listas = autenticacion.get_id_lista(aux_id)
    k = []
    lista = 0
    nombres = []
    while lista < len(id_listas):
        mostrar_listas = autenticacion.mostrar_listas((id_listas[lista])[0])
        nombre_l = autenticacion.get_nombre_lista((id_listas[lista])[0])
        nombres = nombres + nombre_l
        k=k+mostrar_listas
        lista += 1
    return render_template('mis_listas.html', nombre_session=nombre_session, listas=k, largo =id_listas, datos=nombres)


@app.route('/lista')
def lista_page():
    if nombre == '':
        return redirect('/login')
    nombre_session = nombre
    mostrar_datos_lista = autenticacion.mostrar_datos_lista(id_lista)
    lista_relacion = autenticacion.mostrar_lista_relacion(id_lista)

    return render_template('lista.html', nombre_session=nombre_session, mostrar_datos=mostrar_datos_lista, relacion=lista_relacion, error=error)


@app.route('/nueva_lista', methods=['POST'])
def crear_lista():
    global nombre
    global error
    global nombre_lista
    global id_lista
    nombre_lista = request.form['nombre_lista']
    color = request.form['color']
    aux_id = autenticacion.get_id(nombre)
    autenticacion.crear_lista(nombre_lista, color, aux_id)
    aux_id_lista = autenticacion.get_id_lista_cre(aux_id)[0]
    id_lista = aux_id_lista[0]
    flash('Lista creada con éxito!')

    return redirect('/lista')



@app.route('/lista', methods=['POST'])
def ingresar_datos_lista():
    global nombre
    global error
    global nombre_lista
    aux_id = autenticacion.get_id(nombre)
    producto = request.form['producto']
    cantidad = request.form['cantidad']
    notas = request.form ['notas']
    consultar_producto = autenticacion.validar_producto(producto, aux_id)
    if consultar_producto == 1:
        autenticacion.crear_producto(producto, aux_id)

    aux_id_producto = (autenticacion.get_id_producto(aux_id, producto)[0])[0]
    if autenticacion.ingresar_datos_lista(id_lista, aux_id_producto, cantidad, notas) == 0:
        error = 'Este producto, cantidad y nota ya fue registrado, intenta con cantidad o nota diferente.'
        return redirect(url_for('lista_page', error=error))

    return redirect(url_for('lista_page', error=error))



'''
///////////////////////////////////////////
     rutas con los form html- recetas
///////////////////////////////////////////
'''


@app.route('/nueva_receta')
def nueva_receta_page():
    if nombre == '':
        return redirect('/login')
    nombre_session = nombre
    return render_template('nueva_receta.html', nombre_session=nombre_session)


@app.route('/mis_recetas')
def mis_recetas_page():
    if nombre == '':
        return redirect('/login')
    nombre_session = nombre
    aux_id = autenticacion.get_id(nombre)
    id_recetas = autenticacion.get_id_receta(aux_id)
    k = []
    lista = 0
    nombres = []
    procedimiento = []
    while lista < len(id_recetas):
        mostrar_recetas = autenticacion.mostrar_recetas((id_recetas[lista])[0])
        m = autenticacion.get_procedimiento((id_recetas[lista])[0])
        nombre_r = autenticacion.get_nombre_receta((id_recetas[lista])[0])
        nombres = nombres + nombre_r
        k=k+mostrar_recetas
        procedimiento=procedimiento+m
        lista += 1
    return render_template('mis_recetas.html', nombre_session=nombre_session, recetas=k, largo =id_recetas, datos=nombres, procedimiento=procedimiento)


@app.route('/receta')
def receta_page():
    if nombre == '':
        return redirect('/login')
    nombre_session = nombre
    mostrar_datos_receta = autenticacion.mostrar_datos_receta(id_receta)
    receta_relacion = autenticacion.mostrar_receta_relacion(id_receta)
    procedimiento = autenticacion.get_procedimiento(id_receta)

    return render_template('receta.html', nombre_session=nombre_session, mostrar_datos=mostrar_datos_receta, relacion=receta_relacion, procedimiento=procedimiento,error=error)


@app.route('/nueva_receta', methods=['POST'])
def crear_receta():
    global nombre
    global error
    global nombre_receta
    global id_receta
    nombre_receta = request.form['nombre_receta']
    color = request.form['color']
    aux_id = autenticacion.get_id(nombre)
    autenticacion.crear_receta(nombre_receta, color, aux_id)
    aux_id_receta = autenticacion.get_id_receta_cre(aux_id)[0]
    id_receta = aux_id_receta[0]
    flash('Receta creada con éxito!')

    return redirect('/receta')


@app.route('/receta', methods=['POST'])
def ingresar_datos_receta():
    global nombre
    global error
    global nombre_receta
    aux_id = autenticacion.get_id(nombre)
    producto = request.form['producto']
    cantidad = request.form['cantidad']
    unidad = request.form ['unidad']
    procedimiento= request.form['procedimiento']
    consultar_producto = autenticacion.validar_producto(producto, aux_id)
    if consultar_producto == 1:
        autenticacion.crear_producto(producto, aux_id)
    aux_id_producto = (autenticacion.get_id_producto(aux_id, producto)[0])[0]
    if not producto:
        pass
    else:
        if autenticacion.ingresar_datos_receta(id_receta, aux_id_producto, cantidad, unidad) == 0:
            error = 'Este producto, cantidad y unidad ya fue registrado, intenta con cantidad o unidad diferente.'
            return redirect(url_for('receta_page', error=error))
    if procedimiento == ' ':
        pass
    else:
        autenticacion.ingresar_procedimiento(id_receta, procedimiento)

    return redirect(url_for('receta_page', error=error))



if __name__ == '__main__':
    app.debug = True
    app.run()