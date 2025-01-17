from flask import Blueprint, render_template

# Crear un Blueprint para las rutas del blog
blog_bp = Blueprint('blog', __name__)

# Rutas del blog
@blog_bp.route('/blog/vapes-tabaco')
def blog_vapes_tabaco():
    return render_template('blog_content/blog/vapes_tabaco.html', canonical_url="https://higadograso.mx/blog/vapes-tabaco")

@blog_bp.route('/blog/evitar_remedios_caseros')
def evitar_remedios_caseros():
    return render_template('blog_content/blog/evitar_remedios_caseros.html', canonical_url="https://higadograso.mx/blog/evitar_remedios_caseros")

@blog_bp.route('/blog/diabetes_prediabetes')
def diabetes_prediabetes():
    return render_template('blog_content/blog/diabetes_prediabetes.html', canonical_url="https://higadograso.mx/blog/diabetes_prediabetes")

@blog_bp.route('/blog/enfermedades_respiratorias')
def enfermedades_respiratorias():
    return render_template('blog_content/blog/enfermedades_respiratorias.html', canonical_url="https://higadograso.mx/blog/enfermedades_respiratorias")

@blog_bp.route('/blog/tendencias_futuras_en_la_mortalidad')
def tendencias_futuras_en_la_mortalidad():
    return render_template('blog_content/blog/tendencias_futuras_en_la_mortalidad.html', canonical_url="https://higadograso.mx/blog/tendencias_futuras_en_la_mortalidad")
