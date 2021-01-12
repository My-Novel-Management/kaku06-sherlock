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
ABSTRACT = """
孤島の事件の後で$sherlockは頻繁に王立図書館に出かけて調べ物をしていた。
元大学教授$steinが自宅で謎の死を遂げる。その関係者の一人として$sherlockが浮上し、容疑者として事情聴取される。
$maryは$limeから編み物を習ったりして良好な関係を築いていたが、孤島から戻ってきて以来、少し考え事をしている時間が増えた。
その$maryは市場からの帰り、ふさぎ込んでいる老人を助ける。
一方自分と$stein教授の関係を話して容疑を晴らす$sherlock。その話から$morianoの名前を出し、彼こそが全ての元凶だと語る。そこに$maryが老人を連れて戻ってきたが、その老人こそが$morianoだった。
$morianoは$maryに毒入りの飴を与えたと言い、$sherlockに自分の件から手を引くように脅す。$morianoは$boss復活を考えていて、人間同士による戦争でやがて人間が滅びると予想していた。
$morianoが去った後、$sherlockは彼の言葉が全て嘘で、世界を混乱に陥れたいだけだと語るが、$maryの心には今の$ajin差別がかつてはなかったという言葉が引っかかっていた。
後日、$maryが姿を消す。$sherlockは放っておけというが$limeは探しに歩く。
$morianoの犯罪研究所を訪れると助手の$muranから彼の研究が世界を良くすることに貢献していると知る。また$maryが現在$morianoの研究を手伝っていることも知った。
何とか説得し、戻ってくるようにと伝えたが、$maryは戻ってこなかった。
ずっと$morianoが犯罪に関わった証拠を探していた$sherlockは$steinの家でやっとその痕跡を発見し、$morianoを追い詰める為に彼の研究所に赴く。
だが洗脳された$maryによりその行為は阻止され、$morianoの逃亡を許す。その上、$maryは$sherlockを傷つけてしまったショックから意識を失う。
目覚めた$maryは$limeから$sherlockが$morianoを追いかけて、滝に落ちたことを知る。
後日届いた手紙には、$sherlockから$morianoの犯罪に関する証拠を警察に送ったことと、$maryへの謝罪が書かれていた。
"""
OUTLINES = [
"""
孤島事件後から$sherlockは頻繁に外に出かけるようになっていた。
$maryたちは少し退屈さを感じつつも、自分の今後の身の振り方について考える時間を持つ良い機会だった。
一方、元大学教授が謎の死を遂げた。その容疑者の一人として$sherlockが浮上する。
$maryは市場への買い物の帰り道で、ふさぎ込んでいる老紳士と遭遇し、彼を助ける。
やってきた$patsonは何かの資料を調べるのに必死になっている$sherlockに、$stein元教授殺人事件について事情をきかせろと迫る。
""",
"""
$sherlockはすぐにアリバイを語り、自分の容疑を晴らす。
そもそも$stein教授とは王立図書館で出会った。彼の論文は$sherlockもよく目を通していて、教授から古代の知識について色々と教わっていたと話す。
そして$steinは$morianoの友人だと言い出す。
$morianoについて誰も知らなかった。
$sherlockは$morianoについて語る。この都市の多くの犯罪の糸が$morianoに繋がっていた。$sherlockは珍しく自分の命に代えても$morianoを倒すと言う。
そこに$maryが連れてきた老人こそが$morianoだった
""",
"""
$morianoは$sherlockに対して自分は$steinの死とは無関係だと言う。証拠がないだろうと。
$sherlockは$morianoがどんな犯罪も自分で直接手をくださず、故に現在の司法では立件できず罪に問えないと言う。
だがそこを何とか見つけ出し、必ず罪を償わせると豪語する$sherlock。
その$sherlockに対し、$morianoは$maryに毒入りの飴を与えたことで脅し、これ以上は深入りしないようにと警告した。
その上で、$morianoは$sherlockが人の気持ちより謎解きの方を大切にすると指摘し、$maryたちも捨てられると予言する。$morianoは$sherlockに犯罪をなくすことは不可能だと言い、これ以上自分を追うと余計な犠牲者が出ると脅した。
その翌日、全員が出払っていた間に$sherlockの家は放火されてしまう。全焼こそ免れたが、中も荒らされていて、しばらく使えないという判断から、少しの間$wilson宅で暮らすことにした。
後日、$maryが市場に買い出しに出かけたまま帰ってこなかった。彼女は失踪した。
""",
        # $morianoの甘言にのり、$maryが姿を消した
"""
$maryがいなくなり、$limeはどこにいったのか探さないといけないと主張するが、$sherlockは放っておけばいいと聞かない。
$limeは$ignesたちに協力してもらい、$maryの行方を探す。
一方$sherlockは$steinの家の再調査に訪れていた。$morianoが関与した証拠を探すためだ。しかし痕跡が綺麗に消されている。だが$steinの日記のページの間に一本の毛髪を見つけた。毛髪を証拠にできないかと考える$sherlock。
$limeは$morianoの研究所に入るのを見たという情報を得て、単身研究所に向かう。研究所では助手の$muranだけがいて、$morianoがどんな人物なのか、何をしようとしているのか、その本当の姿を語った。
そこに$maryを連れて$morianoが戻ってくる。彼女は誘拐された訳でも監禁された訳でも何か弱みを握られている訳でもなく、自分の考えでここにいると言った。
$maryは戻らないと$limeに言った。
""",
"""
$maryが$morianoと一緒にいると知り、どうにかしないといけないと$sherlockに言う$limeだったが、$sherlockは何もしない。彼女の考えに任せればいいと言う。
$wilsonたちにも相談したが、$mary自身の考えはどうしようもないとだけ。
$sherlockは何かに夢中になり、頻繁に外出を繰り返し、頼りない状態だった。
そんな$limeに王室の執務官$mikelがやってきて、王室に戻るように言う。王の病気が悪化したというのだ。$limeは$maryを放っておいたままではいけないと悩む。
一方$sherlockは頼んでおいた毛髪鑑定により、人毛で$morianoと同一の血液型ということまで判明した。しかし決定的証拠にはならない。そこを騙ることでボロを出させようと、研究所に向かう。
だがそこで待ち構えていたのは$transformした$maryだった。$morianoは逃げ出したのだ。
$sherlockの説得むなしく、彼女により$sherlockは酷い傷を追う。それで正気に戻り、$maryは気絶した。
""",
"""
$maryが病院で目覚めると$limeから$sherlockが国外逃亡した$morianoを追っていることを聞かされる。
$maryが自分が$sherlockを傷つけてしまったことを後悔していた。
後日、$sherlockから手紙が届く。そこには$morianoを道連れにしてでも滅ぼす決意と、彼の犯罪関与の証拠とそれについて書いた書類が既に警察に発送されていると記されていた。
最後に$maryについての謝罪が書かれていた。
警察の捜査で$sherlockと$morianoが滝から落下したことが判明。現場に残されていた彼の帽子と血液から、二人は死亡したものと見られた。
""",
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
            outline=OUTLINES[0])


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
            outline=OUTLINES[1])


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
            outline=OUTLINES[2])


def lookfor_mary(w: World):
    return w.episode("$maryの捜索",
            # NOTE
            #   ・$mary失踪
            w.plot_setup("$maryが買い物に行ったまま帰ってこない"),
            w.plot_setup("$limeが探しに出かけていたが見つからない"),
            w.plot_setup("$limeが最近様子が変だったと言う"),
            w.plot_turnpoint("$ignesがやってきて、変なじいさんについていくのを見たと証言した"),
            w.plot_develop("$morianoに連れ去られたと言う"),
            w.plot_develop("$sherlockは目撃証言から、自分でついていったんじゃないかと推測する"),
            w.plot_develop("$sherlockは$maryなんてほっとけばいいとすら"),
            w.plot_develop("$limeと$wilsonはそれでも探しに行く"),
            w.plot_develop("$sherlockは自分の研究に必死だった"),
            #   ・$maryを探せ
            w.plot_develop("$limeと$ignesと協力して$morianoがどこにいるか調べる"),
            w.plot_develop("$morianoの犯罪研究所を訪れる$lime"),
            w.plot_develop("助手の$muranだけがいて研究所の仕事と$morianoについて語ってくれる"),
            w.plot_develop("$morianoは$sherlockが語ったような人物とは異なっていた"),
            w.plot_develop("現在多くの人が苦しんでいる。その社会構造を変えるためには多少の犯罪を助けてでも、弱者の味方が必要だと"),
            w.plot_develop("人殺しはいけないことなのに、弱者を飢えや病で殺すことは犯罪じゃないのかと"),
            w.plot_develop("$limeはわからなくなる"),
            w.plot_turnpoint("そこに$maryとともに$morianoが現れた"),
            outline=OUTLINES[3])


def rescue_mary(w: World):
    return w.episode("$mary救出劇",
            # NOTE
            #   ・$maryの本心は
            w.plot_setup("$morianoの研究所を訪れた$lime"),
            w.plot_setup("$maryは$morianoとともに戻ってきた"),
            w.plot_turnpoint("$maryは帰らないと$limeに告げる"),
            w.plot_develop("$maryは$morianoの考えを聞き、$sherlockがやっていることは本当は良くないことじゃないかと思い始めていた"),
            w.plot_develop("人が幸せを掴むために仕方なく犯した罪を、全く関係のない$sherlockが裁き、警察に突き出す"),
            w.plot_develop("真実が明るみにならなかった方が幸せだったケースもある"),
            w.plot_develop("特に孤島事件の時は巻き込まれたとはいえ、事件の裏側にあったのは$cherryの寂しさとどうしようもなさだった"),
            w.plot_develop("社会を変えるのは$morianoの考えだと思い、今勉強していると言う"),
            w.plot_develop("$limeはそれでも犯罪は悪いことだと言う"),
            w.plot_develop("貧しい人を助けられないのは王室や議員たちの怠慢だと認めつつも、全てを助けることはできないと"),
            w.plot_develop("$limeは$maryが帰ってくると信じていると、言い残して、後にする"),
            #   ・$sherlockの気持ちは
            w.plot_develop("$limeは帰って$sherlockに$maryのことを伝えた"),
            w.plot_develop("$sherlockはほとんど寝ずに何か実験を繰り返していた"),
            w.plot_turnpoint("$sherlockは色の変わった小瓶を見て、やっと$morianoを追い詰められると言った"),
            #   ・世直しの為に
            w.plot_develop("$maryは$morianoの世話をしながら、考えていた"),
            w.plot_develop("彼が言うように$sherlockが悪いとは考えていなかったが$limeを近づけたくはなかった"),
            w.plot_develop("自分が$limeに嫉妬していたのは分かった"),
            w.plot_develop("$muranは$maryにそれでいいと言う"),
            w.plot_develop("ここでは様々なことが肯定された。居心地がよかった"),
            w.plot_develop("$morianoがやってきて世界のシステムを変えるための儀式に必要なものが揃ったという"),
            w.plot_develop("$maryは$sherlockからの預かりものである$blue_stoneを渡す"),
            w.plot_turnpoint("しかし、そこに$sherlockが殺人の証拠品を持って現れた"),
            outline=OUTLINES[4])


def his_letter(w: World):
    return w.episode("$sherlockからの手紙",
            # NOTE
            #   ・対決
            w.plot_setup("$sherlockは$morianoの殺人の証拠を手に、やってきた"),
            w.plot_setup("$maryは預かっていた$blue_stoneを$morianoに渡す"),
            w.plot_setup("$sherlockは$morianoに自主するように言う"),
            w.plot_turnpoint("$transformした$maryは$sherlockを貫いてしまう"),
            w.plot_develop("$sherlockを殺してしまったと思った$mary"),
            w.plot_develop("感情が制御できず$morianoにも襲いかかる"),
            w.plot_turnpoint("$muranにより阻止され、$maryは意識を失う"),
            #   ・$sherlockからの手紙が届いた
            w.plot_resolve("$maryが気づくと$sherlockの家にいた"),
            w.plot_resolve("$limeからその後の事情を聞く$mary"),
            w.plot_resolve("$sherlockは家を爆破して逃げ出した$morianoを追いかけて出ていった"),
            w.plot_resolve("$limeは家に$maryを運び込み、手当をした"),
            w.plot_turnpoint("$sherlockから手紙がきた"),
            w.plot_resolve("手紙は$sherlockが$morianoを追い詰めたところで書かれていた"),
            w.plot_turnpoint("滝で$sherlockの遺品が見つかった"),
            outline=OUTLINES[5])


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
            the_fixer(w),
            about_moriano(w),
            his_warning(w),
            lookfor_mary(w),
            rescue_mary(w),
            his_letter(w),
            outline=ABSTRACT)


