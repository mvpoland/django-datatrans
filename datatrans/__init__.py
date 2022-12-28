from importlib import import_module

VERSION = "1.0.5"
__version__ = VERSION


def autodiscover():
    """
    Same principle as for importing the admin modules with autodiscover() from django.contrib.admin
    """
    from django.conf import settings

    for app in settings.INSTALLED_APPS:
        try:
            import_module("{}.datatranslation".format(app))
        except ImportError:
            pass
