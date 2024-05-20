#!/bin/bash


python3 -m venv .venv
source .venv/bin/activate
PYGOBJECT_STUB_CONFIG=Gtk4,Gdk4 pip3 install --no-cache-dir PyGObject-stubs
pip install --editable .
