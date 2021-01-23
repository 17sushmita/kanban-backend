from http import HTTPStatus
from typing import Dict

from app.database.models.goal import GoalModel, StageModel, TaskModel


class GoalDAO:
    """Data Access Object for User functionalities"""

    @staticmethod
    def create_goal(data: Dict[str, str]):
        """Creates a new goal.
        Creates a new goal with provided data.
        Arguments:
            data: A list containing the goal's data.
        Returns:
            A tuple with two elements. The first element
            is a dictionary containing a key 'message'
            containing a string which indicates whether
            or not the user was created successfully.
            The second is the HTTP response code.
        """

        name = data["name"]
        goal = GoalModel(name)
        id = goal.save_to_db()

        return {"id": id}, HTTPStatus.CREATED

    @staticmethod
    def delete_goal(goal_id: int):
        """ Deletes a goal.
        Deletes the specified goal and removes them from the directory,
        Arguments:
            goal_id: The ID of the user to be deleted.
        Returns:
            A tuple with two elements. The first element is a dictionary
            containing a key 'message' containing a string which indicates
            whether or not the goal was deleted successfully.
            The second is the HTTP response code.
        """

        goal = GoalModel.find_by_id(goal_id)

        if goal:
            goal.delete_from_db()
            return {"message": "Deleted successfully"}, HTTPStatus.OK

        return {"message": "Not Found"}, HTTPStatus.NOT_FOUND

    @staticmethod
    def get_goal(goal_id: int):
        """ Retrieves a goal information using a specified ID.
        Provides the goal information of the goal whose ID matches the
        one specified.
        Arguments:
            goal_id: The ID of the goal to be searched.
        Returns:
            The GoalModel class of the goal whose ID was searched, containing
            the public information.
        """
        goal = GoalModel.find_by_id(goal_id)
        if goal:
            return goal.json()
        return {"message": "Not Found"}, 404

    @staticmethod
    def list_goals():
        goals = GoalModel.query.all()
        print(goals)
        goals_list = [
            user.json()
            for user in goals
        ]
        return goals_list


class StageDAO:
    """Data Access Object for User functionalities"""

    @staticmethod
    def create_stage(goal_id, data: Dict[str, str]):
        """Creates a new goal.
        Creates a new goal with provided data.
        Arguments:
            data: A list containing the goal's data.
        Returns:
            A tuple with two elements. The first element
            is a dictionary containing a key 'message'
            containing a string which indicates whether
            or not the user was created successfully.
            The second is the HTTP response code.
        """

        title = data["title"]
        goal_id = goal_id

        if GoalModel.find_by_id(goal_id):
            stage = StageModel(goal_id, title)
            id = stage.save_to_db()
            return {"id": id}, HTTPStatus.CREATED
        return {"message": "Goal not found"}, 404

    @staticmethod
    def delete_stage(stage_id: int):
        """ Deletes a goal.
        Deletes the specified goal and removes them from the directory,
        Arguments:
            goal_id: The ID of the user to be deleted.
        Returns:
            A tuple with two elements. The first element is a dictionary
            containing a key 'message' containing a string which indicates
            whether or not the goal was deleted successfully.
            The second is the HTTP response code.
        """

        stage = StageModel.find_by_id(stage_id)

        if stage:
            stage.delete_from_db()
            return {"message": "Deleted successfully"}, HTTPStatus.OK

        return {"message": "Not Found"}, HTTPStatus.NOT_FOUND

    @staticmethod
    def get_stage(stage_id: int):
        """ Retrieves a goal information using a specified ID.
        Provides the goal information of the goal whose ID matches the
        one specified.
        Arguments:
            goal_id: The ID of the goal to be searched.
        Returns:
            The GoalModel class of the goal whose ID was searched, containing
            the public information.
        """
        stage = StageModel.find_by_id(stage_id)
        if stage:
            return stage.json()
        return {"message": "Not Found"}, 404

    @staticmethod
    def list_stages(goal_id: int):
        stages = StageModel.query.filter_by(goal_id=goal_id)
        print(stages)
        stages_list = [
            stage.json()
            for stage in stages
        ]
        return stages_list


class TaskDAO:
    """Data Access Object for User functionalities"""

    @staticmethod
    def create_task(stage_id, data: Dict[str, str]):
        """Creates a new goal.
        Creates a new goal with provided data.
        Arguments:
            data: A list containing the goal's data.
        Returns:
            A tuple with two elements. The first element
            is a dictionary containing a key 'message'
            containing a string which indicates whether
            or not the user was created successfully.
            The second is the HTTP response code.
        """

        title = data["title"]
        stage_id = stage_id
        if (StageModel.find_by_id(stage_id)):
            task = TaskModel(stage_id, title)
            id = task.save_to_db()
            return {"id": id}, HTTPStatus.CREATED
        return {"message": "Stage not found"}

    @staticmethod
    def delete_task(task_id: int):
        """ Deletes a goal.
        Deletes the specified goal and removes them from the directory,
        Arguments:
            goal_id: The ID of the user to be deleted.
        Returns:
            A tuple with two elements. The first element is a dictionary
            containing a key 'message' containing a string which indicates
            whether or not the goal was deleted successfully.
            The second is the HTTP response code.
        """

        task = TaskModel.find_by_id(task_id)

        if task:
            task.delete_from_db()
            return {"message": "Deleted successfully"}, HTTPStatus.OK

        return {"message": "Not Found"}, HTTPStatus.NOT_FOUND

    @staticmethod
    def get_task(task_id: int):
        """ Retrieves a goal information using a specified ID.
        Provides the goal information of the goal whose ID matches the
        one specified.
        Arguments:
            goal_id: The ID of the goal to be searched.
        Returns:
            The GoalModel class of the goal whose ID was searched, containing
            the public information.
        """
        task = TaskModel.find_by_id(task_id)
        if task:
            return task.json()
        return {"message": "Not Found"}, 404

    @staticmethod
    def list_tasks(stage_id: int):
        tasks = TaskModel.query.filter_by(stage_id=stage_id)
        print(tasks)
        tasks_list = [
            task.json()
            for task in tasks
        ]
        return tasks_list
