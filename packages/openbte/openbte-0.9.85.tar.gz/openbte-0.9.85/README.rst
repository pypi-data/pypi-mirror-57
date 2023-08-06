Description
===========

Space-dependent Boltzmann transport equation solver for phonons

Community
=========

`Mailing list <https://groups.google.com/forum/#!forum/openbte>`_


Reference
=========

`G. Romano et al. J. Heat Transfer (2015) <https://heattransfer.asmedigitalcollection.asme.org/article.aspx?articleid=2119334>`_


Installation
====================

The easiest way to install OpenBTE on Linux/MacOS/Windows is through Anaconda:

1) Install Anaconda 3
2) On Anaconda Prompt type:

.. code-block:: shell

  conda create -n openbte python=3.6
  activate openbte
  conda install -c conda-forge -c gromano openbte
  
  
For Windows you will have to install MSMPI

If you want to avoid installing Anaconda, you can still use the pip system (see below)

Linux
---------------------------------------------------------------

Requirements:

apt-get install -y libopenmpi-dev 

pip install --upgrade openbte     

Note that some users report that Gmsh does not work properly if installed via the package manager and launched in parallel. If you have trouble, install Gmsh via command line

.. code-block:: shell

  wget http://geuz.org/gmsh/bin/Linux/gmsh-3.0.0-Linux64.tgz
  tar -xzf gmsh-3.0.0-Linux64.tgz
  cp gmsh-3.0.0-Linux/bin/gmsh /usr/bin/
  rm -rf gmsh-3.0.0-Linux
  rm gmsh-3.0.0-Linux64.tgz




MacOS
---------------------------------------------------------------

You will have to install gmsh from source, then type

.. code-block:: shell

  pip install --no-cache-dir --upgrade openbte 


Tutorial
=======

 `Nongray disordered material  <https://colab.research.google.com/drive/1eAfX3PgyO7TyGWPee8HRx5ZbQ7tZfLDr>`_

Example
=======

.. code-block:: python

  from openbte import Material,Geometry,Solver,Plot

  #Create material file
  Material(filename='Si-300K.dat')

  #Create geometry file
  Geometry(porosity=0.30,lx=100,ly=100,step=10,shape='square')

  #Create solver file
  Solver(multiscale=True,max_bte_error=1e-2)

  #Plot the temperature map
  Plot(variable='map/temperature',iso_values=True)


.. image:: flux.png
   :height: 400 px
   :width: 400 px
   :scale: 25 %
   :align: left


