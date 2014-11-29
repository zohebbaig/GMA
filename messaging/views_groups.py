from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponseForbidden
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from messaging.models import Group, Message
from messaging.forms import GroupForm


@login_required()
def my_groups(request):
    text = "My memberships"
    return render_to_response('GMA/groups.html', {'text': text, 'groups': request.user.messaging_groups.all()}, RequestContext(request))

@login_required()
def all_groups(request):
    text = "Browse all groups"
    return render_to_response('GMA/groups.html', {'text': text, 'groups': Group.objects.all()}, RequestContext(request))

@login_required()
def owned_groups(request):
    text = "Groups I created"
    return render_to_response('GMA/groups.html', {'text': text, 'groups': request.user.owned_groups.all()}, RequestContext(request))

#Get request to pass group ID, add or remove member to group
@login_required()
def group_by_id(request, group_id):
    context_dict = {}

    try:
        group = Group.objects.get(id=group_id)
    except Group.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        if request.POST.get("action_type", "") == "add":
            group.members.add(request.user)
        elif request.POST.get("action_type", "") == "remove":
            group.members.remove(request.user)

#assigning python objects with names, template, data for the template (dictionary) context
    context_dict['group'] = group
    context_dict['is_member'] = group.members.filter(id=request.user.id).exists()
    context_dict['is_owner'] = is_group_owned(request.user, group_id)

    return render_to_response('GMA/group.html', context_dict, RequestContext(request))

#create group
@login_required()
def create_group(request):
    return alter_group(request, -1)

#edit group
@login_required()
def edit_group(request, group_id):
    return alter_group(request, group_id)

#alter group
@login_required()
def alter_group(request, group_id):
    created = False

    if group_id != -1:
        try:
            group = Group.objects.get(id=group_id)
        except Group.DoesNotExist:
            raise Http404
        if group.owner != request.user:
            raise PermissionDenied()


    if request.method == 'POST':
        if group_id == -1:
            form = GroupForm(data=request.POST)
        else:
            form = GroupForm(data=request.POST, instance=group)

        if form.is_valid():
            group = form.save(commit=False)
            group.owner = request.user
            group.save()
            if group_id == -1:
                group.members.add(request.user)
            group.save()
            created = True
        else:
            print form.errors
    else:
        if group_id == -1:
            form = GroupForm()
        else:
            form = GroupForm(instance=Group.objects.get(id=group_id))

    return render_to_response('GMA/group_form.html', {'group_id': group_id, 'created': created, 'group_form': form}, RequestContext(request))

#helper method to show if a user is a owner of a group
def is_group_owned(user, group_id):
    group = Group.objects.get(id = group_id)
    return group.owner == user

#helper method to get all the messages from the groups of a certain user, looks at top 10 messages
def messages_to_user_groups(user):
    groups = user.messaging_groups.all()
    messages = Message.objects.filter(recipient__in=groups)
    return messages.order_by('-time')[:10]

#the AJAX, returns table of groups that match a users search from the db
@login_required()
def search_group(request):
    context_dict = {}

    if request.method == 'GET':
        group_name = request.GET.get('grp_name')
        if group_name:
            context_dict['search_term'] = group_name
            context_dict['groups'] = Group.objects.filter(name__contains=group_name)

    return render_to_response('GMA/search_group.html',context_dict, RequestContext(request))


#AJAX helper to retrieve groups based on a group name token
@login_required()
def ajax_search(request):
    groups = []
    group_name = ''

    if request.method == 'GET':
        group_name = request.GET['group_name']

    if group_name:
        groups = Group.objects.filter(name__contains=group_name)

    return render_to_response('GMA/ajax_groups.html', {'group_list': groups}, RequestContext(request))
