from VistaInicio import VistaInicio
from controladorInicio import controladorInicio

if __name__ == "__main__":
    login_view = VistaInicio()
    login_controller = controladorInicio(VistaInicio)
    login_view.mainloop()