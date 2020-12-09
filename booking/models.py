from django.db import models


class Event(models.Model):
    type = models.CharField('Тип события', max_length=35)
    created_datetime = models.DateTimeField('Создано', auto_now=True)
    start_datetime = models.DateTimeField('Начало')
    initiator_name = models.CharField('Инициатор', max_length=50)
    initiator_phone = models.CharField('Тел.', max_length=14)
    initiator_email = models.EmailField('e-mail', max_length=254, blank=True)
    initiator_istelegram = models.BooleanField('Телега?', blank=True)
    users_number = models.IntegerField('Участников')
    allow_join = models.BooleanField('Можно + ', default=True)
    approved = models.BooleanField('Одобрено', default=False)
    done = models.BooleanField('Проведено', default=False)
    annulled = models.BooleanField('Отменено', default=False)


class Added(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_datetime = models.DateTimeField('Создано', auto_now=True)
    initiator_name = models.CharField('Инициатор', max_length=50)
    initiator_phone = models.CharField('Телефон', max_length=14)
    initiator_email = models.EmailField('e-mail', max_length=254)
    initiator_istelegram = models.BooleanField('Телега?', blank=True)
    users_number = models.IntegerField()


