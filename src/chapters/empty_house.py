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
def lookfor_sherlock(w: World):
    return w.episode("$sherlockを探して",
            SherlockHouse.believed_his_alive(w),
            Market.shal_disappearance_talk(w),
            Market.new_religions(w),
            SherlockHouse.news_of_sherlock_alive(w),
            )


def empty_house(w: World):
    return w.episode("空き家の冒険",
            SlumTown.goto_empty_house(w),
            EmptyHouse.strange_empty_house(w),
            EmptyHouse.resident_of_empty_house(w),
            EmptyHouse.night_and_light(w),
            EmptyHouse.silent_house(w),
            EmptyHouse.discover_dead(w),
            )


def fake_reunion(w: World):
    return w.episode("偽りの再会",
            PoliceStation.interrogation(w),
            PoliceStation.shal_is_suspect(w),
            SherlockHouse.consideration_of_sherlock(w).omit(),
            EmptyHouse.searching_house(w),
            EmptyHouse.mystery_subway(w),
            AbandonedFactory.many_dead(w),
            AbandonedFactory.sherlocks_confession(w).omit(),
            )


def in_the_darkness(w: World):
    return w.episode("暗闇の中で",
            AbandonedFactory.in_the_darkness(w),
            SherlockHouse.help_from_sherlock(w),
            AbandonedFactory.desparete_escape(w),
            SlumTown.rescue_mary(w),
            AbandonedFactory.hero_appairs(w),
            )


def his_alive(w: World):
    return w.episode("$sherlockの帰還",
            Hospital.shal_comes_back(w),
            SherlockHouse.injured_wilson(w).omit(),
            SherlockHouse.burned_shal_home(w),
            InCar.goto_wilson_house(w),
            WilsonHouse.this_is_wilson_house(w),
            )


def purpose_of_cases(w: World):
    return w.episode("事件の本当の目的",
            WilsonHouse.search_wilson_house(w),
            WilsonHouse.secret_of_sherlock(w),
            WilsonHouse.sherlocks_request(w),
            InCar.about_this_cases(w),
            )


def truth(w: World):
    return w.episode("真実",
            Hideout.visit_hideout(w).omit(),
            Hideout.sherlocks_talk(w).omit(),
            Church.cult_facility(w),
            Church.lookfor_ritual_place(w),
            Church.goto_ritual_room(w),
            Church.basement_hall(w),
            )


def strange_end(w: World):
    return w.episode("奇妙な結末",
            Church.betray_man(w),
            MountCottage.his_dead(w),
            WilsonHouse.strange_end(w),
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
            empty_house(w),
            fake_reunion(w),
            his_alive(w),
            purpose_of_cases(w),
            truth(w),
            strange_end(w),
            )


