from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        connessione=get_connection()

        if connessione is None:
            return None

        cursore = connessione.cursor(dictionary=True)
        query = """SELECT * FROM Strumento
                ORDER BY codice"""
        cursore.execute(query)
        righe = cursore.fetchall()

        strumenti = []

        for riga in righe:
            strumento = Strumento(
                codice=riga["codice"],
                tipo=riga["tipo"],
                marca=riga["marca"],
                anno_acquisto=riga["anno_acquisto"],
                valore=riga["valore"],
                disponibile=bool(riga["disponibile"])
            )

            strumenti.append(strumento)

        cursore.close()
        connessione.close()
        return strumenti

        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """

    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        # TODO
