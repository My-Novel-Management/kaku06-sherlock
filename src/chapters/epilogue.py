# -*- coding: utf-8 -*-
'''
Chapter "エピローグ"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES


# Episode
def true_wilson(w: World):
    return w.episode("本物の$wilson",
            "ここで「展開」までやる",
            "ここはまだ三人称のまま",
            "すべてが終わった",
            w.plot_note("事件は偽$wilsonの自殺と関連する人や施設の消滅により、すべてが闇に葬り去られた"),
            "住居を出ていくように言われる",
            w.plot_note("事務所を失った$sherlockたちは一旦そのまま$wilsonの住宅で暮らしていた"),
            w.plot_note("$maryたちは新居の候補地を探していたがなかなかいい物件は見つからない"),
            w.plot_note("不動産屋の$stanryがやってきて、家主が長らく家賃を滞納していて、それをまとめて払ってほしいと言ってくる"),
            w.plot_note("その上、改装したいから出ていってほしいと言ってくる"),
            w.plot_note("$sherlockは金を工面する宛はなく、自分に$wilsonの支払いをする義務もないと言う"),
            w.plot_note("今までのように一人ならどんなところでも暮らせると言い出して読書を始める$sherlock"),
            w.plot_note("困る$maryたち"),
            "本物の$wilsonが帰ってくる",
            w.plot_note("そこに訪問者がくる。依頼人かと思ったら、知らない男だった"),
            w.plot_note("「君たちはここで何をしているんだい？」と男"),
            w.plot_note("男は本物の$wilsonだった"),
            "すべての事情を聞く",
            w.plot_note("$wilsonは$sherlockたちから自分の偽物によって行われたことや、多くの事件を解決したことなどを聞く"),
            w.plot_note("$wilsonは滞納家賃の取り立て書を見つけて、頭を抱える"),
            w.plot_note("$wilsonは$sherlockたちから借りようとするが、ないと突っぱねられる"),
            w.plot_note("自分の隠し金庫から金を出そうとするが、すでに空っぽだった"),
            "$wilsonが活躍を小説にして出版することを提案する",
            w.plot_note("$wilsonに客がくる。新聞社の人間で一つ小話を書いてもらいたいと"),
            w.plot_note("そこで$wilsonは探偵小説の提案をする"),
            w.plot_note("探偵という言葉について$wilsonが$sherlockのような人間のことだと説明する"),
            w.plot_note("そして$wilsonは「$Office」としてここを立ち上げ、その仕事を自分が小説にして金にしようと提案した"),
            )


def heros_office(w: World):
    return w.episode("$hero探偵社",
            "ここで$wilsonの一人称に変更",
            "これからの物語",
            w.plot_note("こうして、$wilsonは探偵小説を書くことになった、と告白する"),
            w.plot_note("またこの作品の記述者は自分だったと告白"),
            w.plot_note("ここまで書いてきたのは全て$wilsonである、と告白"),
            w.plot_note("$wilsonはずっとライターをしてきた"),
            w.plot_note("$sherlockが$heroだということには驚きを隠せないが、その知性は自分が知る「探偵」そのものだ"),
            w.plot_note("この世界で再び$bossが復活し、世界を闇に包み込むようなことがないよう監視する必要もある"),
            w.plot_note("いつか$sherlockが本物の$heroとして冒険の旅に出るなら、それも見届けたいと思うと記述"),
            w.plot_note("そこに再び奇妙な依頼主が現れる"),
            w.plot_note("そこからとんでもない冒険の旅にまきこまれるのだが、それはまた別の物語としよう、と閉める"),
            )


# Chapter
def main(w: World):
    return w.chapter(TITLES[-1],
            w.plot_setup("莫大な弁護士費用などで借りていた住居を追い出されそうになる"),
            w.plot_turnpoint("本物の$wilsonが帰ってくる"),
            w.plot_develop("$wilsonは$sherlockたちから全ての事情を聞く"),
            w.plot_turnpoint("$wilsonが$sherlockの活躍を小説にして出版することになる"),
            w.plot_resolve("正式に$officeを設立し、情報を集めながら$bossを復活させようという勢力と闘うことになった"),
            #
            true_wilson(w),
            heros_office(w),
            )


