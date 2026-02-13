===================================
Estructura del modelo
===================================

El sector energético analiza el consumo de energía, considerando la oferta primaria de combustibles, su producción, importación y exportación. Las categorías utilizadas se basan en el INGEI de la 5ta Comunicación Nacional (5CN) del Ecuador (MAATE, n.d.).

.. _table_categories_energy:
.. table:: Categorías del INGEI consideradas en el modelo de Energía

   +-----------+----------------+--------------------------------------+
   | Categoría | Nombre         | Descripción                          |
   | INGEI     |                |                                      |
   +===========+================+======================================+
   | 1A1       | Industrias de  | Abarca tecnologías de generación     |
   |           | energía como   | eléctrica reportadas en informes de  |
   |           | actividad      | ARCONEL (2022)                       |
   |           | principal      |                                      |
   +-----------+----------------+--------------------------------------+
   | 1A2       | Industrias     | Engloba el consumo por tipo de       |
   |           | manufactureras | combustible según el Balance de      |
   |           | y de la        | Energía Nacional (MEM, 2023).        |
   |           | construcción   |                                      |
   +-----------+----------------+--------------------------------------+
   | 1A3       | Transporte     | Incluye el consumo energético del    |
   |           |                | sector transporte en todas sus       |
   |           |                | formas.                              |
   +-----------+----------------+--------------------------------------+
   | 1A4       | Otros sectores | Registra el consumo por tipo de      |
   |           |                | combustible en el sector             |
   |           |                | residencial, comercial y público.    |
   +-----------+----------------+--------------------------------------+
   | 1A5       | No             | Incluye otras categorías energéticas |
   |           | especificado   | no detalladas en el Balance de       |
   |           |                | Energía Nacional.                    |
   +-----------+----------------+--------------------------------------+
   | 1B        | Emisiones      | Se asocian a la producción de        |
   |           | fugitivas      | petróleo y gas natural.              |
   +-----------+----------------+--------------------------------------+


.. figure:: ../_static/images/energy/model_structure.png
   :name: model_structure_energy
   :align: center
   :alt: Estructura del modelo de Energía

   Estructura del modelo de Energía

**Vectores energéticos**

.. _table_vector_energy:
.. table:: Vectores energético incluidos en el modelo de Energía

   +-------------------------+----------------+
   | Vector energético       | Código         |
   +=========================+================+
   | Transport Demand - Non  | DEMTRN_NOMOT   |
   | motorized reductions    |                |
   +-------------------------+----------------+
   | Transport Demand -      | DEMTRNFREHEA   |
   | Heavy Freight           |                |
   +-------------------------+----------------+
   | Transport Demand -      | DEMTRNFRELIG   |
   | Light Freight           |                |
   +-------------------------+----------------+
   | Transport Demand -      | DEMTRNFREMED   |
   | Medium Freight          |                |
   +-------------------------+----------------+
   | Transport Demand -      | DEMTRNPASPRI   |
   | Passsenger Private      |                |
   +-------------------------+----------------+
   | Transport Demand -      | DEMTRNPASPUB   |
   | Passenger Public        |                |
   +-------------------------+----------------+
   | Aceite_Pinon            | E0_ACP         |
   +-------------------------+----------------+
   | Produced Biogas         | E0_BGS         |
   +-------------------------+----------------+
   | Produced Biomass        | E0_BMS         |
   +-------------------------+----------------+
   | Coal                    | E0_COA         |
   +-------------------------+----------------+
   | Crude_reserves          | E0_CRU         |
   +-------------------------+----------------+
   | Produced Firewood       | E0_FIR         |
   +-------------------------+----------------+
   | Natural_Gas             | E0_NGS         |
   +-------------------------+----------------+
   | Produced Sugarcane      | E0_SUG         |
   +-------------------------+----------------+
   | Waste                   | E0_WAS         |
   +-------------------------+----------------+
   | Biodiesel               | E1_BIODSL      |
   +-------------------------+----------------+
   | Coke                    | E1_COK         |
   +-------------------------+----------------+
   | Crude_Oil_Transport     | E1_CRU         |
   +-------------------------+----------------+
   | Diesel                  | E1_DSL         |
   +-------------------------+----------------+
   | Electricity             | E1_ELE         |
   +-------------------------+----------------+
   | Etanol                  | E1_ETA         |
   +-------------------------+----------------+
   | Fuel_Oil                | E1_FOI         |
   +-------------------------+----------------+
   | Gases from Natural Gas  | E1_GAS         |
   +-------------------------+----------------+
   | Gasoline                | E1_GSL         |
   +-------------------------+----------------+
   | Heat_from_cogeneration  | E1_HEC         |
   +-------------------------+----------------+
   | Kerosene                | E1_KJF         |
   +-------------------------+----------------+
   | LPG from Natural Gas    | E1_LPG         |
   +-------------------------+----------------+
   | Produced Natural_Gas    | E1_NGS         |
   +-------------------------+----------------+
   | Non_energy              | E1_NOE         |
   +-------------------------+----------------+
   | Pure_Diesel             | E1_PURDSL      |
   +-------------------------+----------------+
   | Pure_Gasoline           | E1_PURGSL      |
   +-------------------------+----------------+
   | Reduced oil             | E1_REDCRU      |
   +-------------------------+----------------+
   | Crude_Oil_Transport     | E2_CRU         |
   +-------------------------+----------------+
   | Secondary - Electricity | E2_ELE         |
   | from Transmission       |                |
   +-------------------------+----------------+
   | Secondary - Produced    | E2_HYD         |
   | Green Hydrogen          |                |
   +-------------------------+----------------+
   | Natural_Gas_distributed | E2_NGS         |
   +-------------------------+----------------+
   | Crude_Oil_Refineries    | E3_CRU         |
   +-------------------------+----------------+
   | Electricity             | E3_ELE         |
   +-------------------------+----------------+
   | Secondary - Transported | E3_HYD         |
   | Hydrogen                |                |
   +-------------------------+----------------+
   | Distributed Diesel for  | E4_DSLHEA      |
   | Heavy Freight           |                |
   +-------------------------+----------------+
   | Distributed Diesel for  | E4_DSLLIG      |
   | Light Freight           |                |
   +-------------------------+----------------+
   | Distributed Diesel for  | E4_DSLMED      |
   | Medium Freight          |                |
   +-------------------------+----------------+
   | Distributed Diesel for  | E4_DSLPRI      |
   | Private                 |                |
   +-------------------------+----------------+
   | Distributed Diesel for  | E4_DSLPUB      |
   | Public                  |                |
   +-------------------------+----------------+
   | Electricity             | E4_ELE         |
   +-------------------------+----------------+
   | Distributed Electricity | E4_ELEHEA      |
   | for Heavy Freight       |                |
   +-------------------------+----------------+
   | Distributed Electricity | E4_ELELIG      |
   | for Light Freight       |                |
   +-------------------------+----------------+
   | Distributed Electricity | E4_ELEMED      |
   | for Medium Freight      |                |
   +-------------------------+----------------+
   | Distributed Electricity | E4_ELEPRI      |
   | for Private             |                |
   +-------------------------+----------------+
   | Distributed Electricity | E4_ELEPUB      |
   | for Public              |                |
   +-------------------------+----------------+
   | Distributed Gasoline    | E4_GSLHEA      |
   | for Heavy Freight       |                |
   +-------------------------+----------------+
   | Distributed Gasoline    | E4_GSLLIG      |
   | for Light Freight       |                |
   +-------------------------+----------------+
   | Distributed Gasoline    | E4_GSLMED      |
   | for Medium Freight      |                |
   +-------------------------+----------------+
   | Distributed Gasoline    | E4_GSLPRI      |
   | for Private             |                |
   +-------------------------+----------------+
   | Distributed Gasoline    | E4_GSLPUB      |
   | for Public              |                |
   +-------------------------+----------------+
   | Distributed Hydrogen    | E4_HYDHEA      |
   | for Heavy Freight       |                |
   +-------------------------+----------------+
   | Distributed Hydrogen    | E4_HYDMED      |
   | for Medium Freight      |                |
   +-------------------------+----------------+
   | Distributed Hydrogen    | E4_HYDPUB      |
   | for Public              |                |
   +-------------------------+----------------+
   | Distributed LPG for     | E4_LPGHEA      |
   | Heavy Freight           |                |
   +-------------------------+----------------+
   | Distributed LPG for     | E4_LPGLIG      |
   | Light Freight           |                |
   +-------------------------+----------------+
   | Distributed LPG for     | E4_LPGMED      |
   | Medium Freight          |                |
   +-------------------------+----------------+
   | Distributed LPG for     | E4_LPGPRI      |
   | Private                 |                |
   +-------------------------+----------------+
   | Distributed LPG for     | E4_LPGPUB      |
   | Public                  |                |
   +-------------------------+----------------+
   | Distributed Natural Gas | E4_NGSLIG      |
   | for Light Freight       |                |
   +-------------------------+----------------+
   | Distributed Natural Gas | E4_NGSMED      |
   | for Medium Freight      |                |
   +-------------------------+----------------+
   | Distributed Natural Gas | E4_NGSPRI      |
   | for Private             |                |
   +-------------------------+----------------+
   | Distributed Natural Gas | E4_NGSPUB      |
   | for Public              |                |
   +-------------------------+----------------+
   | Demand Biomass for      | T5BMSEXP       |
   | power for Exports       |                |
   +-------------------------+----------------+
   | Demand for bunkers      | T5BUN          |
   +-------------------------+----------------+
   | Demand Petroleum Coke   | T5COKIND       |
   | for Industrial          |                |
   +-------------------------+----------------+
   | Demand Crude for SOTE   | T5CRUCRUTRN    |
   +-------------------------+----------------+
   | Demand Crude Oil for    | T5CRUEXP       |
   | Exports                 |                |
   +-------------------------+----------------+
   | Demand Electricity for  | T5ELEAGR       |
   | Agriculture             |                |
   +-------------------------+----------------+
   | Demand Electricity for  | T5ELECOM       |
   | Commercial              |                |
   +-------------------------+----------------+
   | Demand Pure_Gasoline    | T5ELECON       |
   | for Construction        |                |
   +-------------------------+----------------+
   | Demand Electricity for  | T5ELECRUTRN    |
   | SOTE                    |                |
   +-------------------------+----------------+
   | Demand Electricity for  | T5ELEEXP       |
   | Exports                 |                |
   +-------------------------+----------------+
   | Demand Electricity for  | T5ELEIND       |
   | Industrial              |                |
   +-------------------------+----------------+
   | Demand Electricity for  | T5ELERES       |
   | Residential             |                |
   +-------------------------+----------------+
   | Demand Firewood for     | T5FIRIND       |
   | Industrial              |                |
   +-------------------------+----------------+
   | Demand Firewood for     | T5FIRRES       |
   | Residential             |                |
   +-------------------------+----------------+
   | Demand Fuel Oil for     | T5FOICOM       |
   | Commercial              |                |
   +-------------------------+----------------+
   | Demand Fuel Oil for     | T5FOIEXP       |
   | Exports                 |                |
   +-------------------------+----------------+
   | Demand Fuel Oil for     | T5FOIIND       |
   | Industrial              |                |
   +-------------------------+----------------+
   | Demand Fuel Oil for     | T5FOIREF       |
   | Refineries              |                |
   +-------------------------+----------------+
   | Demand Fuel Oil for     | T5FOISHITRN    |
   | Shipping                |                |
   +-------------------------+----------------+
   | Demand Gasoline for     | T5GSLCRUTRN    |
   | SOTE                    |                |
   +-------------------------+----------------+
   | Demand Heat from        | T5HECIND       |
   | cogeneration for        |                |
   | Industrial              |                |
   +-------------------------+----------------+
   | Demand Hydrogen for     | T5HYDIND       |
   | Industrial              |                |
   +-------------------------+----------------+
   | Demand Kerosene and Jet | T5KJFAERTRN    |
   | Fuel for Air Transport  |                |
   +-------------------------+----------------+
   | Demand Kerosene and Jet | T5KJFCON       |
   | Fuel for Construction   |                |
   +-------------------------+----------------+
   | Demand Kerosene and Jet | T5KJFREF       |
   | Fuel for Refineries     |                |
   +-------------------------+----------------+
   | Demand LPG for          | T5LPGAGR       |
   | Agriculture             |                |
   +-------------------------+----------------+
   | Demand LPG for          | T5LPGCOM       |
   | Commercial              |                |
   +-------------------------+----------------+
   | Demand LPG for          | T5LPGCON       |
   | Construction            |                |
   +-------------------------+----------------+
   | Demand LPG for SOTE     | T5LPGCRUTRN    |
   +-------------------------+----------------+
   | Demand LPG for Exports  | T5LPGEXP       |
   +-------------------------+----------------+
   | Demand LPG for          | T5LPGIND       |
   | Industrial              |                |
   +-------------------------+----------------+
   | Demand GLP for          | T5LPGREF       |
   | Refineries              |                |
   +-------------------------+----------------+
   | Demand LPG for          | T5LPGRES       |
   | Residential             |                |
   +-------------------------+----------------+
   | Demand Natural Gas for  | T5NGSIND       |
   | Industrial              |                |
   +-------------------------+----------------+
   | Demand Natural Gas for  | T5NGSRES       |
   | Residential             |                |
   +-------------------------+----------------+
   | Demand Non energy for   | T5NOEAGR       |
   | Agriculture             |                |
   +-------------------------+----------------+
   | Demand Non energy for   | T5NOECON       |
   | Construction            |                |
   +-------------------------+----------------+
   | Demand Propane and Gas  | T5PROGAS       |
   | for multiple            |                |
   +-------------------------+----------------+
   | Demand Pure_Diesel for  | T5PURDSLCOM    |
   | Commercial              |                |
   +-------------------------+----------------+
   | Demand Pure_Diesel for  | T5PURDSLCON    |
   | Construction            |                |
   +-------------------------+----------------+
   | Demand Pure_Diesel for  | T5PURDSLEXP    |
   | Exports                 |                |
   +-------------------------+----------------+
   | Demand Pure_Diesel for  | T5PURDSLIND    |
   | Industrial              |                |
   +-------------------------+----------------+
   | Demand Diesel for       | T5PURDSLREF    |
   | Refineries              |                |
   +-------------------------+----------------+
   | Demand Pure_Diesel for  | T5PURDSLSHITRN |
   | Shipping                |                |
   +-------------------------+----------------+
   | Demand Pure_Gasoline    | T5PURGSLAERTRN |
   | for Air Transport       |                |
   +-------------------------+----------------+
   | Demand Pure_Gasoline    | T5PURGSLAGR    |
   | for Agriculture         |                |
   +-------------------------+----------------+
   | Demand Pure_Gasoline    | T5PURGSLCOM    |
   | for Commercial          |                |
   +-------------------------+----------------+
   | Demand Pure_Gasoline    | T5PURGSLCON    |
   | for Construction        |                |
   +-------------------------+----------------+
   | Demand Pure_Gasoline    | T5PURGSLEXP    |
   | for Exports             |                |
   +-------------------------+----------------+
   | Demand Pure_Gasoline    | T5PURGSLIND    |
   | for Industrial          |                |
   +-------------------------+----------------+
   | Demand Gasoline for     | T5PURGSLREF    |
   | Refineries              |                |
   +-------------------------+----------------+
   | Demand Pure_Gasoline    | T5PURGSLSHITRN |
   | for Shipping            |                |
   +-------------------------+----------------+
   | Demand Reduced Crude    | T5REDCRUEXP    |
   | for Exports             |                |
   +-------------------------+----------------+
   | Demand Sugarcane and    | T5SUGIND       |
   | subproducts for         |                |
   | Industrial              |                |
   +-------------------------+----------------+

**Emisiones**

.. _table_emission_types_energy:
.. table:: Clasificación de emisiones estimadas en el modelo de Energía

   +-------------------+-------------------------------------------------------+
   |   Código          | Descripción                                           |
   +===================+=======================================================+
   | CO2               | Dióxido de carbono equivalente del combustible        |
   +-------------------+-------------------------------------------------------+
   | CO2_scc           | Dióxido de carbono equivalente específico del         |
   |                   | combustible                                           |
   +-------------------+-------------------------------------------------------+
   | CO2_fugitivas     | Dióxido de carbono equivalente no intencionales de    |
   |                   | gases que se escapan durante la producción,           |
   |                   | procesamiento, transporte, almacenamiento o           |
   |                   | distribución de combustibles, sin que exista          |
   |                   | combustión.                                           |
   +-------------------+-------------------------------------------------------+
   | CO2_fugitivas_scc | Dióxido de carbono equivalente específico no          |
   |                   | intencionales de gases que se escapan durante la      |
   |                   | producción, procesamiento, transporte, almacenamiento |
   |                   | o distribución de combustibles, sin que exista        |
   |                   | combustión.                                           |
   +-------------------+-------------------------------------------------------+

**Tecnologías**

.. _table_techs_energy:
.. table:: Tecnologías incluidas en el modelo de Energía

   +------------------------+-----------------+
   | Descripción            | Código          |
   +========================+=================+
   | Blend diesel           | BLEND_DSL       |
   +------------------------+-----------------+
   | Blend gasoline         | BLEND_GSL       |
   +------------------------+-----------------+
   | Centros de Gas         | CENGASGSL       |
   | Gasoline               |                 |
   +------------------------+-----------------+
   | Centros de Gas LPG     | CENGASLPG       |
   +------------------------+-----------------+
   | Centros de Gas Propano | CENGASPRO       |
   +------------------------+-----------------+
   | Secondary - Power      | ELE_DISTR       |
   | Distribution           |                 |
   +------------------------+-----------------+
   | Secondary - Power      | ELE_TRANS       |
   | Transmission           |                 |
   +------------------------+-----------------+
   | Secondary -            | HYD_DISTR       |
   | Distribution of        |                 |
   | Hydrogen               |                 |
   +------------------------+-----------------+
   | Secondary - Green      | HYDPROBIO       |
   | Hydrogen Production -  |                 |
   | Biomass                |                 |
   +------------------------+-----------------+
   | Secondary - Green      | HYDPROELEGRI    |
   | Hydrogen Production -  |                 |
   | Electrolysis-Grid      |                 |
   +------------------------+-----------------+
   | Secondary - Green      | HYDPROELEISO    |
   | Hydrogen Production -  |                 |
   | Electrolysis-Isolated  |                 |
   | Systems                |                 |
   +------------------------+-----------------+
   | Secondary - Green      | HYDPRONGS       |
   | Hydrogen Production -  |                 |
   | Natural_Gas Reforming  |                 |
   +------------------------+-----------------+
   | Import/Distribution -  | IMPCOA          |
   | Coal                   |                 |
   +------------------------+-----------------+
   | Import - Petroleum     | IMPCOK          |
   | Coke                   |                 |
   +------------------------+-----------------+
   | Import - Crude         | IMPCRU          |
   +------------------------+-----------------+
   | Import - Electricity   | IMPELE          |
   +------------------------+-----------------+
   | Import/Distribution -  | IMPFOI          |
   | Fuel_Oil               |                 |
   +------------------------+-----------------+
   | Import/Distribution -  | IMPKJF          |
   | Kerosene and Jet Fuel  |                 |
   +------------------------+-----------------+
   | Import/Distribution -  | IMPLPG          |
   | LPG                    |                 |
   +------------------------+-----------------+
   | Imports - Natural_Gas  | IMPNGS          |
   | (LNG and               |                 |
   | Regasification)        |                 |
   +------------------------+-----------------+
   | Import/Distribution -  | IMPPURDSL       |
   | Pure Diesel            |                 |
   +------------------------+-----------------+
   | Import/Distribution -  | IMPPURGSL       |
   | Pure Gasoline          |                 |
   +------------------------+-----------------+
   | Distribution of        | NGS_DISTR       |
   | Natural_Gas            |                 |
   +------------------------+-----------------+
   | Power Plant Biogas -   | PP_BGSICE       |
   | Internal Combustion    |                 |
   | Engine                 |                 |
   +------------------------+-----------------+
   | Power Plant Biomass -  | PP_BMSTST       |
   | Steam Trubine          |                 |
   +------------------------+-----------------+
   | Power Plant            | PP_CHP          |
   | Sugarcane_Cogeneration |                 |
   +------------------------+-----------------+
   | Power Plant Coal       | PP_COA          |
   +------------------------+-----------------+
   | Power Plant Crude      | PP_CRU          |
   +------------------------+-----------------+
   | Power Plant Diesel -   | PP_DSLICE       |
   | Internal Combustion    |                 |
   | Engine                 |                 |
   +------------------------+-----------------+
   | Power Plant Diesel -   | PP_DSLTGS       |
   | Gas turbine            |                 |
   +------------------------+-----------------+
   | Power Plant Fuel_Oil - | PP_FOIICE       |
   | Internal Combustion    |                 |
   | Engine                 |                 |
   +------------------------+-----------------+
   | Power Plant Fuel_Oil - | PP_FOITST       |
   | Steam Trubine          |                 |
   +------------------------+-----------------+
   | Primary -              | PP_GEO          |
   | Transformation -       |                 |
   | Geothermal             |                 |
   +------------------------+-----------------+
   | Primary -              | PP_HYDAMADAMLAR |
   | Transformation -       |                 |
   | Hydroelectric Amazonas |                 |
   | dam (large)            |                 |
   +------------------------+-----------------+
   | Primary -              | PP_HYDAMADAMMED |
   | Transformation -       |                 |
   | Hydroelectric Amazonas |                 |
   | dam (medium)           |                 |
   +------------------------+-----------------+
   | Primary -              | PP_HYDAMADAMSMA |
   | Transformation -       |                 |
   | Hydroelectric Amazonas |                 |
   | dam (small)            |                 |
   +------------------------+-----------------+
   | Primary -              | PP_HYDAMARORLAR |
   | Transformation -       |                 |
   | Hydroelectric Amazonas |                 |
   | Run-of-the-river       |                 |
   | (large)                |                 |
   +------------------------+-----------------+
   | Primary -              | PP_HYDAMARORMED |
   | Transformation -       |                 |
   | Hydroelectric Amazonas |                 |
   | Run-of-the-river       |                 |
   | (medium)               |                 |
   +------------------------+-----------------+
   | Primary -              | PP_HYDAMARORSMA |
   | Transformation -       |                 |
   | Hydroelectric Amazonas |                 |
   | Run-of-the-river       |                 |
   | (small)                |                 |
   +------------------------+-----------------+
   | Primary -              | PP_HYDPACDAMLAR |
   | Transformation -       |                 |
   | Hydroelectric Pacific  |                 |
   | dam (large)            |                 |
   +------------------------+-----------------+
   | Primary -              | PP_HYDPACDAMMED |
   | Transformation -       |                 |
   | Hydroelectric Pacific  |                 |
   | dam (medium)           |                 |
   +------------------------+-----------------+
   | Primary -              | PP_HYDPACDAMSMA |
   | Transformation -       |                 |
   | Hydroelectric Pacific  |                 |
   | dam (small)            |                 |
   +------------------------+-----------------+
   | Primary -              | PP_HYDPACRORLAR |
   | Transformation -       |                 |
   | Hydroelectric Pacific  |                 |
   | Run-of-the-river       |                 |
   | (large)                |                 |
   +------------------------+-----------------+
   | Primary -              | PP_HYDPACRORMED |
   | Transformation -       |                 |
   | Hydroelectric Pacific  |                 |
   | Run-of-the-river       |                 |
   | (medium)               |                 |
   +------------------------+-----------------+
   | Primary -              | PP_HYDPACRORSMA |
   | Transformation -       |                 |
   | Hydroelectric Pacific  |                 |
   | Run-of-the-river       |                 |
   | (small)                |                 |
   +------------------------+-----------------+
   | Power Plant            | PP_NGSTGS       |
   | Natural_Gas - Gas      |                 |
   | turbine                |                 |
   +------------------------+-----------------+
   | Primary -              | PP_SPV_DG       |
   | Transformation - Solar |                 |
   | distributed            |                 |
   +------------------------+-----------------+
   | Primary -              | PP_SPV_US       |
   | Transformation -       |                 |
   | Photovoltaic           |                 |
   +------------------------+-----------------+
   | Primary -              | PP_SPV_US_H2    |
   | Transformation -       |                 |
   | Photovoltaic for H2    |                 |
   +------------------------+-----------------+
   | Power Plant Sugarcane  | PP_SUG          |
   +------------------------+-----------------+
   | Power Plant Waste -    | PP_WASICE       |
   | Internal Combustion    |                 |
   | Engine                 |                 |
   +------------------------+-----------------+
   | Primary -              | PP_WND_OF       |
   | Transformation -       |                 |
   | Offshore wind          |                 |
   +------------------------+-----------------+
   | Primary -              | PP_WND_OF_H2    |
   | Transformation -       |                 |
   | Offshore wind for H2   |                 |
   +------------------------+-----------------+
   | Primary -              | PP_WND_US       |
   | Transformation - Wind  |                 |
   +------------------------+-----------------+
   | Primary -              | PP_WND_US_H2    |
   | Transformation - Wind  |                 |
   | for H2                 |                 |
   +------------------------+-----------------+
   | Isolated - Petroleras  | PPICRUPETICE    |
   | - Power Plant Crude -  |                 |
   | Internal Combustion    |                 |
   | Engine                 |                 |
   +------------------------+-----------------+
   | Isolated - Petroleras  | PPICRUPETTST    |
   | - Power Plant Crude -  |                 |
   | Steam Turbine          |                 |
   +------------------------+-----------------+
   | Isolated - Cementeras  | PPIDSLCEMTST    |
   | - Power Plant Diesel - |                 |
   | Steam Trubine          |                 |
   +------------------------+-----------------+
   | Isolated - Rural       | PPIDSLELRICE    |
   | Electrification -      |                 |
   | Power Plant Diesel -   |                 |
   | Internal Combustion    |                 |
   | Engine                 |                 |
   +------------------------+-----------------+
   | Isolated - Rural       | PPIDSLELRTST    |
   | Electrification -      |                 |
   | Power Plant Diesel -   |                 |
   | Steam Trubine          |                 |
   +------------------------+-----------------+
   | Isolated - Galapagos - | PPIDSLGALICE    |
   | Power Plant Diesel -   |                 |
   | Internal Combustion    |                 |
   | Engine                 |                 |
   +------------------------+-----------------+
   | Isolated - Petroleras  | PPIDSLPETICE    |
   | - Power Plant Diesel - |                 |
   | Internal Combustion    |                 |
   | Engine                 |                 |
   +------------------------+-----------------+
   | Isolated - Petroleras  | PPIDSLPETTGS    |
   | - Power Plant Diesel - |                 |
   | Gas turbine            |                 |
   +------------------------+-----------------+
   | Isolated - Petroleras  | PPIFOIPETICE    |
   | - Power Plant Fuel_Oil |                 |
   | - Internal Combustion  |                 |
   | Engine                 |                 |
   +------------------------+-----------------+
   | Primary -              | PPIHYDAMACEM    |
   | Transformation -       |                 |
   | Cementeras -           |                 |
   | Hydroelectric Amazonas |                 |
   +------------------------+-----------------+
   | Primary -              | PPIHYDAMAELR    |
   | Transformation - Rural |                 |
   | Electrification -      |                 |
   | Hydroelectric Amazonas |                 |
   +------------------------+-----------------+
   | Primary -              | PPIHYDPACCEM    |
   | Transformation -       |                 |
   | Cementeras -           |                 |
   | Hydroelectric Pacific  |                 |
   +------------------------+-----------------+
   | Primary -              | PPIHYDPACELR    |
   | Transformation - Rural |                 |
   | Electrification -      |                 |
   | Hydroelectric Pacific  |                 |
   +------------------------+-----------------+
   | Isolated - Petroleras  | PPINGSPETICE    |
   | - Power Plant          |                 |
   | Natural_Gas - Internal |                 |
   | Combustion Engine      |                 |
   +------------------------+-----------------+
   | Isolated - Petroleras  | PPINGSPETTGS    |
   | - Power Plant          |                 |
   | Natural_Gas - Gas      |                 |
   | turbine                |                 |
   +------------------------+-----------------+
   | Isolated - Petroleras  | PPINGSPETTST    |
   | - Power Plant          |                 |
   | Natural_Gas - Steam    |                 |
   | Turbine                |                 |
   +------------------------+-----------------+
   | Primary -              | PPISPVELR       |
   | Transformation - Rural |                 |
   | Electrification -      |                 |
   | Solar PV               |                 |
   +------------------------+-----------------+
   | Primary -              | PPISPVGAL       |
   | Transformation -       |                 |
   | Galapagos - Solar PV   |                 |
   +------------------------+-----------------+
   | Primary -              | PPIWNDGAL       |
   | Transformation -       |                 |
   | Galapagos - Wind       |                 |
   +------------------------+-----------------+
   | Aceite de Piñón        | PROACG          |
   +------------------------+-----------------+
   | Production - Biogas    | PROBGS          |
   +------------------------+-----------------+
   | Produce biodiesel      | PROBIODSL       |
   +------------------------+-----------------+
   | Production - Biomass   | PROBMS          |
   +------------------------+-----------------+
   | Production - Crude     | PROCRU          |
   +------------------------+-----------------+
   | Produce etanol         | PROETA          |
   +------------------------+-----------------+
   | Production - Firewood  | PROFIR          |
   +------------------------+-----------------+
   | Production -           | PRONGS          |
   | Natural_Gas            |                 |
   +------------------------+-----------------+
   | Production - Sugarcane | PROSUG          |
   +------------------------+-----------------+
   | Production - Waste     | PROWAS          |
   +------------------------+-----------------+
   | Refineries             | REFCRU          |
   +------------------------+-----------------+
   | Refinery coke          | REFCRUCOK       |
   +------------------------+-----------------+
   | Refinery diesel        | REFCRUDSL       |
   +------------------------+-----------------+
   | Refinery Fuel_Oil      | REFCRUFOI       |
   +------------------------+-----------------+
   | Refinery gasoline      | REFCRUGSL       |
   +------------------------+-----------------+
   | Refinery KJF           | REFCRUKJF       |
   +------------------------+-----------------+
   | Refinery LPG           | REFCRULPG       |
   +------------------------+-----------------+
   | Refinery reduced oil   | REFCRURED       |
   +------------------------+-----------------+
   | Refinery Non energy    | REFNONENE       |
   +------------------------+-----------------+
   | Reserves - Crude       | RSVCRU          |
   +------------------------+-----------------+
   | Reserves - Natural Gas | RSVNGS          |
   +------------------------+-----------------+
   | Distribute Diesel for  | T4_DSLHEA       |
   | Heavy Freight          |                 |
   +------------------------+-----------------+
   | Distribute Diesel for  | T4_DSLLIG       |
   | Light Freight          |                 |
   +------------------------+-----------------+
   | Distribute Diesel for  | T4_DSLMED       |
   | Medium Freight         |                 |
   +------------------------+-----------------+
   | Distribute Diesel for  | T4_DSLPRI       |
   | Private                |                 |
   +------------------------+-----------------+
   | Distribute Diesel for  | T4_DSLPUB       |
   | Public                 |                 |
   +------------------------+-----------------+
   | Distribute Electricity | T4_ELEHEA       |
   | for Heavy Freight      |                 |
   +------------------------+-----------------+
   | Distribute Electricity | T4_ELELIG       |
   | for Light Freight      |                 |
   +------------------------+-----------------+
   | Distribute Electricity | T4_ELEMED       |
   | for Medium Freight     |                 |
   +------------------------+-----------------+
   | Distribute Electricity | T4_ELEPRI       |
   | for Private            |                 |
   +------------------------+-----------------+
   | Distribute Electricity | T4_ELEPUB       |
   | for Public             |                 |
   +------------------------+-----------------+
   | Distribute Gasoline    | T4_GSLHEA       |
   | for Heavy Freight      |                 |
   +------------------------+-----------------+
   | Distribute Gasoline    | T4_GSLLIG       |
   | for Light Freight      |                 |
   +------------------------+-----------------+
   | Distribute Gasoline    | T4_GSLMED       |
   | for Medium Freight     |                 |
   +------------------------+-----------------+
   | Distribute Gasoline    | T4_GSLPRI       |
   | for Private            |                 |
   +------------------------+-----------------+
   | Distribute Gasoline    | T4_GSLPUB       |
   | for Public             |                 |
   +------------------------+-----------------+
   | Distribute Hydrogen    | T4_HYDHEA       |
   | for Heavy Freight      |                 |
   +------------------------+-----------------+
   | Distribute Hydrogen    | T4_HYDMED       |
   | for Medium Freight     |                 |
   +------------------------+-----------------+
   | Distribute Hydrogen    | T4_HYDPUB       |
   | for Public             |                 |
   +------------------------+-----------------+
   | Distribute LPG for     | T4_LPGHEA       |
   | Heavy Freight          |                 |
   +------------------------+-----------------+
   | Distribute LPG for     | T4_LPGLIG       |
   | Light Freight          |                 |
   +------------------------+-----------------+
   | Distribute LPG for     | T4_LPGMED       |
   | Medium Freight         |                 |
   +------------------------+-----------------+
   | Distribute LPG for     | T4_LPGPRI       |
   | Private                |                 |
   +------------------------+-----------------+
   | Distribute LPG for     | T4_LPGPUB       |
   | Public                 |                 |
   +------------------------+-----------------+
   | Distribute Natural Gas | T4_NGSLIG       |
   | for Light Freight      |                 |
   +------------------------+-----------------+
   | Distribute Natural Gas | T4_NGSMED       |
   | for Medium Freight     |                 |
   +------------------------+-----------------+
   | Distribute Natural Gas | T4_NGSPRI       |
   | for Private            |                 |
   +------------------------+-----------------+
   | Distribute Natural Gas | T4_NGSPUB       |
   | for Public             |                 |
   +------------------------+-----------------+
   | Demand Biomass for     | T5BMSEXP        |
   | power for Exports      |                 |
   +------------------------+-----------------+
   | Demand for bunkers     | T5BUN           |
   +------------------------+-----------------+
   | Demand Petroleum Coke  | T5COKIND        |
   | for Industrial         |                 |
   +------------------------+-----------------+
   | Demand Crude for SOTE  | T5CRUCRUTRN     |
   +------------------------+-----------------+
   | Demand Crude Oil for   | T5CRUEXP        |
   | Exports                |                 |
   +------------------------+-----------------+
   | Demand Electricity for | T5ELEAGR        |
   | Agriculture            |                 |
   +------------------------+-----------------+
   | Demand Electricity for | T5ELECOM        |
   | Commercial             |                 |
   +------------------------+-----------------+
   | Demand Pure_Gasoline   | T5ELECON        |
   | for Construction       |                 |
   +------------------------+-----------------+
   | Demand Electricity for | T5ELECRUTRN     |
   | SOTE                   |                 |
   +------------------------+-----------------+
   | Demand Electricity for | T5ELEEXP        |
   | Exports                |                 |
   +------------------------+-----------------+
   | Demand Electricity for | T5ELEIND        |
   | Industrial             |                 |
   +------------------------+-----------------+
   | Demand Electricity for | T5ELERES        |
   | Residential            |                 |
   +------------------------+-----------------+
   | Demand Firewood for    | T5FIRIND        |
   | Industrial             |                 |
   +------------------------+-----------------+
   | Demand Firewood for    | T5FIRRES        |
   | Residential            |                 |
   +------------------------+-----------------+
   | Demand Fuel Oil for    | T5FOICOM        |
   | Commercial             |                 |
   +------------------------+-----------------+
   | Demand Fuel Oil for    | T5FOIEXP        |
   | Exports                |                 |
   +------------------------+-----------------+
   | Demand Fuel Oil for    | T5FOIIND        |
   | Industrial             |                 |
   +------------------------+-----------------+
   | Demand Fuel Oil for    | T5FOIREF        |
   | Refineries             |                 |
   +------------------------+-----------------+
   | Demand Fuel Oil for    | T5FOISHITRN     |
   | Shipping               |                 |
   +------------------------+-----------------+
   | Demand Gasoline for    | T5GSLCRUTRN     |
   | SOTE                   |                 |
   +------------------------+-----------------+
   | Demand Heat from       | T5HECIND        |
   | cogeneration for       |                 |
   | Industrial             |                 |
   +------------------------+-----------------+
   | Demand Hydrogen for    | T5HYDIND        |
   | Industrial             |                 |
   +------------------------+-----------------+
   | Demand Kerosene and    | T5KJFAERTRN     |
   | Jet Fuel for Air       |                 |
   | Transport              |                 |
   +------------------------+-----------------+
   | Demand Kerosene and    | T5KJFCON        |
   | Jet Fuel for           |                 |
   | Construction           |                 |
   +------------------------+-----------------+
   | Demand Kerosene and    | T5KJFREF        |
   | Jet Fuel for           |                 |
   | Refineries             |                 |
   +------------------------+-----------------+
   | Demand LPG for         | T5LPGAGR        |
   | Agriculture            |                 |
   +------------------------+-----------------+
   | Demand LPG for         | T5LPGCOM        |
   | Commercial             |                 |
   +------------------------+-----------------+
   | Demand LPG for         | T5LPGCON        |
   | Construction           |                 |
   +------------------------+-----------------+
   | Demand LPG for SOTE    | T5LPGCRUTRN     |
   +------------------------+-----------------+
   | Demand LPG for Exports | T5LPGEXP        |
   +------------------------+-----------------+
   | Demand LPG for         | T5LPGIND        |
   | Industrial             |                 |
   +------------------------+-----------------+
   | Demand GLP for         | T5LPGREF        |
   | Refineries             |                 |
   +------------------------+-----------------+
   | Demand LPG for         | T5LPGRES        |
   | Residential            |                 |
   +------------------------+-----------------+
   | Demand Natural Gas for | T5NGSIND        |
   | Industrial             |                 |
   +------------------------+-----------------+
   | Demand Natural Gas for | T5NGSRES        |
   | Residential            |                 |
   +------------------------+-----------------+
   | Demand Non energy for  | T5NOEAGR        |
   | Agriculture            |                 |
   +------------------------+-----------------+
   | Demand Non energy for  | T5NOECON        |
   | Construction           |                 |
   +------------------------+-----------------+
   | Demand Propane and Gas | T5PROGAS        |
   | for multiple           |                 |
   +------------------------+-----------------+
   | Demand Pure_Diesel for | T5PURDSLCOM     |
   | Commercial             |                 |
   +------------------------+-----------------+
   | Demand Pure_Diesel for | T5PURDSLCON     |
   | Construction           |                 |
   +------------------------+-----------------+
   | Demand Pure_Diesel for | T5PURDSLEXP     |
   | Exports                |                 |
   +------------------------+-----------------+
   | Demand Pure_Diesel for | T5PURDSLIND     |
   | Industrial             |                 |
   +------------------------+-----------------+
   | Demand Diesel for      | T5PURDSLREF     |
   | Refineries             |                 |
   +------------------------+-----------------+
   | Demand Pure_Diesel for | T5PURDSLSHITRN  |
   | Shipping               |                 |
   +------------------------+-----------------+
   | Demand Pure_Gasoline   | T5PURGSLAERTRN  |
   | for Air Transport      |                 |
   +------------------------+-----------------+
   | Demand Pure_Gasoline   | T5PURGSLAGR     |
   | for Agriculture        |                 |
   +------------------------+-----------------+
   | Demand Pure_Gasoline   | T5PURGSLCOM     |
   | for Commercial         |                 |
   +------------------------+-----------------+
   | Demand Pure_Gasoline   | T5PURGSLCON     |
   | for Construction       |                 |
   +------------------------+-----------------+
   | Demand Pure_Gasoline   | T5PURGSLEXP     |
   | for Exports            |                 |
   +------------------------+-----------------+
   | Demand Pure_Gasoline   | T5PURGSLIND     |
   | for Industrial         |                 |
   +------------------------+-----------------+
   | Demand Gasoline for    | T5PURGSLREF     |
   | Refineries             |                 |
   +------------------------+-----------------+
   | Demand Pure_Gasoline   | T5PURGSLSHITRN  |
   | for Shipping           |                 |
   +------------------------+-----------------+
   | Demand Reduced Crude   | T5REDCRUEXP     |
   | for Exports            |                 |
   +------------------------+-----------------+
   | Demand Sugarcane and   | T5SUGIND        |
   | subproducts for        |                 |
   | Industrial             |                 |
   +------------------------+-----------------+
   | Buses Diesel           | TRNBUSDSL       |
   +------------------------+-----------------+
   | Buses Electric         | TRNBUSELE       |
   +------------------------+-----------------+
   | Buses Hybrid Diesel    | TRNBUSHYBDSL    |
   +------------------------+-----------------+
   | Buses Hydrogen         | TRNBUSHYD       |
   +------------------------+-----------------+
   | Buses LPG              | TRNBUSLPG       |
   +------------------------+-----------------+
   | Buses Natural Gas      | TRNBUSNGV       |
   | Vehicular              |                 |
   +------------------------+-----------------+
   | Minivan Diesel         | TRNCAMDSL       |
   +------------------------+-----------------+
   | Minivan Electric       | TRNCAMELE       |
   +------------------------+-----------------+
   | Minivan Gasoline       | TRNCAMGSL       |
   +------------------------+-----------------+
   | Minivan Hybrid Diesel  | TRNCAMHYBDSL    |
   +------------------------+-----------------+
   | Minivan Hybrid         | TRNCAMHYBGSL    |
   | Gasoline               |                 |
   +------------------------+-----------------+
   | Minivan LPG            | TRNCAMLPG       |
   +------------------------+-----------------+
   | Minivan Natural Gas    | TRNCAMNGV       |
   | Vehicular              |                 |
   +------------------------+-----------------+
   | Catenary trucking      | TRNCATTRUELE    |
   | Electric               |                 |
   +------------------------+-----------------+
   | Transport of crude     | TRNCRU          |
   +------------------------+-----------------+
   | Heavy freight Diesel   | TRNFREHEADSL    |
   +------------------------+-----------------+
   | Heavy freight Electric | TRNFREHEAELE    |
   +------------------------+-----------------+
   | Heavy freight Gasoline | TRNFREHEAGSL    |
   +------------------------+-----------------+
   | Heavy freight Hybrid   | TRNFREHEAHYBDSL |
   | Diesel                 |                 |
   +------------------------+-----------------+
   | Heavy freight Hydrogen | TRNFREHEAHYD    |
   +------------------------+-----------------+
   | Heavy freight LPG      | TRNFREHEALPG    |
   +------------------------+-----------------+
   | Light freight Diesel   | TRNFRELIGDSL    |
   +------------------------+-----------------+
   | Light freight Electric | TRNFRELIGELE    |
   +------------------------+-----------------+
   | Light freight Gasoline | TRNFRELIGGSL    |
   +------------------------+-----------------+
   | Light freight Hybrid   | TRNFRELIGHYBDSL |
   | Diesel                 |                 |
   +------------------------+-----------------+
   | Light freight Hybrid   | TRNFRELIGHYBGSL |
   | Gasoline               |                 |
   +------------------------+-----------------+
   | Light freight LPG      | TRNFRELIGLPG    |
   +------------------------+-----------------+
   | Light freight Natural  | TRNFRELIGNGV    |
   | Gas Vehicular          |                 |
   +------------------------+-----------------+
   | Medium freight Diesel  | TRNFREMEDDSL    |
   +------------------------+-----------------+
   | Medium freight         | TRNFREMEDELE    |
   | Electric               |                 |
   +------------------------+-----------------+
   | Medium freight         | TRNFREMEDGSL    |
   | Gasoline               |                 |
   +------------------------+-----------------+
   | Medium freight Hybrid  | TRNFREMEDHYBDSL |
   | Diesel                 |                 |
   +------------------------+-----------------+
   | Medium freight         | TRNFREMEDHYD    |
   | Hydrogen               |                 |
   +------------------------+-----------------+
   | Medium freight LPG     | TRNFREMEDLPG    |
   +------------------------+-----------------+
   | Medium freight Natural | TRNFREMEDNGV    |
   | Gas Vehicular          |                 |
   +------------------------+-----------------+
   | Freight rail Diesel    | TRNFRERAIDSL    |
   +------------------------+-----------------+
   | Freight rail Electric  | TRNFRERAIELE    |
   +------------------------+-----------------+
   | Freight rail Hydrogen  | TRNFRERAIHYD    |
   +------------------------+-----------------+
   | Microbuses Diesel      | TRNMICDSL       |
   +------------------------+-----------------+
   | Microbuses Electric    | TRNMICELE       |
   +------------------------+-----------------+
   | Microbuses Gasoline    | TRNMICGSL       |
   +------------------------+-----------------+
   | Microbuses Hybrid      | TRNMICHYBDSL    |
   | Diesel                 |                 |
   +------------------------+-----------------+
   | Microbuses Hydrogen    | TRNMICHYD       |
   +------------------------+-----------------+
   | Microbuses LPG         | TRNMICLPG       |
   +------------------------+-----------------+
   | Motorcycles Electric   | TRNMOTELE       |
   +------------------------+-----------------+
   | Motorcycles Gasoline   | TRNMOTGSL       |
   +------------------------+-----------------+
   | Rail Diesel            | TRNPASRAIDSL    |
   +------------------------+-----------------+
   | Rail Electric          | TRNPASRAIELE    |
   +------------------------+-----------------+
   | Rail Hydrogen          | TRNPASRAIHYD    |
   +------------------------+-----------------+
   | Sedanes Diesel         | TRNSEDDSL       |
   +------------------------+-----------------+
   | Sedanes Electric       | TRNSEDELE       |
   +------------------------+-----------------+
   | Sedanes Gasoline       | TRNSEDGSL       |
   +------------------------+-----------------+
   | Sedanes Hybrid         | TRNSEDHYBGSL    |
   | Gasoline               |                 |
   +------------------------+-----------------+
   | Sedanes LPG            | TRNSEDLPG       |
   +------------------------+-----------------+
   | SUVs Diesel            | TRNSUVDSL       |
   +------------------------+-----------------+
   | SUVs Electric          | TRNSUVELE       |
   +------------------------+-----------------+
   | SUVs Gasoline          | TRNSUVGSL       |
   +------------------------+-----------------+
   | SUVs Hybrid Diesel     | TRNSUVHYBDSL    |
   +------------------------+-----------------+
   | SUVs Hybrid Gasoline   | TRNSUVHYBGSL    |
   +------------------------+-----------------+
   | SUVs LPG               | TRNSUVLPG       |
   +------------------------+-----------------+
   | SUVs Natural Gas       | TRNSUVNGV       |
   | Vehicular              |                 |
   +------------------------+-----------------+
   | Taxis Diesel           | TRNTAXDSL       |
   +------------------------+-----------------+
   | Taxis Electric         | TRNTAXELE       |
   +------------------------+-----------------+
   | Taxis Gasoline         | TRNTAXGSL       |
   +------------------------+-----------------+
   | Taxis Hybrid Diesel    | TRNTAXHYBDSL    |
   +------------------------+-----------------+
   | Taxis Hybrid Gasoline  | TRNTAXHYBGSL    |
   +------------------------+-----------------+
   | Taxis LPG              | TRNTAXLPG       |
   +------------------------+-----------------+
