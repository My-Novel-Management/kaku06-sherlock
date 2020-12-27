# -*- coding: utf-8 -*-
'''
Chapter "空き家"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES
from scenes import AbandonedFactory
from scenes import AbandonedHouse
from scenes import Church
from scenes import EmptyHouse
from scenes import Hideout
from scenes import Hospital
from scenes import InCar
from scenes import Market
from scenes import MountCottage
from scenes import PoliceStation
from scenes import SherlockHouse
from scenes import SlumTown
from scenes import WilsonHouse


# Episode
# NOTE
#   .$sherlockを探して＞$sherlockを空き家で見たという情報が入る
#   .空き家の冒険＞空き家の殺人事件の容疑者に$sherlock
#   .$maryの探検＞$maryが捕らえられた
#   .彼が戻ってきた＞$sherlockが戻ってきた
#   .$boss復活＞祭壇は大爆発した
#   .偽$wilsonの思惑＞偽$wilsonは山小屋で自殺しているのが見つかった

# NOTE: outlines
OUTLINES = [
        "$sherlockが消えてから半年、$maryは市場の手伝いをし、$limeは護衛のアルバイトしながら、彼を探し続けていた。そんな中、$wilsonが$sherlockを見たという情報を掴む",
        "スラム街の空き家に$sherlockが出没すると言われ、そこを監視する$maryたち。確かによく似た風貌の男がそこに出入りしていた。だが監視している中で、殺人事件が発生する。その容疑者になったのは$sherlockだった",
        "$maryは再び空き家を調査に訪れるが、そこで人影を目撃し、あとをつけると抜け道が見つかる。その先は廃工場へと繋がっていて、そこには失踪者の遺体が転がっていた。それを目撃した$maryは何者かに襲われ気を失う",
        # $maryの前に殺人鬼$sherlockが現れた
        "$maryが気がつくとそこには$sherlockがいた。彼は自分が全ての犯人だったと告白する。しかしよく見ると$sherlockにはない痣があり、何より匂いが違っていた。偽物と見抜いた$maryは何とか逃げ出そうとするが、追い詰められ、そこをホームレスに助けられる。それこそ本物の$sherlockだった",
        "家に戻ると荒らされた形跡があった。なぜか$sherlockの研究室から彼の血液が盗まれている。$sherlockは改装中の大聖堂に向かう。そこでは$boss復活の儀式が$wilsonによって行われようとしていた",
        "全ての黒幕は偽物の$wilsonだった。$boss復活のために$heroの血が必要だったが、一番濃い血が$sherlockだと分かり、それを盗んだ。しかし四つの$stoneのうち一つが偽物にすり替えられていて、儀式は失敗に終わる。逃げた$wilsonはその後、山中の小屋で自殺しているのが発見された",
        ]

# NOTE: charas

# NOTE: stages
#   ・大聖堂（中は初出
#   ・イーストエンド（スラム街。少し扱ってきたが本格的はここで
#   ・空き家（事件に使われる場所。ここのみ
#   ・抜け道（EE内に数多くある、地下道の一つ。ここのみ
#   ・廃工場（EE内にいくつもある。ここのみ

# NOTE: items
#   ・$red_stone
#   ・$blue_stone
#   ・$white_stone
#   ・$black_stone
#   ・$bossの杯
#   ・$bossのドクロ（大聖堂の地下に厳重に保管されていたはずのもの

# NOTE: case
#   ・空き家殺人事件　→失踪者の一人の遺体を放置し、$sherlockに容疑が向かうようにした。実行犯は$jake

def lookfor_sherlock(w: World):
    return w.episode("$sherlockを探して",
            w.plot_setup("$sherlockが失踪してから三ヶ月が経ち、誰もが彼の死を考えていた"),
            w.plot_turnpoint("$sherlockの目撃情報が、$wilsonによってもたらされる"),
            )


def adventure_of_empty_house(w: World):
    return w.episode("空き家の冒険",
            w.plot_setup("$wilsonと一緒に$maryたちは$sherlockを目撃したというホームレスに会う"),
            w.plot_resolve("部屋には$sherlockの着ていた帽子が残されていた"),
            w.plot_turnpoint("空き家の中で、殺されている$ronald教授を発見した"),
            )


def marys_investigation(w: World):
    return w.episode("$maryの捜査",
            w.plot_setup("（密室）殺人を警察に連絡した"),
            w.plot_turnpoint("$sherlockが重要参考人として手配される"),
            w.plot_develop("$patsonが$sherlockの血液を調べたいと申し出て、彼が研究用に置いている自分の血液を貸し出す"),
            w.plot_resolve("抜け穴は廃工場に繋がっていた"),
            w.plot_turnpoint("多数の失踪者の遺体を目撃した$maryは何者か（$jake）により失神させられる"),
            )


def he_is_back(w: World):
    return w.episode("英雄の帰還",
            w.plot_setup("目覚めると$maryは縛られた状態"),
            w.plot_resolve("$sherlockにより救出された"),
            w.plot_turnpoint("$sherlockは$boss復活の儀式を"),
            )


def revive_boss(w: World):
    return w.episode("$bossの復活",
            w.plot_setup("$boss復活を阻止するために改装中の大聖堂にやってくる"),
            w.plot_turnpoint("大聖堂の地下に巨大な祭壇が隠されていた"),
            w.plot_develop("地下に祭壇があり、血みどろの凄惨な光景（一度失敗した）が広がっていた"),
            w.plot_develop("$sherlockにより$boss復活が失敗したことが語られる"),
            w.plot_develop("その失敗が三ヶ月前の大地震だった"),
            w.plot_turnpoint("$sherlockこそが正当な$heroの血を引く後継者だった"),
            w.plot_turnpoint("$wilsonが偽物で、全ての黒幕だった"),
            w.plot_turnpoint("$patsonが偽$wilsonの配下だった"),
            w.plot_resolve("$patsonの$gunにより$sherlockは肩を撃ち抜かれ、血を出す"),
            w.plot_resolve("必要だった$heroの血（$sherlockのもの）が盃に捧げられ、儀式に必要なものが全て揃う"),
            w.plot_turnpoint("$boss復活の儀式が始まった"),
            )


def fake_wilsons_thought(w: World):
    return w.episode("偽$wilsonの思惑",
            w.plot_setup("正当な$heroの血（$sherlockの）が捧げられ、$boss復活の儀式が始まる"),
            w.plot_setup("$sherlockは負傷して動けない"),
            w.plot_setup("$maryは$sherlockを人質に取られて動けない"),
            w.plot_setup("入り口は閉じられている"),
            w.plot_turnpoint(""),
            w.plot_develop(""),
            w.plot_turnpoint("$patsonは偽$wilsonを殺そうとして逆に殺される"),
            w.plot_develop("偽$wilsonの$zeronは自分が何者でもないことを語る"),
            w.plot_develop(""),
            w.plot_develop("四つの$stoneから順番に封じ込められた$bossの力が$bossのドクロに集まっていく"),
            w.plot_turnpoint("$limeの宝剣が$stoneを砕く"),
            w.plot_develop("集約していた$bossの力は霧散し、祭壇が爆発した"),
            w.plot_develop("$maryは獣化して$sherlockたちを柱の影に押し込めて守る"),
            w.plot_develop("$boss復活の儀式は失敗に終わる"),
            w.plot_turnpoint("偽$wilsonは姿を消した"),
            w.plot_resolve("$boss復活は阻止できたが、大切な四つの$stoneは全て姿を消し、各地に$bossの残り香がばらまかれた"),
            w.plot_resolve("偽$wilson（$zeron）が山中の山小屋で自殺しているのが発見された、と報告があった"),
            )


# Chapter
def main(w: World):
    return w.chapter(TITLES[7],
            # NOTE
            #   事件：空き家密室殺人／連続失踪事件
            #   被害者：$ronald卿
            #   容疑者：$sherlock
            #   犯人：$jake（$sherlockに似た$ajin）
            #   依頼者：$wilson？
            #   トリック：偽装トリック（争ったように見せかけて遺体を部屋に置いた）＆抜け道を使った密室
            #   結果：$jakeを殺して事件解決
            #   ポイント：連続失踪事件の犯人／$boss復活の儀式とその失敗
            w.plot_setup("$sherlockが見つからないまま三ヶ月が過ぎた"),
            w.plot_setup("$morianoの影も消え、世間では犯罪が減っているはずだったが、逆に増加傾向だった"),
            w.plot_setup("$sherlockが解決していた事件の多くが野放しになることで、犯罪が増えていた"),
            w.plot_setup("街の治安も悪化、経済も悪くなり、王室批判やデモも起こっていた"),
            w.plot_setup("市場にでかけた$maryは石を投げられる。$animalなどの$ajinが恐れの対象になりつつあった"),
            w.plot_setup("街角では宗教団体$cultXが目立つようになる"),
            w.plot_setup("ちょうど$sherlockが消えてから数日後にあった地震で崩れた大聖堂は改装中"),
            w.plot_turnpoint("$wilsonが$sherlockを見かけたという情報を持ってくる"),
            w.plot_develop("$wilsonについて$sherlockが入るのを見たという空き家を監視する"),
            w.plot_develop("夜になり、$sherlockに似た男が入っていくのを見る。明かりが灯るとたしかによく$sherlockがしていた格好"),
            w.plot_develop("$wilsonが見張りを交代し、$maryは少し眠る"),
            w.plot_develop("$wilsonに言われ、明け方、見ると影が二つ争っている"),
            w.plot_develop("部屋の明かりが消える"),
            w.plot_develop("じっと待っていたが誰も出てこない"),
            w.plot_turnpoint("翌朝調べると、部屋に一人の男の遺体があった"),
            w.plot_develop("警察に連絡し、調べてもらう"),
            w.plot_develop("事情聴取を受ける$maryたち"),
            w.plot_develop("その中で顔なじみになった刑事の$patsonから被害者が$ronaldだと教わる"),
            w.plot_develop("$ronaldは$sherlockに一度ある頼みごとをしてきた教授だと思い出す"),
            w.plot_turnpoint("警察は$sherlockを重要参考人と見ていると知る"),
            w.plot_develop("$maryは$sherlockが犯人でない証拠を探そうとする"),
            w.plot_develop("一人で空き家を調べる"),
            w.plot_turnpoint("$maryは空き家で抜け道を見つける"),
            w.plot_develop("抜け道は廃工場に繋がっていた"),
            w.plot_develop("廃工場には今までに失踪したとされる人らしき遺体が転がっていた"),
            w.plot_develop("誰もが何かの目的で血を抜かれ、殺されていた"),
            w.plot_turnpoint("$maryは何者かに捕まってしまう"),
            w.plot_develop("$limeと$wilsonはいなくなった$maryを探す"),
            w.plot_develop("警察は$maryが$sherlock逃亡を手伝っている可能性を考えて、重要参考人として探し始めた"),
            w.plot_develop("$ignesたちが$maryによく似た女の子を見かけたという証言を手に入れる"),
            w.plot_develop("廃工場に$maryがいることを突き止める"),
            w.plot_turnpoint("$maryの前に$sherlock（$jake）が現れる"),
            w.plot_develop("$jakeは$maryを無視して、自分がいかに卑屈な生き物で、血反吐をすすっていきてきたかを語る"),
            w.plot_develop("そのうちに$maryは彼が$sherlockによく似た偽物だと気づき、今までにあった$sherlockが関与したと思われる事件が全て彼の仕業だと思う"),
            w.plot_develop("$maryはなんとかして脱出し、警察にこの事実を持ち込みたい"),
            w.plot_develop("$morianoの名前を出したが、全く知らないようだった"),
            w.plot_develop("$maryは隙きを見て縄をほどき、逃げ出す"),
            w.plot_develop("しかしそれがばれて捕まり、再度、今度は鎖でしばられて動けなくされ、証拠隠滅として廃工場に火をつけられた"),
            w.plot_develop("火事場から逃げ出そうと獣化するが、火の周りが早く、絶体絶命"),
            w.plot_turnpoint("そこを本物の$sherlockがきて助け出す"),
            w.plot_develop("気づくと$limeたちに介抱されていた$mary"),
            w.plot_develop("警察が$jakeを追っていると聞いた"),
            w.plot_develop("$sherlockは何故か身内に気をつけるように注意して、姿を消した"),
            w.plot_develop("空き家事件は$jakeが犯人ということで収まりそうだったが、依然$sherlockは行方不明のまま"),
            w.plot_turnpoint("$wilsonは$sherlockが残したメッセージを見つける"),
            w.plot_develop("$maryは$wilsonと一緒に$sherlockがいるという大聖堂に向かう"),
            w.plot_develop("大聖堂の地下に巨大な空間を見つける"),
            w.plot_develop("そこでかつて何かの儀式が行われたが失敗したことが分かる"),
            w.plot_turnpoint("$wilsonが$maryを人質にとり、$sherlockを呼び出す"),
            w.plot_develop("$sherlockは警官に紛れていて、姿を見せる"),
            w.plot_develop("$sherlockは$wilsonが全てを仕組んでいたことを話す"),
            w.plot_develop("そのうえで、$boss復活の儀式に必要だった四つの$stoneのほかに$heroの血が必要だったと語る"),
            w.plot_turnpoint("$sherlockは$heroの血を引くものだった"),
            w.plot_develop("$patsonが$sherlockに切りかかり、血を流させる"),
            w.plot_develop("$patsonを撃ち殺す$restrade"),
            w.plot_develop("しかし$heroの血液が注がれた盃により、儀式が始まってしまう"),
            w.plot_turnpoint("$boss復活する間際、四つの$stoneの一つが$limeの剣で割られてしまう"),
            w.plot_develop("$bossの力が弾け飛び、大爆発する"),
            w.plot_develop("なんとか助かった$sherlockたちだが、$wilsonの姿は消え去っていた"),
            w.plot_resolve("$sherlockはずっと$wilsonが本物でないことに気づいていた"),
            w.plot_resolve("決定的だったのは$wilsonの家に行った時で、そこで彼が本物ではないと気づいた"),
            w.plot_resolve("後日、$wilsonは山小屋で自殺しているのが発見された"),
            w.plot_resolve("ただ持ち逃げされたと思われる$bossのドクロは見つからなかった"),
            #
            lookfor_sherlock(w),
            adventure_of_empty_house(w),
            marys_investigation(w),
            he_is_back(w),
            revive_boss(w),
            fake_wilsons_thought(w),
            )


