from django.shortcuts import render_to_response

from django.contrib.auth.decorators import login_required

from mainapp.models import (Trajectory, Course)

#@login_required
def compare(request):
    trajectories = Trajectory.objects.all()
    
    return render_to_response('compare.html', {
        'trajectories' : trajectories,
    })

#@login_required
def analytics(request):
    trajectories = Trajectory.objects.all()
    
    return render_to_response('analytics.html', {
        'trajectories' : trajectories,
    })
