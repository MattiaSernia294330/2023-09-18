import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Esame 18/09/023- TURNO UNICO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.ddyear = None
        self.ddnation = None
        self.btn_graph = None
        self.btn_volume = None
        self.txt_path = None

        self.txt_result = None
        self.btn_retailer = None


    def load_interface(self):
        # title
        self._title = ft.Text("Lab13 - Ufo sighting", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        self.ddyear = ft.Dropdown(label="Anno")
        self.ddnation = ft.Dropdown(label="Nazione")


        # button for the "creat graph" reply
        self.btn_graph = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handle_graph)
        row1 = ft.Row([self.ddyear, self.btn_graph],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        self.btn_volume = ft.ElevatedButton(text="Calcola Volume", on_click=self._controller.handle_volume, disabled=True)
        row2 = ft.Row([self.ddnation, self.btn_volume],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)
        self._controller.fillDD()


        self._txt_path=ft.TextField(label="Lunghezza percorso", on_change=self._controller.read_path)
        self.btn_retailer = ft.ElevatedButton(text="Retailer Rappresentativi", on_click=self._controller.handle_retailer, disabled=True)

        row2 = ft.Row([self._txt_path,self.btn_retailer],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()
    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
