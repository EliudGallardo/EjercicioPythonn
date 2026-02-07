logs = [
    ("192.168.1.1", "/home", "Chrome"),
    ("192.168.1.2", "/login", "Firefox"),
    ("192.168.1.1", "/dashboard", "Chrome"),
    ("192.168.1.3", "/home", "Edge"),
    ("192.168.1.2", "/home", "Firefox")
]

urls_por_ip = {}

for log in logs:
    ip = log[0]
    url = log[1]

    if ip in urls_por_ip:
        urls_por_ip[ip].add(url)
    else:
        urls_por_ip[ip] = set()
        urls_por_ip[ip].add(url)

print("URLs por IP:", urls_por_ip)


visitas_url = {}

for log in logs:
    url = log[1]

    if url in visitas_url:
        visitas_url[url] += 1
    else:
        visitas_url[url] = 1

print("Visitas por URL:", visitas_url)


uso_navegador = {}

for log in logs:
    navegador = log[2]

    if navegador in uso_navegador:
        uso_navegador[navegador] += 1
    else:
        uso_navegador[navegador] = 1

mayor_navegador = ""
mayor_uso = 0

for navegador, total in uso_navegador.items():
    if total > mayor_uso:
        mayor_uso = total
        mayor_navegador = navegador

print("Navegador más usado:", mayor_navegador, "con", mayor_uso)


ips_unicas = set()

for log in logs:
    ips_unicas.add(log[0])

lista_ips = list(ips_unicas)
lista_ips.sort()

print("Lista ordenada de IPs únicas:", lista_ips)
