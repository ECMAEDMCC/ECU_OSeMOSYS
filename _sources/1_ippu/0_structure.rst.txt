===================================
Estructura del modelo
===================================

El sector Procesos Industriales comprende las emisiones de GEI generadas
por transformaciones químicas y físicas de materias primas en la
fabricación y producción de bienes y en su uso. Es pertinente indicar,
que el uso de combustibles como fuente de energía en estos procesos de
transformación, se declaran en el sector de energía. En el país, dentro
del sector Procesos Industriales se identifican actividades como como la
producción de cemento, de cal, de acero, de cerámica, de vidrio, y el
uso de solventes, lubricantes, así como el de compuestos de
hidrofluorocarbonos (HFC), perfluorocarbonos (PFC), principalmente en
sistemas de refrigeración y aire acondicionado. Este sector abarca
varias categorías y subcategorías emisoras de GEI, de acuerdo con el
INGEI de la 5ta Comunicación Nacional (5CN) del Ecuador (MAE,2024), que
se enlistan a continuación:

- **Categoría 2A: Industria de los minerales**

  - **Subcategoría 2A1:** Producción de Cemento

  - **Subcategoría 2A2:** Producción de Cal

  - **Subcategoría 2A3:** Producción de Vidrio

  - **Subcategoría 2A4a:** Cerámica

  - **Subcategoría 2A4b:** Otros Usos de la Soda Ash

- **Categoría 2C: Industria de los metales**

  - **Subcategoría 2C1:** Producción de Hierro y Acero

  - **Subcategoría 2C5:** Producción de Plomo

- **Categoría 2D: Uso de Productos no Energéticos de combustibles y de
  solventes**

  - **Subcategoría 2D1:** Uso de Lubricantes

  - **Subcategoría 2D2:** Uso de Cera Parafina

- **Categoría 2F: Uso de Productos como sustitutos para las substancias
  que agotan la capa de ozono**

  - **Subcategoría 2F1:** Refrigeración y Aire Acondicionado

Basado en lo anterior, el modelado se basa en la plataforma OSeMOSYS y
amplía los desarrollos previos, a través de un proceso de referenciación
metodológica abreviado que prioriza la información de la Segunda
Contribución Determinada a Nivel Nacional (NDC) y la complementa con
insumos provenientes del Plan Nacional de Mitigación del Cambio
Climático (PLANMICC). De forma simplificada, el modelo se ilustra en la
:numref:`ippu_model_structure`.

.. figure:: ../_static/images/energy/model_structure.png
   :name: ippu_model_structure
   :align: center
   :alt: Diagrama de referencia del modelo del sector Procesos Industriales

   Diagrama de referencia del modelo del sector Procesos Industriales.

En la :numref:`ippu_techs`, :numref:`ippu_commodities` y :numref:`ippu_included_emissions` se incluye la nomenclatura de los
Sets, Technologies, Commodities y Emission del modelo de la :numref:`ippu_model_structure`.

.. _ippu_techs:
.. table:: Tecnologías incluidas en el modelo del sector Procesos Industriales.

   +-------------------------------------------+---------------+
   | Descripción                               | Código        |
   +===========================================+===============+
   | Energía térmica para Clinker              | ENE_TERM      |
   +-------------------------------------------+---------------+
   | Materiales para Clinker                   | RAW_MAT_CLK   |
   +-------------------------------------------+---------------+
   | Electricidad para energía térmica         | ELEC_TERM     |
   +-------------------------------------------+---------------+
   | Electricidad para cemento                 | ELEC_CEM      |
   +-------------------------------------------+---------------+
   | Materiales para cemento                   | RAW_MAT_CEM   |
   +-------------------------------------------+---------------+
   | Resto de emisiones del sector PIUP        | REST_PI       |
   +-------------------------------------------+---------------+
   | Producción de Clinker con combustibles de | PROD_CLK_TRAD |
   | origen fósil                              |               |
   +-------------------------------------------+---------------+
   | Producción de Clinker con electricidad    | PROD_CLK_ELEC |
   +-------------------------------------------+---------------+
   | Producción de cemento                     | PROD_CEM      |
   +-------------------------------------------+---------------+
   | Uso de HFC                                | HFC_use       |
   +-------------------------------------------+---------------+
   | Producción de Cal                         | LIME_PROD     |
   +-------------------------------------------+---------------+
   | Producción de Vidrio                      | GLASS_PROD    |
   +-------------------------------------------+---------------+
   | Producción de Cerámica                    | CERAMICS      |
   +-------------------------------------------+---------------+
   | Otros usos de Soda Ash                    | SODA_ASH      |
   +-------------------------------------------+---------------+
   | Producción de Hierro y Acero              | IRON_STEEL    |
   +-------------------------------------------+---------------+
   | Producción de Plomo                       | LEAD_PROD     |
   +-------------------------------------------+---------------+
   | Uso de Lubricantes                        | LUBRI         |
   +-------------------------------------------+---------------+
   | Uso de Ceras de parafina                  | PARAFFIN      |
   +-------------------------------------------+---------------+

.. _ippu_commodities:
.. table:: Commodities incluidos en el modelo del sector Procesos Industriales.

   +--------------------------+-------------+
   | Descripción              | Código      |
   +==========================+=============+
   | Energía térmica para     | ENE_TERM    |
   | Clinker                  |             |
   +--------------------------+-------------+
   | Materiales para Clinker  | RAW_MAT_CLK |
   +--------------------------+-------------+
   | Electricidad para        | ELEC_TERM   |
   | energía térmica          |             |
   +--------------------------+-------------+
   | Electricidad para        | ELEC_CEM    |
   | Cemento                  |             |
   +--------------------------+-------------+
   | Materiales para Cemento  | RAW_MAT_CEM |
   +--------------------------+-------------+
   | Clinker para cemento     | CLK_PROD    |
   +--------------------------+-------------+
   | Producción de cemento    | CEM_PROD    |
   +--------------------------+-------------+

.. _ippu_included_emissions:
.. table::  Emisiones incluidas en el modelo del sector Procesos Industriales.

   +-----------------------------------------------------------+-----------+
   | Descripción                                               | Código    |
   +===========================================================+===========+
   | Dióxido de carbono equivalente producido por              | CO2eq_HFC |
   | Hidrofluorocarbonos                                       |           |
   +-----------------------------------------------------------+-----------+
   | Dióxido de carbono equivalente producido por el proceso   | CO2eq     |
   | de producción de cemento                                  | \_CEM     |
   +-----------------------------------------------------------+-----------+
   | Dióxido de carbono equivalente producido por otros        | CO2eq     |
   | Procesos Industriales y Uso de Productos                  | \_IPPU    |
   +-----------------------------------------------------------+-----------+
