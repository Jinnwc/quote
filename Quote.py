import flet as ft


def main(page: ft.Page):
    page.title = "quotes"
    page.color = "blackblackblack"

    quotes = {
        "english": "You can't blame gravity for falling in love.",
        "chinese": "你不能责怪重力让你坠入爱河。",
        "korean": "당신이 사랑에 빠진 것을 중력의 탓으로 돌릴 수 없습니다."
    }

    def change_quote(e):
        quote_text.value = quotes[e.control.value]
        page.update()

    quote_text = ft.Text(value=quotes["chinese"], size=18, italic=True, color="green")

    radio_buttons = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="english", label="english"),
            ft.Radio(value="chinese", label="chinese"),
            ft.Radio(value="korean", label="korean")
        ]),
        value="chinese",
        on_change=change_quote
    )

    page.add(ft.Column([
        ft.Text("choose", size=20, weight=ft.FontWeight.BOLD),
        quote_text,
        radio_buttons
    ], alignment=ft.MainAxisAlignment.CENTER, spacing=15))


ft.app(target=main)
