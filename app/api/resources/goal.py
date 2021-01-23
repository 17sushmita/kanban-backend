from flask_restx import Resource, Namespace
from app.api.dao.goal import GoalDAO, StageDAO, TaskDAO
from app.api.models.goal import *
from flask import request


goals_ns = Namespace("Goals", description="Operations related to goals")
add_models_to_namespace(goals_ns)

GoalDAO = GoalDAO()  # User data access object
StageDAO = StageDAO()
TaskDAO = TaskDAO()

# To do
# GET	/goal			get all goals info
# POST	/goal			create a new goal with some data in params 
# DELETE	/goal/<int:goal_id>	delete a goal with goal id
# GET	/goal/<int:goal_id>	get a goal with goal id

# GET	/goal/<int:goal_id>/stage			get all stages in goal with some data in params
# POST	/goal/<int:goal_id>/stage			create new stage to goal with goal id
# DELETE	/goal/<int:goal_id>/stage/<int:stage_id>	delete a stage with stage id of goal with goal id
# GET	/goal/<int:goal_id>/stage/<int:stage_id>	get a stage with stage id of goal with goal id

# GET	/goal/<int:goal_id>/stage/<int:stage_id>/task			get all the tasks in goal with goal id and stage with stage id
# POST	/goal/<int:goal_id>/stage/<int:stage_id/task			create new task in goal with goal id and stage with stage id
# DELETE	/goal/<int:goal_id>/stage/<int:stage_idtask/<int:task_id>	delete a task with task id in goal with goal id and stage with stage id 
# GET	/goal/<int:goal_id>/stage/<int:stage_idtask/<int:task_id>	get a task with task id in goal with goal id and stage with stage id


# GET	/goal			get all goals info
# POST	/goal			create a new goal with some data in params 
@goals_ns.route('goal')
class goals(Resource):
    def get(self):
        return GoalDAO.list_goals()

    @goals_ns.expect(create_goal_api_model, validate=False)
    def post(self):
        data = request.json
        print(data)
        return GoalDAO.create_goal(data)


# DELETE	/goal/<int:goal_id>	delete a goal with goal id
# GET	/goal/<int:goal_id>	get a goal with goal id
@goals_ns.route('goal/<int:goal_id>')
class get_goal(Resource):
    def delete(self, goal_id):
        return GoalDAO.delete_goal(goal_id)

    def get(self, goal_id):
        return GoalDAO.get_goal(goal_id)


# GET	/goal/<int:goal_id>/stage			get all stages in goal with some data in params
# POST	/goal/<int:goal_id>/stage			create new stage to goal with goal id
@goals_ns.route('goal/<int:goal_id>/stage')
class stages(Resource):
    def get(self, goal_id):
        return StageDAO.list_stages(goal_id)
    
    @goals_ns.expect(create_stage_api_model, validate=True)
    def post(self, goal_id):
        data = request.json
        return StageDAO.create_stage(goal_id, data)



# DELETE	/goal/<int:goal_id>/stage/<int:stage_id>	delete a stage with stage id of goal with goal id
# GET	/goal/<int:goal_id>/stage/<int:stage_id>	get a stage with stage id of goal with goal id
@goals_ns.route('stage/<int:stage_id>')
class get_stage(Resource):
    def delete(self, stage_id):
        return StageDAO.delete_stage(stage_id)

    def get(self, stage_id):
        return StageDAO.get_stage(stage_id)


# GET	/goal/<int:goal_id>/stage/<int:stage_id>/task			get all the tasks in goal with goal id and stage with stage id
# POST	/goal/<int:goal_id>/stage/<int:stage_id/task			create new task in goal with goal id and stage with stage id
@goals_ns.route('stage/<int:stage_id>/task')
class tasks(Resource):
    def get(self, stage_id):
        return TaskDAO.list_tasks(stage_id)

    @goals_ns.expect(create_task_api_model, validate=True)
    def post(self, stage_id):
        data=request.json
        return TaskDAO.create_task(stage_id, data)


# DELETE	/goal/<int:goal_id>/stage/<int:stage_idtask/<int:task_id>	delete a task with task id in goal with goal id and stage with stage id 
# GET	/goal/<int:goal_id>/stage/<int:stage_idtask/<int:task_id>	get a task with task id in goal with goal id and stage with stage id
@goals_ns.route('task/<int:task_id>')
class get_task(Resource):
    def delete(self, task_id):
        return TaskDAO.delete_task(task_id)
    
    def get(self, task_id):
        return TaskDAO.get_task(task_id)
