===================================================
Datos de entrada
===================================================

En la :numref:`table_waste_inputs` se presentan las fuentes de información que fueron
utilizadas para la satisfacción de datos de los parámetros del modelo
del sector Residuos.

.. _table_waste_inputs:
.. table:: Fuentes de información para parametrizar el sector Residuos.

   +------+---------------------------+-----------------------------------+
   | Ítem | Información requerida     | Fuente de Información             |
   +======+===========================+===================================+
   | 1    | Proyección de la          | INEC 2024.                        |
   |      | población                 |                                   |
   +------+---------------------------+-----------------------------------+
   | 2    | Producción per cápita     | PPC del modelo de NDC.            |
   |      | (PPC)                     |                                   |
   +------+---------------------------+-----------------------------------+
   | 3    | Generación de residuos    | Calculado en base a la población  |
   |      | sólidos                   | y la PCC                          |
   +------+---------------------------+-----------------------------------+
   | 4    | Caracterización de los    | La información para el período    |
   |      | residuos sólidos          | 2014–2023 se tomó de los          |
   |      |                           | Boletines de Estadística de       |
   |      |                           | Información Ambiental Económica   |
   |      |                           | en Gobiernos Autónomos            |
   |      |                           | Descentralizados Municipales del  |
   |      |                           | INEC, mientras que para el        |
   |      |                           | período 2010–2013 provino del     |
   |      |                           | Censo de Información Ambiental    |
   |      |                           | Económica en Gobiernos Autónomos  |
   |      |                           | Descentralizados Municipales del  |
   |      |                           | INEC                              |
   +------+---------------------------+-----------------------------------+
   | 5    | Porcentaje de Recolección | Período 2014–2023 se consideran   |
   |      | diferenciada              | los Boletines de Estadística de   |
   |      |                           | Información Ambiental Económica   |
   |      |                           | en Gobiernos Autónomos            |
   |      |                           | Descentralizados Municipales del  |
   |      |                           | INEC, mientras que para el        |
   |      |                           | período 2010–2013 provino del     |
   |      |                           | Censo de Información Ambiental    |
   |      |                           | Económica en Gobiernos Autónomos  |
   |      |                           | Descentralizados                  |
   +------+---------------------------+-----------------------------------+
   | 6    | Porcentaje de residuos    | Período 2014–2023 se consideran   |
   |      | que va a un sitio de      | de los Boletines de Estadística   |
   |      | disposición final         | de Información Ambiental          |
   |      |                           | Económica en Gobiernos Autónomos  |
   |      |                           | Descentralizados Municipales del  |
   |      |                           | INEC, mientras que para el        |
   |      |                           | período 2010–2013 provino del     |
   |      |                           | Censo de Información Ambiental    |
   |      |                           | Económica en Gobiernos Autónomos  |
   |      |                           | Descentralizados                  |
   +------+---------------------------+-----------------------------------+
   | 7    | Generación de aguas       | Período 2014–2023 se consideran   |
   |      | residuales y su           | los Boletines de Estadística de   |
   |      | distribución              | Información Ambiental Económica   |
   |      |                           | en Gobiernos Autónomos            |
   |      |                           | Descentralizados Municipales del  |
   |      |                           | INEC, sección de Gestión de Agua  |
   |      |                           | Potable y Saneamiento mientras    |
   |      |                           | que para el período 2010–2013     |
   |      |                           | provino del Censo de Información  |
   |      |                           | Ambiental Económica en Gobiernos  |
   |      |                           | Autónomos Descentralizados        |
   +------+---------------------------+-----------------------------------+

Los parámetros considerados en el proceso de modelado y los supuestos
empleados para la generación del Escenario Tendencial Nacional, se
describen en la :numref:`table_waste_inputs_params`.

.. _table_waste_inputs_params:
.. table:: Parámetros y supuestos considerados en el proceso de modelado del Escenario Tendencial Nacional del sector Residuos.

   +--------+-------------------------------+--------------------------------+
   | Ít     | Parámetros de modelación      | Supuestos                      |
   | em     |                               |                                |
   +========+===============================+================================+
   | 1      | Generación total de residuos  | Calculada en función de la     |
   |        | sólidos                       | población proyectada y la      |
   |        |                               | producción per cápita (PPC)    |
   |        |                               | ajustada.                      |
   +--------+-------------------------------+--------------------------------+
   | 2      | Producción per cápita (PPC)   | Se adopta la PPC utilizada en  |
   |        |                               | el modelo de la Segunda NDC.   |
   +--------+-------------------------------+--------------------------------+
   | 3      | Composición de fracciones     | Caracterización basada en el   |
   |        | orgánicas e inorgánicas       | Censo de Información Ambiental |
   |        |                               | Económica (2010–2013) y los    |
   |        |                               | Boletines de Estadística       |
   |        |                               | Ambiental Económica            |
   |        |                               | (2014–2023) del INEC.          |
   +--------+-------------------------------+--------------------------------+
   | 4      | Porcentaje de recolección     | Supuesto: lo separado en la    |
   |        | diferenciada                  | fuente equivale a lo           |
   |        |                               | recolectado diferenciadamente. |
   +--------+-------------------------------+--------------------------------+
   | 5      | Gestión y disposición final   | Distribución elaborada con     |
   |        | (rellenos, botaderos, celdas  | información del INEC y Censo   |
   |        | emergentes)                   | Ambiental Económico de los     |
   |        |                               | GAD.                           |
   +--------+-------------------------------+--------------------------------+
   | 6      | Tratamiento y valorización    | Se considera que el 50 % de    |
   |        | (compostaje, reciclaje,       | los residuos orgánicos         |
   |        | lombricultura)                | diferenciados se aprovecha y   |
   |        |                               | el 10 % de los inorgánicos     |
   |        |                               | reciclables se recicla         |
   |        |                               | efectivamente.                 |
   +--------+-------------------------------+--------------------------------+
   | 7      | Generación de aguas           | Se consideran tres rutas:      |
   |        | residuales                    | vertimientos directos, tanques |
   |        |                               | sépticos y alcantarillado con  |
   |        |                               | o sin PTAR.                    |
   +--------+-------------------------------+--------------------------------+
   | 8      | Cobertura y tipo de           | Datos provenientes de los      |
   |        | tratamiento de aguas          | Boletines de Estadística       |
   |        | residuales                    | Ambiental Económica del INEC   |
   |        |                               | (2014–2023).                   |
   +--------+-------------------------------+--------------------------------+
   | 9      | Factores de emisión           | Definidos según las            |
   |        |                               | Directrices del IPCC (2006) y  |
   |        |                               | calibrados con el Inventario   |
   |        |                               | Nacional de GEI 2022 y su      |
   |        |                               | serie histórica.               |
   +--------+-------------------------------+--------------------------------+
   | 10     | Calibración del modelo        | Escenario ajustado para        |
   |        |                               | garantizar consistencia        |
   |        |                               | metodológica y comparabilidad  |
   |        |                               | entre instrumentos nacionales. |
   +--------+-------------------------------+--------------------------------+

Para acceder a la versión completa de los datos de entrada del sector,
descargue el archivo de datos del sector Residuos aquí: :download:`Modelo Residuos Plan de Acción <../_static/docs/Modelo Residuos Plan de Acción.xlsx>`
