import django_tables2 as tables

from .models import Project, Flag, Sh0t, Assessment, Project, Template, MethodologyMaster, ModuleMaster, CaseMaster


"""ProjectTable class."""
class ProjectTable(tables.Table):

    selection = tables.CheckBoxColumn(accessor='pk', attrs={"th__input": {"onclick": "toggle(this)"}}, orderable=False)
    name = tables.TemplateColumn('<a href="/app/project/{{ record.pk }}/summary"> {{ record.name }}</a>')

    class Meta:
        model = Project
        template_name = "django_tables2/bootstrap-responsive.html"
        sequence = ('selection', 'name', 'added')
        fields = ('name', 'added')


"""ProjectTable class."""
class FlagTable(tables.Table):

    selection = tables.CheckBoxColumn(accessor='pk', attrs={"th__input": {"onclick": "toggle(this)"}}, orderable=False)
    name = tables.TemplateColumn('<a href="/app/flag/{{ record.pk }}"> {{ record.title }}</a>')
    done = tables.BooleanColumn(yesno='done,')
    project = tables.TemplateColumn('<a href="/app/project/{{ record.assessment.project.pk}}/summary">{{ record.assessment.project }}</a>')
    assessment = tables.TemplateColumn('<a href="/app/assessment/{{ record.assessment.pk}}">{{ record.assessment }}</a>')

    class Meta:
        model = Flag
        template_name = "django_tables2/bootstrap-responsive.html"
        sequence = ('selection', 'name', 'done', 'project', 'assessment', 'added')
        fields = ('name', 'added', 'done', 'project', 'assessment')
        empty_text = "No Flags yet"


"""ProjectTable class."""
class OpenFlagTable(tables.Table):

    selection = tables.CheckBoxColumn(accessor='pk', attrs={"th__input": {"onclick": "toggle(this)"}}, orderable=False)
    name = tables.TemplateColumn('<a href="/app/flag/{{ record.pk }}"> {{ record.title }}</a>')
    project = tables.TemplateColumn('<a href="/app/project/{{ record.assessment.project.pk}}/summary">{{ record.assessment.project }}</a>')
    assessment = tables.TemplateColumn('<a href="/app/assessment/{{ record.assessment.pk}}">{{ record.assessment }}</a>')

    class Meta:
        model = Flag
        template_name = "django_tables2/bootstrap-responsive.html"
        sequence = ('selection', 'name', 'project', 'assessment', 'added')
        fields = ('name', 'added', 'project', 'assessment')


"""ProjectTable class."""
class Sh0tTable(tables.Table):

    selection = tables.CheckBoxColumn(accessor='pk', attrs={"th__input": {"onclick": "toggle(this)"}}, orderable=False)
    severity = tables.TemplateColumn('<span class="bc-badge bc-badge--p{{ record.severity }}">P{{ record.severity }}</span>')
    title = tables.TemplateColumn('<a href="/app/sh0t/{{ record.pk }}">{{ record.title }}</a>')
    project = tables.TemplateColumn('<a href="/app/project/{{ record.assessment.project.pk}}/summary">{{ record.assessment.project }}</a>', order_by=('assessment.project'))
    assessment = tables.TemplateColumn('<a href="/app/assessment/{{ record.assessment.pk}}">{{ record.assessment }}</a>')

    class Meta:
        model = Sh0t
        template_name = "django_tables2/bootstrap-responsive.html"
        sequence = ('selection','severity', 'title', 'project', 'assessment', 'added')
        fields = ('severity', 'title', 'project', 'assessment', 'added')


"""ProjectTable class."""
class AssessmentTable(tables.Table):

    selection = tables.CheckBoxColumn(accessor='pk', attrs={"th__input": {"onclick": "toggle(this)"}}, orderable=False)
    name = tables.TemplateColumn('<a href="/app/assessment/{{ record.pk }}"> {{ record.name }}</a>')
    project = tables.TemplateColumn('<a href="/app/project/{{ record.project.pk}}/summary">{{ record.project }}</a>')

    class Meta:
        model = Assessment
        template_name = "django_tables2/bootstrap-responsive.html"
        sequence = ('selection', 'name', 'project', 'added')
        fields = ('name', 'project', 'added')


"""ProjectTable class."""
class TemplateTable(tables.Table):

    selection = tables.CheckBoxColumn(accessor='pk', attrs={"th__input": {"onclick": "toggle(this)"}}, orderable=False)
    severity = tables.TemplateColumn('<span class="bc-badge bc-badge--p{{ record.severity }}">P{{ record.severity }}</span>')
    name = tables.TemplateColumn('<a href="/app/template/{{ record.pk }}">{{ record.name }}</a>')
    
    class Meta:
        model = Template
        template_name = "django_tables2/bootstrap-responsive.html"
        sequence = ('selection','severity', 'name')
        fields = ('severity', 'name')


"""MethodologyMasterTable class."""
class MethodologyMasterTable(tables.Table):

    selection = tables.CheckBoxColumn(accessor='pk', attrs={"th__input": {"onclick": "toggle(this)"}}, orderable=False)
    name = tables.TemplateColumn('<a href="/app/methodology-master/{{ record.pk }}"> {{ record.name }}</a>')

    class Meta:
        model = MethodologyMaster
        template_name = "django_tables2/bootstrap-responsive.html"
        sequence = ('selection', 'name')
        fields = ('name', )


"""ModuleMasterTable class."""
class ModuleMasterTable(tables.Table):

    selection = tables.CheckBoxColumn(accessor='pk', attrs={"th__input": {"onclick": "toggle(this)"}}, orderable=False)
    name = tables.TemplateColumn('<a href="/app/module-master/{{ record.pk }}"> {{ record.name }}</a>')
    methodology = tables.TemplateColumn('<a href="/app/methodology-master/{{ record.methodology.pk}}">{{ record.methodology }}</a>')

    class Meta:
        model = ModuleMaster
        template_name = "django_tables2/bootstrap-responsive.html"
        sequence = ('selection', 'name', 'methodology')
        fields = ('name', 'methodology')


"""CaseMasterTable class."""
class CaseMasterTable(tables.Table):

    selection = tables.CheckBoxColumn(accessor='pk', attrs={"th__input": {"onclick": "toggle(this)"}}, orderable=False)
    name = tables.TemplateColumn('<a href="/app/case-master/{{ record.pk }}"> {{ record.name }}</a>')
    module = tables.TemplateColumn('<a href="/app/module-master/{{ record.module.pk}}">{{ record.module }}</a>')

    class Meta:
        model = CaseMaster
        template_name = "django_tables2/bootstrap-responsive.html"
        sequence = ('selection', 'name', 'module')
        fields = ('name', 'module')