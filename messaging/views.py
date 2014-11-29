from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from messaging.models import UserProfile, Message
from messaging.forms import UserForm, UserProfileForm, MessageForm, UserEditForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from messaging.views_groups import messages_to_user_groups

def encode_url(str):
    return str.replace(' ', '_')

def decode_url(str):
    return str.replace('_', ' ')

def index(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    else:
        return redirect('/login/')

@login_required
def home(request):
    context = RequestContext(request)
    context_dict = {}

    context_dict['group_messages'] = messages_to_user_groups(request.user)
    context_dict['personal_messages'] = request.user.profile.messages.order_by('-time')[:10]

    # Render and return the rendered response back to the user.
    return render_to_response('GMA/home.html', context_dict, context)


def user_login(request):
    context = RequestContext(request)
    context_dict = {}

    # If HTTP POST, pull out form data and process it.
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                context_dict['disabled_account'] = True
                return render_to_response('GMA/login.html', context_dict, context)
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            context_dict['bad_details'] = True
            return render_to_response('GMA/login.html', context_dict, context)

    else:
        return render_to_response('GMA/login.html', context_dict, context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def about(request):
    return render_to_response('GMA/about.html', {}, RequestContext(request))


def register(request):
    context = RequestContext(request)
    context_dict = {}
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        registered = save_user_form(user_form, profile_form)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context_dict['user_form'] = user_form
    context_dict['profile_form']= profile_form
    context_dict['registered'] = registered

    return render_to_response('GMA/register.html', context_dict, context)


@login_required
def profile(request):
    context = RequestContext(request)
    context_dict = {}
    profile = request.user.profile
    registered = False

    if request.method == 'POST':
        user_form = UserEditForm(data=request.POST, instance=request.user)
        profile_form = UserProfileForm(data=request.POST, instance=profile)

        registered = save_user_form(user_form, profile_form)

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = UserProfileForm(instance=profile)

    context_dict['user_form'] = user_form
    context_dict['profile_form'] = profile_form
    context_dict['registered'] = registered
    return render_to_response('GMA/profile.html', context_dict, context)


def save_user_form(user_form, profile_form):
    if user_form.is_valid() and profile_form.is_valid():
        user = user_form.save()

        user.set_password(user.password)
        user.save()

        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()

        return True

    else:
        print user_form.errors, profile_form.errors
        return False

