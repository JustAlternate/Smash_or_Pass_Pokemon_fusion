import requests, json

for i in range(1,990):
    
    pokemon = requests.get("https://pokeapi.co/api/v2/pokemon/"+str(i)).text
    pokemon = json.loads(pokemon)

    url = pokemon["sprites"]["front_default"]
    """
    img_data = requests.get(url).content
    with open(pokemon["name"]+".png", 'wb') as handler:
        handler.write(img_data)
    """
    
    filename = url.split('/')[-1]
    r = requests.get(url, allow_redirects=True)
    open("/home/justalternate/Projects/PokeNotif/assets/pokemon/"+filename, 'wb').write(r.content)
