from django.shortcuts import render
from workshop.subscriptions.forms import SubscriptionForm


def subscription(request):

    form = SubscriptionForm()

    return render(request, 'subscriptions/subscription_form.html', {'form': form})