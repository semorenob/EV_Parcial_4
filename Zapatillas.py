reservas = []
stock = 20
reservado = 0

def reservarZapatillas():
    global reservado
    if reservado == 20:
        print("No hay stock disponible.")
    else:
        print("-- Reservar Zapatillas --")
        nombre = input("Nombre del comprador: ")
        for r in reservas:
            if r["Nombre"] == nombre:
                print("Este comprador ya tiene la máxima cantidad de reservas por comprador.")
                return    
        clave = input("Digite la palabra secreta para confirmar la reserva: ")
        if clave == "EstoyEnListaDeReserva":
            print(f"Reserva realizada exitosamente para {nombre}.")
            reserva = {"Nombre": nombre, "Reservas": 1}
            reservas.append(reserva)
            reservado += 1
        else:
            print("Error: palabra clave incorrecta. Reserva no realizada.")
    

def buscarReservas():
    global reservado
    print("-- Buscar Zapatillas Reservadas --")
    nombre = input("Nombre del comprador a buscar: ")
    for r in reservas:
        if r["Nombre"] == nombre:
            if r["Reservas"] == 1:
                print(f"Reserva encontrada: {r["Nombre"]} - {r["Reservas"]} par(es) (estándar).")
                vip = input("¿Desea pagar adicional para VIP y reservar 2 pares? (s/n): ").strip().lower()
                if vip == "s":
                    print(f"Reserva actualizada a VIP. Ahora {nombre} tiene 2 pares reservados")
                    r["Reservas"] = 2
                    reservado += 1
                    return
                else:
                    print("Manteniendo reserva actual.")
                    return
            else:
                print(f"Reserva encontrada: {r["Nombre"]} - {r["Reservas"]} par(es) (VIP).")
                return
    print("No se encontró ninguna reserva con ese nombre.")
            

def cancelarReserva():
    nombre = input("Nombre del comprador cuya reserva desea cancelar: ")
    for r in reservas:
        if r["Nombre"] == nombre:
            reservas.remove(r)
            print(f"La reserva de {nombre} ha sido cancelada.")
            return
        print("No se encontró ninguna reserva con ese nombre.")

def main():
    while True:
        print("TOTEM AUTOATENCIÓN RESERVA STRIKE")
        print("1.- Reservar zapatillas\n2.- Buscar zapatillas reservadas\n3.- Cancelar reservas\n4.- Salir")

        op = input("Seleccione una opción(1-4): ")

        if op == "1":
            reservarZapatillas()
        elif op == "2":
            buscarReservas()
        elif op == "3":
            cancelarReserva()
        elif op == "4":
            print("Programa terminado...")
            break
        else:
            print("Debe ingresar una opción válida!!")

main()