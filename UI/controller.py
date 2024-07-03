import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._nazione=None
        self._anno=None
        self._numero=None
    def fillDD(self):
        for element in self._model.get_Nations():
            self._view.ddnation.options.append(ft.dropdown.Option(text=f"{element}", on_click=self.read_nazione))
            pass
        for i in range(2015,2019):
            self._view.ddyear.options.append(ft.dropdown.Option(text=f"{i}", on_click=self.read_anno))
    def read_nazione(self,e):
        self._nazione=e.control.text
        self._view.btn_volume.disabled = True
        self._view.btn_retailer.disabled = True
        self._view.update_page()
    def read_anno(self,e):
        self._view.btn_volume.disabled = True
        self._view.btn_retailer.disabled = True
        self._view.update_page()
        try:
            self._anno=int(e.control.text)
        except ValueError:
            return
    def handle_graph(self,e):
        self._view.txt_result.clean()
        if not self._nazione:
            self._view.create_alert("scegli una nazione")
            return
        if not self._anno:
            self._view.create_alert("scegli un anno")
            return
        self._model.creaGrafo(self._nazione,self._anno)
        self._view.txt_result.controls.append(
            ft.Text(f"Grafo Creato \nci sono {self._model.numNodi()} vertici\nci sono: {self._model.numArchi()} archi"))
        self._view.btn_volume.disabled=False
        self._view.btn_retailer.disabled=False
        self._view.update_page()

        pass
    def handle_volume(self,e):
        dizionario=self._model.Volume()
        self._view.txt_result.clean()
        self._view.txt_result.controls.append(
            ft.Text(
                "I volumi di vendita dei retailer nel grafo sono:"))
        for element in dizionario:
            self._view.txt_result.controls.append(
                ft.Text(
                    f"{element.name}-->{dizionario[element]}"))
        self._view.update_page()
        pass
    def read_path(self,e):
        try:
            self._numero=int(e.control.value)
        except ValueError:
            return
    def handle_retailer(self,e):
        if not self._numero:
            self._view.create_alert("scegli un numero di archi")
            return
        if self._numero<2:
            self._view.create_alert("scegli un numero di archi maggiore o uguale ad 1")
            return
        self._view.txt_result.clean()
        self._view.txt_result.controls.append(
            ft.Text(
                "Percorso massimo"))
        for element in self._model.handle_ricorsione(self._numero):
            self._view.txt_result.controls.append(
                ft.Text(
                    f"{element}"))
        self._view.update_page()
        pass