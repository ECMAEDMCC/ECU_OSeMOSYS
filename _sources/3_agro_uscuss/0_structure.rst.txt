===================================
Estructura del modelo
===================================

Los sectores Agricultura y USCUSS fueron modelados de manera conjunta,
utilizando una única estructura para estos 2 sectores, similar a la
planteada en el PLANMICC. Este modelo no corresponde únicamente al
PLANMICC, sino que integra información actualizada de la NDC.

En particular:

- Del PLANMICC se toman las estructuras base de tecnologías y factores
  de emisión y datos históricos

- Del NDC se toman datos de actividad, factores de emisión actualizados
  con información de la 5CN2BTR

**Representación Gráfica del Modelo**

El modelo de los sectores Agricultura y USCUSS fue estructurado a partir
de la base desarrollada en el PLANMICC (Proyecto CZZ 2739), no se
aumentaron tecnologías ni se adicionaron variables únicamente se
actualizó información.

En la :numref:`agro_uscuss_model_structure` se presenta la estructura final del modelo de Agricultura
y USCUSS que constituye el insumo de referencia para el sector.


.. figure:: ../_static/images/agro_uscuss/model_structure.png
   :align: center
   :name: agro_uscuss_model_structure
   :alt: Estructura base del Modelo de Agricultura y USCUSS.

   Estructura base del Modelo de Agricultura y USCUSS

En la :numref:`table_agro_uscuss_techs` se detallan los nombres de las tecnologías/fuels y las
unidades de la actividad de cada tecnología/fuel acorde a Proyecto
PLANMICC mismos que se encuentran en los documentos:

.. _table_agro_uscuss_techs:
.. table:: Tecnologías incluidas en el modelo del sector Residuos.

   +------------+---------------------------+-------------------------+------------+
   | Tipo de    | Nomenclatura              |   Detalle               | Unidades   |
   | Set        |                           |                         | físicas    |
   +============+===========================+=========================+============+
   | Tecnología | Banano                    | Área de cultivo         | Mha        |
   |            |                           | cosechado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Arroz                     | Área de cultivo         | Mha        |
   |            |                           | cosechado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Cacao                     | Área de cultivo         | Mha        |
   |            |                           | cosechado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Cafe                      | Área de cultivo         | Mha        |
   |            |                           | cosechado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Cana                      | Área de cultivo         | Mha        |
   |            |                           | cosechado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Maiz                      | Área de cultivo         | Mha        |
   |            |                           | cosechado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Palma                     | Área de cultivo         | Mha        |
   |            |                           | cosechado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Soya                      | Área de cultivo         | Mha        |
   |            |                           | cosechado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Palmito                   | Área de cultivo         | Mha        |
   |            |                           | cosechado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Legumbres                 | Área de cultivo         | Mha        |
   |            |                           | cosechado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Cereales                  | Área de cultivo         | Mha        |
   |            |                           | cosechado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Tuberculos                | Área de cultivo         | Mha        |
   |            |                           | cosechado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Fruta                     | Área de cultivo         | Mha        |
   |            |                           | cosechado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Verduras                  | Área de cultivo         | Mha        |
   |            |                           | cosechado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Floricolas                | Área de cultivo         | Mha        |
   |            |                           | cosechado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Otros_cultivos            | Área de cultivo         | Mha        |
   |            |                           | cosechado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Exp_Banano                | Volumen de producto     | Mton       |
   |            |                           | exportado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Exp_Arroz                 | Volumen de producto     | Mton       |
   |            |                           | exportado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Exp_Cacao                 | Volumen de producto     | Mton       |
   |            |                           | exportado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Exp_Cafe                  | Volumen de producto     | Mton       |
   |            |                           | exportado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Exp_Cana                  | Volumen de producto     | Mton       |
   |            |                           | exportado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Exp_Maiz                  | Volumen de producto     | Mton       |
   |            |                           | exportado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Exp_Palma                 | Volumen de producto     | Mton       |
   |            |                           | exportado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Exp_Soya                  | Volumen de producto     | Mton       |
   |            |                           | exportado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Exp_Palmito               | Volumen de producto     | Mton       |
   |            |                           | exportado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Exp_Legumbres             | Volumen de producto     | Mton       |
   |            |                           | exportado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Exp_Cereales              | Volumen de producto     | Mton       |
   |            |                           | exportado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Exp_Tuberculos            | Volumen de producto     | Mton       |
   |            |                           | exportado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Exp_Fruta                 | Volumen de producto     | Mton       |
   |            |                           | exportado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Exp_Verduras              | Volumen de producto     | Mton       |
   |            |                           | exportado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Exp_Floricolas            | Volumen de producto     | Mton       |
   |            |                           | exportado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Imp_Banano                | Volumen de producto     | Mton       |
   |            |                           | importado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Imp_Arroz                 | Volumen de producto     | Mton       |
   |            |                           | importado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Imp_Cacao                 | Volumen de producto     | Mton       |
   |            |                           | importado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Imp_Cafe                  | Volumen de producto     | Mton       |
   |            |                           | importado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Imp_Cana                  | Volumen de producto     | Mton       |
   |            |                           | importado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Imp_Maiz                  | Volumen de producto     | Mton       |
   |            |                           | importado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Imp_Palma                 | Volumen de producto     | Mton       |
   |            |                           | importado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Imp_Soya                  | Volumen de producto     | Mton       |
   |            |                           | importado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Imp_Palmito               | Volumen de producto     | Mton       |
   |            |                           | importado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Imp_Legumbres             | Volumen de producto     | Mton       |
   |            |                           | importado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Imp_Cereales              | Volumen de producto     | Mton       |
   |            |                           | importado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Imp_Tuberculos            | Volumen de producto     | Mton       |
   |            |                           | importado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Imp_Fruta                 | Volumen de producto     | Mton       |
   |            |                           | importado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Imp_Verduras              | Volumen de producto     | Mton       |
   |            |                           | importado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Imp_Floricolas            | Volumen de producto     | Mton       |
   |            |                           | importado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Pastizales                | Área de categoría de    | Mha        |
   |            |                           | suelo                   |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Humedal                   | Área de categoría de    | Mha        |
   |            |                           | suelo                   |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Zona_atropica             | Área de categoría de    | Mha        |
   |            |                           | suelo                   |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Otras_tierras             | Área de categoría de    | Mha        |
   |            |                           | suelo                   |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Bosque_nativo_protegido   | Área de bosque con      | Mha        |
   |            |                           | algún régimen de        |            |
   |            |                           | protección legal: Socio |            |
   |            |                           | Bosque, SNAP, BVP       |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Bosque_nativo_sinproteger | Área de bosque sin      | Mha        |
   |            |                           | régimen de protección   |            |
   |            |                           | legal                   |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Plantacion_forestal       | Área de Plantaciones    | Mha        |
   |            |                           | Forestales              |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Ganaderia_importada       | Área de ganado bobino   | Mha        |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Ganaderia_criolla         | Área de ganado bobino   | Mha        |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Ganaderia_mestiza         | Área de ganado bobino   | Mha        |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Exp_Carne                 | Volumen de producto     | Mton       |
   |            |                           | exportado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Exp_Leche                 | Volumen de producto     | Mton       |
   |            |                           | exportado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Imp_Carne                 | Volumen de producto     | Mton       |
   |            |                           | importado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Imp_Leche                 | Volumen de producto     | Mton       |
   |            |                           | importado               |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Gallinas_campos           | Cantidad de aves de     | k cabezas  |
   |            |                           | corral                  |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Gallinas_planteles        | Cantidad de aves de     | k cabezas  |
   |            |                           | corral                  |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Pasturas                  | Área de categoría de    | Mha        |
   |            |                           | suelo                   |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Vacuno_porcino            | Cantidad de cabeza de   | k cabezas  |
   |            |                           | ganado                  |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Vacuno_ovino              | Cantidad de cabeza de   | k cabezas  |
   |            |                           | ganado                  |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Vacuno_otras_especies     | Cantidad de cabeza de   | k cabezas  |
   |            |                           | ganado                  |            |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | Cambio_de_uso             | /                       |   /        |
   +------------+---------------------------+-------------------------+------------+
   | Tecnología | area_restaurada           | /                       |   /        |
   +------------+---------------------------+-------------------------+------------+
