# -*- coding: utf-8 -*-
'''
Episode 6-5
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "$sherlockからの手紙"


# NOTE: outlines
ABSTRACT = """
$maryが病院で目覚めると$limeから$sherlockが国外逃亡した$morianoを追っていることを聞かされる。
$maryが自分が$sherlockを傷つけてしまったことを後悔していた。
後日、$sherlockから手紙が届く。そこには$morianoを道連れにしてでも滅ぼす決意と、彼の犯罪関与の証拠とそれについて書いた書類が既に警察に発送されていると記されていた。
最後に$maryについての謝罪が書かれていた。
警察の捜査で$sherlockと$morianoが滝から落下したことが判明。現場に残されていた彼の帽子と血液から、二人は死亡したものと見られた。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("負傷した$sherlockは入院し、精神的ショックを受けた$maryも入院する"),
            w.plot_turnpoint("見舞いに訪れた$limeの前から$sherlockは姿を消してしまう"),
            w.plot_develop("$maryたちは$sherlockの行方を探したが見つからない。$moriano犯罪研究所も閉じられ、手がかりが完全に失われた"),
            w.plot_turnpoint("後日$sherlockから手紙がくる"),
            w.plot_resolve("警察の捜索により滝壺から$morianoと$sherlock両名の遺品と思われるものが見つかった"),
            w.plot_note("それから後は推測よりも願望が入っていると書かれている"),
            w.plot_note("$morianoは$sherlockを待ち構えていた"),
            w.plot_note("彼は$sherlockに「人を殺してみたいと思ったことはあるか？」と聞いた"),
            w.plot_note("$sherlockの中にその感情を作ったのは$morianoだった"),
            w.plot_note("人が人を殺したいと思うことは正常だ、と言う"),
            w.plot_note("なぜならそれは憎しみこそが人を進化させる原動力だったからだ"),
            w.plot_note("その憎しみが$bossを生んだ。魔物を生んだ。闇の者を生んだ"),
            w.plot_note("それは$morianoの一番最新の論文に書かれていたことだった"),
            w.plot_note("人はまた望むと望まざるとにかかわらず、$bossを生み出すだろうと"),
            w.plot_note("$morianoは既に病におかされていて先が短い"),
            w.plot_note("$morianoは$sherlockにもう一度だけ尋ねる"),
            w.plot_note("私の代わりに$bossを復活させないか、と"),
            w.plot_note("断り、$sherlockはそこで初めて殺人を犯した"),
            w.plot_note("だがそれを待っていた$morianoは$sherlockの手をつかみ、共に滝壺へと落下"),
            #
            w.plot_note("手紙にそこまでは書かれていなかったが、後に現場検証をした$restradeたちからは、足がすべって落ちた形跡があると"),
            w.plot_note("$maryは入院している"),
            w.plot_note("$limeは王室に帰ってしまった"),
            w.plot_note("$wilsonは$sherlockが残したものを整理している"),
            w.plot_note("そこに$sherlockの血液の研究の成果があった"),
            w.plot_note("それをこっそりとポケットに入れる$wilson"),
            w.plot_note("$wilsonは$morianoの資料を郵便に出して、それからある場所に向かう"),
            w.plot_note("途中$ignesたちとすれ違う"),
            w.plot_note("$ignesは$sherlockがどこかで生きていると信じて、情報を追っているらしい"),
            w.plot_note("$maryの見舞いにもいったが、まだ精神衰弱であまりよくないと"),
            w.plot_note("$wilsonは先に行く"),
            #
            w.plot_note("$wilsonがやってきたのは$edoの研究所だった"),
            w.plot_note("そこで$sherlockのところから持ち出した血液を鑑定してもらう"),
            w.plot_note("待っている間に$wilsonは$sherlockのことを尋ねる"),
            w.plot_note("あれの学生時代、まだ$edoが警察に入ってこき使われていた頃、ある事件で出会った"),
            w.plot_note("学校内でもちょっとした評判だった$sherlock"),
            w.plot_note("そこで殺人事件が発生し、現場に向かうと、そこで一人の学生が事件を捜査していた"),
            w.plot_note("数日後、彼のおかげで事件は解決する"),
            w.plot_note("それが$sherlockだった"),
            w.plot_note("そこからの付き合いだからかれこれ十年ほどになるという"),
            w.plot_note("$sherlockが何者かは自分はあまり興味ないという"),
            w.plot_note("鑑定結果が出たらそちらに届けると言われ、出ていく$wilson"),
            #
            w.plot_note("$maryのもとに見舞いにきた$lime"),
            w.plot_note("$limeは王室に一旦帰ることにした、と伝える"),
            w.plot_note("$maryは部屋を出ていく$limeに「$sherlockは、生きてる」と伝える"),
            w.plot_note("$limeは信じたいと返す"),
            w.plot_note("病室を出たところで、$adelが待っていた"),
            w.plot_note("$limeは$adelに命じる。「$sherlockを探して」と"),
            #
            w.plot_note("$wilsonはあるパブにいた"),
            w.plot_note("そこに$mikelがやってくる"),
            w.plot_note("「結果は見た」と答える"),
            w.plot_note("$wilsonにどう思うか尋ねる"),
            w.plot_note("$wilsonはまさかこんなに身近にいるとは思いませんでした、と"),
            w.plot_note("$mikelは$sherlockが自分の遠縁だと教える"),
            w.plot_note("そして「プロジェクトの最重要ファクター」だと"),
            w.plot_note("$wilsonになんとしても$sherlockを探せと命じた"),
            w.plot_note("$hero$sherlockを"),
            outline=ABSTRACT)

