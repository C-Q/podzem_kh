from django.contrib import admin

from .models import Event, Added


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    # todo: добавить поле "количество присоединившихся групп". Title="Присоединилось" и метод для подсчета количества связанных объектов Added
    # todo: добавить поле и метод "всего участников в событии". Title="Всего участников"
    list_display = ('type', 'start_datetime', 'initiator_name', 'initiator_phone',
                    'initiator_email', 'initiator_istelegram', 'users_number',
                    'created_datetime', 'allow_join', 'approved', 'done', 'annulled',)
