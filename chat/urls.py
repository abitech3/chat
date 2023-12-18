from django.urls import path
from . import views


app_name = "chat"


urlpatterns = [
    path("home", views.home, name="home"),
    path("chat", views.chatboard_view, name="chat"),
    path("", views.login_view, name="login"),
    path("signup", views.sign_up, name="signup"),
    path("setting", views.setting_view, name="setting"),
    path("bot_setting", views.botset_view, name="bot_setting"),
    path("lead", views.lead_view, name="lead"),
    path("app_setting", views.app_setting_view, name="app_setting"),
    path("add_user", views.add_user, name="add_user"),
    path("add_company", views.add_company_view, name="add_company"),
    path("integrate", views.integrate_view, name="integrate"),
    path("logout", views.logout, name="logout"),
    path("forgot", views.forgot, name="forgot"),
    path("bot", views.bot_view, name="bot"),
    path("conversation", views.conversation, name="conversation"),
    path("profile", views.profile, name="profile"),
    path("del_company/<int:del_id>", views.delcompany, name="del_company"),
    path("edit_company/<int:update_id>", views.editcompany, name="edit_company"),
    path("edit_app/<int:update_id>", views.edit_appsetting, name="edit_app"),
    path("edit_template", views.edit_template, name="edit_template"),
    path("del_app/<int:del_id>", views.del_app, name="del_app"),






]
