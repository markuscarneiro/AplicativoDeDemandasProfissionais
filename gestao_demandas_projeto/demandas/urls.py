"""
URLs do aplicativo de demandas.

Este módulo define todas as rotas do sistema de gestão de demandas,
incluindo CRUD, exportações e funcionalidades auxiliares.
"""

from django.urls import path

from . import views

app_name = 'demandas'

urlpatterns = [
    # -------------------------------------------------------------------------
    # DASHBOARD
    # -------------------------------------------------------------------------
    path('', views.dashboard, name='dashboard'),
    path('index/', views.index, name='index'),  # Compatibilidade
    
    # -------------------------------------------------------------------------
    # CRUD DE DEMANDAS
    # -------------------------------------------------------------------------
    path('demandas/', views.DemandaListView.as_view(), name='demanda_list'),
    path('demandas/<int:pk>/', views.DemandaDetailView.as_view(), name='demanda_detail'),
    path('demandas/nova/', views.DemandaCreateView.as_view(), name='demanda_create'),
    path('demandas/<int:pk>/editar/', views.DemandaUpdateView.as_view(), name='demanda_update'),
    path('demandas/<int:pk>/excluir/', views.DemandaDeleteView.as_view(), name='demanda_delete'),
    
    # -------------------------------------------------------------------------
    # FUNCIONALIDADES DE DEMANDAS
    # -------------------------------------------------------------------------
    path('demandas/<int:pk>/comentario/', views.adicionar_comentario, name='adicionar_comentario'),
    path('demandas/<int:pk>/anexo/', views.upload_anexo, name='upload_anexo'),
    
    # -------------------------------------------------------------------------
    # MATRIZ DE EISENHOWER
    # -------------------------------------------------------------------------
    path('matriz-eisenhower/', views.matriz_eisenhower, name='matriz_eisenhower'),
    
    # -------------------------------------------------------------------------
    # GESTÃO DE TAGS
    # -------------------------------------------------------------------------
    path('tags/', views.tags_list, name='tags_list'),
    path('tags/nova/', views.tag_create, name='tag_create'),
    path('tags/<int:pk>/editar/', views.tag_edit, name='tag_edit'),
    path('tags/<int:pk>/excluir/', views.tag_delete, name='tag_delete'),
    
    # -------------------------------------------------------------------------
    # EXPORTAÇÃO DE RELATÓRIOS
    # -------------------------------------------------------------------------
    path('exportar/excel/', views.exportar_excel, name='exportar_excel'),
    path('exportar/pdf/', views.exportar_pdf, name='exportar_pdf'),
    
    # -------------------------------------------------------------------------
    # API / AJAX
    # -------------------------------------------------------------------------
    path('api/notificacoes/', views.get_notificacoes_json, name='notificacoes_json'),
]