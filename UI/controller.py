import flet as ft

import model.model
from UI.view import View
from model.model import DepositoStrumenti


'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
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
    def mostra_strumenti(self):
        self._view.lista_strumenti.controls.clear()
        # Serve a svuotare la lista grafica degli strumenti, rimuovendo tutti gli elementi che contiene.
        # self._view --> La View collegata al Controller
        # .lista_strumenti --> La ListView creata nella View
        # .controls --> La lista dei controlli al suo interno
        # .clear() --> Rimuove tutti gli elementi

        strumenti = self._model.get_strumenti()

        if strumenti is None:
            self._view.update()
            self._view.show_alert("Errore durante la lettura del database.")
            return

        if not strumenti:
            self._view.update()
            self._view.show_alert("Non ci sono strumenti nel database.")
            return

        for strumento in strumenti:
            descrizione = str(strumento)
            # Creo un elemento grafico che contiene la descrizione dello strumento.
            testo = ft.Text(descrizione)
            # Aggiungo l'elemento alla lista dell'interfaccia.
            self._view.lista_strumenti.controls.append(testo)
            # self.lista_strumenti è una listview che è già stata creata nella view e va solo popolata

        self._view.update()
