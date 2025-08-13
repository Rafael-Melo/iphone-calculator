import flet as ft
from decimal import Decimal

# Lista de botões da calculadora, com informações sobre operadores, cores de fonte e fundo.
botoes = [
    {'operador': 'AC', 'fonte': ft.Colors.BLACK, 'fundo': ft.Colors.BLUE_GREY_100, 'ink': ft.Colors.RED},
    {'operador': '±', 'fonte': ft.Colors.BLACK, 'fundo': ft.Colors.BLUE_GREY_100, 'ink': ft.Colors.GREY},
    {'operador': '%', 'fonte': ft.Colors.BLACK, 'fundo': ft.Colors.BLUE_GREY_100, 'ink': ft.Colors.GREY},
    {'operador': '/', 'fonte': ft.Colors.WHITE, 'fundo': ft.Colors.ORANGE, 'ink': ft.Colors.AMBER_600},
    {'operador': '7', 'fonte': ft.Colors.WHITE, 'fundo': ft.Colors.WHITE24, 'ink': ft.Colors.WHITE10},
    {'operador': '8', 'fonte': ft.Colors.WHITE, 'fundo': ft.Colors.WHITE24, 'ink': ft.Colors.WHITE10},
    {'operador': '9', 'fonte': ft.Colors.WHITE, 'fundo': ft.Colors.WHITE24, 'ink': ft.Colors.WHITE10},
    {'operador': '*', 'fonte': ft.Colors.WHITE, 'fundo': ft.Colors.ORANGE, 'ink': ft.Colors.AMBER_600},
    {'operador': '4', 'fonte': ft.Colors.WHITE, 'fundo': ft.Colors.WHITE24, 'ink': ft.Colors.WHITE10},
    {'operador': '5', 'fonte': ft.Colors.WHITE, 'fundo': ft.Colors.WHITE24, 'ink': ft.Colors.WHITE10},
    {'operador': '6', 'fonte': ft.Colors.WHITE, 'fundo': ft.Colors.WHITE24, 'ink': ft.Colors.WHITE10},
    {'operador': '-', 'fonte': ft.Colors.WHITE, 'fundo': ft.Colors.ORANGE, 'ink': ft.Colors.AMBER_600},
    {'operador': '1', 'fonte': ft.Colors.WHITE, 'fundo': ft.Colors.WHITE24, 'ink': ft.Colors.WHITE10},
    {'operador': '2', 'fonte': ft.Colors.WHITE, 'fundo': ft.Colors.WHITE24, 'ink': ft.Colors.WHITE10},
    {'operador': '3', 'fonte': ft.Colors.WHITE, 'fundo': ft.Colors.WHITE24, 'ink': ft.Colors.WHITE10},
    {'operador': '+', 'fonte': ft.Colors.WHITE, 'fundo': ft.Colors.ORANGE, 'ink': ft.Colors.AMBER_600},
    {'operador': 'DEL', 'fonte': ft.Colors.WHITE, 'fundo': ft.Colors.WHITE24, 'ink': ft.Colors.WHITE},
    {'operador': '0', 'fonte': ft.Colors.WHITE, 'fundo': ft.Colors.WHITE24, 'ink': ft.Colors.WHITE10},
    {'operador': '.', 'fonte': ft.Colors.WHITE, 'fundo': ft.Colors.WHITE24, 'ink': ft.Colors.WHITE10},
    {'operador': '=', 'fonte': ft.Colors.WHITE, 'fundo': ft.Colors.ORANGE, 'ink': ft.Colors.AMBER_600},
]

def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLACK
    page.title = 'Calculator'
    page.window.resizable = False
    page.window.width = 270
    page.window.height = 420
    page.window.always_on_top = True

    result = ft.Text(value="0", color=ft.Colors.WHITE, size=40)

    def calculate(operador, value_at):
        try:
            value = Decimal(eval(value_at))

            if operador == '%':
                value /=100
            elif operador == '±':
                value = -value
        except:
            return 'Error'
        
        digits = min(abs(Decimal(value).as_tuple().exponent), 5)
        return format(value, f'.{digits}f')

    def select(e):
        nonlocal result
        value_at = result.value if result.value not in ('0', 'Error') else ''
        value = e.control.content.value

        if value.isdigit():
            value = value_at + value
        elif value == 'AC':
            value = '0'
        elif value == 'DEL':
            value = value_at[:-1] if value_at else '0'
            if not value:
                value = '0'
        elif value in ('%', '±', '='):
            value = calculate(operador=value, value_at=value_at)
        else: 
            if value_at and value_at[-1] in ('/', '*', '-', '+', '.'):
                value_at = value_at[:-1]
            value = value_at + value

        result.value = value
        result.update()

    display = ft.Row(
        width=250,
        controls=[result],
        alignment='end',
    )

    btn = [ft.Container(
        content=ft.Text(value=btn['operador'], color=btn['fonte']),
        width=50,
        height=50,
        bgcolor=btn['fundo'],
        border_radius=100,
        alignment=ft.alignment.center,
        ink=True,
        ink_color=btn['ink'],
        on_click=select
    ) for btn in botoes]

    keyboard = ft.Row(
        width=250,
        wrap=True,
        controls=btn,
        alignment='end',
    )

    page.add(display, keyboard)


if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')

# flet run .\src\iphone_calculator\main.py 