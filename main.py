import flet as ft


def main(page: ft.Page):
    def set_reversed_text(e):
        re_t = input_text.value[::-1]
        reversed_text.value = re_t
        reversed_text.update()
        result_text.value = ""
        result_text.update()
    
    def judge(e):
        if(input_text.value == reversed_text.value):
            result_text.value = "これは回分です"
        else:
            result_text.value = "これは回分ではありません"
        result_text.update()

    text1 = ft.Text(value="入力された言葉が回文かどうかを判定します。")
    text2 = ft.Text(value="空白は無視されます。")
    input_text = ft.TextField(label="ここに言葉を入力", value="", on_change=set_reversed_text)
    reversed_text = ft.TextField(label="反転した結果", value="", read_only=True)
    judge_button = ft.ElevatedButton(text="Judge!", on_click=judge)
    result_text = ft.Text(value="")

    page.add(text1, text2, input_text, reversed_text, judge_button, result_text)

ft.app(main)
