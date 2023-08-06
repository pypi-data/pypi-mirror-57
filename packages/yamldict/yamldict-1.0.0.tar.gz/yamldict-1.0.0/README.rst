A library that allows accessing ``yaml`` content as a kind of a
dictionary.

Features
========

1. **not** a dictionary. That means properties such as ``get`` are still
   accessible from the object.

2. Accessible via properties, *and* via indexes:

   .. code:: python

       assert myyaml["item"] == myyaml.item

3. Handles missing properties *without creating them* unless asked:

   .. code:: python

       assert not myyaml.this.property.does.not.exist
       myyaml.this.property = "3"  # only now the content is actually in the data

4. Serializable

Installation
============

.. code:: sh

    pip install yamldict
