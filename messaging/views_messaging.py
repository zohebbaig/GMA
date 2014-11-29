from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from messaging.models import Message, Group

@login_required()
def send_message_to_user(request):
    user_id = request.POST.get("user_id")
    message_text = request.POST.get("message")
    user = User.objects.get(id=user_id)
    message = Message(text=message_text, sender=request.user, recipient=user.profile)
    message.save()

    return HttpResponse()

@login_required()
def send_message_to_group(request):
    id = request.POST.get('group_id')
    group = Group.objects.get(id=id)
    message = Message(text=request.POST.get("message", ""), sender=request.user, recipient=group)
    message.save()

    return HttpResponse()

@login_required()
def get_messages_ajax(request):
    id = request.GET.get('group_id')
    if id == None:
        id = request.GET.get('user_id')
        user = User.objects.get(id=id)
        messages = get_conversation(request.user, user)
    else:
        group = Group.objects.get(id=id)
        messages = group.messages.order_by('-time')

    return render_to_response('GMA/ajax_messages.html', {'messages': messages}, RequestContext(request))

def get_conversation(user1, user2):
    crit1 = Q(sender=user1) & Q(recipient=user2.profile)
    crit2 = Q(sender=user2) & Q(recipient=user1.profile)
    message_list = Message.objects.filter(crit1 | crit2).order_by('-time')
    return message_list