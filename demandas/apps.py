from django.apps import AppConfig


class DemandasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'demandas'
    verbose_name = 'Gestão de Demandas'

    def ready(self):
        """Registra os signals quando o app estiver pronto"""
        import demandas.signals
