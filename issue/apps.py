from django.apps import AppConfig


class IssueAppConfig(AppConfig):
    name = 'issue'

    def ready(self):
        from django.core import signals

        signals.request_finished.connect(lambda **kwargs: print('request_finished'))
