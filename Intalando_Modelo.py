from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
import os

modelo_local = "/save_data/Meu_Modelo_mBART"

if not os.path.exists(modelo_local):
    print("Baixando o modelo MBART para uso offline...")
    modelo = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
    tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")

    modelo.save_pretrained(modelo_local)
    tokenizer.save_pretrained(modelo_local)
    print("Modelo baixado e salvo localmente.")

else:
    print("O modelo já está salvo localmente. Nenhum download necessário.")

