# The gdbplugins.

[![Build Status](https://travis-ci.org/jaryn/gdbplugins.svg?branch=master)](https://travis-ci.org/jaryn/gdbplugins)

Python plugins for gdb making debugging various languages with gdb easy.

## Installation

    pip install gdbplugins

Then you need to make sure the gdb loads the plugins. On RHEL and Fedora, this
should make it happen:

    sudo ln -s $(which _gdbplugin_loader) /etc/gdbinit.d/_gdbplugin_loader.py

Next time you start gdb, the plugins should load.
