"""
Modulo Calcolatrice

Esegue operazioni aritmetiche base.
"""

class Calcolatrice:
    """
    Una semplice calcolatrice con metodi per addizione, sottrazione, moltiplicazione e divisione.
    """

    def somma(self, a: float, b: float) -> float:
        """
        Somma due numeri.

        Args:
            a (float): Primo addendo
            b (float): Secondo addendo

        Returns:
            float: La somma di a e b
        """
        return a + b

    def sottrai(self, a: float, b: float) -> float:
        """
        Sottrae b da a.

        Args:
            a (float): Minuendo
            b (float): Sottraendo

        Returns:
            float: Il risultato di a - b
        """
        return a - b

    def moltiplica(self, a: float, b: float) -> float:
        """
        Moltiplica due numeri.

        Args:
            a (float): Primo fattore
            b (float): Secondo fattore

        Returns:
            float: Il prodotto
        """
        return a * b

    def dividi(self, a: float, b: float) -> float:
        """
        Divide a per b.

        Args:
            a (float): Il numeratore
            b (float): Il denominatore

        Returns:
            float: Il risultato della divisione

        Raises:
            ZeroDivisionError: Se b è zero
        """
        if b == 0:
            raise ZeroDivisionError("Divisione per zero")
        return a / b