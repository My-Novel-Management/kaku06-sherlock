# -*- coding: utf-8 -*-
'''
Chapter "最後の事件"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES
from scenes import AbandonedHouse
from scenes import InCar
from scenes import InCity
from scenes import Market
from scenes import MorianoHouse
from scenes import SherlockHouse
from scenes import SteinHouse


# Episode
# NOTE
#   .ある殺人事件＞$sherlockが$morianoの名を口に出す
#   .犯罪学者$moriano＞老人は$morianoだった
#   .$maryの不安＞$maryが姿を消した
#   .$maryと$moriano＞$sherlockが救出にやってきた
#   .$maryの不審＞$sherlockは姿を消した
#   .$sherlockの消息＞$sherlockの帽子が見つかった

# NOTE: outlines
OUTLINES = [
        "元大学教授の謎の死を受けて$sherlockは調査に訪れていた。その人物は$boss復活の技法について研究をしていた。$sherlockはその男の書き残したものに$morianoの名を見つけた",
        "$sherlockは$morianoについて語る。この都市の多くの犯罪の糸が$morianoに繋がっていた。$sherlockは珍しく自分の命に代えても$morianoを倒すと言う。そこに$maryが連れてきた老人こそが、$morianoだった",
        "$morianoは$sherlockが人の気持ちより謎解きの方を大切にすると指摘し、$maryたちも捨てられると予言する。$morianoは$sherlockに犯罪をなくすことは不可能だと言い、これ以上自分を追うと余計な犠牲者が出ると脅した。後日、$maryが姿を消した",
        # $morianoの甘言にのり、$maryが姿を消した
        "$sherlockは責任を感じて$maryを探す。$morianoの別荘を突き止めたが、そこにはナイフを手にした$maryがいて$sherlockは襲われる。しかし$limeにより阻止される",
        "$maryは$sherlockがやがて$ajinを迫害する世の中を復活させるときいて恐ろしくなったと告白する。それは$morianoによる言葉の洗脳だった。$sherlockは$morianoとの対決に単独で向かう",
        "$sherlockが消息をたち数日後、彼からの手紙が届く。そこには$morianoとの決闘直前に書かれた遺書めいたメッセージがあった。警察とともに$sherlockを探すが、$morianoの宿泊先の滝で見つかったのは彼のトレードマークの帽子だった",
        ]

# NOTE: charas
#   ・$moriano（名前もここが初出。ほぼここのみ
#   ・$stein教授（事件被害者。$morianoの知人。$boss復活研究家

# NOTE: stages
#   ・$steinの家
#   ・$moriano研究所
#   ・$morianoの別荘
#   ・王立大学

# NOTE: items

# NOTE: case
#   ・$stein元教授殺人事件　→$cultXの支援を受けて研究していたが、危険なことだと分かり、裏切ったために処分（$jakeによる

# NOTE: tech
#   ・

def the_fixer(w: World):
    return w.episode("事件の黒幕",
            # NOTE
            #   ・闇の儀式（前回のラストから引き続きで
            w.plot_setup("$sherlockは孤島の事件の後、頻繁に図書館に通っていた"),
            w.plot_setup("$wilsonも忙しそうにあちこち出かけていた"),
            w.plot_setup("$maryと$limeは仲良くしていた。家事を分担し、落ち着いていた"),
            w.plot_turnpoint("大家$lisaがやってきて、家賃が半年ばかり振り込まれていないと告げる"),
            w.plot_develop("$maryは$sherlockに相談するが、彼は気にしない。今までも大丈夫だったからと"),
            w.plot_develop("$wilsonに相談したかったが、姿を見せない"),
            w.plot_develop("市場で$ignesや$nowlisに相談すると、何か仕事を探すかという話に"),
            w.plot_develop("就職情報誌をもらって帰って$limeと二人で相談する"),
            w.plot_turnpoint("$patsonがやってきて、$sherlockに事件のことでアリバイを聞きたいと言ってきた。殺人事件が発生したらしい"),
            #   ・元大学教授の殺人
            w.plot_develop("殺されたのは古代の技術を研究していた元大学教授の$stein"),
            w.plot_develop("$steinは最近$sherlockが口にしていた名前で、図書館以外にも何度か話を聞きに訪れたらしい"),
            w.plot_develop("戻ってきた$sherlockはそこで$steinが亡くなったことを知る"),
            w.plot_develop("ずっと闇の儀式のことを調べていたと証言する$sherlock"),
            w.plot_turnpoint("$steinは$morianoの旧友で、今回の件でついに黒幕が動き出したと言った"),
            )


def about_moriano(w: World):
    return w.episode("$morianoについて",
            # NOTE
            #   ・$morianoとは
            w.plot_setup("元大学教授$stein殺害容疑が$sherlockにかかっていた"),
            w.plot_setup("$sherlockは$steinが$morianoの知人と言う"),
            w.plot_setup("$morianoについて、$sherlockはついに語り始めた"),
            w.plot_turnpoint("$morianoは今起こっている多くの犯罪の裏側で糸を引く黒幕だと語る"),
            w.plot_develop("$morianoは幼少期から神童と呼ばれ、十代にして国立大学で博士号を取得する"),
            w.plot_develop("文学、言語学はもちろん、社会学、心理学、数学に長け、特に研究熱心だったのは$scienceだった"),
            w.plot_develop("現在の技術革新があるのも$morianoのお陰だと語る"),
            w.plot_develop("その$morianoはある日突然大学を去り、独自の研究所を開設した"),
            w.plot_develop("それが犯罪研究所だ"),
            w.plot_develop("表向きは犯罪に関する研究を行うが、裏では犯罪者の助けとなる仕組みや道具を横流ししていた"),
            #   ・市場の変化
            w.plot_develop("一方$maryは買い出しに市場にきていた"),
            w.plot_develop("続いている$jackの連続殺人事件もあって、市場にも警備の兵士が立ち、物々しい雰囲気"),
            w.plot_develop("最近宗教の宣伝も増えていて、男が憲兵に取り締まられていた"),
            w.plot_develop("$maryはうずくまっていた老人を助ける"),
            w.plot_turnpoint("$maryが連れて帰ってきた老人こそが、$morianoだった"),
            )


def his_warning(w: World):
    return w.episode("$morianoの警告",
            # NOTE
            #   ・$morianoの警告
            w.plot_setup("$maryが助けた老人が$morianoだった"),
            w.plot_setup("$sherlockは$maryに$morianoが犯罪の黒幕と説明する"),
            w.plot_turnpoint("$morianoは$maryにあげた飴に毒が入っていたと言う"),
            w.plot_develop("解毒剤を見せ、$morianoは$sherlockに警告する"),
            w.plot_develop("$moriano側も$sherlockの動向は把握していて、今までの行動の全てが記録されていた"),
            "ここで記述者が$morianoかも知れないと勘違いさせること",
            w.plot_develop("$morianoは$sherlockの活躍を新聞小説のように楽しんでいると"),
            w.plot_develop("ただ今までの事件でもっと早くに手が打てれば傷つく人が少なかったと"),
            w.plot_develop("いつも犠牲者が出てから動くのは弱者の行動だと笑う"),
            w.plot_develop("$morianoは$maryに解毒剤といってソーダ水を渡し、去っていく"),
            w.plot_develop("$sherlockは$morianoからもらった飴をなめて、ただの砂糖菓子だと苦笑する"),
            #   ・事件調査
            w.plot_develop("$sherlockは亡くなった$stein教授の調査に向かう"),
            w.plot_develop("$patsonと遭遇し、また疑われる"),
            w.plot_develop("殺害方法は$gunだったが、部屋はロックされた状態で密室だった"),
            w.plot_develop("凶器も見つからず、捜査は難航していた"),
            w.plot_turnpoint("$sherlockは部屋で$boss復活に関する資料を見つけた"),
            #   ・$maryの異変
            w.plot_develop("一方$maryは$morianoに言われてから、不安定だった"),
            w.plot_develop("市場に買い出しにでかけた$maryは、$morianoと再会する"),
            )


def lookfor_mary(w: World):
    return w.episode("$maryの捜索",
            # NOTE
            #   ・$mary失踪
            w.plot_setup("$maryが買い物に行ったまま帰ってこない"),
            w.plot_setup(""),# TODO
            #   ・$maryを探せ
            )


def rescue_mary(w: World):
    return w.episode("$mary救出劇",
            # NOTE
            #   ・$maryの本心は
            #   ・最終決戦
            )


def his_letter(w: World):
    return w.episode("$sherlockからの手紙",
            # NOTE
            #   ・$sherlockからの手紙が届いた
            )


# Chapter
def main(w: World):
    return w.chapter(TITLES[6],
            # NOTE
            #   事件：研究者密室殺害事件／$moriano殺人
            #   被害者：$stein元教授／$moriano
            #   容疑者：$moriano／$sherlock
            #   犯人：$jake／$jake
            #   依頼者：$appolo（$sherlockの恩師）
            #   トリック：改造$gunにより外から遠隔操作で毒薬を打ち込み、死亡
            #   結果：$morianoが死に、姿を消した$sherlockがその重要参考人として手配された
            #   ポイント：$stone黒（$sherlockの手紙と一緒に届く）／目的は$boss復活
            w.plot_setup("孤島の事件の後、$sherlockはやたらと図書館にでかけていた"),
            w.plot_setup("事件の陰で暗躍した$cultXについては小規模の新興宗教団体として以上の情報なかった"),
            w.plot_setup("他にも四つの$stoneについて調べたり、ブラックマーケットの情報を漁ったりしていた"),
            w.plot_setup("$maryと$limeは料理を教わったり、仲良くなっていた"),
            w.plot_setup("世間では$festivalを前にして、賑わいの空気に満ちていた"),
            w.plot_setup("元研究者の謎の密室殺人事件が発生する"),
            w.plot_turnpoint("$restradeがやってきて、殺人事件の解決を依頼する"),
            w.plot_develop("$restradeから事件の概要を詳しく聞く"),
            w.plot_develop("$sherlockは研究者の家を訪れて調査する"),
            w.plot_develop("一方$maryは市場にでかけて、$sherlockに言われた言葉が気になっていた"),
            w.plot_develop("いつかは自分の将来のことを決めなければいけない、ということに悩んでいた"),
            w.plot_develop("その$maryは不思議な老人と出会う"),
            w.plot_develop("家に戻った$sherlockは$wilsonに興奮気味に$morianoについて語る"),
            w.plot_develop("$morianoは$sherlockがやっと突き止めた様々な犯罪の裏側にいる大きな黒幕だった"),
            w.plot_develop("$morianoの経歴は大学教授になり最初の論文を発表するまではすさまじい"),
            w.plot_develop("幼少期から神童と呼ばれ、十代で博士号を取得した"),
            w.plot_develop("特に数学的見地に長け、論理的に人間を動かす方法に長けていた"),
            w.plot_develop("しかしある時を境に表舞台から姿を消し、自分の研究所を作ってひっそりと暮らす"),
            w.plot_develop("そこからこの街の犯罪は複雑性をましたと$sherlockは語る"),
            w.plot_turnpoint("$maryが連れてきた老人は$morianoだった"),
            w.plot_develop("$morianoは挨拶をして、$maryに与えた飴が毒薬だと語る"),
            w.plot_develop("解毒剤は準備してあるが、$sherlockが自分について調べるのをやめるのと引き換えだと脅す"),
            w.plot_develop("$sherlockはそれでも$morianoを排除することを諦めないと抵抗する"),
            w.plot_develop("$sherlockはその毒薬入の飴を食べて、ブラフだと見抜いた"),
            w.plot_develop("$morianoは$sherlockが自分の理想のためには大切な人ですら犠牲にすると言って、立ち去る"),
            w.plot_develop("$maryは$sherlockに不信感を抱くようになる"),
            w.plot_turnpoint("$sherlockの家が火事にあう"),
            w.plot_develop("住む場所を失った$sherlockたち"),
            w.plot_develop("いったん$wilsonの家で世話になる"),
            w.plot_develop("$sherlockは変わらない生活を続けるが、$wilsonは調べものなどの仕事でよく出かけるようになる"),
            w.plot_develop("$maryは自分のせいかもしれないと悩んでいた"),
            w.plot_turnpoint("$maryが失踪する"),
            w.plot_develop("$sherlockはそのうち戻ってくると言うが、$limeは探しに向かう"),
            w.plot_develop("市場で$maryが黒服にシルクハットの老人と歩いているのを目撃したと知る"),
            w.plot_develop("その老人は$morianoだと判明する"),
            w.plot_develop("$maryが誘拐されたのではなく、自分の意志で$morianoの許に向かったと知る"),
            w.plot_develop("$sherlockは少年探偵団などに指示をし、$morianoの別荘を調べる"),
            w.plot_turnpoint("$sherlock単独で$morianoの別荘に向かう"),
            w.plot_develop("$maryは自身が$animalなことで悩んでいた"),
            w.plot_develop("$boss復活した際には人とは違う側に立つことになり、また差別されると教わった"),
            w.plot_develop("そうならないように$boss復活を阻止するのを手伝ってほしいと頼まれた"),
            w.plot_turnpoint("$sherlockが$maryを助けにやってくる"),
            w.plot_develop("$maryは$sherlockが$boss復活を考えてるんじゃないかと恐れている"),
            w.plot_develop("$sherlockは$morianoの居場所を聞く"),
            w.plot_develop("$sherlockは$maryが騙されていると説くが、$maryは彼の言葉を信じられない"),
            w.plot_develop("$sherlockはその場に残された本から場所を推定し、出ていく"),
            w.plot_develop("$maryを助けに$limeがやってきたが、彼女は泣いていた"),
            w.plot_turnpoint("それから$sherlockは消息を絶つ"),
            w.plot_develop("街では$festivalが行われ、賑わいの雰囲気"),
            w.plot_develop("何事も起こらず、$sherlockの言ったことが正しかったのだと$maryは知る"),
            w.plot_develop("$maryは$shserlockと$moriano二人の行方を追う"),
            w.plot_turnpoint("$sherlockが書き残しておいた手紙が見つかった"),
            w.plot_resolve("手紙には$sherlockが$morianoの悪事の情報をまとめた資料が同封されていた"),
            w.plot_resolve("また$maryを救出にいった先でどうなるかの予測が書かれていて、それによれば一緒に死ぬ可能性が最も高いとあった"),
            w.plot_turnpoint("警察から$morianoたちの消息がわかったと連絡が入る"),
            w.plot_resolve("$maryは$wilsonたちとともに$sherlockが向かったという$morianoの別荘に向かう"),
            w.plot_resolve("しかしそこで警察の捜索隊により$sherlockの帽子が事故現場から発見された"),
            #
            the_fixer(w),
            about_moriano(w),
            his_warning(w),
            lookfor_mary(w),
            rescue_mary(w),
            his_letter(w),
            )


