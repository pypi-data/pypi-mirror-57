Installing COT
==============

.. contents::
  :local:

System requirements
-------------------

* COT requires either Python 2.7 or Python 3.4 or later.
* COT is tested to work under Mac OS X and Ubuntu Linux and similar distros.
* COT now has limited support for CentOS and related distros as well.

Installing COT using ``pip``
----------------------------

Since COT is written in Python, it can be installed like any other Python
package using the pip_ tool. For most users this is the recommended
installation method.

::

  sudo pip install cot

or, to install for the current user only (typically installing to ``~/.local/``):

::

  pip install --user cot

If you have already installed COT and wish to update to the latest available version:

::

  sudo pip install --upgrade cot

or

::

  pip install --user --upgrade cot

Installing optional features
''''''''''''''''''''''''''''

COT has a number of optional Python package dependencies that enable optional
features. If you want to use these features, you can instruct ``pip`` to
install them as part of the COT installation process, or you can install them
separately after the fact.

* Tab-completion of COT CLI parameters in ``bash``, enabled with the
  `argcomplete`_ package.

  ::

     sudo pip install cot[tab-completion]

  or

  ::

     sudo pip install argcomplete

  .. note::
     After installing `argcomplete`_ by either method, you must configure
     your ``bash`` environment to enable it. Refer to the argcomplete
     documentation for the required steps.

Installing COT from source
--------------------------

If you wish to install bleeding-edge unreleased code or make code
contributions of your own, you can install COT from source as described below.

Downloading COT
'''''''''''''''

You can download COT via Git or using HTTP.

::

  git clone git://github.com/glennmatthews/cot
  cd cot

or

::

  wget -O cot.tgz https://github.com/glennmatthews/cot/archive/master.tar.gz
  tar zxf cot.tgz
  cd cot-master

or

::

  curl -o cot.tgz https://github.com/glennmatthews/cot/archive/master.tar.gz
  tar zxf cot.tgz
  cd cot-master

Install the COT libraries and script
''''''''''''''''''''''''''''''''''''

::

  sudo python setup.py install

Troubleshooting
---------------

"ValueError: Expected version spec"
'''''''''''''''''''''''''''''''''''

If you get an error like 

::

  ValueError: ('Expected version spec in', 'enum34; python_version < "3.4"', 'at', '; python_version < "3.4"')

then you may need to update your version of ``pip`` and/or ``setuptools``:

::

  sudo pip install --upgrade pip setuptools

Installing helper programs
--------------------------

Certain COT features require helper programs - you can install these as part
of the COT installation process, or they can be installed as-needed by COT:

* COT uses `qemu-img`_ as a helper program for various operations involving
  the creation, inspection, and modification of hard disk image files
  packaged in an OVF.
* The ``cot add-disk`` command requires either `qemu-img`_ (version 2.1 or
  later) or vmdktool_ as a helper program when adding hard disks to an OVF.
* The ``cot inject-config`` command requires mkisofs_ (or its fork
  ``genisoimage``) and/or xorriso_ to create ISO (CD-ROM) images for
  platforms that use ISOs to package the configuration.
* Similarly, for platforms using hard disks for bootstrap configuration,
  ``cot inject-config`` requires `fatdisk`_ to format hard disk images.
* The ``cot deploy ... esxi`` command requires ovftool_ to communicate
  with an ESXi server. If ovftool is installed, COT's automated unit tests
  will also make use of ovftool to perform additional verification that
  OVFs and OVAs created by COT align with VMware's expectations for these
  file types.

COT can attempt to install these tools using the appropriate package manager
for your platform (i.e., MacPorts_ or Homebrew_ for Mac OS X, and either ``apt-get`` or
``yum`` for Linux).

.. warning::
  Unfortunately, VMware requires a site login to download ovftool_, so if you
  need this tool, you will have to install it yourself. COT cannot install it
  for you at present.

To let COT attempt to pre-install all of the above helpers, you can optionally
run:

::

  cot install-helpers

See :doc:`here <usage_install_helpers>` for more details.

If you skip this step, then when you are running COT, and it encounters the
need for a helper that has not been installed, COT will prompt you to allow it
to install the helper in question.

.. _pip: https://pip.pypa.io/en/stable/
.. _qemu-img: http://www.qemu.org
.. _vmdktool: http://www.freshports.org/sysutils/vmdktool/
.. _mkisofs: http://cdrecord.org/
.. _xorriso: https://www.gnu.org/software/xorriso/
.. _fatdisk: http://github.com/goblinhack/fatdisk
.. _ovftool: https://www.vmware.com/support/developer/ovf/
.. _MacPorts: http://www.macports.org/
.. _Homebrew: https://brew.sh/
.. _argcomplete: https://argcomplete.readthedocs.io/en/latest/
