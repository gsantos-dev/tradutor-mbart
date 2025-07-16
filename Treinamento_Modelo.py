import torch
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
from datasets import Dataset
from torch.utils.data import DataLoader

model_path = "C:/Users/Guilherme/Desktop/Projetos/Projeto_Tradutor/save_data/Meu_Modelo_mBART"

tokenizer = MBart50TokenizerFast.from_pretrained(model_path)
model = MBartForConditionalGeneration.from_pretrained(model_path)

tokenizer.src_lang = "pt_XX"
tokenizer.tgt_lang = "en_XX"


def carregar_texto(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as file:
        return [linha.strip() for linha in file.readlines()]


textos_pt = carregar_texto("C:/Users/Guilherme/Desktop/Projetos/Projeto_Tradutor/Texto_pt/Texto_Completo_PT.txt")
textos_en = carregar_texto("C:/Users/Guilherme/Desktop/Projetos/Projeto_Tradutor/Texto_en/Texto_Completo_EN.txt")


dataset = Dataset.from_dict({"source": textos_pt, "target": textos_en})

# Tokenizar dados corretamente
def tokenizar_exemplo(exemplos):
    inputs = tokenizer(exemplos["source"], max_length=512, truncation=True, padding="max_length", return_tensors="pt")
    targets = tokenizer(exemplos["target"], max_length=512, truncation=True, padding="max_length", return_tensors="pt")

    return {
        "input_ids": inputs["input_ids"].squeeze(0),  # Remover dimensão extra
        "attention_mask": inputs["attention_mask"].squeeze(0),
        "labels": targets["input_ids"].squeeze(0),
    }

dataset = dataset.map(tokenizar_exemplo, remove_columns=["source", "target"], batched=True)


# Função para processar lotes corretamente
def collate_fn(batch):
    return {
        "input_ids": torch.tensor([ex["input_ids"] for ex in batch], dtype=torch.long),
        "attention_mask": torch.tensor([ex["attention_mask"] for ex in batch], dtype=torch.long),
        "labels": torch.tensor([ex["labels"] for ex in batch], dtype=torch.long),
    }



# Criar DataLoader corretamente
batch_size = 2
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True, collate_fn=collate_fn)


optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5)


device = torch.device("cpu")
model.to(device)

# Número de épocas
num_epochs = 3

model.train()

for epoch in range(num_epochs):
    print(f"Epoch {epoch+1}/{num_epochs}")

    for batch in dataloader:
        inputs = {k: v.to(device) for k, v in batch.items()}  #Garantir que os tensores estejam na CPU

        outputs = model(**inputs)
        loss = outputs.loss

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        print(f"Loss: {loss.item()}")

print("Treinamento concluído! 🎉")

# Salvar o modelo e o tokenizer treinados
model.save_pretrained("C:/Users/Guilherme/Desktop/Projetos/Projeto_Tradutor/Modelo_Mbart_Treinado")
tokenizer.save_pretrained("C:/Users/Guilherme/Desktop/Projetos/Projeto_Tradutor/Modelo_Mbart_Treinado")
