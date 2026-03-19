===================================
Datos de Entrada
===================================

La Tabla :numref:`table_inputs_energy` presenta una síntesis de fuentes de información empleadas
para la construcción del Escenario Tendencial Nacional del sector
Energía. El proceso de modelado que da lugar al Escenario Tendencial
Nacional integra información proveniente tanto del PLANMICC como de la
Segunda NDC, garantizando consistencia con las Directrices del IPCC
(2006), su refinamiento de 2019 y el Inventario Nacional de GEI 2022 de
la 5CN2BTR


.. _table_inputs_energy:
.. table:: Fuentes de información utilizadas para el proceso de modelado del Escenario Tendencial Nacional del sector Energía

   +----------+---------------------------------+-------------------------------+
   |   Ítem   |   Información Utilizada         |   Fuente                      |
   +----------+---------------------------------+-------------------------------+
   | 1        | Tecnologías generadoras de      | ARCONEL 2022, Centro Nacional |
   |          | electricidad: fuente            | de Energía y Control          |
   |          | energética, capacidad instalada | (CENACE), Inventario Nacional |
   |          | (MW), factor de planta (%), año | de Gases de Efecto            |
   |          | de operación, energía generada  | Invernadero (INGEI de la 5ta  |
   |          | (GWh)                           | (1994-2022)                   |
   +----------+---------------------------------+-------------------------------+
   | 2        | Demanda de energía por fuente   | Balance de Energía Nacional   |
   |          | energética en el sector         | 202 4, INGEI (1994-2022)      |
   |          | industrial y construcción (TJ)  | (5CN/1RBT, 2024)              |
   +----------+---------------------------------+-------------------------------+
   | 3        | Demanda de energía por fuente   | Balance de Energía Nacional   |
   |          | energética por tipo de          | 2024, ANT, INGEI (1994-2022)  |
   |          | transporte: terrestre           |                               |
   |          | (pasajeros y carga), marítimo,  | (5CN/1RBT, 2024)              |
   |          | aéreo (TJ)                      |                               |
   +----------+---------------------------------+-------------------------------+
   | 4        | Demanda de energía por tipo de  | Balance de Energía Nacional   |
   |          | fuente energética en sectores   | 2024, INGEI de la 5ta         |
   |          | comercial, residencial,         | (1994-2022)                   |
   |          | servicios públicos,             |                               |
   |          | agricultura/pesca/minería (TJ)  | (5CN/1RBT, 2024)              |
   +----------+---------------------------------+-------------------------------+
   | 5        | Demanda de energía por tipo de  | Balance de Energía Nacional   |
   |          | fuente energética en otros      | 202 4, INGEI de la 5ta        |
   |          | sectores no clasificados (TJ)   | (1994-2022) (5CN/1RBT, 2024)  |
   +----------+---------------------------------+-------------------------------+
   | 6        | Producción de crudo de petróleo | EP PETROECUADOR, ARCH, INGEI  |
   |          | (barriles), gas natural (m³),   | de la 5ta (1994-2022)         |
   |          | emisiones por venteo y flaring  |                               |
   +----------+---------------------------------+-------------------------------+
   | 7        | Población nacional,             | Instituto Nacional de         |
   |          | proyecciones de crecimiento.    | Estadística y Censos (INEC)   |
   +----------+---------------------------------+-------------------------------+
   | 8        | PIB nacional y sectorial,       | Banco Central del Ecuador     |
   |          | proyecciones de crecimiento     |                               |
   +----------+---------------------------------+-------------------------------+
   | 9        | Vehículos matriculados por tipo | Agencia Nacional de Tránsito  |
   |          | y año, clasificación NTE INEN   |                               |
   |          | 2656                            |                               |
   +----------+---------------------------------+-------------------------------+

La Tabla :numref:`table_inputs_params` resume los parámetros de modelación y supuestos adoptados
para la construcción del Escenario Tendencial Nacional del sector
Energía. En ella se establecen los criterios utilizados para proyectar
la generación eléctrica, producción petrolera, demanda de energía,
transporte, variables económicas y demográficas, así como la métrica y
factores de emisión empleados en el modelo.

.. _table_inputs_params:
.. table:: Fuentes de información para parametrizar el Escenario Tendencial Nacional del sector Energía

   +----------+----------------------+----------------------------------------+
   |   ítem   | Parámetros de        |   Supuestos                            |
   |          | modelación           |                                        |
   +----------+----------------------+----------------------------------------+
   | 1        | Generación eléctrica | Desde 2010, la generación eléctrica    |
   |          |                      | no considera el ingreso de proyectos   |
   |          |                      | de generación renovable.               |
   |          |                      |                                        |
   |          |                      | Expansión de capacidad de generación   |
   |          |                      | basada en tendencias históricas sin    |
   |          |                      | políticas de promoción de energías     |
   |          |                      | renovables.                            |
   |          |                      |                                        |
   |          |                      | Participación de generación            |
   |          |                      | termoeléctrica mantiene niveles        |
   |          |                      | históricos.                            |
   |          |                      |                                        |
   |          |                      | No se consideran proyectos de          |
   |          |                      | Energía Renovable no Convencional      |
   |          |                      | (solar, eólica, geotérmica)            |
   |          |                      | posteriores a 2010.                    |
   |          |                      |                                        |
   +----------+----------------------+----------------------------------------+
   | 2        | Producción petrolera | Desde 2010, la producción petrolera    |
   |          |                      | y sus emisiones fugitivas no considera |
   |          |                      | medidas de mitigación.                 |
   |          |                      |                                        |
   |          |                      | Tasas de venteo y flaring se           |
   |          |                      | mantienen constantes conforme los      |
   |          |                      | niveles de 2010.                       |
   |          |                      |                                        |
   +----------+----------------------+----------------------------------------+
   | 3        | Demanda de energía   | Desde 2010, no se implementan          |
   |          |                      | medidas para reducir el consumo de     |
   |          |                      | combustibles fósiles mediante acciones |
   |          |                      | de eficiencia energética.              |
   |          |                      |                                        |
   |          |                      | No se consideran programas de          |
   |          |                      | recambio de equipos eficientes,        |
   |          |                      | etiquetado energético ni la            |
   |          |                      | implementación de sistemas de gestión  |
   |          |                      | de la energía conforme la norma ISO    |
   |          |                      | 50001.                                 |
   |          |                      |                                        |
   +----------+----------------------+----------------------------------------+
   | 4        | Sector transporte    | Parque automotor evoluciona según      |
   |          |                      | tendencias históricas del sector       |
   |          |                      | automotor.                             |
   |          |                      |                                        |
   |          |                      | No se considera la penetración de      |
   |          |                      | vehículos eléctricos o híbridos        |
   |          |                      | (vehículos cero/bajas emisiones).      |
   |          |                      |                                        |
   |          |                      | No se implementan sistemas de          |
   |          |                      | transporte público masivo de bajas     |
   |          |                      | emisiones de GEI.                      |
   |          |                      |                                        |
   |          |                      | Demanda de movilidad vinculada a       |
   |          |                      | Producto Interno Bruto.                |
   |          |                      |                                        |
   |          |                      | La demanda de movilidad 2018 se        |
   |          |                      | mantiene constante en el periodo       |
   |          |                      | 2010-2017 por falta de información     |
   |          |                      | histórica.                             |
   |          |                      |                                        |
   +----------+----------------------+----------------------------------------+
   | 5        | Clasificación        | Según Norma Técnica Ecuatoriana NTE    |
   |          | vehicular            | INEN 2656: Microbuses, buses, taxis,   |
   |          |                      | motocicleta, sedanes, SUVs, Minivan,   |
   |          |                      | carga pesada, transporte con           |
   |          |                      | suministro eléctrico por catenaria,    |
   |          |                      | carga media.                           |
   |          |                      |                                        |
   +----------+----------------------+----------------------------------------+
   | 6        | Tasas de crecimiento | Crecimiento del PIB según proyecciones |
   |          | económico            | consideradas en el PLANMICC.           |
   +----------+----------------------+----------------------------------------+
   | 7        | Tasas de crecimiento | Proyecciones demográficas del INEC.    |
   |          | poblacional          |                                        |
   |          |                      | Aumento poblacional influye            |
   |          |                      | directamente en demanda energética     |
   |          |                      | residencial, comercial y transporte.   |
   |          |                      |                                        |
   |          |                      | Tasa de urbanización afecta patrones   |
   |          |                      | de consumo energético.                 |
   |          |                      |                                        |
   +----------+----------------------+----------------------------------------+
   | 8        | Año base y línea     | Año base: 2010.                        |
   |          | base                 |                                        |
   |          |                      | Línea base: INGEI 2010 de la Quinta    |
   |          |                      | Comunicación Nacional y Primer Reporte |
   |          |                      | Bienal de Transparencia.               |
   |          |                      |                                        |
   +----------+----------------------+----------------------------------------+
   | 9        | Métrica y factores   | Potencial de Calentamiento Global a    |
   |          | de emisión           | 100 años (GWP-100), valores IPCC AR5.  |
   |          |                      |                                        |
   |          |                      | Factores de emisión Tier 1 según       |
   |          |                      | IPCC 2006/2019.                        |
   |          |                      |                                        |
   +----------+----------------------+----------------------------------------+

Para acceder a la versión completa de los datos de entrada del sector,
descargue el archivo de datos del sector Energía aquí: :download:`Modelo Energía Plan de Acción <../_static/docs/Modelo Energía Plan de Acción.xlsx>`
