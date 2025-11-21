from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import threading
import socket
import hashlib
import os

class Universale_Nucleare(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.listener_avviato = False

    def build(self):
        app = BoxLayout(orientation="vertical")

        # Title label
        title = Label(text="Universale Nucleare", font_size=40, size_hint=(1, 0.2))
        app.add_widget(title)

        bottone = Button(text="Avvia Listener", font_size=30)
        bottone.bind(on_press=self.avvia_listener)
        app.add_widget(bottone)

        scansione = Button(text="Test Connessione", font_size=30)
        scansione.bind(on_press=self.test_connection)
        app.add_widget(scansione)

        segreto = Button(text="Genera Hash", font_size=30)
        segreto.bind(on_press=self.genera_hash)
        app.add_widget(segreto)

        rudati = Button(text="Info Sistema", font_size=30)
        rudati.bind(on_press=self.info_sistema)
        app.add_widget(rudati)

        # Status label
        self.status_label = Label(text="Pronto", font_size=20, size_hint=(1, 0.2))
        app.add_widget(self.status_label)

        return app

    def genera_hash(self, _):
        """Genera un hash SHA256"""
        try:
            data = os.urandom(32)
            hash_obj = hashlib.sha256(data)
            hash_hex = hash_obj.hexdigest()
            self.status_label.text = f"Hash: {hash_hex[:20]}..."
        except Exception as e:
            self.status_label.text = f"Errore: {str(e)}"

    def test_connection(self, _):
        """Test di connessione di base"""
        try:
            hostname = socket.gethostname()
            self.status_label.text = f"Hostname: {hostname}"
        except Exception as e:
            self.status_label.text = f"Errore: {str(e)}"

    def avvia_listener(self, _):
        """Avvia un listener di base"""
        if not self.listener_avviato:
            self.listener_avviato = True
            self.status_label.text = "Listener avviato"
            threading.Thread(target=self._listener_thread, daemon=True).start()
        else:
            self.status_label.text = "Listener già attivo"

    def _listener_thread(self):
        """Thread del listener"""
        try:
            self.status_label.text = "Listener in esecuzione..."
        except Exception as e:
            self.status_label.text = f"Errore listener: {str(e)}"

    def info_sistema(self, _):
        """Mostra informazioni sul sistema"""
        try:
            import platform
            info = f"OS: {platform.system()}"
            self.status_label.text = info
        except Exception as e:
            self.status_label.text = f"Errore: {str(e)}"


if __name__ == "__main__":
    Universale_Nucleare().run()
