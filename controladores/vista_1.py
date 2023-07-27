class controlador_inicio():
    def __init__(self,app):
        self.app = app
        
    def mostrar_Menu(self):
        self.app.cambiar_frame(self.app.menu)