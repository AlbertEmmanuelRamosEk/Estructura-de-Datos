class Nodo {
    Object dato;
    Nodo siguiente;

    public Nodo(Object dato) {
        this.dato = dato;
        this.siguiente = null;
    }
}

class ColaListaEnlazada{
    private Nodo frente;
    private Nodo finalCola;

    public ColaListaEnlazada(){
        this.frente = null;
        this.finalCola = null;
    }

    public boolean estaVacia(){
        return frente == null;
    }

    public void encolar(Object elemento){
        Nodo nuevo = new Nodo(elemento);
        if (estaVacia()){
            frente = nuevo;
            finalCola = nuevo;
        } else {
            finalCola.siguiente = nuevo;
            finalCola = nuevo;
        }
        System.out.println("Elemento agregado: " + elemento);
    }

    public Object desencolar(){
        if (estaVacia()){
            System.out.println("La cola está vacía, no se puede eliminar");
            return null;
        }
        Object dato = frente.dato;
        frente = frente.siguiente;
        if (frente == null){
            finalCola = null;
        }
        System.out.println("Elemento eliminado: " + dato);
        return dato;
    }

    public Void mostrarCola(){
        if (estaVacia()){
            System.out.println("la cola está vacía");
            return null;
        }
        Nodo actual = frente;
        System.out.println("Cola: ");
        while (actual != null){
            System.out.println(actual.dato + " ");
            actual = actual.siguiente;
        }
        System.out.println();
        return null;
    }
}

public class Main{
    public static void main(String[] args){
        ColaListaEnlazada cola = new ColaListaEnlazada();

        cola.encolar(10);
        cola.encolar(20);           
        cola.encolar(30);
        cola.mostrarCola(); 

       
        cola.desencolar();
        cola.mostrarCola();
    }
}
