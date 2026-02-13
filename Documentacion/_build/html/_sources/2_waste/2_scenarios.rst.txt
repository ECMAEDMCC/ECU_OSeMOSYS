===================================================
Escenarios
===================================================

En lo que respecta al sector Residuos, al igual que en los sectores
anteriores, primeramente, se construye un escenario *Tendencial*. Este
escenario pretende reflejar un futuro sin iniciativas que combina la
variabilidad temporal de los FE del modelo NDC con la estructura
tecnológica del PLANMICC.

El segundo escenario es el escenario *Plan de Acción*. Este escenario
integra la trayectoria del escenario tendencial (2010–2035) y añade de
forma progresiva las iniciativas identificadas en las Contribuciones
Determinadas a Nivel Nacional (NDC) del Ecuador tanto la primera como la
segunda, en sus componentes incondicionales y condicionales, junto con
los proyectos estratégicos adicionales priorizados en el marco del
PLANMICC (2024). Este escenario representa, por tanto, el conjunto de
medidas e intervenciones de mitigación que el país se ha comprometido a
implementar para reducir las emisiones de gases de efecto invernadero
(GEI) en el sector Residuos, incorporando acciones de:

- Captura y aprovechamiento de biogás en rellenos sanitarios.

- Tratamiento de aguas residuales domésticas e industriales.

- Valorización de residuos orgánicos mediante compostaje, lombricultura,
  bokashi y tecnologías emergentes.

- Reducción de pérdidas de alimentos, incluyendo iniciativas de bancos
  de alimentos y programas de recuperación.

Cada iniciativa fue caracterizada según los siguientes criterios:

- Potencial de mitigación al 2035, expresado en kt CO₂eq/año.

- Año de inicio, correspondiente al momento estimado en que la medida
  entra en operación.

- Trayectoria de incorporación anual, que permite reflejar la
  gradualidad en la implementación.

- Asignación tecnológica en OSeMOSYS, garantizando su integración en el
  modelo nacional de planificación energética y de mitigación.

En la :numref:`table_waste_scenarios` se detallan de mejor forma las iniciativas mencionadas.

.. _table_waste_scenarios:
.. table:: Descripción de iniciativas del sector Residuos para el escenario Plan de Acción.

   +------+-------------------+------------+----------------+---------------+-------------------+
   | NRO. | DESCRIPCIÓN       | POTENCIAL  | AÑO DE         | TECNOLOGÍA    | META PLANMICC     |
   |      |                   | DE         | IMPLEMENTACIÓN | OSEMOSYS      | -2035             |
   |      |                   | MITIGACIÓN |                |               |                   |
   |      |                   | AL 2035    |                |               |                   |
   |      |                   | [KT        |                |               |                   |
   |      |                   | CO₂EQ/AÑO] |                |               |                   |
   +======+===================+============+================+===============+===================+
   | 1    | Captura y         | 7.50       | 2026-2035      | LANDFILL_ELEC | R.1 10% procesado |
   |      | aprovechamiento   |            |                |               | en plantas nuevas |
   |      | de biogás en      |            |                |               | de generación de  |
   |      | rellenos          |            |                |               | energía eléctrica |
   |      | sanitario         |            |                |               | a partir de       |
   |      |                   |            |                |               | biogás en esos    |
   |      |                   |            |                |               | rellenos          |
   |      |                   |            |                |               | sanitarios.       |
   +------+-------------------+------------+----------------+---------------+-------------------+
   | 2    | Captura y quema   | 1710.0     | 2026-2035      | LANDFILL_ELEC | R.1 10% procesado |
   |      | de biogás en      |            |                |               | en plantas nuevas |
   |      | rellenos          |            |                |               | de generación de  |
   |      | sanitarios        |            |                |               | energía eléctrica |
   |      |                   |            |                |               | a partir de       |
   |      |                   |            |                |               | biogás en esos    |
   |      |                   |            |                |               | rellenos          |
   |      |                   |            |                |               | sanitarios.       |
   +------+-------------------+------------+----------------+---------------+-------------------+
   | 3    | Tratamiento de    | 37.0       | 2026-2035      | WWWT          | R.2 8% de aguas   |
   |      | aguas residuales  |            |                |               | residuales        |
   |      |                   |            |                |               | tratadas mediante |
   |      |                   |            |                |               | plantas de        |
   |      |                   |            |                |               | tratamiento       |
   |      |                   |            |                |               | biológico de      |
   |      |                   |            |                |               | aguas residuales  |
   |      |                   |            |                |               | (PTAR).           |
   +------+-------------------+------------+----------------+---------------+-------------------+
   | 4    | Tratamiento de    | 51.0       | 2027-2035      | WWWT          | R.2 8% de aguas   |
   |      | aguas residuales  |            |                |               | residuales        |
   |      |                   |            |                |               | tratadas mediante |
   |      |                   |            |                |               | plantas de        |
   |      |                   |            |                |               | tratamiento       |
   |      |                   |            |                |               | biológico de      |
   |      |                   |            |                |               | aguas residuales  |
   |      |                   |            |                |               | (PTAR).           |
   +------+-------------------+------------+----------------+---------------+-------------------+
   | 5    | Tratamiento de    | 44.5       | 2026-2035      | IWW           | R.2 8% de aguas   |
   |      | aguas residuales  |            |                |               | residuales        |
   |      |                   |            |                |               | tratadas mediante |
   |      |                   |            |                |               | plantas de        |
   |      |                   |            |                |               | tratamiento       |
   |      |                   |            |                |               | biológico de      |
   |      |                   |            |                |               | aguas residuales  |
   |      |                   |            |                |               | (PTAR).           |
   +------+-------------------+------------+----------------+---------------+-------------------+
   | 6    | Compostaje        | 11.0       | 2026-2035      | COMPOST       | R.1 Corto plazo:  |
   |      | municipal de      |            |                |               | 10% de residuos   |
   |      | residuos          |            |                |               | sólidos generados |
   |      | orgánicos         |            |                |               | son gestionados   |
   |      |                   |            |                |               | mediante          |
   |      |                   |            |                |               | tecnologías de    |
   |      |                   |            |                |               | reciclaje como    |
   |      |                   |            |                |               | tratamiento y     |
   |      |                   |            |                |               | valorización de   |
   |      |                   |            |                |               | residuos sólidos  |
   +------+-------------------+------------+----------------+---------------+-------------------+
   | 7    | Compostaje        | 6.97       | 2026-2035      | COMPOST       | R.1 Corto plazo:  |
   |      | privado o de      |            |                |               | 10% de residuos   |
   |      | pequeña escala    |            |                |               | sólidos generados |
   |      |                   |            |                |               | son gestionados   |
   |      |                   |            |                |               | mediante          |
   |      |                   |            |                |               | tecnologías de    |
   |      |                   |            |                |               | reciclaje como    |
   |      |                   |            |                |               | tratamiento y     |
   |      |                   |            |                |               | valorización de   |
   |      |                   |            |                |               | residuos sólidos  |
   +------+-------------------+------------+----------------+---------------+-------------------+
   | 8    | Tratamiento de    | 14.0       | 2026-2035      | WWWT          | R.2 33% instalado |
   |      | aguas residuales  |            |                |               | y funcionando     |
   |      | (Plantas          |            |                |               | óptimamente.      |
   |      | descentralizadas) |            |                |               |                   |
   +------+-------------------+------------+----------------+---------------+-------------------+
   | 9    | Tratamiento de    | 7.0        | 2026-2035      | WWWT          | R.2 33% instalado |
   |      | aguas residuales  |            |                |               | y funcionando     |
   |      |                   |            |                |               | óptimamente.      |
   +------+-------------------+------------+----------------+---------------+-------------------+
   | 10   | Captura y         | 860.428    | 2025-2035      | LANDFILL_ELEC | R.1 10% procesado |
   |      | aprovechamiento   |            |                |               | en plantas nuevas |
   |      | de biogás en      |            |                |               | de generación de  |
   |      | rellenos          |            |                |               | energía eléctrica |
   |      | sanitario         |            |                |               | a partir de       |
   |      |                   |            |                |               | biogás en esos    |
   |      |                   |            |                |               | rellenos          |
   |      |                   |            |                |               | sanitarios.       |
   +------+-------------------+------------+----------------+---------------+-------------------+
   | 11   | Aprovechamiento y | 5.0        | 2028-2035      | COMPOST       | R.1 Corto plazo:  |
   |      | valorización de   |            |                |               | 10% de residuos   |
   |      | residuos          |            |                |               | sólidos generados |
   |      |                   |            |                |               | son gestionados   |
   |      |                   |            |                |               | mediante          |
   |      |                   |            |                |               | tecnologías de    |
   |      |                   |            |                |               | reciclaje como    |
   |      |                   |            |                |               | tratamiento y     |
   |      |                   |            |                |               | valorización de   |
   |      |                   |            |                |               | residuos sólidos  |
   +------+-------------------+------------+----------------+---------------+-------------------+
   | 12   | Gestión integral  | 90.0       | 2030-2035      | LANDFILL_ELEC | R.1 Gestión del   |
   |      | de residuos con   |            |                |               | 5% de residuos    |
   |      | aprovechamiento   |            |                |               | sólidos orgánicos |
   |      | de biogás         |            |                |               | en plantas de     |
   |      |                   |            |                |               | valorización de   |
   |      |                   |            |                |               | orgánicos a gran  |
   |      |                   |            |                |               | escala para MBT   |
   |      |                   |            |                |               | (tratamiento      |
   |      |                   |            |                |               | mecánico          |
   |      |                   |            |                |               | biológico).       |
   +------+-------------------+------------+----------------+---------------+-------------------+
   | 13   | Captura y quema   | 50.0       | 2026-2035      | LANDFILL_ELEC | R.1 70% de los    |
   |      | de biogás en      |            |                |               | sitios de         |
   |      | relleno sanitario |            |                |               | disposición final |
   |      |                   |            |                |               | de residuos       |
   |      |                   |            |                |               | sólidos operan    |
   |      |                   |            |                |               | técnicamente.     |
   +------+-------------------+------------+----------------+---------------+-------------------+
   | 14   | Reducción y       | 4.0        | 2026-2035      | TSW           | R.1 Corto plazo:  |
   |      | perdidas de       |            |                |               | -1% de reducción  |
   |      | desperdicio de    |            |                |               | de kilogramos de  |
   |      | alimentos         |            |                |               | residuos sólidos  |
   |      |                   |            |                |               | generados per     |
   |      |                   |            |                |               | cápita a escala   |
   |      |                   |            |                |               | nacional          |
   +------+-------------------+------------+----------------+---------------+-------------------+
   | 15   | Compostaje        | 0.02       | 2026-2035      | COMPOST       | R.1 Corto plazo:  |
   |      | municipal de      |            |                |               | 10% de residuos   |
   |      | residuos          |            |                |               | sólidos generados |
   |      | orgánicos         |            |                |               | son gestionados   |
   |      |                   |            |                |               | mediante          |
   |      |                   |            |                |               | tecnologías de    |
   |      |                   |            |                |               | reciclaje como    |
   |      |                   |            |                |               | tratamiento y     |
   |      |                   |            |                |               | valorización de   |
   |      |                   |            |                |               | residuos sólidos  |
   +------+-------------------+------------+----------------+---------------+-------------------+
   | 16   | Compostaje en     | 10.1       | 2026-2035      | COMPOST       | R.1 Corto plazo:  |
   |      | centros de abasto |            |                |               | 10% de residuos   |
   |      | y mercados        |            |                |               | sólidos generados |
   |      | mayoristas        |            |                |               | son gestionados   |
   |      |                   |            |                |               | mediante          |
   |      |                   |            |                |               | tecnologías de    |
   |      |                   |            |                |               | reciclaje como    |
   |      |                   |            |                |               | tratamiento y     |
   |      |                   |            |                |               | valorización de   |
   |      |                   |            |                |               | residuos sólidos  |
   +------+-------------------+------------+----------------+---------------+-------------------+
   | 17   | Tratamiento de    | 0.1        | 2026-2035      | WWWT          | R.2 33% instalado |
   |      | aguas residuales  |            |                |               | y funcionando     |
   |      | institucional     |            |                |               | óptimamente.      |
   +------+-------------------+------------+----------------+---------------+-------------------+
   | 18   | Tratamiento       | 0.108      | 2026-2035      | COMPOST       | R.1 Corto plazo:  |
   |      | biológico de      |            |                |               | 10% de residuos   |
   |      | residuos          |            |                |               | sólidos generados |
   |      | orgánicos en      |            |                |               | son gestionados   |
   |      | instalaciones     |            |                |               | mediante          |
   |      | aeroportuarias    |            |                |               | tecnologías de    |
   |      |                   |            |                |               | reciclaje como    |
   |      |                   |            |                |               | tratamiento y     |
   |      |                   |            |                |               | valorización de   |
   |      |                   |            |                |               | residuos sólidos  |
   +------+-------------------+------------+----------------+---------------+-------------------+
   | 19   | Aprovechamiento   | 2.5        | 2028-2035      | COMPOST       | R.1 Corto plazo:  |
   |      | orgánico y        |            |                |               | 10% de residuos   |
   |      | lombricultura     |            |                |               | sólidos generados |
   |      | municipal         |            |                |               | son gestionados   |
   |      |                   |            |                |               | mediante          |
   |      |                   |            |                |               | tecnologías de    |
   |      |                   |            |                |               | reciclaje como    |
   |      |                   |            |                |               | tratamiento y     |
   |      |                   |            |                |               | valorización de   |
   |      |                   |            |                |               | residuos sólidos  |
   +------+-------------------+------------+----------------+---------------+-------------------+
   | 20   | Planta de         | 60         | 2034-2035      | WWWT          | 8 % de aguas      |
   |      | Tratamiento de    |            |                |               | residuales        |
   |      | Aguas Residuales  |            |                |               | tratadas mediante |
   |      | (PTAR) domésticas |            |                |               | plantas de        |
   |      |                   |            |                |               | tratamiento       |
   |      |                   |            |                |               | biológico de      |
   |      |                   |            |                |               | aguas             |
   +------+-------------------+------------+----------------+---------------+-------------------+
   | 21   | Planta de         | 0.17       | 2026-2035      | WWWT          | 33% instalado y   |
   |      | Tratamiento de    |            |                |               | funcionando       |
   |      | Aguas Residuales  |            |                |               | óptimamente.      |
   |      | (PTAR) domésticas |            |                |               |                   |
   +------+-------------------+------------+----------------+---------------+-------------------+
