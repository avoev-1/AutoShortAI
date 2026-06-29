from app.modules.workflows.domain.workflow_template import WorkflowTemplate
from app.modules.workflows.templates.short_form_templates import fast_draft_template, standard_short_form_template

class WorkflowTemplateRegistry:
    def __init__(self)->None:
        self._templates={"standard_short_form":standard_short_form_template(),"fast_draft":fast_draft_template()}
    def list_templates(self)->list[WorkflowTemplate]:
        return list(self._templates.values())
    def get(self, template_id:str)->WorkflowTemplate:
        return self._templates[template_id]
workflow_template_registry=WorkflowTemplateRegistry()
