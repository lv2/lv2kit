########
Overview
########

.. default-domain:: c
.. highlight:: c

LV2Kit includes several libraries that can be useful in different contexts.
Typically, hosts use Lilv to discover and load plugins,
and Suil to load plugin UIs.
Simple plugins often depend only on the LV2 specification itself,
but some may use Pugl to implement a portable UI.
Lilv is built atop the lower level libraries Sratom and Serd,
which can also be used directly for more advanced data storage,
transmission, and transformation.

.. image:: ../_static/lv2kit_structure.svg
  :width: 70%
  :align: center
  :alt: LV2Kit Module Structure

.. toctree::

   lilv_overview
   suil_overview
   sratom_overview
   serd_overview
   exess_overview
