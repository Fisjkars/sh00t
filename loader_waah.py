import json
import os
import django

#
# WAAH Methodology loader.
#

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sh00t.settings")
django.setup()

from app.models import Methodology, Module, Case

current_methodology = Methodology.objects.filter(name="WAHH")
if not current_methodology :
    methodology_master = Methodology(name="WAHH")
    methodology_master.save()
    wahh_file = open('data/wahh.json',  'rt', encoding='latin1')
    methodology = json.load(wahh_file)

    for method in methodology['checklist']['Functionality']:
        module_master = Module(name=method, methodology=methodology_master)
        module_master.save()
        for case in methodology['checklist']['Functionality'][method]['tests']:
            descriptions_json = methodology['checklist']['Functionality'][method]['tests'][case]['description']
            description_consolidated = ""
            for description in descriptions_json:
                description_consolidated = description_consolidated + description + '\n\n'
            case = Case(name=case, description=description_consolidated, module=module_master)
            case.save()
    print("Waah methodology has been imported !")
else :
    print("Waah methodology was already present in Sh00t!. No changes has been made.")
