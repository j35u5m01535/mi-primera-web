# Tu primer acercamiento a la IA: Analizador de Sentimientos
print("--- Iniciando Mini-Cerebro ---")
nombre = input("Hola, soy tu script. ¿Como te llamas? ")
print(f"Mucho gusto, {nombre}. Analizando tu estado de animo...")

sentimiento = input("¿Como te sientes hoy? (bien/mal/estresado): ").lower()

if "bien" in sentimiento:
    print("Respuesta: ¡Genial! Tu productividad hoy sera del 100%.")
elif "mal" in sentimiento or "estresado" in sentimiento:
    print("Respuesta: Entiendo. Segun mis datos, deberias tomar un descanso de 5 min.")
else:
    print("Respuesta: Interesante... todavia estoy aprendiendo sobre esa emocion.")
    