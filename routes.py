from flask import render_template, request, flash, redirect, url_for
from flask_mail import Message
import logging

def register_routes(app, mail):
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
    
    @app.route('/blog')
    def blog():
        return render_template('blog.html')
    
    @app.route('/blog/vapes-tabaco')
    def blog_vapes_tabaco():
        return render_template('blog_content/blog/vapes_tabaco.html', canonical_url="https://higadograso.mx/blog/vapes-tabaco")

    @app.route('/inicio', methods=['GET', 'POST'])
    def inicio():
        return render_template('inicio.html')

    @app.route('/solicitar-cita', methods=['POST'])
    def solicitar_cita():
        # Recopila datos del formulario
        padecimientos = request.form.getlist('padecimientos[]')
        referido = request.form.get('referido')
        referido_nombre = request.form.get('referido_nombre', '')
        sede = request.form.get('sede')
        participar = request.form.get('participar')
        metodo_contacto = request.form.get('contacto')
        telefono = request.form.get('telefono', '')
        whatsapp = request.form.get('whatsapp', '')
        correo = request.form.get('correo', '')

        # Validación de campos obligatorios
        if not sede or not metodo_contacto:
            flash('Por favor, selecciona una sede y un método de contacto.', 'warning')
            return redirect(url_for('index'))
        
        # Crear el correo
        subject = "Nueva solicitud de cita"
        msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=['cigcitas@gmail.com'])
        msg.body = f"""
        Nueva solicitud de cita:
        Padecimientos: {', '.join(padecimientos)}
        Referido: {referido} ({referido_nombre})
        Sede seleccionada: {sede}
        Interés en participar: {participar}
        Método de contacto preferido: {metodo_contacto}
        Teléfono: {telefono}
        WhatsApp: {whatsapp}
        Correo: {correo}
        """
    
        # Enviar el correo
        try:
            mail.send(msg)
            logging.info('Correo enviado correctamente.')
            flash('Tu solicitud de cita se ha enviado correctamente. Te contactaremos pronto.', 'success')
        except Exception as e:
            logging.error(f'Error al enviar el correo: {e}')
            flash('Hubo un error al enviar tu solicitud. Inténtalo nuevamente más tarde.', 'danger')

        return redirect('/')



   