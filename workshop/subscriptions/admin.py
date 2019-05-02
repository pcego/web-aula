from django.contrib import admin
from django.utils.timezone import now
from workshop.subscriptions.models import Subscriptions



class SubscriptionsAdmin(admin.ModelAdmin):

    list_display = ('name', 'cpf', 'email', 'phone', 'created_at', 'subscribed_today')
    search_fields = ('name', 'cpf', 'email', 'phone')
    date_hierarchy = 'created_at'
    list_filter = ('created_at',)

    verbose_name = 'inscrição'
    verbose_name_plural = 'inscrições'


    def subscribed_today(self, obj):

        return obj.created_at.date() == now().date()


    subscribed_today.short_description = 'inscrito hoje?'

    subscribed_today.boolean = True


admin.site.register(Subscriptions, SubscriptionsAdmin)
