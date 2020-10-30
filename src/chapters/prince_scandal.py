# -*- coding: utf-8 -*-
'''
Chapter "皇太子の醜聞"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES


## chapter
def main(w: World):
    return w.chapter(TITLES[1],
            "街が舞台",
            w.plot_setup("世間では怪盗$jackという謎の存在が人気を集めていた"),
            w.plot_setup("王室からの使者として$wilsonがある短刀を取り返して欲しいと依頼する"),
            w.plot_setup("実は皇太子が結婚を控えているが、過去の女に預けた宝剣を取り戻したいというのだ"),
            w.plot_setup("だが$sherlockは王室からの依頼は全て断っていた"),
            w.plot_turnpoint("翌日、その$ailyが$sherlockに依頼に訪れた"),
            w.plot_develop("$ailyの恋人が行方不明になったという"),
            w.plot_develop("その上、その男が宝剣を持ち去ったと"),
            w.plot_develop("$sherlockは調査を開始する"),
            w.plot_develop("けれど調べるほどにその男の存在は希薄だった"),
            w.plot_turnpoint("調査結果を伝えに行くと$ailyの家はもぬけの殻になっていた"),
            w.plot_resolve("自分の家に荷物を届けにきた配達人こそが$ailyと分かったが、既に彼女は高跳びした後だった"),
            w.plot_resolve("送られた小包は宝剣だった"),
            w.plot_resolve("だがそこにはまっていた宝珠は消えていた"),
            w.plot_resolve("しかし宝剣に新しい宝珠がつけられ、皇太子の結婚式は無事に行われた"),
            "ここから本編。三人称で、視点変更も可能。ただし誤認させるために$wilsonから始める",
            "宮殿から北側",
            w.plot_note("$wilsonはその日、ある仕事を依頼するためにその家を訪れた"),
            w.plot_note("$Baker街"),
            w.plot_note("もともと高級住宅地だが少しずつ商業施設に変わっている"),
            w.plot_note("住所のメモを見ながら$wilsonは歩く"),
            "少年の案内（ここですられている）",
            w.plot_note("地域に似つかわしくないボロボロの服装の少年たちがこっちを見てにやついている"),
            w.plot_note("少年の一人が声をかけてくる「誰か探してるの？」"),
            w.plot_note("と、他の少年たちが口論を始める"),
            w.plot_note("$wilsonは$ln_sherlock氏の場所を尋ねる"),
            w.plot_note("知ってるから案内すると言う少年に$wilsonはついていく"),
            w.plot_note("家まで案内されたが、少年は対価を求める"),
            w.plot_note("$wilsonは紙幣を握らせ、少年たちを帰らせる"),
            "$sherlockと初対面",
            w.plot_note("呼び鈴を鳴らすが返事がない"),
            w.plot_note("留守かもしれないと思いつつ何度か呼び鈴を押して待つ"),
            w.plot_note("腕時計を確認し、再度押そうとしたところで、覗き窓が開いた"),
            w.plot_note("「帰れ」といきなり言われて覗き窓が閉まる"),
            w.plot_note("$wilsonはこういう「変わり者」か困ったなと思いつつ、どうしても頼みたいことがあると"),
            w.plot_note("「王室からの依頼は全て断っているんだ」と言われる。何も説明していないのに"),
            w.plot_note("「なぜ分かったんだ？」と疑問に思う"),
            w.plot_note("$sherlockはいやいやながら説明する"),
            w.plot_note("通りに魔導タクシーを止め、そこからここまで歩いてくるのをずっと観察していたこと"),
            w.plot_note("こんな時間から魔導タクシーが使える人間は一般市民ではない"),
            w.plot_note("言葉遣いや着ているもの、また武術の心得は多少あるが、財布を擦り取られたことには気づいていないところから、武官ではないと判断"),
            w.plot_note("警察関係者でもなく、その上頼みたいことがあると口にした"),
            w.plot_note("あらゆる条件から絞られるのは王室から依頼を持ってきた執務官か事務官あたりという推察だ"),
            w.plot_note("「驚いたよ。変わっている男とは聞いたがそういう変わっているだったのか。確かにこれはよく切れる男のようだ」と"),
            w.plot_note("そこで改めて依頼をしようとするが、王室とは関係を断っているといい、追い返される"),
            "持ち込み事件",
            w.plot_note(""),
            "そこから普段は自分と関係ない、非常に厄介な案件を持ち込んでくると言い当てた",
            "その上で「王室からの依頼は受けないことにしている」とぴしゃりと断る",
            "そこに別の人間がやってきて、ちょっとした謎解きを依頼する",
            "（簡単だが$sherlockが興味を持つものを）",
            "でかけていって、その小さな謎解きをさっとやって、満足げに帰宅しようとする",
            "",
            )


