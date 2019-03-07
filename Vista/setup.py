#!/usr/bin/python
# -*- coding: utf-8 -*-
import cx_Freeze

executables = [cx_Freeze.Executable("Vistas.py",
                                    base="Win32GUI",
                                    icon="../iconosSILD/iconSILD1.ico")]

build_exe_options = {"packages": [],
                     "include_files": ["../GUI/SILD.ui",
                                       "../iconosSILD/iconSILD.jpg",
                                       "../iconosSILD/labdental1.jpg",
                                       "../iconosSILD/logo.PNG"]}

cx_Freeze.setup(
    name="SILD",
    version="1.0",
    description="Laboraorio Dental",
    options={"build_exe": build_exe_options},
    executables=executables
)