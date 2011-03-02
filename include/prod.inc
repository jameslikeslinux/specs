#
# Default settings for GNOME packages on Solaris
#
# Copyright 2007 Sun Microsystems, Inc.
#
SUNW_ProdName:             GNOME
SUNW_ProdVers:             2.23.4

%define default_pkg_version 2.23.4

%{?jds_version:#}%define jds_version JDSosol
%define default_category   GNOME2,application,%{jds_version}
%{?support_level:#}%define support_level      unsupported

Vendor:			   Sun Microsystems, Inc.

%define                    pkg_prefix SUNW

# ChangeLog:
# 2007-09-27  Laszlo (Laca) Peter  <laca@sun.com>
# - move tjds build option to options.inc
# 2007-03-15  Laszlo (Laca) Peter  <laca@sun.com>
# - create by moving product specific stuff out of Solaris.inc
