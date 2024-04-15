from django.shortcuts import render
from django.http import JsonResponse
from threading import Thread
from .utils import voice
from django.http import HttpResponse
import pyscript
from django.views.decorators.csrf import csrf_exempt


# Global variable to control the voice assistant state
voice_assistant_thread = None

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def listen(request):
    global voice_assistant_thread

    if request.method == 'GET':
        action = request.GET.get('action')

        if action == 'start':
          
            if voice_assistant_thread is None or not voice_assistant_thread.is_alive():
                # Start voice assistant in a separate thread
                voice_assistant_thread = Thread(target=voice.start_voice_assistant)
                voice_assistant_thread.start()
                return JsonResponse({'status': 'started'})
            else:
                    return JsonResponse({'status': 'already_running'})
                    
        elif action == 'stop':
            if voice_assistant_thread is not None and voice_assistant_thread.is_alive():
                # Stop voice assistant
                voice.stop_voice_assistant()
                voice_assistant_thread.join() 
                return JsonResponse({'status': 'stopped'})
            else:
                return JsonResponse({'status': 'not_running'})
    return JsonResponse({'status': 'error'})
   
   