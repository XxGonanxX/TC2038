#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>

using namespace std;

// Función para calcular el hash
string calcularHash(vector<int>& a) {
    string hash;
    for (int i = 0; i < a.size(); ++i) {
        // Convierte el valor a hexadecimal y lo agrega al hash
        hash += to_string(a[i] / 16);
        hash += to_string(a[i] % 16);
    }
    return hash;
}

int main() {
    string nombreArchivo;
    int n;

    // Solicita el nombre del archivo y el valor de n
    cout << "Ingrese el nombre del archivo de texto: ";
    cin >> nombreArchivo;
    cout << "Ingrese el valor de n (multiplo de 4, 16 <= n <= 64): ";
    cin >> n;

    // Abre el archivo
    ifstream archivo(nombreArchivo);
    if (!archivo) {
        cerr << "No se pudo abrir el archivo." << endl;
        return 1;
    }

    // Lee el archivo y calcula el hash
    vector<int> a(n, 0);
    char c;
    int col = 0;
    while (archivo.get(c)) {
        a[col] += int(c);
        col = (col + 1) % n;
    }

    // Genera la salida
    string hash = calcularHash(a);

    // Muestra la tabla generada
    cout << "Tabla generada:" << endl;
    for (int i = 0; i < n; ++i) {
        cout << setw(4) << a[i];
        if (i % 4 == 3) cout << " ";
    }
    cout << endl;

    // Muestra el arreglo a
    cout << "Arreglo a:" << endl;
    for (int i = 0; i < n; ++i) {
        cout << a[i] << " ";
    }
    cout << endl;

    // Muestra la cadena de salida
    cout << "Cadena de salida (representacion hexadecimal):" << endl;
    cout << hash << endl;

    archivo.close();

    return 0;
}
