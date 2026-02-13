===================================================
Datos de entrada
===================================================

La :numref:`table_agro_uscuss_inputs_old` muestra los paquetes de datos históricos considerados en los
procesos de modelado del sector Agricultura y USCUSS

.. _table_agro_uscuss_inputs_old:
.. table:: Comparación de datos históricos y actuales de la producción agropecuaria (PLANMICC vs. NDC) empleados en el modelo.

   +--------------+-----------------------+---------------+---------------+
   | Tipo de      | Descripción           | Fuente NDC    | Fuente Plan   |
   | Información  |                       |               | MICC          |
   +==============+=======================+===============+===============+
   | Datos de     | Banano [ton]          | Datos de      | ESPAC         |
   | actividad    |                       | actividad     |               |
   |              | Cacao - Almendra seca | usados para   |               |
   | Producción   | [ton]                 | la            |               |
   | Cultivos     |                       | construcción  |               |
   | cosechados:  | Café - Grano Oro      | de            |               |
   |              | [ton]                 | inventarios   |               |
   |              |                       | nacionales de |               |
   |              | Caña de azúcar [ton]  | gases de      |               |
   |              |                       | efecto        |               |
   |              | Maíz [ton]            | invernadero   |               |
   |              |                       | serie         |               |
   |              | Palma africana [ton]  | 1994-2021     |               |
   |              |                       | 5CN/1BTR,     |               |
   |              | Soya [ton]            | directrices   |               |
   |              |                       | ipcc 2006     |               |
   |              | Palmito [ha]          | refinamiento  |               |
   |              |                       | 2019          |               |
   |              | Legumbres (Pulses)    |               |               |
   |              | [ton]                 |               |               |
   |              |                       |               |               |
   |              | Cereales y            |               |               |
   |              | pseudocereales [ton]  |               |               |
   |              |                       |               |               |
   |              | Tubérculos [ton]      |               |               |
   |              |                       |               |               |
   |              | Fruta fresca [ton]    |               |               |
   |              |                       |               |               |
   |              | Verduras [ton]        |               |               |
   +--------------+-----------------------+---------------+---------------+
   | Datos de     | Banano [ton/ha]       | Datos de      | ESPAC         |
   | actividad    |                       | actividad     |               |
   |              | Cacao - Almendra seca | usados para   |               |
   | Rendimientos | [ton/ha]              | la            |               |
   | de Cultivos  |                       | construcción  |               |
   | Agrícolas    | Café - Grano Oro      | de            |               |
   | Cosechados   | [ton/ha]              | inventarios   |               |
   |              |                       | nacionales de |               |
   |              | Caña de azúcar        | gases de      |               |
   |              | [ton/ha]              | efecto        |               |
   |              |                       | invernadero   |               |
   |              | Maíz [ton/ha]         | serie         |               |
   |              |                       | 1994-2021     |               |
   |              | Palma africana (Fruta | 5CN/1BTR,     |               |
   |              | Fresca) [ton/ha]      | directrices   |               |
   |              |                       | ipcc 2006     |               |
   |              | Soya [ton/ha]         | refinamiento  |               |
   |              |                       | 2019          |               |
   |              | Palmito [ton/ha]      |               |               |
   |              |                       |               |               |
   |              | Legumbres (Pulses)    |               |               |
   |              | [ton/ha]              |               |               |
   |              |                       |               |               |
   |              | Cereales y            |               |               |
   |              | pseudocereales        |               |               |
   |              | [ton/ha]              |               |               |
   |              |                       |               |               |
   |              | Tubérculos [ton/ha]   |               |               |
   |              |                       |               |               |
   |              | Fruta fresca [ton/ha] |               |               |
   |              |                       |               |               |
   |              | Verduras [ton/ha]     |               |               |
   |              |                       |               |               |
   |              | Florícola [ton/ha]    |               |               |
   +--------------+-----------------------+---------------+---------------+
   | Datos de     | Misma clasificación   | BCE           | BCE           |
   | actividad    | de producción y       |               |               |
   |              | rendimiento de        | Proyecciones  | Proyecciones  |
   | Exportación  | Cultivos Agrícolas    |               | PLANMICC      |
   | e            |                       | PLANMICC      |               |
   | importación  | [Mton]                |               |               |
   | de Productos |                       |               |               |
   |              |                       |               |               |
   | Agrícolas    |                       |               |               |
   +--------------+-----------------------+---------------+---------------+
   | Datos de     | Misma clasificación   | Proyección    | Datos y       |
   | actividad    | de producción y       | calculados en | Proyección    |
   |              | rendimiento de        | PLANMICC      | calculados en |
   | Demanda      | Cultivos Agrícolas    |               | PLANMICC      |
   | Local de     |                       |               |               |
   | Productos    | [Mton]                |               | Producción    |
   | Agrícolas    |                       |               |               |
   |              |                       |               | + Importación |
   |              |                       |               |               |
   |              |                       |               | - Exportación |
   +--------------+-----------------------+---------------+---------------+
   | Datos de     | Vacuno total          | ESPAC         | ESPAC         |
   | actividad    | (Cabezas)             |               |               |
   |              |                       |               | MAG           |
   | Población de | Raza importada        |               | (Agrocalidad) |
   | ganado       | (Cabezas)             |               |               |
   | bobino       |                       |               |               |
   |              | Raza criolla          |               |               |
   |              | (Cabezas)             |               |               |
   |              |                       |               |               |
   |              | Raza mestiza          |               |               |
   |              | (Cabezas)             |               |               |
   |              |                       |               |               |
   |              | porcino (Cabezas)     |               |               |
   |              |                       |               |               |
   |              | ovino (Cabezas)       |               |               |
   |              |                       |               |               |
   |              | otras especies        |               |               |
   |              | (Cabezas)             |               |               |
   +--------------+-----------------------+---------------+---------------+
   | Datos de     | Vacuno carne (ton)    | BCE           | BCE           |
   | actividad    |                       |               |               |
   |              | Vacuno leche (ton)    |               |               |
   | Producción,  |                       |               |               |
   | Exportación, |                       |               |               |
   |              |                       |               |               |
   | Importación  |                       |               |               |
   | de ganado    |                       |               |               |
   +--------------+-----------------------+---------------+---------------+
   | Datos de     | campo (Cabezas)       | ESPAC         | ESPAC         |
   | actividad    |                       |               |               |
   |              | planteles avícolas    |               |               |
   | Aves de      | (Cabezas)             |               |               |
   | corral       |                       |               |               |
   |              | Huevos (# huevos)     |               |               |
   | Producción,  |                       |               |               |
   | consumo      | Huevos autoconsumo (# |               |               |
   |              | huevos)               |               |               |
   +--------------+-----------------------+---------------+---------------+

La :numref:`table_agro_uscuss_inputs_new` muestra los datos históricos y actuales utilizados en el
modelado para los 2 sectores

.. _table_agro_uscuss_inputs_new:
.. table:: Datos históricos y actuales de coberturas.

   +------------+---------------------------+---------------+---------------+
   | Aspecto    | Descripción               | Fuente NDC    | Fuente Plan   |
   |            |                           |               | MICC          |
   +============+===========================+===============+===============+
   | Datos de   | B. Seco Pluvioestacional  | "Datos        | “Datos        |
   | actividad  |                           | 2010-2022     | 2010-2018 4ta |
   |            | B. Siempre verde andino   |               | Comunicación” |
   | Cobertura  | Montano                   | 5ta           |               |
   | de Bosque  |                           | Comunicación" | Se separan 2  |
   |            | B. Siempre verde andino   |               | categorías:   |
   |            | Pie montano               | Cada          |               |
   |            |                           | categoría de  | Bosque nativo |
   |            | B. Siempre verde andino   | bosque es     | [ha]          |
   |            | de Ceja Andina            | analizada de  |               |
   |            |                           | manera        | Plantación    |
   |            | B. Siempre verde de       | individual    | forestal [ha] |
   |            | tierras bajas de la       |               |               |
   |            | Amazonía                  |               |               |
   |            |                           |               |               |
   |            | B. Siempre verde de       |               |               |
   |            | tierras bajas del Chocó   |               |               |
   |            |                           |               |               |
   |            | Manglar                   |               |               |
   |            |                           |               |               |
   |            | Moretal                   |               |               |
   |            |                           |               |               |
   |            | Plantación forestal       |               |               |
   +------------+---------------------------+---------------+---------------+
   | Datos de   | Bosque nativo no          | "Datos        | “Datos        |
   | actividad  | protegido [Mha]           | 2010-2022     | 2010-2018 4ta |
   |            |                           |               | Comunicación” |
   | Cobertura  | Bosque nativo bajo        | 5ta           |               |
   | de Bosque  | régimen de proteccion     | Comunicación” |               |
   |            | legal [Mha]               |               |               |
   | Protegido  |                           |               |               |
   | / No       |                           |               |               |
   | protegido  |                           |               |               |
   +------------+---------------------------+---------------+---------------+
   | Datos de   | Cultivo anual [ha]        | "Datos        | "Datos        |
   | actividad  |                           | 2010-2022     | 2010-2018     |
   |            | Cultivo semipermanente    |               |               |
   | Tierras de | [ha]                      | 5ta           | 4ta           |
   | Cultivo    |                           | Comunicación” | Comunicación” |
   |            | Cultivo permanente [ha]   |               |               |
   |            |                           | Analiza una   | Analiza dos   |
   |            | Pastura [ha]              | sola          | categorías:   |
   |            |                           | categoría:    |               |
   |            | Mosaico agropecuario [ha] |               | Cultivos      |
   |            |                           | Tierras de    | [Mha]         |
   |            |                           | cultivo [Mha] |               |
   |            |                           |               | Pastura [Mha] |
   +------------+---------------------------+---------------+---------------+
   | Datos de   | Pastizales (grasslands)   | "Datos        | "Datos        |
   | actividad  |                           | 2010-2022     | 2010-2018     |
   |            | Humedal                   |               |               |
   | Otras      |                           | 5ta           | 4ta           |
   | coberturas | Zona antrópica            | Comunicación” | Comunicación” |
   |            | (Asentamientos)           |               |               |
   |            |                           |               |               |
   |            | Otras tierras             |               |               |
   +------------+---------------------------+---------------+---------------+

Para acceder a la versión completa de los datos de entrada del sector,
descargue el archivo de datos del sector Agricultura y USCUSS aquí: :download:`Modelo Agricultura USCUSS Plan de Acción <../_static/docs/Modelo Agricultura USCUSS Plan de Acción.xlsx>`
