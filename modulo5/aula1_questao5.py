import emoji

emojis_disponiveis = {
    "❤️": ":red_heart:",
    "👍": ":thumbs_up:",
    "🤔": ":thinking_face:",
    "🥳": ":partying_face:"
}

print("Emojis disponíveis:")
for emj, cod in emojis_disponiveis.items():
    print(f"{emj} - {cod}")

frase_codificada = input("Digite uma frase e ela será emojizada:\n")

frase_emojizada = emoji.emojize(frase_codificada, language='alias')

print("Frase emojizada:")
print(frase_emojizada)
