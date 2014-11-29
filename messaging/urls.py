from django.conf.urls import include, patterns, url
from messaging import views, views_groups, views_users, views_messaging

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       #BASE URLS
                       url(r'^$', views.index, name='index'),
                       url(r'^about/$', views.about, name='about'),
                       url(r'^home/$', views.home, name='home'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^logout/$', views.user_logout, name='logout'),
                       url(r'^profile/$', views.profile, name='profile'),
                       url(r'^register/$', views.register, name='register'),

                       #GROUP URLS
                       url(r'^all_groups/$', views_groups.all_groups, name='all_groups'),
                       url(r'^owned_groups/$', views_groups.owned_groups, name='owned_groups'),
                       url(r'^my_groups/$', views_groups.my_groups, name='my_groups'),
                       url(r'^group/id/(?P<group_id>\w+)/$', views_groups.group_by_id, name='group_page'),
                       url(r'^create_group/$', views_groups.create_group, name='create_group'),
                       url(r'^edit_group/id/(?P<group_id>\w+)/$', views_groups.edit_group, name='group_edit_page'),
                       url(r'^group/search/', views_groups.search_group, name='group_edit_page'),

                       #USER URLS
                       url(r'^all_users/$', views_users.all_users, name='all_users'),
                       url(r'^contacts/$', views_users.contact_users, name='contact_users'),
                       url(r'^user/id/(?P<user_id>\w+)/$', views_users.user_by_id, name='user_page'),
                       url(r'^user/search', views_users.search_user, name='user_search'),

                       #AJAX
                       url(r'^ajax/user_search/', views_users.ajax_search, name='ajax_user_search'),
                       url(r'^ajax/group_search/', views_groups.ajax_search, name='ajax_group_search'),
                       url(r'^ajax/messages/', views_messaging.get_messages_ajax, name='ajax_messages'),
                       url(r'^ajax/send_grp_msg/', views_messaging.send_message_to_group, name='ajax_send_grp_msg'),
                       url(r'^ajax/send_user_msg/', views_messaging.send_message_to_user, name='ajax_send_user_msg'),

                       #ADMIN
                       url(r'^admin/', include(admin.site.urls)),
                       )


