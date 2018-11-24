from django.shortcuts import render
from models import BugManager

def bug_manage(request):
    username = request.session.get('user','')
    bug_list = BugManager.objects.all()
    return render(request,'bug_manager.html',{'user':username,'bugs':bug_list})

# Create your views here.
