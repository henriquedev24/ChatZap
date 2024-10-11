# Importar flet
import flet as ft  
# Criar função principal para rodar o aplicativo
def app_main(page):
    # Criar o aplicativo
    titulo = ft.Text("HashZap")
    def enviar_mensagem(ev):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        texto = f"{nome_usuario}: {texto_campo_mensagem}"
        page.pubsub.publish(texto)
        chat.controls.append(texto)
        campo_enviar_mensagem.value = ""
        page.update()

    campo_enviar_mensagem = ft.TextField(label="Mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar" , on_click=enviar_mensagem)
    linha_enviar = ft.Row(
        [campo_enviar_mensagem, botao_enviar],
    )

    chat = ft.Column()
    def entrar_chat(ev):
        popup.open = False
        page.remove(titulo)
        page.remove(botao)
        page.add(campo_enviar_mensagem)
        page.add(botao_enviar)
        page.add(chat)
        page.add(linha_enviar)

        nome_usuario = caixa_nome.value
        chat.controls.append(ft.Text(f"Olá {nome_usuario}"))
        page.update()
    # Criar popup
    titulo_popup = ft.Text("Bem-vindo")
    caixa_nome = ft.TextField()
    botao_popup = ft.ElevatedButton("Chat")

    popup = ft.AlertDialog(
        title=titulo_popup,
        content=caixa_nome,
        actions=[botao_popup],
    )
    # Criar botão inicial
    def abrir_popup(ev):
        page.dialog = popup
        popup.open = True
        print("Abrir")
    botao = ft.ElevatedButton("Iniciar", on_click=abrir_popup)
    # Definir o conteúdo da tela inicial
    page.add(titulo)
    page.add(botao)
# Executar a função com flet
ft.app(app_main)
