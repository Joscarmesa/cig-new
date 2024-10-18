from flask import render_template

def register_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/citas')
    def citas():
        return render_template('citas.html')

    @app.route('/contact')
    def contact():
        return render_template('contact.html')

    @app.route('/enfermedades')
    def enfermedades():
        return render_template('enfermedades.html')

    @app.route('/eventos')
    def eventos():
        return render_template('eventos.html')

    @app.route('/especialistas')
    def especialistas():
        return render_template('especialistas.html')

    @app.route('/manifiesto')
    def manifiesto():
        return render_template('manifiesto.html')
    
    @app.route('/ensayos')
    def ensayos():
        return render_template('ensayos.html')
    
    @app.route('/inicio')
    def inicio():
        return render_template('inicio.html')
