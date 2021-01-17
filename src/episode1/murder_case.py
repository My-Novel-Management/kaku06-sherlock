# -*- coding: utf-8 -*-
'''
Episode 1-2: "殺人事件"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "殺人事件"


# NOTE: outlines
ABSTRACT = """
家の中に入る$sherlock。そこで謎の女性の遺体を発見する。
すぐ警察に連絡する。警察が到着するまでに$sherlockは部屋を調査する。
強盗に荒らされた部屋。寝室。だが台所は綺麗だった。まるで新品のよう。
一人暮らしと聞いていたが、食器もない。色々と奇妙だった。
やってきた警察は$restradeで$sherlockもよく知る人物だった。
凶器は落ちていたナイフで、亡くなっていた女性が$ailyかどうか、オペラ座の座長にきてもらい確かめてもらったが、$ailyではなかった。
警察は家主の$ailyを参考人として指名手配する。
"""


# Scenes


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$ailyの家の中を調べる$sherlockと$wilson"),
            w.plot_turnpoint("寝室のドアを破壊して中を見ると知らない女の遺体が転がっていた"),
            w.plot_develop("事件として警察に届け出た後$sherlockは彼女が働いていたオペラハウスに向かう。そこで歌手$ailyのことを聞き込みした"),
            w.plot_turnpoint("$ailyが寄付していた孤児院の存在を知る"),
            w.plot_resolve("$sherlockは王子の言う性悪女$ailyと周囲の評判のいい$ailyのギャップに違和感を覚える"),
            w.plot_turnpoint("警察が$ailyを指名手配にしたことを知った"),
            w.plot_note("家の中に入った$sherlockは表情が引き締まる"),
            w.plot_note("静まり返った家の中"),
            w.plot_note("物はほとんど置かれていない"),
            w.plot_note("まるで新居のよう。引っ越してくる前の"),
            w.plot_note("「彼女は綺麗好きなんだね」と$wilson。それに対して「観察眼がない」と$sherlock"),
            w.plot_note("ほとんどものがない棚にはうっすらホコリがある"),
            w.plot_note("リビングには小さなテーブル。椅子が転んでいる。やや荒らされた風"),
            w.plot_note("いくつか部屋があるが、どれも使われてない"),
            w.plot_note("キッチンはわずかに使用形跡がある"),
            w.plot_note("最新機器の冷蔵庫があった。$scienceの力で冷気を巡回させて一定温度に保つらしい。だが中身はない。飲み物のボトルだけ"),
            w.plot_note("棚に酒がいくつか並ぶ"),
            w.plot_note("奥の寝室らしき部屋のドアだけが施錠されていた"),
            w.plot_note("ノックして応答を確かめる$sherlock。だが何もない"),
            w.plot_note("$sherlockは花瓶を取り出して鍵のところを破壊する"),
            w.plot_note("「こういうのは後であいつらに請求することになっている」と"),
            w.plot_note("室内に入ると、すぐにベッドの上で女性が倒れているのが見つかる"),
            w.plot_note("胸にナイフが突き立てられて亡くなっている"),
            w.plot_note("「密室殺人だ」と$sherlockは言った"),
            #
            w.plot_note("警察がやってくる"),
            w.plot_note("$restradeは$sherlockと知人で、がっしりした体格にたくましい髭面"),
            w.plot_note("$burnsは鑑識で、険しい顔つきに細マッチョ。顔に傷がある。明らかにやくざ風"),
            w.plot_note("$burnsが$sherlockに「何も触ってないだろうな？」と聞く"),
            w.plot_note("$sherlockは触ってないと答えつつも、$wilsonは彼が既にべたべたと色々なものを調べているのを目撃していた"),
            w.plot_note("以前は鑑識などなかったが、$science捜査部門ができてから行われるようになった、と$sherlock"),
            w.plot_note("だがまだまだ技術が未熟で、$sherlockもそっち方面の開発に日夜励んでいると"),
            w.plot_note("寝室以外は大して変化がない。寝室は荒らされていた"),
            w.plot_note("本当に鍵がかかっていたのか？　と質問"),
            w.plot_note("$sherlockに続いて$wilsonも確かめていた"),
            w.plot_note("簡単な事情聴取に答えて、$sherlockは$wilsonに次の場所に向かうという"),
            #
            w.plot_note("やってきたのはオペラハウス"),
            w.plot_note("いくつかある劇場の中でも比較的新しく、座長が若い人をスカウトしてきて使っている、最近人気のオペラハウスだ"),
            w.plot_note("練習中の風景"),
            w.plot_note("支配人の$godonにきてもらい、$ailyについて尋ねる"),
            w.plot_note("$ailyは彼がスカウトしてきた女性だった"),
            w.plot_note("パブで歌っていて、当時は消え入りそうな存在感で、ただ歌だけが抜群にうまかった"),
            w.plot_note("最初は乗り気じゃなかった彼女だが、歌が仕事になるというのでなんとか練習に参加してくれた"),
            w.plot_note("ただ当初は歌以外はてんで駄目で、演技はものにならないと覚悟していた"),
            w.plot_note("最初の舞台は歌以外はほぼ使えなかった"),
            w.plot_note("団員ともあまり親交せず、一人でいつも先に帰ってしまう"),
            w.plot_note("そんな時、王子と出会い、人が変わったみたいに演技ができるようになった"),
            w.plot_note("確かに見た目は病的なところがあり、妖精のようなはかない美貌を持っていた"),
            w.plot_note("彼女は一躍人気歌手に躍り出た"),
            w.plot_note("それがこの三ヶ月ほどの間の出来事"),
            w.plot_note("だが一週間前から$ailyが休んでいるという"),
            w.plot_note("何度か家を訪ねたが不在で、どうしているのだろうと心配していると"),
            w.plot_note("最近若い女性ばかりが狙われる殺人事件があったとも聞く"),
            w.plot_note("$godonからは知っていることがあったら教えて欲しいと言われた"),
            w.plot_note("別れ際に、思い出したと$godonが彼女が寄付していた孤児院の存在を教えてくれた"),
            #
            w.plot_note("その孤児院に向かおうとしたところで聞き込みにきた$restradeと遭遇"),
            w.plot_note("$restradeは$ailyを容疑者として探していると言った"),
            outline=ABSTRACT)

