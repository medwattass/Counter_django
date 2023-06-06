from django.shortcuts import render, redirect


def root(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    if 'visited_counter' in request.session:
        request.session['visited_counter'] += 1
    else:
        request.session['visited_counter'] = 1
    return render(request, 'index.html')


def destroy_session(request):
    del request.session['counter']
    return redirect('/')


def increment_2(request):
    request.session['counter'] += 1
    return redirect('/')


def incrementation(request):
    request.session['counter'] += int(request.POST['incrementation']) - 1
    return redirect('/')