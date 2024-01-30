from django.shortcuts import render
from django.http import JsonResponse
import code
import sys
from io import StringIO

# Create your views here.

def indexView(request):
    return render(request, "myCLI/index.html")

def runPythonCode(request):
    if request.method == "GET":
        query = request.GET.get("query")
        interpreter = code.InteractiveInterpreter()

        original_stdout = sys.stdout
        sys.stdout = StringIO()
        
        success = interpreter.runcode(compile(query, '<string>', 'exec'))
        printed_content = sys.stdout.getvalue()
        printed_content = printed_content.split("\n")
        
        if printed_content:
            data = {'result': f'This is the command: {printed_content}'}
        else:
            data = {'result': f'This is the command: not_working'}

        # Create a JsonResponse object with additional parameters
        response = JsonResponse(data)
        return response

