timemachine(5) -- Fichero de configuración de timemachine
=========================================================

## UBICACIÓN

`/etc/timemachine.ini`

## DESCRIPCIÓN

`timemachine` es un sistema de copia de seguridad basado en la capacidad del sistema de archivos Btrfs de realizar capturas instantáneas de subvolúmenes.

Cuando `timemachine` es ejecutado sin opciones leerá el archivo de configuración situado en `/etc/timemachine.ini` y realizará copias de los directorios indicados allí. Simultáneamente también eliminará las copias más antiguas que excedan la cuota establecida.

En el archivo de configuración se establece de qué directorios se hará copia y dónde se almacenará dicha copia, además de otros parámetros como la frecuencia y la cantidad máxima de copias permitidas para cada directorio.


## FORMATO

El archivo de configuración está escrito en formato `ini`, que será interpretado por el módulo `parseconfig` de `python3`.

El archivo está divido en secciones. Las secciones son líneas entre corchetes, como por ejemplo: `[datos]`. Las secciones representan una unidad de copia y configuran individualmente las copias que se hacen de determinado subvolumen, al que hacen referencia. El nombre de la sección será usado para nombrar a la copia. Vea más adelante la opción `directories` en [OPCIONES DE SECCIÓN].

Debe existir una sección especial, de nombre `[DEFAULT]`, que no representa a ninguna unidad de copia, sino que sólo sirve para que todas las demás unidades tomen sus opciones por defecto de ella.

Las opciones que pueda tomar una sección son los siguientes. Si se omite alguna, se tomará de la sección `[DEFAULT]`.


## OPCIONES DE SECCIÓN

`store` El almacén donde serán guardadas las copias. Debe representar un directorio. Si este directorio no existiese se crearía al almacenar alguna copia.

`subvolume` Ruta completa al subvolumen a copiar. Debe indicar un subvolumen Btrfs. Si no existe generaría un error.

`directories` Directorios donde se guardarán las copias individualmente. El valor de esta opción tiene un formato especial `nombre_del_directorio:edad_minima[m|h|d|y]:cuota_máxima`, donde hay tres campos separados por el símbolo de dos puntos `:`.

El primer campo indica el nombre del directorio, que será ubicado en `store/nombre_de_la_sección/nombre_del_directorio`.

El segundo campo establece la edad mínima de las copias. Esto se refiere a la edad mínima que debe tener la copia más moderna que allí se encuentre. Si se fuera a guardar una nueva copia en el directorio anteriormente referido, pero la copia más moderna que allí se encotrara no superase esta edad mínima, no se realizaría la copia pretendida. La edad estará por defecto expresada en segundos. No obstante, puede ser expresada en minutos, horas, días o años; añadiendo `m`, `h`, `d` ó `y`, respectivamente.

El tercer campo establece la cuota máxima. Esto se refiere a la cantidad máxima de copias que se pueden almacenar en `store/sección/nombre/`. Si se fuera a guardar una nueva copia en el directorio anteriormente referido, pero hubiese un número de copias igual al de la cuota, se eliminarían todas las copias más antiguas que excedan el cupo.

`readonly` Admite valores booleanos para establecer si la copia será de sólo lectura. Para que la copia sea de sólo lectura hay que asignar `true`.

`ignore` Admite valores booleanos. Si se establece a `true` no se harán copias de esta unidad de copia.


## AUTOR

Esta página del manual ha sido escrita por el autor original del programa. Manuel Domínguez López.


## FALLOS
Por favor, si encuentras alguno, házmelo saber.


## COPYRIGHT
GPLv3


## VER TAMBIÉN

timemachine(1)

