import functools

import requests
from requests.compat import urljoin


PATH_PING = '/api/ping'
PATH_VERSION = '/api/version'
PATH_I18N_CONFIG = '/api/config/i18n'

PATH_ACTIVITIES = '/api/activities'
PATH_CUSTOMERS = '/api/customers'
PATH_PROJECTS = '/api/projects'
PATH_TAGS = '/api/tags'
PATH_TEAMS = '/api/teams'
PATH_TIMESHEETS = '/api/timesheets'
PATH_USERS = '/api/users'


class KimaiAPIException(Exception):
    pass


class KimaiAPI(object):

    def __init__(self, url, username, password):
        self._url = url
        self._username = username
        self._password = password

    def __str__(self):
        return 'Kimai API (url: {}, user: {})'.format(
            self._url, self._username)

    def __repr__(self):
        return self.__str__()

    def _get_headers(self):
        return {
            'X-AUTH-USER': self._username,
            'X-AUTH-TOKEN': self._password,
        }

    def _request(self, path, params=None, data=None, method=None):
        headers = self._get_headers()
        url = urljoin(self._url, path)

        ret = requests.request(method, url, params=params, headers=headers,
                               data=data)
        ret.raise_for_status()
        return ret.json()

    _get = functools.partialmethod(_request, method='get')
    _post = functools.partialmethod(_request, method='post')
    _patch = functools.partialmethod(_request, method='patch')
    _delete = functools.partialmethod(_request, method='delete')

    def ping(self):
        return self._get(PATH_PING)

    def get_version(self):
        return self._get(PATH_VERSION)

    def get_i18n_config(self):
        return self._get(PATH_I18N_CONFIG)

    # Activities

    def get_activities(self, id=None):
        path = PATH_ACTIVITIES
        if id is not None:
            path = '/'.join((path, str(id)))

        return self._get(path)

    def set_activity_meta_field(self, id, name, value):
        meta = {
            'name': name,
            'value': value,
        }
        path = '/'.join((PATH_ACTIVITIES, id, 'meta'))

        return self._patch(path, data=meta)

    def create_activity(self, data):
        return self._post(PATH_ACTIVITIES, data=data)

    def update_activity(self, id, data):
        path = '/'.join((PATH_ACTIVITIES, id))
        return self._patch(path, data=data)

    # Customers

    def get_customers(self, id=None):
        path = PATH_CUSTOMERS
        if id is not None:
            path = '/'.join((path, str(id)))

        return self._get(path)

    def set_customer_meta_field(self, id, name, value):
        meta = {
            'name': name,
            'value': value,
        }
        path = '/'.join((PATH_CUSTOMERS, id, 'meta'))

        return self._patch(path, data=meta)

    def create_customer(self, data):
        return self._post(PATH_CUSTOMERS, data=data)

    def update_customer(self, id, data):
        path = '/'.join((PATH_CUSTOMERS, id))
        return self._patch(path, data=data)

    # Projects

    def get_projects(self, id=None):
        path = PATH_PROJECTS
        if id is not None:
            path = '/'.join((path, str(id)))

        return self._get(path)

    def set_project_meta_field(self, id, name, value):
        meta = {
            'name': name,
            'value': value,
        }
        path = '/'.join((PATH_PROJECTS, id, 'meta'))

        return self._patch(path, data=meta)

    def create_project(self, data):
        return self._post(PATH_PROJECTS, data=data)

    def update_project(self, id, data):
        path = '/'.join((PATH_PROJECTS, id))
        return self._patch(path, data=data)

    # Tags

    def get_tags(self, id=None):
        path = PATH_TAGS
        if id is not None:
            path = '/'.join((path, str(id)))

        return self._get(path)

    def create_tag(self, data):
        return self._post(PATH_TAGS, data=data)

    def delete_tag(self, id):
        path = '/'.join((PATH_TAGS, id))
        return self._delete(path)

    # Teams

    def get_teams(self, id=None):
        path = PATH_TEAMS
        if id is not None:
            path = '/'.join((path, str(id)))

        return self._get(path)

    def delete_team(self, id):
        path = '/'.join((PATH_TEAMS, id))
        return self._delete(path)

    # Tiemsheets

    def get_recent_timesheets(self):
        path = '/'.join((PATH_TIMESHEETS, 'recent'))
        return self._get(path)

    def get_active_timesheets(self):
        path = '/'.join((PATH_TIMESHEETS, 'active'))
        return self._get(path)

    def get_timesheets(self, id=None):
        path = PATH_TIMESHEETS
        if id is not None:
            path = '/'.join((path, str(id)))

        return self._get(path)

    def restart_timesheet(self, id):
        path = '/'.join((PATH_TIMESHEETS, id, 'restart'))
        return self._patch(path)

    def stop_timesheet(self, id):
        path = '/'.join((PATH_TIMESHEETS, id, 'stop'))
        return self._patch(path)

    def export_timesheet(self, id):
        path = '/'.join((PATH_TIMESHEETS, id, 'export'))
        return self._patch(path)

    def set_timesheet_meta_field(self, id, name, value):
        meta = {
            'name': name,
            'value': value,
        }
        path = '/'.join((PATH_TIMESHEETS, id, 'meta'))

        return self._patch(path, data=meta)

    def create_timesheet(self, data):
        return self._post(PATH_TIMESHEETS, data=data)

    def update_timesheet(self, id, data):
        path = '/'.join((PATH_TIMESHEETS, id))
        return self._patch(path, data=data)

    def delete_timesheet(self, id):
        path = '/'.join((PATH_TIMESHEETS, id))
        return self._delete(path)

    # Users

    def get_users(self, id=None):
        path = PATH_USERS
        if id is not None:
            path = '/'.join((path, str(id)))

        return self._get(path)
