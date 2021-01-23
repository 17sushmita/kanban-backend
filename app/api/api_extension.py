from flask_restx import Api
from app.api.resources.goal import goals_ns as goal_namespace

api = Api(
    title="Kanban System API",
    version="1.0",
    description="API documentation for the backend of Kanban System. \n \n"
)
api.namespaces.clear()

# Adding namespaces
print(goal_namespace)
api.add_namespace(goal_namespace, path="/")
