from django.conf.urls import url
from . import views

app_name = 'dashboard'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('topic-distribution', views.topic_distribution,
        name='topic-distribution'),
    url('instructor-distribution', views.instructor_distribution,
        name='instructor-distribution'),
    url('upload', views.upload_view, name='upload'),
    url('stopword', views.stopword_view, name='stopword'),
    url('export', views.export_view, name='export'),
]

# refactor later in classes when have models
# urlpatterns = [
#     url(r'^$', views.DashboardView.as_view(), name='index'),
#     url('topic-distribution', views.TopicDistributionView.as_view(),
#         name='topic-distribution'),
#     url('instructor-distribution',
#         views.InstructorDistributionView.as_view(),
#         name='instructor-distribution'),
#     ]