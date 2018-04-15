
from flask_appbuilder import ModelView


class BaseObservationView(ModelView):
    _base_edit = ['observation_datetime', 'observer', 'verified']
    _base_add = ['observation_datetime', 'observer']
    _base_list = ['observation_datetime', 'observer', 'verified']
    _base_show = ['observation_datetime', 'observer', 'verified', 'created_by',
                  'created_on', 'changed_by', 'changed_on']
