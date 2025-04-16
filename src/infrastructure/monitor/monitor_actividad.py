from pynput import keyboard, mouse
from threading import Thread, Event
from datetime import datetime, timedelta
import time

class MonitorInactividad:
    def __init__(self, inactividad_callback, reanudar_callback, timeout=300):
        """
        :param inactividad_callback: Función que se llama tras timeout segundos sin actividad.
        :param reanudar_callback: Función que se llama al detectar actividad después de pausa.
        :param timeout: Tiempo de inactividad permitido (en segundos). Por defecto 5 min.
        """
        self.inactividad_callback = inactividad_callback
        self.reanudar_callback = reanudar_callback
        self.timeout = timeout
        self.ultima_actividad = datetime.now()
        self.en_pausa = False

        self._stop_event = Event()

    def iniciar(self):
        Thread(target=self._verificar_inactividad, daemon=True).start()
        mouse.Listener(on_move=self._resetear_timer, on_click=self._resetear_timer).start()
        keyboard.Listener(on_press=self._resetear_timer).start()

    def detener(self):
        self._stop_event.set()

    def _resetear_timer(self, *args):
        if self.en_pausa:
            self.reanudar_callback()
            self.en_pausa = False

        self.ultima_actividad = datetime.now()

    def _verificar_inactividad(self):
        while not self._stop_event.is_set():
            if not self.en_pausa and datetime.now() - self.ultima_actividad > timedelta(seconds=self.timeout):
                self.inactividad_callback()
                self.en_pausa = True
            time.sleep(1)
