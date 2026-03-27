===================================================
Escenarios
===================================================

En los sectores **Agricultura y Uso del Suelo, cambio de Uso del Suelo y
Silvicultura (USCUSS)** se modelaron **dos escenarios de proyección**,
ambos construidos a partir de la información descrita en los apartados
anteriores.

- **Escenario Tendencial:** Representa el "business as usual" sin
  intervenciones adicionales, considera únicamente los datos históricos
  y proyecciones sin la incorporación de medidas adicionales de
  mitigación. Este escenario sirve como línea de base para evaluar el
  impacto de las políticas y acciones propuestas.

.. _table_agro_uscuss_scenario_tendencial:
.. table:: Parámetros y supuestos de cambio utilizados para el escenario tendencial

   +-----------------------------------+-----------------------------------+
   | Parámetro                         | Supuesto                          |
   +===================================+===================================+
   | Bosques: Deforestación Bruta      | -0.78 Se mantiene constante       |
   |                                   |                                   |
   | Deforestación Neta                | -0.76 Se mantiene constante       |
   |                                   |                                   |
   | \*\* Deforestación en áreas       | \*\* El Modelo NDC aplica una     |
   | protegidas                        | tasa de deforestación de 0,049%   |
   |                                   | para áreas protegidas.            |
   +-----------------------------------+-----------------------------------+
   | Plantaciones Forestales           | Tasa de crecimiento al 1% de      |
   |                                   | crecimiento del PIB               |
   +-----------------------------------+-----------------------------------+
   | Cultivos                          | Tasa de crecimiento sectorial     |
   |                                   |                                   |
   |                                   | Contribución del sector al PIB    |
   +-----------------------------------+-----------------------------------+
   | Pasturas                          | Categoría flexible o de ajuste    |
   +-----------------------------------+-----------------------------------+
   | Vegetación arbustiva y herbácea   | Tasa de crecimiento de suelo de   |
   |                                   | cultivos                          |
   |                                   |                                   |
   |                                   | Tasa de crecimiento destinada a   |
   |                                   | ganadería                         |
   +-----------------------------------+-----------------------------------+
   | Humedales                         | Tasa de cambio de humedales       |
   +-----------------------------------+-----------------------------------+

- **Escenario Plan de Acción (PAC):** integra las iniciativas
  establecidas en la Segunda NDC del Ecuador (condicional e
  incondicional) que aplican a los dos sectores. Estas iniciativas son
  consideradas de manera integral reflejándose en las metas finales.

El Escenario Plan de Acción comparte similar información en los años
2010 – 2022. Los Principales cambios se resumen en la siguiente tabla:

.. _table_agro_uscuss_scenario_changes:
.. table:: Cambios efectuados en los archivos del modelo mixto de Agricultura y USCUSS (PAC)

   +-----------------+---------------------------------+---------------------------+--------------+---------------+
   | Archivo         | Hoja                            | Tecnología/Fuel           | parámetro    | Observación   |
   +=================+=================================+===========================+==============+===============+
   | ModeloSuelo_BAU | EmmisionActivitiyRatio          | Bosque_nativo_protegido   | co2_remocion | Se considera  |
   |                 |                                 |                           |              | el aumento de |
   |                 |                                 |                           |              | área de       |
   |                 |                                 |                           |              | bosque bajo   |
   |                 |                                 |                           |              | régimen de    |
   |                 |                                 |                           |              | protección    |
   |                 |                                 |                           |              | legal hasta   |
   |                 |                                 |                           |              | llegar al     |
   |                 |                                 |                           |              | 2035 a 7,9    |
   |                 |                                 |                           |              | Mha           |
   +-----------------+---------------------------------+---------------------------+--------------+---------------+
   | ModeloSuelo_BAU | TotalTechnologyAnnualActivityLo | Bosque_nativo_sinproteger | Mha          | Se resta el   |
   |                 |                                 |                           |              | área que se   |
   |                 |                                 |                           |              | adiciona a    |
   |                 |                                 |                           |              | Bosque Nativo |
   |                 |                                 |                           |              | Protegido     |
   +-----------------+---------------------------------+---------------------------+--------------+---------------+
   | ModeloSuelo_BAU | EmmisionActivitiyRatio          | Area_restaurada           | co2_remocion | Se considera  |
   |                 |                                 |                           |              | un aumento    |
   |                 |                                 |                           |              | progresivo de |
   |                 |                                 |                           |              | la tasa de    |
   |                 |                                 |                           |              | restauración  |
   |                 |                                 |                           |              | hasta llegar  |
   |                 |                                 |                           |              | a un promedio |
   |                 |                                 |                           |              | de 3200       |
   |                 |                                 |                           |              | ha/año        |
   +-----------------+---------------------------------+---------------------------+--------------+---------------+
   | ModeloSuelo_BAU | TotalTechnologyAnnualActivityLo | Plantacion_forestal       | Mh           | Se considera  |
   |                 |                                 |                           |              | un amento     |
   |                 |                                 |                           |              | progresivo    |
   |                 |                                 |                           |              | hasta llegar  |
   |                 |                                 |                           |              | a un valor de |
   |                 |                                 |                           |              | 198600 ha     |
   +-----------------+---------------------------------+---------------------------+--------------+---------------+
