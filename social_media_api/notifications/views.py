from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Notification


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_notifications(request):

    notifications = Notification.objects.filter(
        recipient=request.user
    ).order_by('-timestamp')

    data = []

    for notification in notifications:
        data.append({
            "actor": notification.actor.username,
            "verb": notification.verb,
            "timestamp": notification.timestamp,
            "read": notification.is_read
        })

    return Response(data)