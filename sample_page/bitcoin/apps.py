from django.apps import AppConfig


class BitcoinConfig(AppConfig):
    name = 'bitcoin'

    def ready(self):
        from auto_updater import updater
        updater.start()
