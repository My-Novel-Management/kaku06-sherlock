# -*- coding: utf-8 -*-
'''
Chapter "悲しみの谷"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES


# Episodes
# NOTE
#   .依頼＞$trainで目的地に
#   .事件について＞$maryと面会可能になる
#   .$maryとの面会＞$maryは$animal
#   .家族の話＞$maryが連れてこられる
#   .母と娘＞使用人$kailが本性を現して人質を取る
#   .事件の顛末＞$maryが同居人に

# NOTE: charas
#   ・$mary（初出。最初は怯えて寡黙になっているただの少女。あとで印象変わる
#   ・$jean（ここのみ。$mary母
#   ・$kail（ここのみ。使用人。$keanの父
#   ・$kean（ここのみ？使用人
#   ・$patson（初出。地元の刑事。後に本庁に取り上げられる。もともと$cultX信者

# NOTE: stages
#   ・西部の田舎町（原作のボスコム谷。ここでも沼地。ただ特殊な鉱石が採掘できるのでそれで一部が儲けていた

# NOTE: items
#   ・魔導列車（初出？

# NOTE: case
#   ・父親殺し事件　→偽装で、本当は遺産目当ての妻と、幼馴染の使用人の共犯

def defence_request(w: World):
    return w.episode("弁護依頼",
            w.plot_setup("$wilsonは頻繁に通ってきて$sherlockに第二王女失踪事件の調査を依頼する"),
            w.plot_setup("$sherlockは常に新聞記事で事件を探している"),
            w.plot_setup("地方の事件記事に自分の父親を殺した容疑で娘が捕まったと掲載"),
            w.plot_turnpoint("$keanが依頼にやってくる"),
            )


def about_this_case(w: World):
    return w.episode("事件について",
            w.plot_turnpoint("$restradeの計らいで$maryと面会許可が降りた"),
            )


def interview_of_mary(w: World):
    return w.episode("$maryの面会",
            w.plot_turnpoint("$maryは$animalだと$wilsonに語った"),
            )


def family_circumstances(w: World):
    return w.episode("家族の事情",
            w.plot_turnpoint("$maryが$patsonによって連れてこられた"),
            )


def mother_and_daughter(w: World):
    return w.episode("母と娘",
            w.plot_turnpoint("$kailが$jeanを人質に取る"),
            )


def new_resident(w: World):
    return w.episode("新しい住人",
            w.plot_resolve("$maryが$sherlockの家に住み込むことになった"),
            )


# Chapter
def main(w: World):
    return w.chapter(TITLES[2],
            # NOTE
            #   事件：$gunによる目撃者のいない殺人
            #   被害者：地元の名士$royd氏
            #   容疑者：$mary
            #   犯人：家の使用人の$kail（共犯としての$jean）
            #   依頼人：家の使用人の息子の$kean
            #   トリック：アリバイ偽装（偽証と指紋偽装）
            #   結果：共犯として母親が逮捕され、$maryが遺産を独り占めすることになった
            #   ポイント：$animalの存在示唆／改造$gun
            w.plot_setup("$wilsonは改めて$sherlockに第二王女失踪の調査を依頼しにやってくる"),
            w.plot_setup("$sherlockは常に世の中の難事件を探して新聞や記事の切り抜きを集めている"),
            w.plot_setup("世間では$jackの動きが沈静化していた"),
            w.plot_setup("最近改造$gunを使ったと思われる事件が起こっていた"),
            w.plot_setup("$gun事件の中でつい最近起こったある地方の悲劇（娘が父親を殺した）に触れる"),
            w.plot_turnpoint("使用人の息子の$keanが依頼に訪れる"),
            w.plot_develop("$keanは容疑者である娘の$maryが絶対に殺人をしていないから、無実を証明してほしいと依頼した"),
            w.plot_develop("$sherlockと$wilsonは$keanと一緒に現場に向かう"),
            w.plot_develop("$sherlockは先に事件現場を見に行く"),
            w.plot_develop("残された夫人$jeanに話を聞く"),
            w.plot_turnpoint("$maryが拾われた子で、父親と確執があったと聞く"),
            w.plot_develop("$sherlockは本当にそうなのか確かめるため$maryとの面会許可をもらう"),
            w.plot_develop("$maryと出会い、話す$sherlock"),
            w.plot_develop("$maryは自分は父親に重要な話があると呼び出されて、それを聞いてすぐにその場から消えたと語った"),
            w.plot_turnpoint("$sherlockは$maryが$animalだと$wilsonに語る"),
            w.plot_develop("警察は$sherlockが現場で見つけた体毛と$maryの$animal情報から、いよいよ彼女を犯人と断定する"),
            w.plot_develop("$sherlockは$roydの古い友人から、彼が拾ってきた自分の娘にいつそれを打ち明けるか悩んでいたと聞く"),
            w.plot_develop("また、$jeanが後妻で、遺産相続について娘の存在を邪魔に感じていたと知る"),
            w.plot_develop("$sherlockは今一度$jeanから事情を聞くために屋敷を訪れる"),
            w.plot_turnpoint("使用人の$kailが$jeanが寝込んだと追い返す"),
            w.plot_develop("$sherlockは$keanに頼んで当日の$kailのアリバイを知る"),
            w.plot_develop("警察とともに再度訪れ、$maryと話してほしいと$jeanに伝えるよう$kailに告げる"),
            w.plot_develop("$jeanと$maryがいる前で、$sherlockは説明を始める"),
            w.plot_develop("実行犯は使用人の$kailで、$jeanと共謀し、口裏を合わせたと"),
            w.plot_develop("$kailと$jeanは同じ街の出で、かつてから面識があり、彼女の力になるためにここの使用人になった"),
            w.plot_develop("恋愛関係があったかどうかは分からないが、二人の証言に微妙な違いがあり、それが偽証を見破るもとになった"),
            w.plot_develop("$kailは自分一人で考えたもので、$jeanは無関係だと突っぱねる"),
            w.plot_turnpoint("$kailが$jeanを人質にして、逃亡を謀ろうとする"),
            w.plot_resolve("しかし$maryが獣化し、$jeanを取り戻す"),
            w.plot_resolve("$kailが逮捕され、事件は終焉を迎える"),
            w.plot_resolve("事件後、$kailが酒場で改造$gunを手に入れたことを知る"),
            w.plot_resolve("共犯者として逮捕された$jean"),
            w.plot_resolve("母親が逮捕され、全財産を相続した$maryが権利を放棄し、屋敷を地元に寄付したと聞いた"),
            w.plot_resolve("$maryは$sherlockに一緒に住まわせてほしいと依頼した"),
            #
            defence_request(w),
            about_this_case(w),
            interview_of_mary(w),
            family_circumstances(w),
            mother_and_daughter(w),
            new_resident(w),
            )


