from django.contrib.auth.models import User
from django.http import Http404
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from messaging.models import Message

@login_required()
def contact_users(request):
    contacts = request.user.profile.contacts.order_by('last_name', 'first_name')
    text = "My contacts"
    return render_to_response('GMA/users.html', {'users': contacts, 'text': text}, RequestContext(request))

@login_required()
def all_users(request):
    users = User.objects.order_by('last_name', 'first_name')
    text = "List of all users"
    return render_to_response('GMA/users.html', {'users': users, 'text': text}, RequestContext(request))

@login_required()
def user_by_id(request, user_id):

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise Http404

    if user == request.user:
        return redirect('/profile/')

    if request.method == 'POST':
        if request.POST.get("action_type", "") == "add":
            request.user.profile.contacts.add(user)
        elif request.POST.get("action_type", "") == "remove":
            request.user.profile.contacts.remove(user)
        elif request.POST.get("action_type", "") == "send":
            message = Message(text=request.POST.get("message", ""), sender=request.user, recipient=user.profile)
            message.save()

    is_friend = request.user.profile.contacts.filter(id=user_id).exists()
    context_dict = {}
    context_dict['u'] = user
    context_dict['is_friend'] = is_friend

    return render_to_response('GMA/user_details.html', context_dict, RequestContext(request))

@login_required()
def search_user(request):
    return render_to_response('GMA/search_user.html',{}, RequestContext(request))

@login_required()
def ajax_search(request):
    first_name = ''
    last_name = ''

    if request.method == 'GET':
        first_name = request.GET['first_name']
        last_name = request.GET['last_name']

    return render_to_response('GMA/ajax_users.html', {'user_list': find_matching_users(first_name, last_name)}, RequestContext(request))

def find_matching_users(first_name='', last_name=''):
    users = []

    if first_name or last_name:
        users = User.objects.filter(first_name__contains=first_name, last_name__contains=last_name)

    return users