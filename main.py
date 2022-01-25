lista_zakupow = {
    'piekarnia': ['Chleb', 'Pączek', 'Bułki'],
    'warzywniak': ['Marchew', 'Seler', 'Rukola']
}
for i , j in lista_zakupow.items():
    print(f"Idę do {i.capitalize()} kupuję tu następujące rzeczy: {[x.capitalize() for x in j]} ")