from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request , 'index.html')
    #return HttpResponse('home')

def analyze(request):
    flag = False
    
    # input string
    inputString = request.POST.get('text' , 'No_Input')
    
    # backup of input
    backupString = inputString   
    
    # utils
    removepunctuation = request.POST.get('removepunctuation' , 'off')
    capitalize = request.POST.get('capitalize' , 'off')
    removenewline = request.POST.get('removenewline' , 'off')
    removeextraspaces = request.POST.get('removeextraspaces' , 'off')
    charcounter = request.POST.get('charcounter' , 'off')

    # purpose
    purpose = ''

    # logic
    if removepunctuation == 'on':
        result = ''
        flag = True
        for char in inputString:
            if char not in ".,;:?!'–—()[]{}<>/\\...&@%$#*•+=_~^`´":
                result = result + char


        purpose =  purpose + '| Removed Punctuation |'
        inputString = result
        #return render(request , 'analyze.html' , {'purpose' : 'Removed Punctuation' , 'result' : result , 'inputstring' : inputString})
    
    if capitalize == 'on':
        flag = True
        result = ''
        for char in inputString:
            result = result + char.upper()
        
        purpose = purpose + '| Capitalize |'
        inputString = result
        #return render(request , 'analyze.html' , {'purpose' : 'Capitalized String' , 'result' : result , 'inputstring' : inputString})
    
    if removenewline == 'on':
        flag = True
        result = ''
        for char in inputString:
            if not (char == '\n' or char == '\r'):
                result = result + char

        purpose = purpose + '| RemoveNewLine |'
        inputString = result
        #return render(request , 'analyze.html' , {'purpose' : 'Removed NewLine' , 'result' : result , 'inputstring' : inputString})
    
    if removeextraspaces == 'on':
        flag = True
        result = ''
        print(len(inputString))
        for index in range(len(inputString)):
            if not (inputString[index] == ' ' and inputString[index + 1] == ' ' and index < len(inputString)):
                result = result + inputString[index]

        purpose = purpose + '| RemoveExtraSpaces |'
        inputString = result
        #return render(request , 'analyze.html' , {'purpose' : 'Removed NewLine character' , 'result' : result , 'inputstring' : inputString })
    
    if charcounter == 'on':
        flag = True
        counter = 0
        for char in inputString:
            counter = counter + 1

        purpose = purpose + '| CharCounter |'
        inputString = str(counter)

        #return render(request , 'analyze.html' , {'purpose' : 'Char Counter' , 'result' : counter , 'inputstring' : inputString})


    if not flag:
        return render(request , 'Error.html')

    return render(request , 'analyze.html' , { 'purpose' : purpose , 'result' : inputString , 'inputstring' : backupString})