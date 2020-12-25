from django.contrib import admin

from .models import Event, Added


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    # todo: добавить после 'start_datetime', поле 'день недели'
    # todo: запилить ограничения при выборе даты и времени
    # todo: вынести полученный функционал на front-end
    list_display = ('type', 'start_datetime', 'initiator_name', 'initiator_phone',
                    'initiator_email', 'initiator_istelegram', 'all_users_number',
                    'created_datetime', 'allow_join', 'approved', 'done', 'annulled',)

    def all_users_number(self, obj):
        joined = obj.added_set.all()
        all = [use_num.users_number for use_num in joined]
        return sum(all) + obj.users_number
    all_users_number.short_description = 'Участников'


@admin.register(Added)
class AddedAdmin(admin.ModelAdmin):
    list_display = ('event', 'users_number', 'created_datetime', 'initiator_name', 'initiator_phone', 'initiator_istelegram', 'initiator_email')