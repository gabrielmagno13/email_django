from django import forms
from django.core.mail.message import EmailMessage


class ContatoForm(forms.Form):
    nome = forms.CharField(label='nome', max_length=50)
    email = forms.EmailField(label='email', max_length=50)
    assunto = forms.CharField(label='assunto', max_length=50)
    mensagem = forms.CharField(label='mensagem', widget=forms.Textarea())

    def enviar_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nEmail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject='Email django',
            body=conteudo,
            from_email='email@email.com',
            to = ['email@email.com',],
            headers={'Repl-to': email}
        )
        mail.send()