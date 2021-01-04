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

# NOTE: tech
#   ・

def lookfor_sherlock(w: World):
    return w.episode("$sherlockを探して",
            # NOTE
            #   ・それぞれの事情
            w.plot_setup("$sherlockは$morianoとともに滝に落ちて行方不明になった"),
            w.plot_setup("$sherlockを亡くなったと警察は見ている（$patson談）"),
            w.plot_setup("$maryは自分のせいで$sherlockがいなくなったと後悔している"),
            w.plot_setup("少年探偵団などに$sherlockを探してもらっている"),
            w.plot_develop("$maryが家事も買い出しもしなくなり、$limeが一人で担っていた"),
            w.plot_develop("$limeに王室の執事が会いに来て、戻ってほしいと頼む"),
            w.plot_develop("$wilsonは新聞社などを当たって情報を集めていた"),
            w.plot_develop("その中で、記者$milkからホームレスが$sherlockに似た人を見たという目撃情報を仕入れる"),
            w.plot_turnpoint("$wilsonが$sherlock目撃情報を持ってくる"),
            #   ・空き家の冒険
            w.plot_develop("$sherlockらしい人影を見たというホームレスの情報で、スラム街の空き家にやってくる"),
            w.plot_develop("$maryたちは遠くから空き家を監視する"),
            w.plot_turnpoint("$shelrockらしき人影が、空き家に入っていった"),
            )


def adventure_of_empty_house(w: World):
    return w.episode("空き家の冒険",
            # NOTE
            #   ・空き家の殺人
            w.plot_setup("$sherlock目撃情報があり、その空き家を見張っていた$maryたち"),
            w.plot_setup("夜になり、そこに明かりがともり、$sherlockに似た人物が入っていった"),
            w.plot_turnpoint("人影は$sherlockに見えたが、そこに男（$ronald）が入っていく"),
            w.plot_develop("監視していると、男二人が争っている姿がシルエット越しに見えた"),
            w.plot_develop("静まり返った中、ずっと監視していた"),
            w.plot_develop("何事も起こらないので$maryたちは注意して空き家に近づく"),
            w.plot_turnpoint("家の中を捜索すると、そこに男の死体があった"),
            #   ・殺人事件
            w.plot_develop("警察に連絡する"),
            w.plot_develop("警察に事情聴取を受ける$maryたち"),
            w.plot_develop("$patsonは状況から$sherlockを容疑者として考えていた"),
            w.plot_turnpoint("$sherlockの容疑を晴らすために$maryは独自で調査し始めた"),
            #   ・家の調査
            w.plot_develop("$maryは一人で家の調査をする"),
            w.plot_develop("抜け穴を見つけて、そこを進むと、先は廃工場だった"),
            w.plot_develop("今までの失踪者が殺されて転がっていた"),
            w.plot_turnpoint("目撃した$maryは誰か（$jake）の手により意識を失った"),
            )


def marys_investigation(w: World):
    return w.episode("英雄の帰還",
            # NOTE
            #   ・$jakeの告白
            w.plot_setup("$maryは抜け道から廃工場に捨てられた死体を見つけた"),
            w.plot_setup("そこで$maryは誰かに殴られて気を失った"),
            w.plot_setup("目覚めるとどこかの廃墟の中"),
            w.plot_turnpoint("そこに現れたのは$sherlockによく似た男（$jake）だった"),
            w.plot_develop("$jakeは訳のわからないことを話す"),
            w.plot_develop("連続猟奇殺人は$jakeがやったことだった"),
            w.plot_develop("普通に生きていると自分の内側の何かが衝動を突き動かし、やってしまう"),
            w.plot_develop("自分もまた、闇の住人の血が流れているのだと告白する"),
            w.plot_develop("$maryは$morianoが言っていた「$sherlockの本性に気づいてない」というから勘違いする"),
            w.plot_turnpoint("$jakeは$maryも殺そうとナイフを構える"),
            #   ・$maryを探して
            w.plot_develop("一方、$limeと$wilsonはいなくなった$maryを探していた"),
            w.plot_develop("警察は$maryが$sherlockの逃亡を幇助していると考えていた"),
            w.plot_develop("$limeは$ignesから廃工場の方で見たという話を手に入れる"),
            w.plot_develop("廃工場に向かい、$maryを探す"),
            w.plot_turnpoint("その時、$maryの悲鳴が聞こえた"),
            )


def he_is_back(w: World):
    return w.episode("英雄の帰還",
            # NOTE
            #   ・英雄の帰還
            w.plot_setup("$maryを探して廃工場へとやってきた$limeたち"),
            w.plot_setup("そこで$maryの悲鳴を聞く"),
            w.plot_turnpoint("悲鳴の場所にかけつけると、$maryが血まみれの男の前で立っていた"),
            w.plot_develop("$maryは茫然自失で、立ち尽くしていた"),
            w.plot_develop("そこに一人の男が警官を連れて戻ってくる"),
            w.plot_turnpoint("現れたのはホームレスに扮した$sherlockだった"),
            #   ・全ての真相
            w.plot_develop("$maryは一旦病院に運ばれた"),
            w.plot_develop("家に戻った$sherlockは$limeたちに自分がどうやって生き残ったかを話した"),
            w.plot_develop("逃げた$morianoを追いかけて滝に追い詰めた後、$morianoは$sherlockを犠牲にするように崖から飛び降りた"),
            w.plot_develop("$sherlockも死を覚悟したが$maryが繕ってくれた袖が途中でひっかかり、落下の衝撃がゆるくなった"),
            w.plot_develop("それでも大怪我を負った$sherlockだったが、彼を救ったのは$jackだった"),
            w.plot_develop("しばらく彼女の下で休養しながら、各国の情報を集めていた"),
            w.plot_develop("空き家の噂は$sherlockを追う勢力をあぶり出すために彼自身が巻いた嘘だったが、それを利用して殺人を犯したのが$jakeだった"),
            w.plot_develop("$jakeは連続猟奇殺人犯で、失踪事件の大半も彼の仕業だった"),
            w.plot_develop("彼は闇の血が入った混血で、陽の光の下では長く生きられない"),
            w.plot_develop("殺人も失踪も常に夜か明け方だったため、そういう推理を立てていた"),
            w.plot_develop("廃工場で$maryが捕虜になったのを知り、助けるために計画し、すんでのところで鏡を使って光を集めた"),
            w.plot_develop("血まみれだったのは、日光を浴びて肉体が破裂したからだった"),
            w.plot_turnpoint("$sherlockは$maryに預けていた$blue_stoneの場所を聞く。それが必要になったと"),
            )


def revive_boss(w: World):
    return w.episode("$bossの復活",
            # NOTE
            #   ・$mary誘拐
            w.plot_setup("$shserlockは儀式を阻止するために戻ってきた"),
            w.plot_setup("儀式に必要な$blue_stoneを預けた$maryは、病院に入院中"),
            w.plot_turnpoint("$maryに$blue_stoneを返してもらいにくると、彼女の姿が消えていた。看護師の話では刑事（$patson）が連れて行ったと"),
            w.plot_develop("改装中の大聖堂に向かう"),
            w.plot_develop("実は半年前の大地震、あれは地震ではなかったと語る"),
            w.plot_develop("大聖堂の修理中になっている部屋の中で、地下に繋がる穴を見つける"),
            w.plot_develop("地下に向かうと、その道は巨大なホールに続いていた"),
            w.plot_develop("地下のホールは酷い有様で、惨殺が行われた後のよう"),
            w.plot_develop("$sherlockはここにかつて$bossの居城があったと語る"),
            w.plot_develop("その跡地に封印目的で建てられたのが大聖堂だったのだ"),
            w.plot_develop("儀式は地震の日に一度行われたが、そこでは必要なものが足りずに失敗した。それが大地震を引き起こした"),
            w.plot_develop("$steinの研究から必要な四つの$stoneを集め、それに加えて$heroの血を探した"),
            w.plot_turnpoint("そこに$maryを人質とした$patsonが現れる"),
            #   ・$boss復活の儀式
            w.plot_develop("$patsonは$sherlockこそがその$heroだと語る"),
            w.plot_develop("$gunにより負傷させる$patson"),
            w.plot_develop("$boss復活の儀式を行う"),
            w.plot_develop("手伝っているのは$cultXの信者たちだった"),
            w.plot_develop("ある人物が$boss復活のために作った宗教だったらしい"),
            w.plot_develop("$morianoが最後に語った「あの方」だ"),
            w.plot_develop("四つの$stoneと血を入れた盃により、儀式が始まる"),
            w.plot_turnpoint("しかし儀式は途中で失敗し、大ホールで爆発が起こる"),
            )


def fake_wilsons_thought(w: World):
    return w.episode("偽$wilsonの思惑",
            # NOTE
            #   ・偽物の$wilson
            w.plot_setup("$patsonにより$boss復活の儀式が行われた"),
            w.plot_setup("しかしそれは何故か失敗に終わり、爆発が発生する"),
            w.plot_turnpoint("見れば$blue_stoneが割れていた"),
            w.plot_develop("$sherlockは$maryに預けたものが偽物だったと理解する"),
            w.plot_develop("$jackに諮られたのだが、それを知っていて黙っていたのだ"),
            w.plot_turnpoint("$patsonは$wilsonに何故失敗したのかと詰め寄る。彼こそが「あの方」だった"),
            w.plot_develop("$wilsonは$patsonを殺してしまう"),
            w.plot_develop("これで全てが終わったと言うが、$sherlockは許さない"),
            w.plot_develop("$wilsonの嘘を$sherlockが暴いていく"),
            #   ・全ての顛末
            w.plot_develop("そもそも$wilsonの家を一度見たときにそこにあった違和感に気づいた"),
            w.plot_develop("いつも帰っているはずなのに、全然住んでいる雰囲気がない"),
            w.plot_develop("$maryはずぼらだと笑ったけれど、自分の家で置いているものが把握できていなかった"),
            w.plot_develop("それから注意深く調べると$wilsonという男は確かに王室の案件をこなしていたが、今はある件で遠出中だったのだ"),
            w.plot_develop("$wilsonは$zeronと名乗った"),
            w.plot_develop("自分が闇の世界で生まれ、ただ$boss復活をするためだけにこちら側に遣わされた存在だと語る"),
            w.plot_develop("計画は失敗に終わり、嘘も見抜かれた"),
            w.plot_develop("観念したかに見えた$zeron"),
            w.plot_turnpoint("闇の翼をはやした$wilson（$zeron）は隙きを見て開いた穴から外へと逃げてしまった"),
            #   ・最後
            w.plot_turnpoint("山小屋で自殺している$wilsonが発見されたと、報告があった"),
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


