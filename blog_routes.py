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

@blog_bp.route('/blog/cirrosis_higadograso')
def cirrosis_higadograso():
    return render_template('blog_content/blog/cirrosis_higadograso.html', canonical_url="https://higadograso.mx/blog/cirrosis_higadograso")        

@blog_bp.route('/blog/nuevo_logo')
def nuevo_logo():
    return render_template('blog_content/blog/nuevo_logo.html', canonical_url="https://higadograso.mx/blog/nuevo_logo") 

@blog_bp.route('/blog/fibroscan_gratis_cdmx')
def fibroscan_gratis_cdmx():
    return render_template('blog_content/blog/fibroscan_gratis_cdmx.html', canonical_url="https://higadograso.mx/blog/fibroscan_gratis_cdmx")       

@blog_bp.route('/blog/higado_graso_sintomas_tratamiento')
def higado_graso_sintomas_tratamiento():
    return render_template('blog_content/blog/higado_graso_sintomas_tratamiento.html', canonical_url="https://higadograso.mx/blog/higado_graso_sintomas_tratamiento")       

@blog_bp.route('/blog/abril_mes_de_conciencia_salud_hepatica_diabetes')
def abril_mes_de_conciencia_salud_hepatica_diabetes():
    return render_template('blog_content/blog/abril_mes_de_conciencia_salud_hepatica_diabetes.html', canonical_url="https://higadograso.mx/blog/abril_mes_de_conciencia_salud_hepatica_diabetes")       

@blog_bp.route('/blog/estatinas_control_colesterol')
def estatinas_control_colesterol():
    return render_template('blog_content/blog/estatinas_control_colesterol.html', canonical_url="https://higadograso.mx/blog/estatinas_control_colesterol")       

@blog_bp.route('/blog/enfermedad_crohn')
def enfermedad_crohn():
    return render_template('blog_content/blog/enfermedad_crohn.html', canonical_url="https://higadograso.mx/blog/enfermedad_crohn")       

@blog_bp.route('/blog/hipertension_infarto')
def hipertension_infarto():
    return render_template('blog_content/blog/hipertension_infarto.html', canonical_url="https://higadograso.mx/blog/hipertension_infarto")       

@blog_bp.route('/blog/enfermedad_renal_cronica')
def enfermedad_renal_cronica():
    return render_template('blog_content/blog/enfermedad_renal_cronica.html', canonical_url="https://higadograso.mx/blog/enfermedad_renal_cronica")       

@blog_bp.route('/blog/hepatitis_b_c')
def hepatitis_b_c():
    return render_template('blog_content/blog/hepatitis_b_c.html', canonical_url="https://higadograso.mx/blog/hepatitis_b_c")       

