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


def sad_case(w: World):
    return w.episode("悲しい事件",
            # NOTE
            w.plot_setup("$wilsonは毎日のようにやってきて$sherlockに仕事を依頼しようとするが$sherlockは無視して新聞から興味深い事件を探す"),
            w.plot_develop("新聞からある地方の悲しい父親殺しの事件をピックアップし、それについて$sherlockは少ない中から情報を推理して見せる"),
            w.plot_resolve("父親殺し事件の容疑者となった娘の家に勤める使用人$keanが、娘の無実を証明してほしいと依頼に訪れた"),
            outline=OUTLINES[0])


def valley_town(w: World):
    return w.episode("谷の田舎町",
            # NOTE
            w.plot_setup("事件のあった田舎町にやってくる$sherlockと$wilsonは$keanの案内で事件の調査を行う"),
            w.plot_develop("事件現場を確認した後に$royd氏の邸宅で$jean夫人と使用人$kailから話を聞く"),
            w.plot_resolve("$restradeのコネにより何とか$maryと面会する許可が降りた"),
            outline=OUTLINES[1])


def suspect_mary(w: World):
    return w.episode("容疑者$mary",
            # NOTE
            w.plot_setup("警察にやってきた$sherlockはそこで容疑者の$maryと面会をする"),
            w.plot_develop("$maryに$keanから依頼されたと話し、彼女の事件前後の行動について教えてもらう"),
            w.plot_resolve("$sherlockは$maryが$animalで現場に彼女のものと思われる獣の毛が落ちていたことが証拠になっていると言った"),
            outline=OUTLINES[2])


def family_circumstances(w: World):
    return w.episode("家族の事情",
            # NOTE
            w.plot_setup("$sherlockは$wilsonにお使いを頼み、その間に街で$royd氏に関する情報を集める"),
            w.plot_develop("$sherlockは$jeanの育った学校に行き、彼女の小さい頃の話などを聞く。またそこで$kailに関する話も入手する"),
            w.plot_resolve("指紋検出と照合の結果、$gunからは$maryの指紋は検出されなかった"),
            outline=OUTLINES[3])


def marys_confession(w: World):
    return w.episode("$maryの告白",
            #   NOTE
            w.plot_setup("$sherlockは再度$jeanと$kailに話を聞く"),
            w.plot_develop("$jeanは$maryが拾われ子であり$animalだということを知っていたのを隠していたことを告白する"),
            w.plot_resolve("$maryが$transformした"),
            outline=OUTLINES[4])


def real_mind(w: World):
    return w.episode("本当の気持ち",
            # NOTE
            w.plot_setup("$transformした$maryを$kailが殺そうとする"),
            w.plot_develop("$maryにより$jeanが守られたが、彼女は最後まで$maryに対して感謝も愛しているの言葉もかけられないままだった"),
            w.plot_resolve("遺産相続を放棄した$maryは荷物を持って$sherlockの家に押しかけた"),
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
            sad_case(w),
            valley_town(w),
            suspect_mary(w),
            family_circumstances(w),
            marys_confession(w),
            real_mind(w),
            outline=ABSTRACT)


