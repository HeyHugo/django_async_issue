import asyncio

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import path


async def test(request):
    """
    If the client cancels the request before this view finishes asyncio.CancelledError will be raised.
    This in turn will make django.core.signals.request_finished never to be sent.
    Since request_finished is used to close the database connection (and other cleanup?), the connection will remain open.
    """
    # When db connection is used it may not be closed
    await User.objects.afirst()
    
    await asyncio.sleep(5)
    return HttpResponse('OK')


urlpatterns = [
    path("", test),
]
