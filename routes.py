from flask import render_template

def register_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/manifiesto')
    def manifiesto():
        return render_template('manifiesto.html')

    @app.route('/enfermedades')
    def enfermedades():
        return render_template('enfermedades.html')

    @app.route('/especialistas')
    def especialistas():
        return render_template('especialistas.html')

    @app.route('/citas')
    def citas():
        return render_template('citas.html')

    @app.route('/ensayos')
    def ensayos():
        return render_template('ensayos.html')

    @app.route('/contacto')
    def contacto():
        return render_template('contacto.html')

    @app.route('/eventos')
    def eventos():
        return render_template('eventos.html')

    @app.route('/blog')
    def blog():
        return render_template('blog.html')
