from django.urls import path
from .views import ProposalListCreateView, ProposalDetailView

urlpatterns = [
    path('', ProposalListCreateView.as_view(), name='proposal-list-create'),
    path('<int:pk>/', ProposalDetailView.as_view(), name='proposal-detail'),
]
