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

# NOTE: outlines
ABSTRACT = """
$wilsonは聞いてもらえなかった依頼をしようと再び$sherlock宅を訪れる。$sherlockは相変わらず$wilsonの話に聞く耳を持たず、新聞記事にあった父親殺しの悲しい事件について感想を述べる。
そこにちょうどその事件の関係者である使用人の$keanがやってきて、$sherlockに事件の容疑者になってしまった娘$maryの容疑を晴らして欲しいと依頼した。
$sherlockは現場に赴いて調査を行う。
$maryと面会し、$sherlockは証言だけでなく彼女が$animalであることが容疑を決定付けていると語る。
しかし更に調査を進めると$jeanと$kailの関係が$jeanが$royd氏と結婚するより遥か以前にあり、莫大な遺産の相続権が娘の$mary一人になりそうだったという事情が判明する。
$sherlockは最新の指紋検出技術を用いて凶器となった$gunから$jeanと$kailの指紋のみが検出されたことで、二人を追い詰める。
$kailが自分一人だけでやったと$jeanを人質に取るが、$transformした$maryにより阻止され、事件は解決した。
後日、遺産相続権を放棄し、邸宅も地元に寄付をした$maryが、荷物を持って$sherlock宅に押しかけた。
"""
OUTLINES = [
"""
$wilsonは毎日のようにやってきては$sherlockに第二王女失踪事件の調査を依頼しようとする。だが$sherlockはその気はなく、新聞記事を見ては興味のある事件を探している。
記事のある事件。資産家の男が娘に$gunによって殺されるという悲しい事件があった。明け方に新聞配達の男により沼地で倒れている$royd氏が見つかり、死亡が確認された。
警察は状況から娘を容疑者として逮捕し、取り調べを行っていると。
$gunについては詳細は書かれていないが、最近ちょくちょく出回っているものだ。闇社会で資金源になっているのかも知れないと$sherlockは言う。
一方、失踪事件については明確な証拠も関連性もなく、王女のそれについてもよく分からないと$sherlock。
$wilsonの依頼は受けないが、警察や他の依頼者の依頼は色々と抱えていた。
また自分自身で犯罪関連の研究も行っていた。今日は自分の血液を採取して、血の研究をしていた。
と、そこに訪問者がある。
その事件の被害者宅に務める使用人の息子$keanが訪れて、$sherlockに容疑者である娘の容疑を晴らして欲しいと依頼した。
""",
"""
$sherlockは$keanから事件のあらましを聞く。おおむね新聞記事の通りだったが、$keanは絶対に娘の$maryが父親を殺すはずはないと断言している。
なけなしの小銭で依頼する$keanに応える$sherlockは、$wilsonとともに事件のあった街に向かう。
電車で向かう最中に、どんな地域なのかを教わる。あまり産業のない土地だったが$royd氏が見つけた$stone鉱脈により潤っていた。それで駅も誕生したと。
街に到着すると、$sherlockたちは事件のあった沼地を訪れる。そこで現場を訪れていた地元の刑事$patsonと遭遇。怪しまれる。
$sehrlockが$restradeの名前を出すとすぐに縮こまり、協力してなんでも教えてくれるという。
どうやらただ証言だけで$maryを犯人と決めている訳ではないと語る。
それについては教えてもらえなかったが、$sherlockは現場で動物の毛を採取した。
$royd邸にやってきた$sherlockは、使用人の$kailと未亡人となった$jeanから話を聞く。
それぞれに互いのアリバイの証言を行う。また娘の$maryが父$roydと事件当日夜、外で出会ったことも目撃証言があった。
二人以外からも外で歩いているのを見たというものもあり、外出し、実際に現場で会ったことは確からしい。
また凶器となった$gunは$maryの部屋から$kailが発見した。
$sherlockは何とかして$maryからも話を聞く必要があると、警察に向かう。
""",
"""
警察にやってきた$sherlockたち。$patsonは$maryとは会わせられないという。
$sherlockは$restradeのツテを利用してなんとか僅かばかりの面会の時間を得る。
面会した$maryは衰弱していたが、$sherlockが$keanの依頼できたことを知ると、全て話すと言った。
$maryは自分が父親に話があるからと呼び出されて事件現場に行った。どうしても家の中で話せないことがあるからと。
そこで自分が拾われた子供だったと告白された。それにショックを受け、そのままその場を立ち去った。途中バラ園で休んでから家に戻った。そのまま部屋から一歩も出ず、翌朝、$kailに起こされて父親が亡くなったことを聞かされた、と。
その時にはまだ誰が殺したか分からず、ただしんだことだけ教わった。
その後、警察が来たり、それぞれ事情聴取された。何故か自分の部屋から凶器の$gunが発見され、容疑者になってしまった。
自分は絶対にやらないし、拾われ子だったことはショックだったが、父親には恩義しか感じていないと。
面会後、$sherlockは全てを語っていないと言う。
$maryは$animalだった。またそれが警察の容疑者候補として強い印象になっていると。
""",
        # 容疑者の$maryは$animalだった
"""
$sherlockは独自に酒場や街を歩いて情報を集める。
その間に$wilsonは一旦$Londonに戻り、$sherlockに頼まれた仕事をこなしていた。
ある老人を訪ねる。$edoという名の老人は、$sherlockから頼まれてあるものを開発していた。
それは指紋検出器だった。指紋とは指の模様だという。
$sherlockはパブである男性から$jeanが同じ学校だという話を聞く。彼女は後妻で玉の輿に乗れたと喜んでいたと。貧しい家の出で、$royd氏はそういった子供たちに支援もしていた。
そういう人物を拾った娘が殺したのは酷い話だと。どうも街では娘が拾い子だという話は誰もが知っている噂だった。
また$royd氏には莫大な遺産があり、本来ならそれは全てあの娘が相続するはずだったとも。
$sherlockは$jeanが育ったという学校にやってくる。そこで若い頃の$jeanの絵を見つける。卒業生による肖像画だというが、そこに$kailのサインを見つけた。
一晩泊まり、翌日、$sherlockは単身$royd邸を訪ねる。しかし$jeanが体調不良で面会できないと言われた。
警察に行くとちょうど$wilsonが戻ったところで、指紋検出を行う。だがそれは$maryの指紋とは異なっていた。
""",
"""
検出結果を受けて$sherlockは再度$royd邸を訪問する。
$jeanは体調悪いからと使用人$kailに断られたが$maryを連れてきて、彼女と直接話があるというと奥から$jeanが出てきて応じてくれた。
$maryはあの場所で父親になんと言われたかを語った。
それは決して遺産相続の話ではなく、自分の出自にかかわることだった。
拾われた子供だ、というのは既に街の人間の噂から察していたが、それだけでなく$animalだと告白された。それも、自分と別の$animalの子供だ、と。実の娘だった。
それは$royd氏がずっと隠していた事実であり、だからこそ$royd氏は遺書で全財産を娘にやると書いていたのだ。
それにショックを受けて家に戻った$mary。一晩中自分の気持を処理できずに寝られなかった。
その告白に対して$jeanはずっとそうじゃないかと疑っていたと。だから余計に愛せなかったと。
そして前日の夜、$roydから直接、話す決意をしたと聞かされた。それは$maryの十六歳の誕生日を迎えるからだった。
$jeanは遺産を$maryにあげたくなくて、$roydを殺して$maryを犯罪者にしたと告白したが、
その時$kailがナイフを振りかざして人質に取った
""",
"""
殺人を計画したのは$kailだった。学校時代から憧れの女性で、ずっと彼女に思いを寄せていた$kailは、彼女の悩みのよき相談相手だった。
彼女が結婚してからも、ここで使用人としていることで彼女の助けになった。
$roydが病気でそう長くないことを知らされ、今回の殺人を思いついた。
$jeanには口裏をあわせてもらっただけで、あとで殺すつもりだったと語る。
だがそれが$jeanをかばっていることは明らかだった。
$kailは剥きになり、$jeanを殺そうとする。
その時$maryが$transformし、$jeanを守った。だが$jeanはそれでも$maryを愛しているとは言えなかった。
こうして事件が終わった。
後日$keanからの手紙で$maryが遺産相続を放棄し、邸宅も地元に寄付することになったと教わる。
$maryは遠くの親戚に預けられるそうだが、$keanは父親と$jeanの戻る場所を守るために邸宅の管理をしつつバラ園を整備するという。
そこに$maryが大きな荷物を持ってやってくる。
$maryは$sherlockの家で暮らすと言った。
""",
        ]

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

# NOTE: tech
#   ・凶器を使った人間を探すために最新技術の「指紋鑑定」を使う
#   ・魔導列車

def defence_request(w: World):
    return w.episode("弁護依頼",
            # NOTE
            #   ・$wilsonと$sherlock
            #   ・世間の情勢（予備知識もろもろ
            w.plot_setup("皇太子の結婚があり、世間がそれなりに賑わいムードに包まれていた"),
            w.plot_setup("$wilsonは頻繁に通ってきて$sherlockに第二王女失踪事件の調査を依頼する"),
            w.plot_setup("$sherlockは常に新聞記事で事件を探している"),
            w.plot_setup("地方の事件記事に自分の父親を殺した容疑で娘が捕まったと掲載"),
            w.plot_turnpoint("$keanが依頼にやってくる"),
            w.plot_develop("$keanは殺人が起こった家に務める使用人の息子だった"),
            w.plot_develop("彼の話によれば事件は十日前に発生し、家からかなり離れた沼地で資産家の$roydが死んでいるのが発見された"),
            w.plot_develop("殺害は改造$gunによるもの（現在最新の指紋鑑定技術というもので鑑定中）"),
            w.plot_develop("その$gunが娘の$maryの部屋から見つかったことから、彼女を容疑者として逮捕した"),
            w.plot_develop("しかし$keanは彼女と父親の仲は悪くなく、そんなことをする人間ではないと力説し、事件の解決をして欲しいと頼む"),
            w.plot_turnpoint("$sherlockは$keanの依頼を引き受け、事件のあった場所に出かけることにした"),
            outline=OUTLINES[0])


def about_this_case(w: World):
    return w.episode("事件について",
            # NOTE
            #   ・魔導列車で現場に向かう
            #   ・事件現場調査
            w.plot_setup("$keanに頼まれ、父親殺しの容疑をかけられた娘$maryの事件調査に訪れる$sherlockと$wilson"),
            w.plot_setup("事件が起こった田舎町で亡くなった$royd氏は有名な資産家だった"),
            w.plot_setup("彼の死で莫大な遺産が家族に残されると言われている"),
            w.plot_setup("$sherlockは$keanに案内してもらい、事件現場を訪れる"),
            w.plot_turnpoint("現場には若い刑事$patsonがいて、$sherlockを見て不審者扱いをする"),
            w.plot_develop("$sherlockが$restradeの名前を出すと$patsonは協力すると言い出す"),
            w.plot_develop("現場は湿地帯で、小さな女の子の足跡が検出できた"),
            w.plot_develop("目撃者こそいないが、家族の証言から事件の日に$roydと$maryが会っていたのは確実視されている"),
            w.plot_develop("何より殺害方法と凶器から、確実に$maryが犯人と警察は考えていて"),
            w.plot_develop("しかし$maryは父親と会ったことは話したが、それ以外については黙秘を貫いている"),
            #   ・家族の証言
            w.plot_develop("$sherlockは$royd邸を訪れる"),
            w.plot_develop("使用人の$kailに説明し、未亡人となった$jeanと話をさせてもらう"),
            w.plot_develop("$jeanは憔悴していたが、事件前後の話をしてくれる"),
            w.plot_develop("最近$maryと父親の仲がうまくいってなかったと証言する"),
            w.plot_develop("使用人の$kailも同じように証言し、また互いのアリバイを証言する"),
            #   ・警察にて
            #   ＞地元の検死担当医師が妙なものが付着していた、という（あとで獣人の暴露
            w.plot_develop("$sherlockは警察にいき、$maryと話せるように交渉する"),
            w.plot_develop("発見者である地元警官$mackingerに目撃状況を聞く"),
            w.plot_develop("$patsonは$sherlockと$wilsonも阻止される"),
            w.plot_turnpoint("$restradeの計らいで$maryと面会許可が降りた"),
            outline=OUTLINES[1])


def interview_of_mary(w: World):
    return w.episode("$maryの面会",
            # NOTE
            #   ・$maryの証言
            w.plot_setup("$sherlockは$maryと面会できることになった"),
            w.plot_setup("$maryは黙秘を貫いているという話だったが、憔悴して、げっそりしていた"),
            w.plot_setup("$sherlockは自分が$keanに頼まれたことを言う"),
            w.plot_turnpoint("$keanに頼まれたと聞いて$maryは$sherlockに話す決断をする"),
            w.plot_develop("$maryは事件の日の夜、父親に呼び出されて湿地の小屋に向かった"),
            w.plot_develop("$roydは$maryにある打ち明け話をして、すぐに$maryは帰った"),
            w.plot_develop("$maryはしばらく泣いてから、自分の部屋にこもって翌朝はずっと寝ていた"),
            w.plot_develop("起こされたのは事件が発覚してから"),
            w.plot_develop("$maryは自分は父親を絶対に殺していないと訴えた"),
            w.plot_turnpoint("面会後、$maryは$animalだと$wilsonに語った"),
            #   ・$animalについて
            w.plot_develop("実は警察が握っていた証拠もそれで、$mary犯人説が高まっていた"),
            w.plot_develop("$sherlockは$animalについて語る"),
            w.plot_develop("$animalはかつて存在していた$monsterの名残りで、今もひっそりと人間界で暮らしている"),
            w.plot_develop("ただ本人は自覚していないようだから、ハーフやクォーターなどの混血児と推測する"),
            #   ・その他の容疑者
            w.plot_develop("$sherlockは$royd氏が資産家だが、金遣いが渋く、地域住民の中ではあまりよく思われていなかったと聞く"),
            w.plot_develop("町を回り情報を集める"),
            w.plot_turnpoint("酒場にいた男から$jeanが後妻で玉の輿に乗ったんだと聞いた"),
            outline=OUTLINES[2])


def family_circumstances(w: World):
    return w.episode("家族の事情",
            # NOTE
            #   ・
            w.plot_setup("$sherlockは事件についての情報を整理する"),
            w.plot_setup("$sherlockはボロ宿に一晩宿を取らせてもらう"),
            w.plot_setup("$wilsonは地元の新聞社に情報収集にでかけた"),
            w.plot_turnpoint("$sherlockは$jeanをよく知るという女教師に会いにでかけた"),
            #   ・$jeanと$royd氏
            w.plot_develop("学校で教師から$jeanがどういう娘だったか聞く"),
            w.plot_develop("$jeanは不幸な家の生まれで、本来なら学校にも行けなかった"),
            w.plot_develop("$royd氏が貧しい娘や身寄りのない娘に出していた基金を利用し学校を卒業した"),
            w.plot_develop("よく気がつく娘で、神経質なところがあった"),
            w.plot_develop("飲み屋で働いているところを$royd氏に見初められて結婚した"),
            w.plot_turnpoint("ただ$royd氏との間には長く子供ができず、知らない間に娘ができていたことを事件で知ったと"),
            #   ・体調不良の$jeanと話せない
            w.plot_develop("$sherlockは$wilsonと合流して、情報を交換する"),
            w.plot_develop("再度$royd邸を訪れる"),
            w.plot_turnpoint("しかし$jeanは体調を崩していて会えないと、使用人$kailに断られた"),
            w.plot_develop("$sherlockは$maryと$roydが何を話していたかについて、情報を持っているという"),
            w.plot_turnpoint("$jeanが顔を出して、話してくれると言った"),
            outline=OUTLINES[3])


def mother_and_daughter(w: World):
    return w.episode("母と娘",
            #   NOTE
            #   ・$jeanの本心（家庭事情）
            w.plot_setup("$sherlockは何とか$jeanと話す機会を得る"),
            w.plot_setup("$jeanは事件のことで色々と言われて相当参っている"),
            w.plot_setup("今は使用人の$kailが色々と取り仕切っている"),
            w.plot_develop("$sherlockは$jeanに、家族関係について質問する"),
            w.plot_develop("$maryが$animalであることを告げる"),
            w.plot_develop("$jeanもそれは感づいていて、それで困っているんじゃないかと"),
            w.plot_develop("$jeanは自分の娘として愛せなかったと発言する"),
            w.plot_turnpoint("そこに$restrade経由で依頼して$maryが連れてこられた"),
            #   ・$maryがきて母親と対話
            w.plot_develop("$maryはあの日、父親から言われたことを告白する"),
            w.plot_develop("$maryが拾われた子で、しかも$animalとの混血だった"),
            w.plot_develop("将来誹謗中傷されるだろうが、全財産をかけて守ると口にしたという"),
            w.plot_develop("$roydは医者からあまり長くないと言われていた"),
            "実は$jeanと$kailで共謀し、少しずつ弱らせていた",
            w.plot_develop("遺言状にあったのは偽装ではなく、本物の言葉だった"),
            w.plot_turnpoint("$jeanは自分が全てやったのだと告白する"),
            #   ・$kailの豹変
            w.plot_develop("遺産を全て$maryにやると言った途端に殺害計画を思いつき、$maryの部屋に凶器を隠したと"),
            w.plot_develop("凶器となった$gunはバーで知らない男から買った"),
            w.plot_develop("もう黙っているのも限界で、告白したと"),
            w.plot_turnpoint("しかしそれを$kailが否定する"),
            w.plot_resolve("$kailは全て自分が計画したことで、一切$jeanには関係ないと言い"),
            w.plot_turnpoint("$jeanを人質に取った"),
            outline=OUTLINES[4])


def new_resident(w: World):
    return w.episode("新しい住人",
            # NOTE
            #   ・事件の終わり
            w.plot_setup("真犯人を名乗った$kailが$jeanを人質に取った"),
            w.plot_turnpoint("$maryは$transformし、$jeanを守った"),
            w.plot_develop("$kailは待機していた警官に逮捕された"),
            w.plot_develop("しかし$jeanは$maryに対して「それでもお前が嫌いだ」と言った"),
            w.plot_develop("二人が逮捕され、事件は終わった"),
            #   ・事件のその後
            w.plot_resolve("後日、$keanから手紙が来る"),
            w.plot_resolve("手紙には事件が二人の共犯として裁判にかけられる予定になったということ"),
            w.plot_resolve("遺産相続した$maryはその権利を放棄し、邸宅は地元に寄付をした"),
            w.plot_resolve("$maryは$roydの遠い親戚に預けられることになった"),
            w.plot_resolve("$keanはいつの日か刑期を終えて父と$jeanが戻ってくるまで、邸宅の管理をすると"),
            w.plot_turnpoint("そこに訪問客がくる"),
            w.plot_resolve("大きな荷物を持った$maryが現れて、一緒に住むと言い出した"),
            w.plot_resolve("$sherlockは断ったが、$maryのことは任せるようにと$keanに言ったことが書き残されており、仕方なく承諾した"),
            outline=OUTLINES[5])


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
            defence_request(w),
            about_this_case(w),
            interview_of_mary(w),
            family_circumstances(w),
            mother_and_daughter(w),
            new_resident(w),
            outline=ABSTRACT)


