#I have created this file - Shreya
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')  

def about(request):
    return render(request,'about.html')

def home(request):
    return render(request,'home.html')     

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    caps= request.POST.get('caps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if removepunc == "on":
        
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)  
    if caps == "on":
        analyzed = ""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params = {'purpose':'changed to uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)  
    
    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose':'new line remove', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)

    if extraspaceremover == "on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed=analyzed + char
        params = {'purpose':'extra space remover', 'analyzed_text': analyzed}
        djtext=analyzed
    # return render(request,'analyze.html',params)              
    elif(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and caps!="on"):

        return HttpResponse('Please select any opration')  
    return render(request,'analyze.html',params)

def navigation(request):
    s=['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
             '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
             '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
             '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
             ]
    # s='''<nav class="navbar navbar-inverse">
    #     <div class="container-fluid">
    #       <div class="navbar-header">
    #         <a class="navbar-brand" href="#">WebSiteName</a>
    #       </div>
    #       <ul class="nav navbar-nav">
    #         <li class="active"><a href="www.google.com/">Google</a></li>
    #         <li><a href="www.facebook.com/">Facebook</a></li>
    #         <li><a href="www.youtube.com/">Youtube</a></li>
    #         <li><a href="www.flipkart.com/">Flipkart</a></li>
    #       </ul>
    #     </div>
    #   </nav>'''            
    return HttpResponse((s))          

            

      