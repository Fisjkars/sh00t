import json
import os
import django

#
# OWASP testing guide v4 Methodology loader.
#

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sh00t.settings")
django.setup()

from configuration.models import MethodologyMaster, ModuleMaster, CaseMaster

current_methodology = MethodologyMaster.objects.filter(name="OWASP Testing Guide V4")
if not current_methodology :
    methodology_master = MethodologyMaster(name="OWASP Testing Guide V4")
    methodology_master.save()
    owasp_file = open('configuration/data/owasp_testing_guide_v4.json', 'r')
    methodology = json.load(owasp_file)
    for method in methodology['modules']:
        module_master = ModuleMaster(name=method, methodology=methodology_master, order=methodology['modules'][method]['order'])
        module_master.save()
        for case in methodology['modules'][method]['tests']:
            order = '2' + str(methodology['modules'][method]['order']) + str(methodology['modules'][method]['tests'][case]['order'])
            steps = methodology['modules'][method]['tests'][case]['steps']
            steps_consolidated = ""
            for step in steps:
                steps_consolidated = steps_consolidated + step + '\n\n'
            case = CaseMaster(name=case, description=steps_consolidated, module=module_master, order=order)
            case.save()
    print("OWASP Testing Guide V4 methodology has been imported !")
else :
    print("OWASP Testing Guide V4 methodology was already present in Sh00t!. No changes has been made.")