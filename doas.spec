Name:     doas
Version:  6.3p2
Release:  1
Summary:  A port of OpenBSD's doas which runs on FreeBSD, Linux, NetBSD, and illumos
License:  BSD-2-Clause License
URL:      https://github.com/slicer69/doas/
Source0:  https://github.com/slicer69/doas/archive/%{version}.tar.gz
BuildArch: noarch

%description
Jesse Smith (slicer69) port of OpenBSD's doas which runs on FreeBSD, Linux, NetBSD, illumos and macOS.

The doas utility is a program originally written for OpenBSD which allows a user to run a command as though they were another user. Typically doas is used to allow non-privleged users to run commands as though they were the root user. The doas program acts as an alternative to sudo, which is a popular method in the Linux community for granting admin access to specific users.

The doas program offers two benefits over sudo: its configuration file has a simple syntax and it is smaller, requiring less effort to audit the code. This makes it harder for both admins and coders to make mistakes that potentially open security holes in the system.

This port of doas has been made to work on FreeBSD 11.x and newer, most distributions of Linux, NetBSD 8.x and newer, and most illumos distributions (tested on OmniOS and SmartOS). It also works on macOS Catalina.

#-- CHANGELOG -----------------------------------------------------------------#

%changelog
* Fri Aug 7 2020 23 commits to master since this release

- This release introduces a new utility called vidoas (vi doas). This tool is a shell script which creates a copy of the doas.conf file, allows the admin to edit the file, and then checks its syntax for errors. If a problem is found, vidoas reports which line the error was on and asks us to try editing the file again. Once the new doas.conf file contains the proper syntax, it is installed and overwrites the old doas.conf file.

- This tool is designed to assist admins and avoid introducing errors to doas.conf which might accidentally revoke admin access to the machine.
