from flask import request, jsonify, redirect, url_for, flash, render_template, session
from flask_mail import Message
import logging
from blog_routes import blog_bp  # Cambia el import relativo por absoluto

def validate_contact_method(metodo_contacto, telefono, whatsapp, correo):
    if metodo_contacto == "Correo electronico" and not correo:
        return 'Por favor, proporciona un correo electrónico válido.'
    if metodo_contacto in ["Telefono", "Whatsapp"] and not (telefono or whatsapp):
        return f'Por favor, proporciona un número de {metodo_contacto.lower()}.' 
    return None

def register_routes(app, mail, db):
    # Registrar el Blueprint del blog
    app.register_blueprint(blog_bp)

    # Rutas principales
    @app.route('/')
    def index():
        return render_template('index.html', canonical_url="https://higadograso.mx/")

    @app.route('/blog')
    def blog():
        return render_template('blog.html', canonical_url="https://higadograso.mx/blog")

    @app.route('/citas')
    def citas():
        return render_template('citas.html', canonical_url="https://higadograso.mx/citas")

    @app.route('/contact')
    def contact():
        return render_template('contact.html', canonical_url="https://higadograso.mx/contact")

    @app.route('/enfermedades')
    def enfermedades():
        return render_template('enfermedades.html', canonical_url="https://higadograso.mx/enfermedades")

    @app.route('/eventos')
    def eventos():
        return render_template('eventos.html', canonical_url="https://higadograso.mx/eventos")

    @app.route('/especialistas')
    def especialistas():
        return render_template('especialistas.html', canonical_url="https://higadograso.mx/especialistas")

    @app.route('/manifiesto')
    def manifiesto():
        return render_template('manifiesto.html', canonical_url="https://higadograso.mx/manifiesto")

    @app.route('/ensayos')
    def ensayos():
        return render_template('ensayos.html', canonical_url="https://higadograso.mx/ensayos")

    @app.route('/solicitar-cita', methods=['POST'])
    def solicitar_cita():
        try:
            # Recopila datos del formulario
            padecimientos = request.form.getlist('padecimientos[]')
            referido = request.form.get('referido')
            referido_nombre = request.form.get('referido_nombre', '').strip()
            sede = request.form.get('sede')
            participar = request.form.get('participar')
            metodo_contacto = request.form.get('contacto')
            telefono = request.form.get('telefono', '').strip()
            whatsapp = request.form.get('whatsapp', '').strip()
            correo = request.form.get('correo', '').strip()

            # Validaciones
            if not sede or not metodo_contacto:
                message = 'Por favor, selecciona una sede y un método de contacto.'
                if request.is_json:
                    return jsonify(success=False, message=message), 400
                flash(message, 'warning')
                return redirect(url_for('index'))

            validation_error = validate_contact_method(metodo_contacto, telefono, whatsapp, correo)
            if validation_error:
                if request.is_json:
                    return jsonify(success=False, message=validation_error), 400
                flash(validation_error, 'warning')
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
            mail.send(msg)
            logging.info('Correo enviado correctamente.')

            success_message = 'Tu solicitud de cita se ha enviado correctamente. Te contactaremos pronto.'
            if request.is_json:
                return jsonify(success=True, message=success_message), 200
            flash(success_message, 'success')
            return redirect(url_for('index'))

        except Exception as e:
            logging.error(f'Error al enviar el formulario: {e}')
            error_message = 'Hubo un error al procesar tu solicitud. Inténtalo nuevamente más tarde.'
            if request.is_json:
                return jsonify(success=False, message=error_message), 500
            flash(error_message, 'danger')
            return redirect('/')

    @app.route('/subscribe', methods=['POST'])
    def subscribe():
        email = request.form.get('email')
        if not email:
            flash('Por favor, ingresa un correo válido.', 'warning')
            return redirect(url_for('index'))

        subscribers_ref = db.collection('subscribers')
        existing_subscriber = subscribers_ref.where('email', '==', email).get()

        if len(existing_subscriber) > 0:
            flash('Ya estás suscrito al newsletter.', 'info')
        else:
            try:
                subscribers_ref.add({'email': email})
                flash('¡Te has suscrito al newsletter exitosamente!', 'success')
            except Exception as e:
                logging.error(f'Error al guardar el correo en Firestore: {e}')
                flash('Hubo un error al procesar tu suscripción. Inténtalo más tarde.', 'danger')

        return redirect(url_for('index'))

    @app.route('/subscribers', methods=['GET'])
    def list_subscribers():
        try:
            subscribers = db.collection('subscribers').stream()
            subscriber_list = [sub.to_dict() for sub in subscribers]
            return render_template('subscribers.html', subscribers=subscriber_list)
        except Exception as e:
            logging.error(f'Error al listar suscriptores: {e}')
            flash('No se pudieron recuperar los suscriptores.', 'danger')
            return redirect(url_for('index'))
