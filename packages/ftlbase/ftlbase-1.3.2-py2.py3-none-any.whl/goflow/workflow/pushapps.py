#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User

# from .logger import Log
#
from common.logger import Log

log = Log('goflow.workflow.pushapps')


def route_to_requester(workitem):
    """Simplest possible pushapp
    """
    return workitem.instance.user


def route_to_user(workitem, user):
    """Route to user given a user name
    """
    return User.objects.get(username=user)
    # return User.objects.get(user=user)


def route_to_superuser(workitem, username='admin'):
    """Route to the superuser
    """
    user = User.objects.get(username=username)
    if user.is_superuser:
        return user
    log.warning('this user is not a super-user:', username)
    return None


def to_current_superuser(workitem, user_pushed):
    """Should be used in all push applications for testing purposes.

        (**NOT IMPLEMENTED**)

        usage::

            return to_current_superuser(workitem, user_pushed)
    """
    return None

def route_to_object_user(workitem):
    """Route to user defined by object
    """
    user = workitem.instance.wfobject().get_workflow_user()

    return user