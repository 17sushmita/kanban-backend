from flask_restx import fields, Model


def add_models_to_namespace(api_namespace):
    api_namespace.models[create_goal_api_model.name] = create_goal_api_model
    api_namespace.models[create_stage_api_model.name] = create_stage_api_model
    api_namespace.models[create_task_api_model.name] = create_task_api_model
create_goal_api_model = Model(
    "Goal creation model",
    {
        "name": fields.String(required=True, description="Goal Title")
    },
)
create_stage_api_model = Model(
    "Stage Creation Model",
    {
        "title": fields.String(required=True, description="Stage Title")
    },
)

create_task_api_model = Model(
    "Task Creation Model",
    {
        "title": fields.String(required=True, description="Task Title")
    },
)