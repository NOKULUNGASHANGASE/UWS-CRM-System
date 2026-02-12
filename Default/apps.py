from django.apps import AppConfig



class DefaultConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Default'

    def ready(self):
        from .groups import create_user_groups
        create_user_groups()
