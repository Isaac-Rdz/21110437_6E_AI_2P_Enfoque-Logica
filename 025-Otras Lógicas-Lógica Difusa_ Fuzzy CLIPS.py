
import clips

# Inicializar el entorno CLIPS
env = clips.Environment()

# Definir reglas difusas en CLIPS
env.build('(defrule regla-difusa '
          '(temperatura ?t) '
          '(humedad ?h) '
          '=> '
          '(assert (potencia (fuzzy-and (fría ?t) (seca ?h)) 0.8)) '
          '(assert (potencia (fuzzy-and (templada ?t) (normal ?h)) 0.5)) '
          '(assert (potencia (fuzzy-and (caliente ?t) (húmeda ?h)) 0.2)))')

# Cargar hechos
env.assert_string('(temperatura 80)')
env.assert_string('(humedad 20)')

# Ejecutar reglas
env.run()

# Obtener resultados
for fact in env.facts():
    if fact.template.name == 'potencia':
        print("Potencia:", fact[1])
