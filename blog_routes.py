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

@blog_bp.route('/blog/dia_mundial_higado_graso')
def dia_mundial_higado_graso():
    return render_template('blog_content/blog/dia_mundial_higado_graso.html', canonical_url="https://higadograso.mx/blog/dia_mundial_higado_graso")       

@blog_bp.route('/blog/cirrosis_compensada_descompensada')
def cirrosis_compensada_descompensada():
    return render_template('blog_content/blog/cirrosis_compensada_descompensada.html', canonical_url="https://higadograso.mx/blog/cirrosis_compensada_descompensada")       

@blog_bp.route('/blog/higado_graso_10_preguntas')
def higado_graso_10_preguntas():
    return render_template('blog_content/blog/higado_graso_10_preguntas.html', canonical_url="https://higadograso.mx/blog/higado_graso_10_preguntas")       

@blog_bp.route('/blog/crohn_vs_cuci_diferencias_clave')
def crohn_vs_cuci_diferencias_clave():
    return render_template('blog_content/blog/crohn_vs_cuci_diferencias_clave.html', canonical_url="https://higadograso.mx/blog/crohn_vs_cuci_diferencias_clave")       

@blog_bp.route('/blog/cirrosis_compensada_diagnostico')
def cirrosis_compensada_diagnostico():
    return render_template('blog_content/blog/cirrosis_compensada_diagnostico.html', canonical_url="https://higadograso.mx/blog/cirrosis_compensada_diagnostico")       

@blog_bp.route('/blog/pbc_mujeres')
def pbc_mujeres():
    return render_template('blog_content/blog/pbc_mujeres.html', canonical_url="https://higadograso.mx/blog/pbc_mujeres")       

@blog_bp.route('/blog/ensayos_clinicos_enfemedades_hepaticas')
def ensayos_clinicos_enfemedades_hepaticas():
    return render_template('blog_content/blog/ensayos_clinicos_enfemedades_hepaticas.html', canonical_url="https://higadograso.mx/blog/ensayos_clinicos_enfemedades_hepaticas")       

@blog_bp.route('/blog/señales_cuci')
def señales_cuci():
    return render_template('blog_content/blog/señales_cuci.html', canonical_url="https://higadograso.mx/blog/señales_cuci")       

@blog_bp.route('/blog/checklist_preconsulta')
def checklist_preconsulta():
    return render_template('blog_content/blog/checklist_preconsulta.html', canonical_url="https://higadograso.mx/blog/checklist_preconsulta")       

@blog_bp.route('/blog/señales_cbp')
def señales_cbp():
    return render_template('blog_content/blog/señales_cbp.html', canonical_url="https://higadograso.mx/blog/señales_cbp")       

@blog_bp.route('/blog/imc_normal_yaunasi_higado_graso')
def imc_normal_yaunasi_higado_graso():
    return render_template('blog_content/blog/imc_normal_yaunasi_higado_graso.html', canonical_url="https://higadograso.mx/blog/imc_normal_yaunasi_higado_graso")       

@blog_bp.route('/blog/dia_colangitis_billiar_primaria')
def dia_colangitis_billiar_primaria():
    return render_template('blog_content/blog/dia_colangitis_billiar_primaria.html', canonical_url="https://higadograso.mx/blog/dia_colangitis_billiar_primaria")       

@blog_bp.route('/blog/semaglutida_nuevo_tratamiento_aprobado')
def semaglutida_nuevo_tratamiento_aprobado():
    return render_template('blog_content/blog/semaglutida_nuevo_tratamiento_aprobado.html', canonical_url="https://higadograso.mx/blog/semaglutida_nuevo_tratamiento_aprobado")       

@blog_bp.route('/blog/como_leer_fibroscan')
def como_leer_fibroscan():
    return render_template('blog_content/blog/como_leer_fibroscan.html', canonical_url="https://higadograso.mx/blog/como_leer_fibroscan")       

@blog_bp.route('/blog/dia_nacional_de_la_donacion_de_organos')
def dia_nacional_de_la_donacion_de_organos():
    return render_template('blog_content/blog/dia_nacional_de_la_donacion_de_organos.html', canonical_url="https://higadograso.mx/blog/dia_nacional_de_la_donacion_de_organos")       

@blog_bp.route('/blog/que_es_un_protocolo_de_investigacion_clinica')
def que_es_un_protocolo_de_investigacion_clinica():
    return render_template('blog_content/blog/que_es_un_protocolo_de_investigacion_clinica.html', canonical_url="https://higadograso.mx/blog/que_es_un_protocolo_de_investigacion_clinica")       

@blog_bp.route('/blog/mash_masd')
def mash_masd():
    return render_template('blog_content/blog/mash_masd.html', canonical_url="https://higadograso.mx/blog/mash_masd")

@blog_bp.route('/blog/mash_por_que_hay_pocas_terapias_aprobadas')
def mash_por_que_hay_pocas_terapias_aprobadas():
    return render_template('blog_content/blog/mash_por_que_hay_pocas_terapias_aprobadas.html', canonical_url="https://higadograso.mx/blog/mash_por_que_hay_pocas_terapias_aprobadas")

@blog_bp.route('/blog/avances_cuci_y_crohn')
def avances_cuci_y_crohn():
    return render_template('blog_content/blog/avances_cuci_y_crohn.html', canonical_url="https://higadograso.mx/blog/avances_cuci_y_crohn")

@blog_bp.route('/blog/fibrosis_hepatica_f0_f4')
def fibrosis_hepatica_f0_f4():
    return render_template('blog_content/blog/fibrosis_hepatica_f0_f4.html', canonical_url="https://higadograso.mx/blog/fibrosis_hepatica_f0_f4")

@blog_bp.route('/blog/esteatosis_s1_s3')
def esteatosis_s1_s3():
    return render_template('blog_content/blog/esteatosis_s1_s3.html', canonical_url="https://higadograso.mx/blog/esteatosis_s1_s3")

@blog_bp.route('/blog/suplementos_naturales')
def suplementos_naturales():
    return render_template('blog_content/blog/suplementos_naturales.html', canonical_url="https://higadograso.mx/blog/suplementos_naturales")

@blog_bp.route('/blog/evolucion_de_lod_protocolos_de_investigacion')
def evolucion_de_lod_protocolos_de_investigacion():
    return render_template('blog_content/blog/evolucion_de_lod_protocolos_de_investigacion.html', canonical_url="https://higadograso.mx/blog/evolucion_de_lod_protocolos_de_investigacion")

@blog_bp.route('/blog/fgf21_en_palabras_simples')
def fgf21_en_palabras_simples():
    return render_template('blog_content/blog/fgf21_en_palabras_simples.html', canonical_url="https://higadograso.mx/blog/fgf21_en_palabras_simples")

@blog_bp.route('/blog/fgf21_podria_cambiar_el_rumbo_del_higado_graso')
def fgf21_podria_cambiar_el_rumbo_del_higado_graso():
    return render_template('blog_content/blog/fgf21_podria_cambiar_el_rumbo_del_higado_graso.html', canonical_url="https://higadograso.mx/blog/fgf21_en_palabras_simples")

@blog_bp.route('/blog/tratamiento-higado-graso-glp-1-vitamina-e')
def tratamiento_higado_graso_glp_1_vitamina_e():
    return render_template(
        'blog_content/blog/tratamiento_higado_graso_glp_1_vitamina_e.html',
        canonical_url="https://higadograso.mx/blog/tratamiento-higado-graso-glp-1-vitamina-e"
    )

@blog_bp.route('/blog/glp_1_por_que_son_relevantes_en_el_higado_graso')
def glp_1_por_que_son_relevantes_en_el_higado_graso():
    return render_template(
        'blog_content/blog/glp_1_por_que_son_relevantes_en_el_higado_graso.html',
        canonical_url="https://higadograso.mx/blog/glp-1-relevantes-higado-graso"
    )

@blog_bp.route('/blog/glp_1_y_fgf21_dos_rutas_que_estan_cambiando_la_investigacion_en_mash')
def glp_1_y_fgf21_dos_rutas_que_estan_cambiando_la_investigacion_en_mash():
    return render_template(
        'blog_content/blog/glp_1_y_fgf21_dos_rutas_que_estan_cambiando_la_investigacion_en_mash.html',
        canonical_url="https://higadograso.mx/blog/glp_1_y_fgf21_dos_rutas_que_estan_cambiando_la_investigacion_en_mash"
    )

@blog_bp.route('/blog/que_es_el_masld_o_mash_explicacion_clara_para_pacientes.html')
def que_es_el_masld_o_mash_explicacion_clara_para_pacientes():
    return render_template(
        'blog_content/blog/que_es_el_masld_o_mash_explicacion_clara_para_pacientes.html',
        canonical_url="https://higadograso.mx/blog/que_es_el_masld_o_mash_explicacion_clara_para_pacientes"
    )

