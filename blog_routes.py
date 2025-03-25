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

@blog_bp.route('/blog/salud_mental_higado')
def salud_mental_higado():
    return render_template('blog_content/blog/salud_mental_higado.html', canonical_url="https://higadograso.mx/blog/salud_mental_higado")

@blog_bp.route('/blog/microplasticos_impacto_higado')
def microplasticos_impacto_higado():
    return render_template('blog_content/blog/microplasticos_impacto_higado.html', canonical_url="https://higadograso.mx/blog/microplasticos_impacto_higado")        

@blog_bp.route('/blog/control_azucar_glucosa_sangre')
def control_azucar_glucosa_sangre():
    return render_template('blog_content/blog/control_azucar_glucosa_sangre.html', canonical_url="https://higadograso.mx/blog/control_azucar_glucosa_sangre")        

@blog_bp.route('/blog/obesidad_relacion_higado_graso')
def obesidad_relacion_higado_graso():
    return render_template('blog_content/blog/obesidad_relacion_higado_graso.html', canonical_url="https://higadograso.mx/blog/obesidad_relacion_higado_graso")        

@blog_bp.route('/blog/control_azucar_glucosa_sangre_perspectivas_estrategias')
def control_azucar_glucosa_sangre_perspectivas_estrategias():
    return render_template('blog_content/blog/control_azucar_glucosa_sangre_perspectivas_estrategias.html', canonical_url="https://higadograso.mx/blog/control_azucar_glucosa_sangre_perspectivas_estrategias")        

@blog_bp.route('/blog/obesidad_un_problema_global')
def obesidad_un_problema_global():
    return render_template('blog_content/blog/obesidad_un_problema_global.html', canonical_url="https://higadograso.mx/blog/obesidad_un_problema_global")        

@blog_bp.route('/blog/medicos_familia_prevencion_manejo_enfermedades')
def medicos_familia_prevencion_manejo_enfermedades():
    return render_template('blog_content/blog/medicos_familia_prevencion_manejo_enfermedades.html', canonical_url="https://higadograso.mx/blog/medicos_familia_prevencion_manejo_enfermedades")        

@blog_bp.route('/blog/cirrosis_diabetes')
def cirrosis_diabetes():
    return render_template('blog_content/blog/cirrosis_diabetes.html', canonical_url="https://higadograso.mx/blog/medicos_familia_prevencion_manejo_enfermedades")        


