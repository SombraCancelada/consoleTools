import time
import sys


class TextDecorator():
    """
    Herramientas para hacer los programas de consola mas dinamicos
    """
    __BLACK = '\033[30m'
    __PINK = '\033[95m'
    __OKBLUE = '\033[94m'
    __OKGREEN = '\033[92m'
    __WARNING = '\033[93m'
    __FAIL = '\033[91m'
    __ENDC = '\033[0m'
    __text = ""
    __start = u"\u001b[38;5"

    # print(u"\u001b[38;5;129;44;1;4;5" +"m" + text + u"\u001b[0m")

    def __base_decorator(self, text, bg_color=None, text_color=None, blink=False, underline=False, bold=False, italic=False):
        bg_color = ";" + \
            str(bg_color) if bg_color and bg_color >= 40 and bg_color <= 47 else ""
        text_color = ";" + \
            str(text_color) if text_color and text_color > 0 and text_color < 255 else ";0"
        blink = ";5" if blink else ""
        bold = ";1" if bold else ""
        underline = ";4" if underline else ""
        italic = ";3" if italic else ""
        return self.__start + text_color + bg_color + blink + italic + underline + bold + "m" + text + self.__ENDC

    def tprint(self, text, bg_color=None, text_color=None, blink=False, underline=False, bold=False, italic=False):
        """
        Imprime un texto decorado
        text: texto para imprimir
        bg_color = Color del fondo ( numero entre 40 - 47)

        """
        print(self.__base_decorator(text, bg_color,
                                    text_color, blink, underline, bold, italic))

    def get_decorators(self, text, bg_color=None, text_color=None, blink=False, underline=False, bold=False, italic=False):
        """ Retorna un texto con decoradores listo para ser impreso """
        return self._base_decorator(text, bg_color, text_color, blink, underline, bold, italic)

    def red(self, arg):
        """ Texto en color rojo """
        return self.__FAIL + arg + self.__ENDC

    def blue(self, arg):
        """ Texto en color azul """
        return self.__OKBLUE + arg + self.__ENDC

    def green(self, arg):
        """ Texto en color verde """
        return self.__OKGREEN + arg + self.__ENDC

    def pink(self, arg):
        """ Texto en color rosado """
        return self.__PINK + arg + self.__ENDC

    def pause(self, text, time):
        print(text)
        time.sleep(time)

    def loader(self, title="loading...", seconds=0.01, bg_color=None, text_color=None, blink=False, underline=False, bold=False, italic=False):
        """Crear un cargador que va del 1% - 100%, puede especifiar color de texto, color de fondo, negrita, cursiva y parpadeo"""
        print(title)
        for i in range(0, 100):
            time.sleep(seconds)
            sys.stdout.write(u"\u001b[1000D" + self.__base_decorator(
                str(i + 1) + "%", bg_color, text_color, blink, underline, bold, italic))
            sys.stdout.flush()
        print("\n")

    def progress_bar(self, title="loading...", seconds=0.01, bg_color=None, text_color=None, blink=False, underline=False, bold=False, italic=False):
        print(title)
        for i in range(0, 100):
            time.sleep(seconds)
            width = (i + 1) / 4
            sys.stdout.write(u"\u001b[1000D" + self.__base_decorator("[" + "#" * int(
                width) + "]", bg_color, text_color, blink, underline, bold, italic))
            sys.stdout.flush()
        print("\n")


colors = TextDecorator()

# colors.tprint("hola", 44, 125, True, True)
# colors.loader(text_color = 145)
# colors.progress_bar(text_color = 122)
