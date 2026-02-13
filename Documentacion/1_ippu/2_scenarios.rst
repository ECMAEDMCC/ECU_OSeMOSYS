===================================================
Escenarios
===================================================

Para el sector Procesos Industriales primeramente se construye un
escenario Tendencial. Este refleja la evolución natural de las emisiones
del sector Procesos Industriales bajo el supuesto de mantener las
prácticas habituales, sin la incorporación de medidas adicionales de
mitigación. Este escenario, es una representación homologada del
escenario tendencial del PLANMICC con la información contenida de la
segunda NDC.

Para la construcción del escenario Tendencial Nacional para el sector de
procesos industriales fue necesario realizar modificaciones en distintos
archivos de configuración de OSeMOSYS, con el fin de integrar
coherentemente los insumos de ambos modelos.

El segundo escenario es el escenario Plan de Acción (PAC), el cual
integra las iniciativas establecidas en la Segunda NDC del Ecuador
(condicional e incondicional) que aplican al sector Procesos
Industriales:

- Sustitución de clínker por adiciones en la producción de cemento.

- Reducción progresiva del consumo de HFC conforme a la Enmienda de
  Kigali, lo que impacta directamente en la categoría 2F (*Uso de
  productos como sustitutos de sustancias que agotan la capa de ozono*).

En la :numref:`table_ippu_scenarios` se detallan de mejor forma las iniciativas mencionadas.

.. _table_ippu_scenarios:
.. table:: Descripción de iniciativas del sector Procesos Industriales para el escenario Plan de Acción.

   +------+---------------------+------------+----------------+-------------------+-------------+
   | NRO. | DESCRIPCIÓN         | POTENCIAL  | AÑO DE         | TECNOLOGÍA        | META        |
   |      |                     | DE         | IMPLEMENTACIÓN | OSEMOSYS          | PLANMICC    |
   |      |                     | MITIGACIÓN |                |                   | -2035       |
   |      |                     | AL 2035    |                |                   |             |
   |      |                     | [KT        |                |                   |             |
   |      |                     | CO₂EQ/AÑO] |                |                   |             |
   +======+=====================+============+================+===================+=============+
   | 1    | Sustitución de      | 530.14     | 2026-2035      | PROD_CEM;CLK_PROD | P.1 Reducir |
   |      | clinker por         |            |                |                   | el factor   |
   |      | adiciones en la     |            |                |                   | clínker en  |
   |      | producción de       |            |                |                   | la          |
   |      | cemento             |            |                |                   | producción  |
   |      |                     |            |                |                   | de cemento  |
   |      |                     |            |                |                   | al 68%.     |
   +------+---------------------+------------+----------------+-------------------+-------------+
   | 2    | Reducir             | 635.8      | 2026-2035      | HFC_use           | P.2 Reducir |
   |      | progresivamente el  |            |                |                   | la          |
   |      | consumo de          |            |                |                   | importación |
   |      | hidrofluorocarbonos |            |                |                   | del 30% de  |
   |      | (HFC) y PFC en el   |            |                |                   | los HFC y   |
   |      | país conforme Hoja  |            |                |                   | PFC.        |
   |      | de Ruta para        |            |                |                   |             |
   |      | reducción los HFC   |            |                |                   |             |
   |      | en Ecuador, bajo la |            |                |                   |             |
   |      | enmienda de Kigali  |            |                |                   |             |
   |      | al protocolo de     |            |                |                   |             |
   |      | Montreal.           |            |                |                   |             |
   +------+---------------------+------------+----------------+-------------------+-------------+
   | 3    | Eliminación         | 1.00       | 2029-2035      | HFC_use           | P.2 Reducir |
   |      | progresiva de       |            |                |                   | la          |
   |      | compuestos que      |            |                |                   | importación |
   |      | contienen HFC y PFC |            |                |                   | del 30% de  |
   |      | contenidos en       |            |                |                   | los HFC y   |
   |      | equipos             |            |                |                   | PFC.        |
   +------+---------------------+------------+----------------+-------------------+-------------+
