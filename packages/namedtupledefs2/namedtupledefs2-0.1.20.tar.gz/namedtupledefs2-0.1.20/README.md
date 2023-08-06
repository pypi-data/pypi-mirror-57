namedtupledefs2 - Python2.7
===========================

The package *namedtupledefs2* provides a patched version of the factory class
*collections.namedtuple* with field defaults for *namedtuple*. The package
*namedtupledefs2* supports *Python2.7* syntax and adds *Jython* support. This
is a drop-in compatible patch with minimal changes only - basically one line
in the class template only.

	import namedtupledefs
	
	Point0 = namedtupledefs.namedtuple('Point', ('x', 'y', 'z'))
	Point1 = namedtupledefs.namedtuple('Point', ('x y z'))
	
	point0 = Point0(11, 22, 33) 
	point1 = Point1(11, 22, 33) 

the same with defaults:

	from namedtupledefs import namedtuple
	
	Point0defs = namedtupledefs.namedtuple('Point', ('x', 'y', 'z'), fielddefaults=(22, 33))
	Point1defs = namedtupledefs.namedtuple('Point', ('x y z'), fielddefaults=(22, 33))
	
	point0defs = Point0defs(11, 22) 
	point1defs = Point1defs(11) 

with the identical results:
	
	point0defs == point0 
	point1defs == point1 

of the printout:

	>>> point0
	Point(x=11, y=22, z=33)
	
	>>> point0defs
	Pointdefs(x=11, y=22, z=33)

The package 'namedtupledefs2' additionally provides the method *_merge* for the
created class with the accurate handling of *_fields* and *_fielddefaults*:

	msg_header._merge('NewClassName', msg_body, msg_data)

See doc-string for more examples.
For the standard library *collections.namedtuple* see Python documentation.

For the *Python3* syntax refer to *namedtupledefs3* or *namedtupledefs*.

**Online documentation**:

* https://namedtupledefs2.sourceforge.io/


**Runtime-Repository**:

* PyPI: https://pypi.org/project/namedtupledefs2/

  Install: *pip install namedtupledefs2*, see also section 'Install' of the online documentation.


**Downloads**:

* sourceforge.net: https://sourceforge.net/projects/namedtupledefs2/files/

* bitbucket.org: https://bitbucket.org/acue/namedtupledefs2

* github.com: https://github.com/ArnoCan/namedtupledefs2/

* pypi.org: https://pypi.org/project/namedtupledefs2/


Project Data
------------

* PROJECT: 'namedtupledefs2'

* MISSION: The extension of the standard *collections.namedtuple* by default values for *Python2.7*.

* VERSION: 00.01

* RELEASE: 00.01.020

* STATUS: alpha

* AUTHOR: Arno-Can Uestuensoez

* COPYRIGHT=Copyright (c) 2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez. 
	
* LICENSE=Artistic-License-2.0 + Forced-Fairplay-Constraints - see following clauses

Patches and this Documentation:

* COPYRIGHT=Copyright (c) 2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez. All rights reserved.

* PSF: In case of integration into standard libraries PSF LICENSE AGREEMENT FOR PYTHON.  

* This library: LICENSE=Artistic-License-2.0 + Forced-Fairplay-Constraints

Original code copied from Standard Python Library see "namedtupledefs.namedtuple_original":

* COPYRIGHT ORIGINAL=Copyright (c) 2001-2018 Python Software Foundation. All rights reserved.

* LICENSE ORIGINAL=PSF LICENSE AGREEMENT FOR PYTHON


Runtime Environment
-------------------
For a comprehensive list refer to the documentation.

**Python Syntax Support**

* Python2
  
  This package requires the *exec* statement/function, it is
  separated into two variants instead of using shared code.  
  For the Python3 refer to the package namedtupledefs3.

**Python Implementation Support**

*  CPython, IPython, IronPython, Jython, and PyPy


**OS on Server, Workstation, Laptops, Virtual Machines, and Containers**

* Linux: AlpineLinux, ArchLinux, CentOS, Debian, Fedora, Gentoo, OpenSUSE, Raspbian, RHEL, Slackware, SLES, Ubuntu, ...  

* BSD: DragonFlyBSD, FreeBSD, NetBSD, OpenBSD, GhostBSD, TrueOS, NomadBSD

* OS-X: Snow Leopard

* Windows: Win10, Win8.1, Win7, WinXP, Win2019, Win2016, Win2012, Win2008, Win2000

* WSL-1.0: Alpine, Debian, KaliLinux, openSUSE, SLES, Ubuntu

* Cygwin

* UNIX: Solaris10, Solaris11

* Minix: Minix3

* ReactOS

**Network and Security**

* Network Devices: OpenWRT

* Security: KaliLinux, pfSense, BlackArch, ParrotOS, Pentoo

**OS on Embedded Devices**

* RaspberryPI: ArchLinux, CentOS, OpenBSD, OpenWRT, Raspbian

* ASUS-TinkerBoard: Armbian

Current Release
---------------

Major Changes:

* Initial release.


ToDo:

* MicroPython, CircuitPython

Known Issues:

* not yet

