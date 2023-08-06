Python for Data Loss Prevention (DLP) TEST
==========================================
Quick Start
-----------

Installation
~~~~~~~~~~~~

Install this library in a `virtualenv`_ using pip. `virtualenv`_ is a tool to
create isolated Python environments. The basic problem it addresses is one of
dependencies and versions, and indirectly permissions.

With `virtualenv`_, it's possible to install this library without needing system
install permissions, and without clashing with the installed system
dependencies.

.. _`virtualenv`: https://virtualenv.pypa.io/en/latest/


Supported Python Versions
^^^^^^^^^^^^^^^^^^^^^^^^^
Python >= 2.7.14

Deprecated Python Versions
^^^^^^^^^^^^^^^^^^^^^^^^^^
Python == 2.7. Python 2.7 support will be removed on January 1, 2020.


Linux
^^^^^^^^^

.. code-block:: console

    pip install virtualenv
    <your-env>/bin/pip install lib2dlp


Windows
^^^^^^^

.. code-block:: console

    pip install virtualenv
    <your-env>\Scripts\pip.exe install lib2dlp

Preview
~~~~~~~

QQCapture
^^^^^^^^^^^^^^^^

.. code:: py

	def QQCapture():
		sysstr = platform.architecture()
		if sysstr[0] == '64bit':
			print u"暂不支持64位系统"
			return False
		else:  
			try:
				dll = ctypes.cdll.LoadLibrary("lib\\CameraDll.dll")
			except Exception as e:
				print("Dll load error!")
				return
			else:
				try:
				   dll.CameraSubArea(0)
				except Exception as e:
				   print("Sth wrong in capture!")
				   return True
			return True