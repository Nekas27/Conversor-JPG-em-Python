from PIL import Image
import os

pasta_entrada = "C:/Users/User/Desktop/carros/pasta_entrada"
pasta_saida = "C:/Users/User/Desktop/carros/pasta_saida"
formato_destino = "JPEG"
nova_largura = 1000
nova_altura = 1000

for arquivo in os.listdir(pasta_entrada):
    if arquivo.endswith((".jpg", ".png", ".gif", ".webp", ".rgba")):
        imagem = Image.open(os.path.join(pasta_entrada, arquivo))

        if imagem is not None:
            # Determina a largura e altura originais da imagem
            largura_original, altura_original = imagem.size

            # Calcula as novas dimensões e mantém a proporção original
            proporcao = min(nova_largura / largura_original, nova_altura / altura_original)
            nova_largura_redimensionada = int(largura_original * proporcao)
            nova_altura_redimensionada = int(altura_original * proporcao)

            # Preenche a nova imagem de 1000x1000 pixels com branco rgb(255,255,255)
            imagem_redimensionada = Image.new("RGB", (nova_largura, nova_altura), (255, 255, 255))

            # Cola a imagem redimensionada no centro da nova imagem
            x_offset = (nova_largura - nova_largura_redimensionada) // 2
            y_offset = (nova_altura - nova_altura_redimensionada) // 2
            imagem_redimensionada.paste(imagem.resize((nova_largura_redimensionada, nova_altura_redimensionada), Image.LANCZOS), (x_offset, y_offset))

            # Salva a imagem final como JPEG na pasta de saída 
            novo_nome = os.path.splitext(arquivo)[0] + ".jpg"
            imagem_redimensionada.save(os.path.join(pasta_saida, novo_nome), formato_destino)
