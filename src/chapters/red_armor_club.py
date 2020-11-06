# -*- coding: utf-8 -*-
'''
Chapter "赤鎧クラブ"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES


## chapter
def main(w: World):
    return w.chapter(TITLES[3],
            w.plot_setup("$maryが居候し始めた"),
            w.plot_setup("買い物にでかけた先で口論からいざこざになったところを、謎の赤鎧の騎士に助けられる"),
            w.plot_setup("王国の第二王女が失踪して半年になっていた"),
            w.plot_turnpoint("その赤鎧の騎士が相談に訪れた"),
            w.plot_develop("騎士は話せず、筆記とジェスチャによる対話となる"),
            w.plot_develop("騎士が言うには自分はある護衛のアルバイトをしているが、護衛仲間に言われて赤鎧の者だけが資格のある報酬のいい短時間仕事をしている"),
            w.plot_develop("その仕事の奇妙さを誰にも相談できずにいたと"),
            w.plot_develop("$sherlockはしばらくそのまま続けるよう指示し、独自に調査を行う"),
            w.plot_turnpoint("赤鎧の騎士が再び訪れ、仕事を首になったと告白した"),
            w.plot_resolve("$sherlockは理由を話す"),
            w.plot_resolve("その店の店長と護衛仲間が共謀し、騎士を護衛場所から一定時間離れさせるのが目的だったと"),
            w.plot_resolve("警察により彼らは逮捕され、店を閉じたから解雇されてしまった"),
            w.plot_resolve("どうやら店の地下に穴を掘り、近所の博物館に展示中のあるものを盗むのが目的だった"),
            w.plot_resolve("しかしそれを偽物に取り替えておいた$sherlockの指示により犯人たちは捕まえられたのだ"),
            w.plot_resolve("事情を理解した騎士$limeは、自分のことについて語る"),
            w.plot_resolve("呪いの鎧を着ていたのは$limeという、かつて失踪した王国の第二王女だった"),
            w.plot_resolve("$limeは事情があり、王室には帰れないというので仕方なく$sherlockたちの家に居候することになった"),
            "奇妙な仕事",
            w.plot_note("$maryを家に迎えたが、彼女は家事全般が苦手で、あまり役立たない"),
            w.plot_note("それでも$sherlockを気に入り、秘書まがいのことをやっている"),
            w.plot_note("その$maryが買い物から帰ってきたら、奇妙な赤鎧の人間を連れてきた"),
            w.plot_note("何やら事情を抱えているので話を聞いてあげてほしいと"),
            w.plot_note("ただその鎧騎士は言葉が話せなかった"),
            "赤鎧クラブ",
            w.plot_note("鎧騎士は$limeと名乗った（実際は筆談である）"),
            w.plot_note("彼の言うところではある質屋の家に世話になっているがそこの護衛を行うことで食費代にしている"),
            w.plot_note("そこは雇いバイトの男$binsがいて、彼が店の切り盛りを、護衛を騎士が行っているらしい"),
            w.plot_note("その$binsに紹介され、小遣い稼ぎにとあるバイトを紹介してもらったという"),
            w.plot_note("それは赤い鎧を着た人間にだけ許可された特別なもので「赤鎧クラブ」の仕事だ"),
            w.plot_note("毎日事務所に行き、三時間、大事な古文書の写本を行うだけで週給７０Gももらえるらしい"),
            w.plot_note("ただ内緒でそのアルバイトをしていて、その分け前を護衛仲間に渡しているのが心に引っかかるらしい"),
            w.plot_note("$sherlockは護衛の方は気にしなくても実際に問題は起こっていないだろうと断言する"),
            w.plot_note("ただその仕事はすぐに辞めた方がいいと進言する"),
            w.plot_note("そうしようと思いますと答えて、彼は帰っていった"),
            "仕事を首になる",
            w.plot_note("数日後、再びその赤鎧の騎士が訪れた"),
            w.plot_note("仕事そのものをクビになったというのだ"),
            w.plot_note("詳細を聞くと、今朝、いきなり警察が入ってきて家探しをしたらしい"),
            w.plot_note("事情を聞くと働いていた仲間が捕まったという"),
            w.plot_note("質屋のものを横流ししていたというのでオーナーが激怒して、それに騎士が加担したことになっていたらしい"),
            w.plot_note("仲間を信頼したのに裏切られた形になった"),
            w.plot_note("しかし$sherlockはそれは本来の目的ではないと断言し、騎士を連れ立ってその質屋へと向かう"),
            "本当に盗まれたもの",
            w.plot_note("$sherlockはそのオーナーである$jakinsに迷惑な顔をされつつも、勝手に中に入り、事務所を調べる"),
            w.plot_note("金庫から盗まれたものがないことを確認すると、その裏側を調べる"),
            w.plot_note("抜け穴が掘られていて、その先を行くと、隣接する国営博物館に繋がっていた"),
            w.plot_note("現在改築工事で閉鎖中だったが、展示品だった宝石が盗まれていた"),
            w.plot_note("それが狙いだったという$sherlock"),
            w.plot_note("そこに展示されていたのは国宝の一つであるサファイアだった"),
            "失踪した王女",
            w.plot_note("結局犯人たちは殺されて発見された"),
            w.plot_note("解雇された鎧騎士が家にやってくる"),
            w.plot_note("彼女は自分が失踪中の第二王女だと告白する"),
            w.plot_note("ただ事情があって王室には戻れないと言う"),
            w.plot_note("ここでしばらく置いてもらえないかと頼む$lime"),
            w.plot_note("$maryは友だちができて喜ぶ"),
            )


