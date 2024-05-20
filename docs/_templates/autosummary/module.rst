{# Create index section with title 'title'. Each element of the 'item_list' list is a section item #}
{# Does not create the section if the 'item_list' list is empty #}
{# Need to be used inside a '.. automodule::' directive '#}
{% macro create_index_section(title, item_list) -%}

   {% if item_list %}
   .. rubric:: {{title | capitalize}}
   .. autosummary::

      {% for item in item_list -%}
      {{ item }}
      {% endfor %}
   {%- endif %}

{%- endmacro %}


{{ name | escape | underline }}

{# 1: Add 'fullname' prefix #}
{# 2: escape especial characters like '.' to avoid being interpreted as other things ##}
{# 3: add a underline to the name #}
{# 4: Remove the last newline character (if any) #}
{# 5: extends the '-----' line to cover the 'fullname: ' prefix #}
{{ "fullname: " ~ fullname | escape | underline('-') | replace('-\n', '-')}}----------------


{# If is a single module #}
{% if not modules %}

{# Add a link to the module file  #}
:code: `{{ name }}.py <{{project_web_link}}/{{ fullname | replace('.','/') }}.py>`_

{# If is a package with some modules #}
{% else %}

{# Add a link to the module folder #}
:folder: `{{ name }} <{{project_web_link}}/{{ fullname | replace('.','/') }}>`_

{% endif %}


{# Module documentation #}

.. automodule:: {{ fullname }}
   {{ create_index_section('classes', classes) }}
   {{ create_index_section('functions', functions) }}
   {{ create_index_section('exceptions', exceptions) }}
   {{ create_index_section('attributes', attributes) }}

   {# If is a single module, add a header to separate the index from the module contents #}
   {% if not modules %}

   Module contents
   ^^^^^^^^^^^^^^^

   {% endif %}


{# If is a package with some modules, shows its modules #}
{% if modules %}

.. rubric:: Package modules

.. autosummary::
   :toctree: {{name}}
   :recursive:

   {% for module in modules -%}
   {{ module }}
   {% endfor %}

{% endif %}


.. vi: tabstop=3 softtabstop=3 shiftwidth=3
