#!/usr/bin/env python
try:
    import django
    print("Django is installed.")
    import config.settings
    print("Settings module is correctly found.")
except ImportError as e:
    print("Error importing modules:", e)
