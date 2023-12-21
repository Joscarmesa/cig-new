from flask import render_template

def register_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/appointment')
    def appointment():
        return render_template('appointment.html')

    @app.route('/contact')
    def contact():
        return render_template('contact.html')

    @app.route('/price')
    def price():
        return render_template('price.html')

    @app.route('/service')
    def service():
        return render_template('service.html')

    @app.route('/team')
    def team():
        return render_template('team.html')

    @app.route('/testimonial')
    def testimonial():
        return render_template('testimonial.html')

    @app.route('/about')
    def about():
        return render_template('about.html')
