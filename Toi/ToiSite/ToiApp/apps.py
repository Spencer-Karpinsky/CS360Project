from django.apps import AppConfig


class ToiappConfig(AppConfig):
    name = 'ToiApp'

    def ready(self):
        import ToiApp.signal
