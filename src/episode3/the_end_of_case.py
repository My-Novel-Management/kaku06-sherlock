# -*- coding: utf-8 -*-
'''
Episode 3-3
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "事件の顛末"


# NOTE: outlines
ABSTRACT = """
$sherlockは$maryに、赤鎧クラブが$limeを店から遠ざけておくための口実だったと語る。
その間に地下道を掘り、大金庫から何かを盗み出した。現金や金の延べ棒、宝石など多数が強奪されていたという。
$limeの証言が赤鎧クラブが存在しなかったことで嘘とみなされ、容疑を晴らせない。
$sherlockは$jakinsがどこから来たのかを辿っていく。やがて賭け事で借金を背負い、裏組織とつながりがあることが判明した。
ただそこから先が辿れず、$sherlockは情報屋に宝石の売買などを洗ってもらっていた。
その後、強盗団が火災現場で遺体となって発見されたことが$restradeから伝えられた。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$maryに頼まれて$sherlockは$limeの容疑を晴らすために調査を開始する"),
            w.plot_turnpoint("$sherlockは赤鎧クラブの存在が$limeを店から遠ざけるためだったと語る"),
            w.plot_develop("質屋オーナー夫婦から聞き取りをして$jakinsがそもそも銀行の大金庫から宝石を盗み出す目的で近づいたこと等を突き止める"),
            w.plot_turnpoint("$jakinsが大量に借金をしていたことが判明する"),
            w.plot_resolve("$jakinsの昔の知人から組織とつながりがあり脅されていたことを知る"),
            w.plot_turnpoint("$jakinsの仲間と見られる強盗団が火災現場から遺体となって発見された"),
            w.plot_note("質屋に掘られていた地下道は銀行の大金庫に繋がっていた"),
            w.plot_note("そこで発見された男の遺体は$jakinsで、質屋の店員だった"),
            w.plot_note("$sherlockたちは現場にいたとして重要参考人で警察に呼ばれ、調書を取られていた"),
            w.plot_note("$sherlockは$restradeが担当した"),
            w.plot_note("ただ彼は事情聴取というよりも、どういった事件なのか、何か知っていたら教えてほしいと"),
            w.plot_note("$sherlockは$limeのアルバイトについて説明する"),
            w.plot_note("オーナー夫婦への聴取も必要だが、と断った上で"),
            w.plot_note("$jakinsという店員が雇われた"),
            w.plot_note("おそらくその頃から地下道は計画されていたのだろう、と"),
            w.plot_note("大金庫改修工事が始まったのもちょうどその頃だった"),
            w.plot_note("信頼を勝ち取り、店番を一人でやるようになってから、仲間を使って掘削させた"),
            w.plot_note("なぜこの店だったのかは、古地図で地下道があることが分かっていたから"),
            w.plot_note("再開発地区でもあり、色々と埋め立てたれ、変化している"),
            w.plot_note("そこで目をつけたやつらが質屋に$jakinsを送り込んだと"),
            w.plot_note("掘削は順調だったが、途中でトラブルが起こる"),
            w.plot_note("オーナー夫婦により$limeが住み込みで働くことになった"),
            w.plot_note("その$limeを店から遠ざけないと掘削できない"),
            w.plot_note("そこで考えられたのが「赤鎧クラブ」という架空のものだ"),
            w.plot_note("これが架空だというのは$sherlockが情報屋経由で手に入れた"),
            w.plot_note("そのバイトで午後の三時間を確保し、なんとか続けて地下道を大金庫まで開通させた"),
            w.plot_note("それがおそらく先週末のこと"),
            w.plot_note("質屋も銀行も休日には閉まる"),
            w.plot_note("その間に$jakinsたちは目的のものを運び出した"),
            w.plot_note("警察が調べれば夜の間に大勢がこの店を出入りしていたことが分かるだろう"),
            w.plot_note("おそらく口封じのために$jakinsは殺されたと"),
            w.plot_note("$sherlockの説明に納得する$restradeだった"),
            #
            w.plot_note("一方$maryたちの担当をしたのは$patsonだった。$sherlockが事件解決したことを自分の手柄にし、栄転してきたのだ"),
            w.plot_note("$patsonは$limeがしゃべれないのをいいことに、彼を$jakins殺しの容疑者にしてしまう"),
            w.plot_note("取り調べが終わり、$limeは拘置所にぶちこまれることになる"),
            w.plot_note("事件の指揮は$patsonが取っていた"),
            w.plot_note("そこで$sherlockは証拠もないのに勝手に逮捕するのは違反だと言うが、彼は「なら証拠とやらを見せてくれ。あいつがやってないっていうな」と"),
            w.plot_note("$sherlockは$maryと$wilsonとともに、再度事件現場を調べに行く"),
            #
            w.plot_note("大金庫は警察（$parker）によりみはられていたが、$restradeの名前を出すと入れてくれた"),
            w.plot_note("$jakinsは上半身脱がされて$gunにより殺害されていた、という"),
            w.plot_note("取られたものについては話せないと銀行の職員"),
            w.plot_note("ただ相当大事なものが盗まれていて頭を悩ませているという"),
            w.plot_note("そこに$mikelと$adelが現れる"),
            w.plot_note("$mikelは$sherlockを見て「また警察の真似事か？」と不愉快そうに"),
            w.plot_note("知人が巻き込まれたので仕方なくだ、と言い訳をしつつ、$sherlockは$mikelが現れたことから王室関連の重要なものが盗まれたと分かる"),
            w.plot_note("ひょっとすると$stoneか？　というブラフに引っかかる銀行職員"),
            w.plot_note("$mikelに追い払われる$sherlock"),
            #
            w.plot_note("$sherlockはオーナー夫婦の家に向かう"),
            w.plot_note("「困ったことになった」とオーナー"),
            w.plot_note("$sherlockは$jakinsについて質問する。どこで彼を雇ったのか、その経緯を"),
            w.plot_note("警察にも話したという話をそのまま聞かせてくれた"),
            w.plot_note("少し腰を痛めて、妻にも言われて店を誰かに任せようという話になり、ある程度信頼できるバイトを探して、しかるべき場所に広告を出した"),
            w.plot_note("そのアルバイト募集にきた男の中で、一番信頼できそうな男に任せたと"),
            w.plot_note("$sherlockは「最初は少し安くてもいい、と言いませんでしたか？」と"),
            w.plot_note("その通りだった"),
            #
            w.plot_note("$sherlockは次に$jakinsが住んでいたというアパートに行く"),
            w.plot_note("最近人の出入りがあったかなどを聞いたが、$jakinsの隣の男が、よくパブに行っていたという"),
            #
            w.plot_note("そのパブにやってくる$sherlock"),
            w.plot_note("そこで聞いた$jakinsの素顔は違っていた"),
            w.plot_note("もともと賭け事にのめり込み、破産して、身元を闇組織に引き取られた"),
            w.plot_note("ある時からどういう訳か羽振りがよくなり、よく飲みに現れた"),
            w.plot_note("付き合っているのは明らかに闇組織の人間だったが、$jakins自体は堅気の格好をしていた"),
            w.plot_note("まともに働いているんだと思っていたが、殺されたときいて「やっぱりね」と思ったという"),
            w.plot_note("ただ最近少し気になっていたのは中に一人、違う男が混ざっていたということだった"),
            w.plot_note("明らかに闇組織の人間でもなく、かといってまともな仕事をしているとも思えない"),
            w.plot_note("白髪が見えたから、それなりの年齢の男だろうと"),
            #
            w.plot_note("$shelrockは$wilsonと別れ、裏路地に入る"),
            w.plot_note("やってきたのはある薄暗い雑貨屋だった"),
            w.plot_note("中に入るとナイフも扱っている喫茶店になっていたが、客はほとんどいない"),
            w.plot_note("頬に傷のある黒眼鏡の男は$flenという情報屋だった"),
            w.plot_note("最近大きな金の動きがあったかどうか尋ねると「買いますか？」と"),
            outline=ABSTRACT)

