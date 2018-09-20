from fab_geoalchemy.views import GeoModelView
from flask import g
from wtforms import DateTimeField
from ..widgets import DateTimeTZPickerWidget
from ..models.filters import FilterM2MRelationOverlapFunction


class BaseObservationView(GeoModelView):

    _base_edit = ['observation_datetime', 'observer', 'verified']
    _base_add = ['observation_datetime', 'observer']
    _base_list = ['observation_datetime', 'observer', 'verified']
    _base_show = ['observation_datetime', 'observer', 'verified', 'created_by',
                  'created_on', 'changed_by', 'changed_on']

    edit_form_extra_fields = {'observation_datetime':
                              DateTimeField('Observation date/time',
                                            format='%Y-%m-%d %H:%M:%S%z',
                                            widget=DateTimeTZPickerWidget())}
    add_form_extra_fields = {'observation_datetime':
                             DateTimeField('Observation date/time',
                                           format='%Y-%m-%d %H:%M:%S%z',
                                           widget=DateTimeTZPickerWidget())}

    _base_filters = [['observer.organizations',
                      FilterM2MRelationOverlapFunction,
                      lambda: g.user.organizations]]
