from app.database.sqlalchemy_extension import db


class GoalModel(db.Model):
    # Specifying database table used for GoalModel
    __tablename__ = "goals"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    stages = db.relationship('StageModel', backref='goal', lazy=True)

    def __init__(self, name='MyGoal'):
        """Initialises userModel class with name. """
        self.name = name

    def json(self):
        """Returns Usermodel object in json format."""
        return {
            "id": self.id,
            "name": self.name
        }

    def __repr__(self):
        """Returns the user's name and username. """
        return f"Goal {self.name}"

    @classmethod
    def find_by_id(cls, _id: int) -> 'GoalModel':
        """Returns the goal that has the id we searched for. """
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def is_empty(cls) -> bool:
        """Returns a boolean if the GoalModel is empty or not. """
        return cls.query.first() is None

    def save_to_db(self) -> int:
        """Adds a goal to the database. """
        db.session.add(self)
        db.session.flush()
        id = self.id
        db.session.commit()
        return id

    def delete_from_db(self) -> None:
        """Deletes a user from the database. """
        db.session.delete(self)
        db.session.commit()

class StageModel(db.Model):
    # Specifying database table used for GoalModel
    __tablename__ = "stages"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    goal_id = db.Column(db.Integer, db.ForeignKey('goals.id'), nullable=False)
    tasks = db.relationship('TaskModel', backref='stages', lazy=True)

    def __init__(self, goal_id, title='mystage'):
        """Initialises userModel class with name. """
        self.title = title
        self.goal_id = goal_id

    def json(self):
        """Returns Usermodel object in json format."""
        return {
            "id": self.id,
            "name": self.title,
            "goal_id": self.goal_id
        }

    def __repr__(self):
        """Returns the user's name and username. """
        return f"Stage {self.title}"

    @classmethod
    def find_by_id(cls,_id: int) -> 'StageModel':
        """Returns the goal that has the id we searched for. """
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def is_empty(cls) -> bool:
        """Returns a boolean if the GoalModel is empty or not. """
        return cls.query.first() is None

    def save_to_db(self) -> int:
        """Adds a goal to the database. """
        db.session.add(self)
        db.session.flush()
        id = self.id
        db.session.commit()
        return id

    def delete_from_db(self) -> None:
        """Deletes a user from the database. """
        db.session.delete(self)
        db.session.commit()


class TaskModel(db.Model):
    # Specifying database table used for GoalModel
    __tablename__ = "tasks"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    stage_id = db.Column(db.Integer, db.ForeignKey('stages.id'), nullable=False)

    def __init__(self, stage_id, title='mystage'):
        """Initialises userModel class with name. """
        self.title = title
        self.stage_id = stage_id

    def json(self):
        """Returns Usermodel object in json format."""
        return {
            "id": self.id,
            "title": self.title,
            "stage_id": self.stage_id
        }

    def __repr__(self):
        """Returns the user's name and username. """
        return f"Task {self.title}"

    @classmethod
    def find_by_id(cls,_id: int) -> 'TaskModel':
        """Returns the goal that has the id we searched for. """
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def is_empty(cls) -> bool:
        """Returns a boolean if the GoalModel is empty or not. """
        return cls.query.first() is None

    def save_to_db(self) -> int:
        """Adds a goal to the database. """
        db.session.add(self)
        db.session.flush()
        id = self.id
        db.session.commit()
        return id

    def delete_from_db(self) -> None:
        """Deletes a user from the database. """
        db.session.delete(self)
        db.session.commit()
