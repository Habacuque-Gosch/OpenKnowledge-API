from django.apps import AppConfig


class TemplateModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.<module_name>'
    # label = '<module_name>'  # only needed if directory name differs from DB label

    # def ready(self):
    #     import apps.<module_name>.signals
