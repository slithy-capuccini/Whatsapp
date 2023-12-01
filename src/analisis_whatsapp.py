from datetime import datetime, timedelta
import re
from collections import namedtuple, Counter, defaultdict
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import math
from typing import List, Dict, NamedTuple, Optional, Tuple

SO = "android"

ANDROID_RE = r'(\d\d?/\d\d?/\d\d?), (\d\d?:\d\d) - ([^:]+): (.+)'
IOS_RE = r'\[(\d\d?/\d\d?/\d\d?) (\d\d?:\d\d):\d\d\] ([^:]+): (.+)'

Mensaje = NamedTuple('Mensaje', [('fecha', datetime.date), ('hora', datetime.time), ('usuario', str), ('texto', str)])

# Esta función se da implementada
def carga_log(fichero: str, os: str = SO, debug: bool = False) -> List[Mensaje]:
    '''
    Carga un log de Whatsapp, devolviéndolo como lista de tuplas.

    :param fichero: Nombre del fichero del que se quieren leer los datos
    :type fichero: str
    :param os: Tipo de sistema operativo del log, por defecto 'android'
    :type os: str
    :param debug: Indica si se desea obtener información sobre la carga, por defecto False
    :type debug: bool
    :return: Lista de mensajes
    :rtype: List[Mensaje]

    Si el parámetro debug es True se mostrarán los usuarios y el intervalo de 
    fechas procesado. Por ejemplo: 
        3779 mensajes leídos.
        Usuarios: {'Penny', 'Sheldon', 'Howard', 'Raj', 'Lesley', 'Leonard'}
        Intervalo de fechas: 2016-02-25 -> 2017-03-04
    
    La función devuelve una lista de tuplas, cada una de ellas conteniendo la fecha,
    la hora, el usuario y el texto de un mensaje. El orden de las tuplas en la lista
    es el mismo que el que aparece en el fichero, es decir, cronológico.
    '''
    if os=='android':
        regex = ANDROID_RE
    elif os=='ios':
        regex = IOS_RE
    else:
        raise Exception('OS no permitido') # Lanza una excepción
        
    log = []
    with open(fichero, encoding='utf8') as f:        
        for linea in f:
            # Aplicamos la expresión regular sobre cada línea
            matches = re.findall(regex, linea)
            if matches:  # Si se encuentran coincidencias para los patrones
                fecha_str, hora_str, usuario, texto = matches[0]
                fecha = datetime.strptime(fecha_str, '%d/%m/%y').date()
                hora = datetime.strptime(hora_str, '%H:%M').time()
                log.append(Mensaje(fecha,hora,usuario, texto))
            
    return log

def calcula_usuarios(log: List[Mensaje]) -> List[str]:
    '''
    Devuelve una lista ordenada con los usuarios que aparecen en el log, sin duplicados.

    :param log: Lista de mensajes
    :type log: List[Mensaje]
    :return: Lista de usuarios
    :rtype: List[str]
    '''
    pass

def cuenta_mensajes_por_usuario(log: List[Mensaje]) -> Dict[str, int]:
    '''
    Devuelve un diccionario en el que las claves son los usuarios y los valores son el número de mensajes de cada usuario.

    :param log: Lista de mensajes
    :type log: List[Mensaje]
    :return: Diccionario de número de mensajes por usuario
    :rtype: Dict[str, int]
    '''
    pass

def muestra_numero_mensajes_por_usuario(log: List[Mensaje]) -> None:
    '''
    Muestra una gráfica de barras indicando el número de mensajes por cada usuario.

    :param log: Lista de mensajes
    :type log: List[Mensaje]

    Esta función no retorna ningún valor, pero muestra en pantalla un diagrama de barras
    con el número de mensajes enviados por cada usuario que aparece en el log.
    '''
    # TODO: Construya las listas usuarios y num_mensajes, que contengan
    # respectivamente los usuarios que aparecen en log y el número de 
    # mensajes de cada uno de ellos. Se aconseja que la lista de usuarios
    # aparezca ordenada alfabéticamente
    usuarios = None # TODO
    num_mensajes = None # TODO

    plt.barh(usuarios, num_mensajes)
    plt.show()

def cuenta_mensajes_por_meses(log: List[Mensaje]) -> Dict[str, int]:
    '''
    Devuelve un diccionario en el que las claves son los meses a lo largo de los años 
    (por ejemplo, "2/2016", "3/2016",...) y los valores son el número de mensajes de cada mes/año.

    :param log: Lista de mensajes
    :type log: List[Mensaje]
    :return: Diccionario de número de mensajes por mes/año
    :rtype: Dict[str, int]
    '''
    pass

def cuenta_mensajes_por_dia_semana(log: List[Mensaje]) -> Dict[str, int]:
    '''
    Devuelve un diccionario en el que las claves son los días de la semana 
    ("L", "M", "X", "J", "V", "S" y "D") y los valores son el número de mensajes de cada día.
    Usa el método weekday() del tipo date para determinar el día de la semana.

    :param log: Lista de mensajes
    :type log: List[Mensaje]
    :return: Diccionario de número de mensajes por día de la semana
    :rtype: Dict[str, int]
    '''
    pass

def cuenta_mensajes_por_momento_del_dia(log: List[Mensaje]) -> Dict[str, int]:
    '''
    Devuelve un diccionario en el que las claves son los momentos del día 
    ("MAÑANA", "TARDE", "NOCHE") y los valores son el número de mensajes de cada momento.
    Los momentos del día se definen como:
    - "MAÑANA": de 7 a 13 horas
    - "TARDE": de 14 a 20 horas
    - "NOCHE": de 21 a 6 horas

    :param log: Lista de mensajes
    :type log: List[Mensaje]
    :return: Diccionario de número de mensajes para cada momento del día
    :rtype: Dict[str, int]
    '''
    pass
   
def calcula_media_horas_entre_mensajes(log: List[Mensaje]) -> float:
    '''
    Devuelve la media de horas entre mensajes consecutivos en el tiempo.

    Para combinar una fecha y una hora en un solo objeto datetime, se utiliza la función datetime.combine.
    Para calcular el número de horas entre dos objetos datetime d1 y d2, se utiliza la expresión: 
    (d1-d2).total_seconds() / 3600

    :param log: Lista de mensajes
    :type log: List[Mensaje]
    :return: Media de horas entre mensajes consecutivos
    :rtype: float
    '''
    pass
   
def genera_conteos_palabras_usuario_y_resto(log: List[Mensaje], usuario: str) -> Tuple[Dict[str, int], Dict[str, int]]:
    '''
    Genera dos diccionarios, uno con el conteo de las palabras usadas por el usuario,
    y otro con el conteo de palabras usadas por el resto de usuarios.

    :param log: Lista de mensajes
    :type log: List[Mensaje]
    :param usuario: Usuario específico para el conteo de palabras
    :type usuario: str
    :return: Tupla conteniendo dos diccionarios, uno para el usuario y otro para el resto
    :rtype: Tuple[Dict[str, int], Dict[str, int]]

    Para dividir el texto en palabras, se usa split. Para cada palabra,
    se utiliza la instrucción palabra.strip(".,:();¿?¡!") para eliminar signos de puntuación.
    '''
    pass

def genera_palabras_caracteristicas_usuario(log: List[Mensaje], usuario: str, umbral: int = 2) -> Dict[str, float]:
    '''
    Genera un diccionario con la importancia de las palabras usadas por un usuario.

    :param log: Lista de mensajes
    :type log: List[Mensaje]
    :param usuario: Usuario del que se calculará la importancia de las palabras
    :type usuario: str
    :param umbral: Frecuencia mínima para tener en cuenta una palabra, por defecto 2
    :type umbral: int
    :return: Diccionario de importancia de las palabras del usuario
    :rtype: Dict[str, float]

    El diccionario contiene palabras con su respectiva importancia, calculada en base 
    a su frecuencia de uso por el usuario indicado, considerando solo aquellas palabras 
    con una frecuencia igual o superior al umbral especificado.
    '''
    pass


# Esta función se da implementada
def muestra_word_cloud(log: List[Mensaje], usuario: str, max_words: int = 150) -> None:
    '''
    Muestra una word cloud (nube de palabras) para un usuario específico a partir de un log de mensajes.

    :param log: Lista de mensajes
    :type log: List[Mensaje]
    :param usuario: Usuario específico para generar la word cloud
    :type usuario: str
    :param max_words: Número máximo de palabras a mostrar en la word cloud, por defecto 150
    :type max_words: int
    '''
    dicc_palabras_caracteristicas = genera_palabras_caracteristicas_usuario(log, usuario)
    wordcloud = WordCloud(
                        font_path='data/seguiemj.ttf',                        
                        background_color='white',
                        width=1800,
                        height=1400,
                        normalize_plurals=False,
                        max_words=max_words
                        ).generate_from_frequencies(dicc_palabras_caracteristicas)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()


# Esta función se da implementada
def genera_informe(log: List[Mensaje], titulo: str = "Informe", usuario: Optional[str] = None) -> None:
    '''
    Muestra un conjunto de gráficas, incluyendo:
     - La evolución del número de mensajes mensualmente.
     - El número de mensajes agregados por día de la semana.
     - El número de mensajes agregados por momento del día.

    Si el parámetro usuario no es None, sólo se usarán los mensajes del usuario indicado 
    para generar el informe.

    :param log: Lista de mensajes
    :type log: List[Mensaje]
    :param titulo: Título del informe, por defecto "Informe"
    :type titulo: str
    :param usuario: Usuario específico para filtrar los mensajes, por defecto None
    :type usuario: Optional[str]
    '''    
    if usuario != None:
        log = [m for m in log if m.usuario == usuario]

    mensajes_por_meses = cuenta_mensajes_por_meses(log)
    meses, num_mensajes_por_meses = zip(*mensajes_por_meses.items())

    mensajes_por_dia = cuenta_mensajes_por_dia_semana(log)
    etiquetas_dias = ['L', 'M', 'X', 'J', 'V', 'S', 'D']
    num_mensajes_por_dias = [mensajes_por_dia[dia] for dia in etiquetas_dias]

    mensajes_por_momento = cuenta_mensajes_por_momento_del_dia(log)
    etiquetas_momentos = ["MAÑANA", "TARDE", "NOCHE"]
    num_mensajes_por_momento = [mensajes_por_momento[momento] for momento in etiquetas_momentos]

    fig, axs = plt.subplots(3)
    fig.suptitle(titulo+f"\nMedia de horas entre mensajes: {calcula_media_horas_entre_mensajes(log):.2f}")       
    
    axs[0].plot(meses, num_mensajes_por_meses)
    axs[0].set_xticklabels(meses, rotation=60, fontsize=10)   
    axs[0].set_title('Evolución mensajes por meses')

    
    axs[1].bar(etiquetas_dias, num_mensajes_por_dias)        
    axs[1].set_title('Mensajes por día de la semana')

    aux = cuenta_mensajes_por_momento_del_dia(log)
    etiquetas = ["MAÑANA", "TARDE", "NOCHE"]

    axs[2].bar(etiquetas_momentos, num_mensajes_por_momento)    
    axs[2].set_title('Mensajes por momento del día')

    plt.tight_layout()    
    plt.show()