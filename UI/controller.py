import flet as ft
from UI.view import View
from model.automobile import Automobile
from model.model import Autonoleggio

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:

    def __init__(self, view : View, model : Autonoleggio):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    # TODO
    def mostra_automobili(self, e):
        automobili = self._model.get_automobili()
        self._view.lista_auto.controls.clear()
        if not automobili:
            self._view.lista_auto.controls.append(ft.Text("Nessuna automobile trovata"))
        else:
            for auto in automobili:
                self._view.lista_auto.controls.append(ft.Text(f"{auto.codice} - {auto.marca} {auto.modello} ({auto.anno}) - {auto.posti} posti - {'Disponibile' if auto.disponibile else 'Non disponibile'}"))
        self._view.update()


    def cerca_automobili(self, e):
        modello = self._view.input_modello.value  # prende il modello dall’input
        automobili = self._model.cerca_automobili_per_modello(modello)
        self._view.lista_auto_ricerca.controls.clear()
        if not automobili:
            self._view.lista_auto_ricerca.controls.append(ft.Text("Nessuna automobile trovata"))
        else:
            for auto in automobili:
                self._view.lista_auto_ricerca.controls.append(ft.Text(f"{auto.codice} - {auto.marca} {auto.modello} ({auto.anno}) - {auto.posti} posti - {'Disponibile' if auto.disponibile else 'Non disponibile'}"))
        self._view.update()