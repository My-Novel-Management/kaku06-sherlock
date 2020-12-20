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

def sadness_case(w: World):
    return w.episode("悲しい事件",
            "$sherlockの家・リビング",
            w.plot_note("$sherlockは新聞を読んでいた"),
            w.plot_note("$wilsonがやってきていつも何か読んでいるねと言う"),
            w.plot_note("$sherlockは新聞に掲載されていた田舎町の事件を説明する"),
            w.plot_note("殺人事件の多くがこういった「身内の揉め事」だと"),
            w.plot_note("ただ娘が利用した$itemが気になると言う"),
            w.plot_note("$wilsonはそんな事件よりも自分の依頼の方をがんばってほしいと言う"),
            w.plot_note("$wilsonは$sherlockに最近増えている謎の失踪事件についての調査を依頼していた"),
            w.plot_note("$sherlockは調査中とだけ答えて何も言わない"),
            w.plot_note("そこに見知らぬ男の子が訪ねてきて、その事件の容疑者を助けてほしいとお願いされた"),
            )


def country_town(w: World):
    return w.episode("田舎町",
            "$sherlockの家・リビング",
            "回想で$Dartmourを使うかも",
            w.plot_note("$keanはある屋敷に務める使用人の一家の息子だった"),
            w.plot_note("彼は自分が使えている家でその殺人事件があったと言う"),
            w.plot_note("その容疑者になっているのがその家の一人娘だが、彼女は絶対にそんなことをしないと力説する"),
            w.plot_note("なけなしの金を見せて$sherlockに頼む"),
            w.plot_note("$wilsonがそんなはした金で受けるのかと尋ねたが$sherlockは「仕事だよ」と席をたった"),
            "駅",
            w.plot_note("駅から$trainにのって$Dartmourに向かう"),
            "列車内",
            "$Dartmour駅・駅前",
            w.plot_note("そこに迎えにきていた$keanに案内され、まずは屋敷に向かう"),
            "屋敷",
            w.plot_note("屋敷の主となった、残された母親の$jeanに出会う"),
            "同・応接間",
            w.plot_note("$jeanはどうしてこんなことになったのか分からないと嘆く"),
            w.plot_note("ただ使用人の$kailが二人が言い争うのを聞いていて、それが決定的な証拠になっているらしい"),
            w.plot_note("$kailにも出会って話を聞こうとするが、買い出しにいっていて不在だった"),
            w.plot_note("そこに警官が訪れる"),
            w.plot_note("$restradeに話を通してもらい、容疑者と面会できることになった"),
            w.plot_note("容疑者として警察に捕まっている少女に会えることになった"),
            )


def suspect_girl(w: World):
    return w.episode("容疑者の少女",
            "$Dartmour警察",
            w.plot_note("警察署にいき、少女と面会する"),
            w.plot_note("ずっと泣いていて、事情聴取にならないと担当刑事が言っていた"),
            "同・取調室",
            w.plot_note("$sherlockは自分が$keanから依頼をされたと説明し、事情を聞く"),
            w.plot_note("$maryと名乗った少女は、自分がどういう状況だったか話す"),
            w.plot_note("事件のあった日、その朝に父親（被害者）から北の沼地に来るように言われた"),
            w.plot_note("父親は大切な話があるから、必ず一人で来るようにと注意した"),
            w.plot_note("時間になり、一人ででかけていくと、そこで待っていた父と少し話をして、それからすぐ別れた"),
            w.plot_note("一人でそのまま夜道を家まで帰った"),
            w.plot_note("翌朝になるまで部屋からは出ていない"),
            w.plot_note("父親は夜の間に殺されていて、かえってこなかったから捜索願が出され、沼地で発見された"),
            w.plot_note("その場に残されていた凶器のナイフが$maryの部屋で発見されたことから、彼女が容疑者として逮捕された"),
            w.plot_note("でも本当にそれだけで、言い争っていたのを聞いたという$kailがよく分からないという"),
            w.plot_note("父親は一人で待っていて、自分と父親以外その場にはいなかった"),
            w.plot_note("場所は近くに高いもの、建物のない沼地で、人影もなかったと"),
            w.plot_note("自分はやってないし、父親のことを恨んだりもしていないといって、$sherlockに助けを求めた"),
            "同・外",
            w.plot_note("面会を終えた$sherlockは$wilsonに彼女が$animalであると告げた"),
            )


def her_mother(w: World):
    return w.episode("彼女の母親",
            "宿・自室",
            w.plot_note("$sherlockは一晩ホテルに泊まり、その間に$maryの家について調べる"),
            "屋敷",
            w.plot_note("翌朝、再び屋敷を訪れた"),
            "同・玄関",
            w.plot_note("$sherlockは$jeanに会いたいといったが使用人の$kailが体調を崩しているから無理だと返す"),
            w.plot_note("$maryに関しての大事な話があると言う"),
            "同・寝室",
            w.plot_note("奥に通されて、顔色の悪い$jeanと出会う"),
            w.plot_note("$sherlockは$jeanに$maryが$animalだと知っているか、と尋ねる"),
            w.plot_note("$jeanは答えなかったことから、$sherlockは事実に気づいた"),
            "同・リビング",
            w.plot_note("それで$jeanに事件当日のアリバイを尋ねる"),
            w.plot_note("彼女はその日は一度も外出してなくて、体調を崩して自分の部屋で寝込んでいた"),
            w.plot_note("それは使用人の$kailも$keanも見ている、証言している"),
            w.plot_note("$sherlockは警察が$maryが獣人だから現場に残されていた獣人の毛が彼女のもので、証拠だとしていると"),
            w.plot_note("そこに$maryが連れてこられた"),
            )


def real_murder(w: World):
    return w.episode("真犯人",
            "同・リビング",
            w.plot_note("$maryのことを$jeanは「お前のせいでいつも無茶苦茶になる」と言う"),
            w.plot_note("$maryは自分が父親を殺していないことを訴えるが、母親は二人があまり仲良くなかったと言う"),
            w.plot_note("その理由は$maryが拾った子供だから"),
            w.plot_note("二人にはずっと子供がいなかった"),
            w.plot_note("それでも$jeanはいいと思っていたが$roydはそうじゃなかった"),
            w.plot_note("ある日、$roydが赤ん坊を抱きかかえて帰ってきて「これが俺たちの子供だ」と見せた。それが$maryだった"),
            w.plot_note("つまり自分たちの子ではない"),
            w.plot_note("それがずっと引っかかっていたという"),
            w.plot_note("最初はよかったが、大きくなるにつれ、自分の子供ではないことが愛せない障害になっていた"),
            w.plot_note("それをいつも自分にこぼしていたと$jeanは証言する"),
            w.plot_note("$keanはなぜそのことを警察に言わなかったのかと尋ねる"),
            w.plot_note("$jeanは自分の最低限の愛情だと弁解する"),
            w.plot_note("なぜなら$jeanは$maryに関するある秘密を知っているからだ"),
            w.plot_note("$sherlockはそれを口にする。彼女は$animalだと"),
            w.plot_note("$maryが獣化した"),
            )


def animal_girl(w: World):
    return w.episode("獣の少女",
            "同・リビング",
            w.plot_note("$kailは壁の斧を手に取り、$maryに襲いかかる"),
            w.plot_note("$jeanを守ろうとしたように見えたが、$sherlockは彼女は何もしないから大丈夫だと立ちふさがる"),
            w.plot_note("$kailは自分たちを陥れようとしていると$sherlockに言う"),
            w.plot_note("$sherlockは事件の真相について語る"),
            w.plot_note("$animlaは自分で獣化できるはずだが、$maryの場合は感情が制御できなくなることにより獣化するのが分かったと"),
            w.plot_note("現場では父親から娘に「拾った子供」という事実が告げられた"),
            w.plot_note("「それで獣化して襲ったんだろ」と$kailが言う"),
            w.plot_note("しかし$sherlockは凶器を使っていると指摘"),
            w.plot_note("凶器が自分の部屋から見つかっていることからも、誰かが仕組んだ可能性を示唆する"),
            w.plot_note("更に備品管理は使用人である$kailたちが行っていて、新しくナイフを購入したのを$keanから聞いている"),
            w.plot_note("最初は$jeanの可能性を疑ったが、$kailが真犯人だと$sherlockは指摘する"),
            w.plot_note("$kailは全部自分が仕組んだことだと$cherryを人質にとったが、$cherryはもういいと諦めて自白した"),
            w.plot_note("そこに用意していた警察が突入する"),
            w.plot_note("$kailは$cherryを殺して自分も死のうとするが、それを$maryが阻止する"),
            w.plot_note("$cherryは自分を守った$maryのことを「それでもお前のことを好きになれない」と言って、警察に逮捕された"),
            )


def living_girl(w: World):
    return w.episode("新しい同居人",
            "$sherlockの家・居間",
            w.plot_note("事件は犯人の$kailが逮捕され、共犯としての$cherryも逮捕され、幕を下ろした"),
            w.plot_note("財産はすべて$maryに相続されることになったが、彼女は全てを放棄して地元に寄付したと$keanから聞いた"),
            w.plot_note("彼からの手紙には自分が残りを管理して、父親と$jeanが罪を償って戻ってくるのを待っていると"),
            w.plot_note("$maryのその後については、知人のところに預けられることになったとだけ書かれていた"),
            w.plot_note("そこに訪問者が現れる"),
            w.plot_note("大きな荷物を持った$maryだった"),
            w.plot_note("彼女は$sherlockに世話になった恩を返したいと、一緒に暮らすと言い出す"),
            w.plot_note("$sherlockは断るが、彼女は言うことをきかず、勝手に部屋を決めて、荷物を広げる"),
            w.plot_note("$maryが$sherlockたちの家に居候することになった"),
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
            sadness_case(w),
            country_town(w),
            suspect_girl(w),
            her_mother(w),
            real_murder(w),
            animal_girl(w),
            living_girl(w),
            )


