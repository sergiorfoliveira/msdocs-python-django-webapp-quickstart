from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import secrets
from hello_azure.templates.hello_azure import pergunta
from hello_azure.templates.hello_azure import chatGPT


def index(request):
    request.session.save()
    session_key = request.session.session_key
    secret = secrets.token_urlsafe(16)
    print(secret)
    ix, p = text.getPergunta(session_key, secret)
    request.session.save()
    args = {'mytext': p, 'key': session_key + secret}
    print('Request for index page received')
    return render(request, 'hello_azure/index.html', args)


@csrf_exempt
def testa(request):
    session_key = request.session.session_key
    print(session_key)
    if request.method == 'POST':
        r = request.POST.get('resposta')
        r = r.replace(" ", "")
        print('r=')
        print(r)
        sk = request.POST.get('key')
        print('sk=')
        print(sk)
        if not(sk in text.sessions):
            mensagem = "Sessão inválida ou expirada."
            context = {'titulo': 'Sessão expirada', 'mensagem': mensagem}
            return render(request, 'hello_azure/getquery.html', context)
        if r is None or r == '':
            print("Request for hello page received with no name or blank name -- redirecting")
            return redirect('index')
        else:
            print("Request for hello page received with result=%s" % r)
            p, resp = text.popSession(sk)
            print('resp=')
            print(resp)
            if r == resp:
                return render(request, 'hello_azure/getquery.html')
            else:
                mensagem = "Embora errar seja humano, esse teste visa ao acerto. Por favor releia as regras na página anterior."
                context = {'titulo': 'Incorreto', 'mensagem': mensagem}
                return render(request, 'hello_azure/hello.html', context)
    else:
        return redirect('hello_azure/index.html')


@csrf_exempt
def getquery(request):
    q = request.POST.get('query')
    r = chatGPT.answer_query(q)
    context = {'titulo': 'Resposta', 'mensagem': r}
    return render(request, 'hello_azure/hello.html', context)


text = pergunta.Pergunta()

