from modama import socketio, appbuilder
from modama.formService import FormService
from modama.exceptions import PermissionDeniedError
from flask_socketio import emit
from flask import g, request
from flask_login import login_user, current_user
import logging
import jwt

log = logging.getLogger(__name__)


@socketio.on_error_default
def error_handler(exc):
    log.error(exc)
    return {'success': False, 'message': str(exc)}


@socketio.on('connect')
def connect():
    token = request.args.get('token')
    log.info("Connection made with token: {} ".format(token))
    av = appbuilder.sm.auth_view
    user = None
    try:
        user = av.getUserFromJWT(token)
    except jwt.exceptions.InvalidTokenError:
        return False
    log.info("User {} logged in on websocket.".format(user))
    if user is not None:
        login_user(user)
        g.user = current_user
        token = av.encodeJWT(av.getJWT())
        datasets = FormService.getDatasets()
        json_schema = FormService.getJsonSchema(datasets)
        log.info("Sending datasets %s" % json_schema)
        emit('newToken', token)
        emit('newDatasets', json_schema)
    else:
        log.error("Could not find user from valid JWT {}".format(token))
        return False


@socketio.on('saveData')
def saveData(data):
    log.info('Saving data for user {}'.format(current_user))
    g.user = current_user
    formname = data['form']
    datasetname = data['dataset']
    formdata = data['formdata']
    view = FormService.getView(datasetname, formname)
    if not FormService.currentUserViewAccess(view, 'add'):
        raise PermissionDeniedError(
            "User {} does not have add access to {}".format(
                FormService.getCurrentUser(), view)
        )
    FormService.storeData(datasetname, formname, formdata)
    return {'success': True}
