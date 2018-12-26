from subprocess import call

def print_menu():
    print 30 * "-", "MENU", 30 * "-"
    print "1. Videojuego de parejas"
    print "2. Videojuego cricugrama"
    print "3. Ver tutorial"
    print "4. Hacer el test"
    print "5. Exit"
    print 67 * "-"


loop = True

while loop:
    print_menu()
    choice = input("Enter your choice [1-5]: ")

    if choice == 1:
        # Open the game parejas
        execfile('parejas/parejas.py')
    elif choice == 2:
        # Open the game crucigrama
        call(["python crucigrama/crucigrama.py"], shell=True)
    elif choice == 3:
        # Open the tutorial
        call(["python tutorial/tutorial.py"], shell=True)
    elif choice == 4:
        # Open the test
        call(["python test/test.py"], shell=True)
    elif choice == 5:
        print "Salir"
        loop = False
    else:
        raw_input("Opcion seleccionada incorrecta")