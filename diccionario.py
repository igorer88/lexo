nombres = {}
nombres["femeninos"] = ['Elsa', 'María', 'Caren', 'Lucia']
nombres["masculinos"] = ['Lucas', 'José', 'Luis', 'Darío', 'Julián']
articulos = {}
articulos['femeninos'] = ['la', 'las', 'una', 'unas']
articulos['masculinos'] = ['los', 'el', 'un', 'unos']
articulos['femeninos_singular'] = ['fruta', 'perra', 'gata', 'pelota', 'niña']
Sustantivos: perro, , gato, , ,
niño, , árbol, frutas, perros, perras, gatos, gatas,
pelotas, niños, niñas, árboles.
• Verbos: juega, juegan, come, comen, quiere,
quieren, es, son, corre, corren, llora, lloran.
preposiciones = ['a', 'con', 'como', 'por']
• Adverbios: poco, poca, mucho, mucha, muy.
• Adjetivos: rápido, rápidos, grande, grandes, verde,
pequeño, pequeños

diccionario = {
    'nombres': {
        'femeninos': {['Elsa', 'María', 'Caren', 'Lucia']},
        'masculinos': {['Lucas', 'José', 'Luis', 'Darío', 'Julián']}
    },
    'articulos': {
        'femeninos': {'singular': ['la', 'una'], 'plural': ['las, unas']},
        'masculinos': {'singular': ['el', 'uno'], 'plural': ['los', 'unos']},
    }
}

sustantivos = {
    0: {
        'nombre': 'perro',
        'genero': 'masculino',
        'cantidad': 'singular'
    },
    1: {
        'nombre': 'perra',
        'genero': 'femenino',
        'cantidad': 'singular'
    },
    2: {
        'nombre': 'perros',
        'genero': 'masculino',
        'cantidad': 'plural'
    },
    3: {
        'nombre': 'perras',
        'genero': 'femenino',
        'cantidad': 'plural'
    }
}
