timemachine(1) -- Un sistema de copia de seguridad basado en Btrfs
==================================================================

## SINOPSIS

`timemachine` [*OPCIÓN*...]

## DESCRIPCIÓN


`timemachine` es un sistema de copia de seguridad basado en la capacidad del sistema de archivos Btrfs de realizar capturas instantáneas de subvolúmenes.

Cuando `timemachine` es ejecutado sin opciones leerá el archivo de configuración situado en `/etc/timemachine.ini` y realizará copias de los directorios indicados allí. Simultáneamente también eliminará las copias más antiguas que excedan la cuota establecida.

En el archivo de configuración se establece de qué directorios se hará copia y dónde se almacenará dicha copia, además de otros parámetros como la frecuencia y la cantidad máxima de copias permitidas para cada directorio. Recomiendo encarecidamente leer más acerca del formato del archivo de configuración en timemachine(5).

Además de la configuración establecida en dicho archivo, `timemachine` admite algunos parámetros por línea de órdenes. Estos parámetros tienen precedencia sobre lo escrito en el archivo de configuración. Incluso hay parámetros que realizan acciones que no están disponibles a través del archivo de configuración.

Hay algunos archivos de configuración disponibles como ejemplo en `/usr/share/timemachine/examples`. Adapte cualquiera de ellos a las necesidades de su sistema, si lo considera más cómodo.


`timemachine` está principalmente pensado para ser ejecutado periódicamente, ya sea por sí mismo (modo daemon) o por otro agente como, por ejemplo,  `systemd` o `cron`.


## EJECUCIÓN CON SYSTEMD

Para que funcione con systemd(1) es necesario instalar timemachine.service y timemachine.timer en `/etc/systemd/system` e iniciar y habilitar dicho servicio.

El instalador proporcionado con el paquete del desarrollador no iniciará ni habilitará la ejecución periódica.


## EJECUCIÓN CON CRON

Para que funcione con cron(1) debe añadir la entrada correspondiente en `/etc/crontab`. Quizá desee parar y deshabilitar el timer de systemd.


## EJECUCIÓN EN MODO DEMON *(Función no implementada todavía)*

Ejecute timemachine con la opción `-d` o `--daemon`. Vea más acerca de esta opción en la sección [OPCIONES]


## OPCIONES

Éstas son las opciones disponibles a través de la línea de comandos.

**Advertencia:** *No todas están implementadas en esta versión del programa*.

* `-c`, `--config`=[<file>]:
    Indica que se usará *file* como archivo de configuración en lugar del predeterminado `/etc/timemachine.ini`.

* `-d`, `--daemon`=[<time>]:
    Inicia `timemachine`  en modo demonio (servicio del sistema). El valor *time* es requerido para indicar la periodicidad en que se comprueba el archivo de configuración y se realizan las copias según lo establecido en él.

* `-D`, `--directories`=[<dir1> <dir2> ...]:
    Indica que los directorios de los que se hará la copia de seguridad son <dir1> <dir2> . Esto implica que se debe especificar la frecuencia, la cuota y el almacén a través de la línea de órdenes con las opciones `-F`, `-Q` y `-S` respectivamente.

* `-f`, `--find`=[<file>]:
    Encuentra todas las versiones de *file* almacenadas en los directorios de copia establecidos en la configuración.

* `-F --frequence`=[<freq>]:
    Indica una frecuencia de copia *freq* para todas los directorios de la configuración. Esto implica que se puede forzar una copia aunque no toque hacerlo.

* `-n`, `--dryrun`
    No realiza ningún cambio en el disco. Pero muestra la salida de texto como si se hubiese realizado algo.

* `-p`, `--purge`=[<file>]:
    Borra todas las versiones de *file* en el almacén. Se mantendrá el original.

* `-P`, `--Purge`=[<file>]:
    Borra el original *file* y todas sus versiones en el almacén. El archivo desaparecerá del sistema.

* `-q`, `--quiet`:
    Modo silencioso. No información alguna por la salida estándar.

* `-Q`, `--quota`=[<quota>]:
    Indica una cuota general. Tiene las mismas implicaciones que `-F`.

* `-r`, `--readonly`:
    Todas las copias serán hechas en modo de sólo lectura.

* `-S`, `--store`=[<directory>]:
    Indica un directorio de almacén general.

* `-u`, `--update`=[<file>][<time>]:
    Actualiza *file* con su versión más reciente en el almacén. Si se
    especifica *time* se actualizará con la copia más reciente desde *time*.

* `-v`, `--verbose`:
    Se mostrará información extra por la salida estándar.


## VALORES DE RETORNO


## FICHEROS
`/etc/timemachine.ini`
    Fichero de configuración. Establece todo lo relativo a las copias de seguridad.
`/etc/systemd/system/timemachine.service`
    El servicio de systemd. Será ejecutado periódicamente por `timemachine.timer`.
`/etc/systemd/system/timemachine.timer`
    El temporizador de systemd. Ejecutará periódicamente `timemachine.service`.


## HISTORY
La idea surgió inspirada en el programa TimeMachine propio del sistema Mac OS X. No obstante, no tienen el menor parecido.


## AUTOR

Esta página del manual ha sido escrita por el autor original del programa. Manuel Domínguez López.


## FALLOS
Por favor, si encuentras alguno, házmelo saber.


## COPYRIGHT
GPLv3


## VER TAMBIÉN

timemachine(5)

