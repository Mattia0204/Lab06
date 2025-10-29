from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
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

    def get_automobili(self) -> list[Automobile] | None:
        conn = get_connection()
        if conn is None:
            return None
        try:
            cur = conn.cursor()
            # usa le colonne esistenti nella tabella 'automobile'
            cur.execute("SELECT codice, marca, modello, anno, posti, disponibile FROM automobile")
            rows = cur.fetchall()
            cur.close()

            if not rows:
                return []

            automobili = []
            for row in rows:
                codice, marca, modello, anno, posti, disponibile = row
                # anno è YEAR -> converti a int o None
                anno_val = int(str(anno)) if anno not in (None, '') else None
                automobili.append(Automobile(codice, marca, modello, anno_val,
                                             int(posti) if posti is not None else None,
                                             bool(disponibile)))
            return automobili
        finally:
            conn.close()

    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        # TODO
        connection = get_connection()
        if connection is None:
            return None
        try:
            automobili=None
            cursor = connection.cursor()
            cursor.execute("SELECT id, marca, modello, anno FROM automobile")
            rows = cursor.fetchall()  # lista di tuple
            cursor.close()
            if rows[0] == modello:
                automobili = [Automobile(*row) for row in rows]
            return automobili
        finally:
            connection.close()

