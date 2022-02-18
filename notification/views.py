from django.shortcuts import render, redirect
from notification.models import Notification

def notification_view(request):
    notifications = Notification.objects.all
    context = {'notice':notifications}
    return render(request, "notifications.html", context)

def notification_delete(request,pk):

    notifications = Notification.objects.get(id=pk)

    if request.method == 'POST':
        notifications.delete()
        return redirect('home')
        
    context = {'object': notifications}
    return render(request, "delete_notification.html", context)