|Snakemake| |Build Status| `snakemake
report <https://erblast.github.io/cookie_ds_demo//snakemake_report/>`__
|gitrepo|

cookie_ds_demo
==============

demo of `cookie_dc project
template <https://github.com/erblast/cookie_ds.git>`__

Run in docker container
-----------------------

::

   docker run -it --rm -v "$PWD":/app cookie_ds_demo

Docker compose
--------------

builds cookie_ds_demo and start a shell_1 and rstudio_1 container

::

   docker-compose up -d --build
   docker container exec -it cookie_ds_demo_shell_1 /bin/bash 
   docker-compose down

Execute
-------

.. code:: shell

   snakemake

Dryrun
------

.. code:: shell

   snakemake -n

Execute after code changes
--------------------------

.. code:: shell

   snakemake -R `snakemake --list-code-changes`

Force re-execution
------------------

.. code:: shell

   snakemake -F

Parallel Processing
-------------------

.. code:: shell

   snakemake --cores 3

Execute and build conda environment
-----------------------------------

The conda environment will be reconstructed from ``yml`` file and stored
in ``./.snakemake/conda``. A single conda environment can be defined for
each rule.

.. code:: shell

   conda env export --name cookie_ds_demo_env -f ./envs/cookie_ds_demo_env_debian.yml

.. code:: shell

   snakemake --use-conda

Test
----

All generalizable R functions are collected in an R package under
``cookiedsdemopkgr`` which is checked and tested

::

   snakemake test

Visualize workflow
------------------

.. code:: shell

   snakemake --dag | dot -Tpng > ./docs/wflow/wflow.png

|image3|

Build Report
------------

::

   snakemake report # executes rules for building report building blocks
   snakemake --report docs/snakemake_report/index.html

.. |Snakemake| image:: https://img.shields.io/badge/snakemake-≥5.6.0-brightgreen.svg?style=flat
   :target: https://snakemake.readthedocs.io
.. |Build Status| image:: https://travis-ci.org/erblast/cookie_ds_demo.svg?branch=master
   :target: https://travis-ci.org/erblast/cookie_ds_demo
.. |gitrepo| image:: https://icons-for-free.com/iconfiles/png/128/git+github+icon-1320191654571298174.png
   :target: https://github.com/erblast/cookie_ds_demo.git
.. |image3| image:: ./docs/wflow/wflow.png
