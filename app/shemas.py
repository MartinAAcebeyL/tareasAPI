from marshmallow import Schema
from marshmallow import fields
from marshmallow.validate import Length

class Taskshema(Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'deadLine', 'date')

class ParamsTaskShema(Schema):
    title = fields.Str(required=True, validate=Length(max=50))
    description = fields.Str(required=True, validate=Length(max=200))
    deadLine = fields.DateTime(required=True)

task_shema = Taskshema()
task_shemas = Taskshema(many=True)

params_task_shema = ParamsTaskShema()
