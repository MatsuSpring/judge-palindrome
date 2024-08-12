import flet as ft

def main(page: ft.Page):
    # input_textに入力された内容を、順次反転させてreversed_textに適応する関数
    def set_reversed_text(e):
        # input_textの内容から半角スペースと全角スペースを削除
        re_t = input_text.value.replace(" ", "").replace("　", "")
        # スペース削除したものをスライスにより反転する
        reversed_text.value = re_t[::-1]
        reversed_text.update()
        # リザルトをリセット
        result_text.value = ""
        result_text.update()

    # 回文判定を行う関数
    def judge(e):
        # input_textの内容からもスペースを削除したものを取得
        in_t = input_text.value.replace(" ", "").replace("　", "")
        # すべて小文字として比較する。
        if(in_t==""):
            result_text.value = "入力してください"
        elif(in_t.lower() == reversed_text.value.lower()):
            result_text.value = "これは回分です"
        else:
            result_text.value = "これは回分ではありません"
        result_text.update()

    # アプリの説明のためのテキストコントロール
    text1 = ft.Text(value="入力された言葉が回文かどうかを判定します。", size=20)
    text2 = ft.Text(value="※空白は無視されます。", color=ft.colors.BLACK54, italic=True)
    # 回文かどうか調べたい言葉を入力するフィールド
    input_text = ft.TextField(label="ここに言葉を入力", value="", on_change=set_reversed_text)
    # 反転した結果を表示するフィールド
    reversed_text = ft.TextField(label="反転した結果", value="", read_only=True)
    # 判定を実行するボタン
    judge_button = ft.ElevatedButton(content=ft.Text(value="Judge!", size=18), on_click=judge)
    # 結果を出力するテキストコントロール
    result_text = ft.Text(value="")

    page.add(text1, text2, input_text, reversed_text, judge_button, result_text)

ft.app(main)
