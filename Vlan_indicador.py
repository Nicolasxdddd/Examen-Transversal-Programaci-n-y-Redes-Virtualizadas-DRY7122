# vlan_checker.py

def verificar_vlan(vlan_id):
    if 1 <= vlan_id <= 1005:
        return "VLAN en el rango normal"
    elif 1006 <= vlan_id <= 4094:
        return "VLAN en el rango extendido"
    else:
        return "VLAN fuera del rango permitido"

if __name__ == "__main__":
    try:
        vlan_id = int(input("Introduce el número de VLAN: "))
        resultado = verificar_vlan(vlan_id)
        print(resultado)
    except ValueError:
        print("Por favor, introduce un número válido.")
