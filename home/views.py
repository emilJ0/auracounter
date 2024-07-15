from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Groups

@login_required(login_url="/user_auth")
def index(request):
    username = request.user.username
    try:
        group = Groups.objects.get(group_users__user__contains=[{'username': username}])
    except:
        group = Groups.objects.get(group_name="Platzhalter")

    if group.group_name != "Platzhalter":
        data = group.group_users["user"]
        users = [[item['username'], item['aura_amount']] for item in data]
        choices = [member["username"] for member in data]
        print(choices)
        context = {
            "group_name": group.group_name,
            "group_users": users,
            "choices": choices,
        }
    else:
        context = {
            "group_name": group.group_name,
        }
    return render(request, "home/test.html", context)

@login_required(login_url="/user_auth")
def start_create_group(request):
    return render(request, "home/create_group.html")

@login_required(login_url="/user_auth")
def create_group(request):
    if request.method == "POST":
        username = request.user.username
        group_name = request.POST.get("group_name")
        group_code = request.POST.get("group_code")
        Groups.objects.create(
            group_name=group_name,
            group_code=group_code,
            group_users={
                "user" : [{
                    "username" : username,
                    "aura_amount" : 0,
                }],
            },
            group_history=None
        )
        return redirect("/home/")
    else:
        return HttpResponse("Fehler bei Übertragung.")

@login_required(login_url="/user_auth")
def start_join_group(request):
    return render(request, "home/join_group.html")

def add_data(existing, new):
    for key, value in new.items():
        if isinstance(value, dict) and key in existing and isinstance(existing[key], dict):
            add_data(existing[key], value)  # Rekursiv nur für verschachtelte Wörterbücher
        else:
            existing[key] = value

def merge_data(existing, new):
    for key, value in new.items():
        if key not in existing:
            existing[key] = [value]
        else:
            if isinstance(existing[key], dict):
                existing[key] = [existing[key]]
            existing[key].append(value)
    return existing

@login_required(login_url="/user_auth")
def join_group(request):
    if request.method == "POST":
        username = request.user.username
        group_code = request.POST.get("group_code")
        print(f"entered code: {group_code}")
        print(f"real code: {Groups.objects.filter(group_code=group_code)}")
        test_group = Groups.objects.get(group_code=group_code)
        if test_group.group_code == group_code:
            group = Groups.objects.get(group_code=group_code)
            existing_group_data = group.group_users
            new_group_data = {
                "user":{
                    "username" : username,
                    "aura_amount": 0,
                },
            }
            existing_group_data = merge_data(existing_group_data, new_group_data)
            group.group_users = existing_group_data
            group.save()
            return redirect("/home/")
        else:
            return HttpResponse("Code stimmt nicht überein.")
    else:
        return HttpResponse("There was an Error in the request.")

@login_required(login_url="/user_auth")
def manage_aura(request):
    if request.method == "POST":
        username = request.user.username
        group = Groups.objects.get(group_users__user__contains=[{'username': username}])
        taken_user = request.POST.get("choice")
        amount = request.POST.get("amount")
        for u in group.group_users["user"]:
            if taken_user == u["username"]:
                u["aura_amount"] += int(amount)
                group.save()
                print("you got some aura")
        return redirect("/home/")

@login_required(login_url="/user_auth")
def leave_group(request):
    if request.method == "POST":
        username = request.user.username
        group = Groups.objects.get(group_users__user__contains=[{'username': username}])
        without_user = [u for u in group.group_users["user"] if u["username"] != username]
        group.group_users = {
            "user": without_user
        }
        group.save()
        return redirect("/home/")
