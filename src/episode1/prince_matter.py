# -*- coding: utf-8 -*-
'''
Episode 1-1: "王子の問題"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "王子の問題"


# NOTE: outlines
ABSTRACT = """
書簡には王子が結婚をすることになったが、その儀式に必要な宝具の一つ$royalswordをある女性にあげてしまったので、何をしてもいいから取り戻して欲しいというお願いが書かれていた。
この国の王子というのは$heroたちの血筋を色濃く引いている四家系の一つ$Arthur家の長男で、次期国王だったが、どうしようもない駄目男で有名だった。
あちこちで子種をばらばいては問題を起こしているらしいとも。
その王子の尻拭いは$sherlockが受けたくない依頼の中でもワースト１だった。
しかしある恩義があり、断れないので、$sherlockは仕方なくその女性について調査を行う。
$sherlockはいつも入念に調査する。資料もそうだが、何より現地調査を重要視していた。
$wilsonの$carでその女の暮らす高級住宅街に向かう。
現地に到着すると、周囲で$ailyについて聞き込みを行う。近所の評判はよく、ちゃんと言えば返してくれそうな雰囲気はある。
家を訪れると、誰も出ない。だが鍵が開いていた。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("王子からの書簡にはある女から$royalswordを取り戻して欲しいと書かれていた"),
            w.plot_turnpoint("王室からの依頼は受けないはずの$sherlockが、王子からの依頼は受けると言った"),
            w.plot_develop("王子に何かしら弱みを握られているらしい$sherlockは仕方なく仕事を受け、$ailyという女を調査に向かう"),
            w.plot_turnpoint("$ailyの近所の評判は王子の書いていたものと異なっていて、良いものだった"),
            w.plot_resolve("$sherlockと$wilsonは$ailyの自宅を訪ねるが、応答はない"),
            w.plot_turnpoint("しかし玄関の鍵は開いていた"),
            w.plot_note("$sherlockは書簡を開く"),
            w.plot_note("書簡に署名はないものの、封筒の材質に加えて、中身の紙に王家の印のすかしがあった"),
            w.plot_note("王室御用達の便箋らしい"),
            w.plot_note("$sherlockは書簡の内容に目を通す"),
            w.plot_note("読み終えた$sherlockはそれをテーブルに投げ出し「こいつはまたとんでもない頼まれ事だ」と"),
            w.plot_note("「この国の王子を知っているか？」"),
            w.plot_note("「あったことは？」"),
            w.plot_note("$sherlockは王子の悪口を言う。確かに顔の造形は整っているが性格は歪んでいる等"),
            w.plot_note("「どうも王族というのは苦手でね。いや得意な人などいないだろうが」"),
            w.plot_note("王子がどうしようもなく女関係が派手で、女とみてはすぐに声をかけて、自分の部屋に招くという"),
            w.plot_note("王子付きの執務官は男性だが彼の言うことは全く聞く耳を持たないと"),
            w.plot_note("侍女をはべらせているが、それにもかかわらず街にこっそり出ては女アサリを繰り返しているという"),
            w.plot_note("その界隈（遊女）では有名だった"),
            w.plot_note("その王子がこの度めでたく結婚することになった"),
            w.plot_note("だがここで問題が発覚。酒癖も悪くすぐに記憶をなくす王子"),
            w.plot_note("どうやら大事な$royalswordをどこかの女にくれてやったらしく、それがないと正式な婚姻の儀式ができないらしい"),
            w.plot_note("$sherlockは因果応報だと笑う"),
            w.plot_note("しかしそれを誰にやったのか調査班を使ってなんとか突き止めた"),
            w.plot_note("だがその女性がどうしても$royalswordを返してくれないという"),
            w.plot_note("そこで便利屋こと王室の面倒事の掃除屋$sherlockにおはちが回ってきた訳だ"),
            w.plot_note("$sherlockは「これが殺人事件や難解な事件ならまだしも」と"),
            w.plot_note("やる気がないがやらざるをえない、という$sherlockは、どうやら王室に弱みを握られているらしい。先程の女性にか"),
            w.plot_note("$sherlockは$wilsonに交換条件を出す。「君の依頼を聞く代わりにあの$carを出してもらえないだろうか」と"),
            w.plot_note("こうして$wilsonは$carに$sherlockを乗せ、その女の家に向かう"),
            #
            w.plot_note("車内で$sherlockは王子の手紙にあった女の情報を軽く話す"),
            w.plot_note("$ailyはその界隈で名の通ったオペラ歌手で、見た目もよく、最近人気が出てきたと語る"),
            w.plot_note("彼女は高級住宅街に暮らす"),
            w.plot_note("市場の脇を抜けていく"),
            w.plot_note("あまり乗り心地がいいものじゃないな、と$sherlock"),
            w.plot_note("住宅街にやってきて、路地に$carを止める"),
            w.plot_note("まっすぐ彼女の家に行かず$sherlockはまず周辺を歩いて、人に声をかける"),
            w.plot_note("$ailyさんを知ってますか？　等と"),
            w.plot_note("どういう訳か反応があまりない。彼女がここに暮らしていることは内緒らしい"),
            w.plot_note("「$ailyさんて今年○○賞最有力のオペラ歌手でしょ？　ここに住んでるの？」"),
            w.plot_note("適当に誤魔化しつつ、聞いて回る"),
            w.plot_note("どうやら彼女はここに存在していないらしい"),
            w.plot_note("「どういうことだろう？」と$wilson"),
            w.plot_note("表札もなにもない家に訪ねていく$sherlock"),
            w.plot_note("呼び鈴を鳴らすが応答はない"),
            w.plot_note("留守だろうか、と思ったところで$sherlockは窓が開いていることに気づく"),
            w.plot_note("玄関ドアを開けてみると開いた。鍵がかかっていないのだ"),
            w.plot_note("中に入る$sherlock"),
            outline=ABSTRACT)

