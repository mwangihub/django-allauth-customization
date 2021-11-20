from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def employee_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    '''
    Decorator for views that checks that the logged in user is a Employee,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_employee,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def staff_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    '''
    Decorator for views that checks that the logged in user is a staff or admin,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_staff,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def non_checker(request, *args, **kwargs):
    pass


def non_required(function=None, redirect_field_name='/', login_url='home'):
    '''
    Decorator for views that checks that the logged in user has no account type,
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_non,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator