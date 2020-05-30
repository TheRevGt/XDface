# -*- coding: utf-8 -*-
"""
Created on Fri May 29 10:37:46 2020

@author: Gerson
"""

#!/usr/bin/env python 

import subprocess


scripts_paths = ("dataset.py")

ps = [subprocess.Popen(["python", script]) for script in scripts_paths]
exit_codes = [p.wait() for p in ps]

if not any(exit_codes):
    print("Todos los procesos terminaroin con éxito")
else:
    print("Algunos procesos terminaron de forma inesperada.")