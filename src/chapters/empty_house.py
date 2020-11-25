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


# Episode
def lookfor_sherlock(w: World):
    return w.episode("$sherlockを探して",
            "$sherlockの家",
            w.plot_note("$maryたちは$sherlockが生きていると思って捜索を続けていた"),
            w.plot_note("しかし何の情報もなく、ただ時間だけが過ぎていく"),
            w.plot_note("家を失い、$wilsonの住まいに居候していた$maryたち"),
            w.plot_note("$wilsonは忙しそうに外に出ていることが増えた"),
            w.plot_note("$maryは$sherlockの手紙にヒントはないかと考えるが、何も見つからない"),
            w.plot_note("だが$limeはそこに$sherlockが生きているという証拠を見つけた"),
            w.plot_note("そこに$wilsonが戻ってくる"),
            w.plot_note("$wilsonは「$sherlockに似た人間を見かけた」という情報を聞いたと話した"),
            )


def empty_house(w: World):
    return w.episode("空き家の冒険",
            "スラム街",
            "空き家・前",
            w.plot_note("$wilsonに連れられて$maryと$limeは$sherlockに似た人を見たという空き家にやってくる"),
            w.plot_note("バラックが並ぶスラム街にあるたくさんの空き家の一つ"),
            w.plot_note("見たというホームレスは夜にその空き家だけ明かりがつくのが妙だと思って監視していたと証言する"),
            w.plot_note("一度空き家の中を探索するが、確かに人が暮らしている証拠が見つかる"),
            w.plot_note("$maryたちは夜になるのを待った"),
            w.plot_note("空き家に人影が入り、そこで明かりが灯る"),
            w.plot_note("明かりの人影は読書しているように見えた"),
            w.plot_note("もう一人の人間もいるようで、二人で会話をしている風でもある"),
            w.plot_note("しばらくするとその明かりは消えてしまう"),
            w.plot_note("誰も出てこないので、翌朝、$maryたちはその空き家に訪問してみる"),
            "空き家・中",
            w.plot_note("呼びかけても応答はなく、奥に入っていく"),
            w.plot_note("空き家の中で殺された男性の死体を発見した"),
            w.plot_note("それは先月から行方不明の神官だった"),
            w.plot_note("現場からは$sherlockの愛用していた手袋が発見される"),
            w.plot_note("警察は$sherlockを重要参考人として指名手配する"),
            )


def fake_reunion(w: World):
    return w.episode("偽りの再会",
            "警察署",
            w.plot_note("警察の事情聴取を受けた$maryたち"),
            "$sherlockの家",
            w.plot_note("一旦家に戻り、犯人にされてしまった$sherlockについて考える"),
            w.plot_note("$wilsonは$sherlockが$moriano一味に騙されたというのだが"),
            w.plot_note("もう一度あの空き家を訪れる"),
            "空き家",
            w.plot_note("そこで$wilsonは抜け道を発見する"),
            "地下道",
            w.plot_note("地下道に繋がっていて、そこを進んでいく"),
            "廃工場",
            w.plot_note("その地下道を抜けた先に廃工場があり、その中に失踪した多くの人間の遺体が放置されていた"),
            w.plot_note("そこで$sherlockと再会する"),
            w.plot_note("$sherlockは自分の正体が「$moriano」だと告白する"),
            w.plot_note("実は二重人格で表は正義感を振りかざしながら裏では犯罪者として振る舞うことに快感を覚えるのだと"),
            w.plot_note("信じられない$maryは$sherlockが薬でおかしくなっているのだと考えた"),
            w.plot_note("獣化し、囲む敵と戦って逃げ出そうとする"),
            w.plot_note("しかし$wilsonを人質にとられてしまい、断念"),
            w.plot_note("おとなしく捕まった"),
            )


def in_the_darkness(w: World):
    return w.episode("暗闇の中で",
            w.plot_note("目覚めると真っ暗な中、縛られた状態で背中合わせだった$maryと$lime"),
            w.plot_note("妙な音が聞こえる"),
            w.plot_note("ぱっと明るくなり、ここがどこかの廃工場の中だと分かる"),
            w.plot_note("明るくなったのは炎だった"),
            w.plot_note("火事で事故死に見せかけて殺すつもりだと分かる"),
            w.plot_note("$maryは獣化して抜け出そうとするが、月の光が遮光されていて変身できない"),
            w.plot_note("$limeは仕込みナイフを使って縄を切ろうとするが、特殊な金属の縄で切れない"),
            w.plot_note("八方塞がりの中でも$sherlockの言葉を思い出して推理する"),
            w.plot_note("$wilsonはここにはいない"),
            w.plot_note("あの$sherlockが本物の$sherlockとは利き腕が違っていたことを思い出す"),
            w.plot_note("偽$sherlockがなぜ自分たちを陥れ、ここで火事で殺そうとしているのか考えると、全てを$sherlockにかぶせたい人間がいることに気づく"),
            w.plot_note("$maryはなんとか足だけ抜け出し、部屋から出ようとする"),
            w.plot_note("そこで闇から現れる銃口が自分を狙っていることに気づく"),
            w.plot_note("これが空き家の殺人の正体だった"),
            w.plot_note("$maryは撃たれそうになる$limeを庇って撃たれる"),
            )


def his_alive(w: World):
    return w.episode("$sherlockは生きている",
            w.plot_note("発射した弾が何かにはじかれる"),
            w.plot_note("突入してきたのは一度見たことのあるホームレスの一人だった"),
            w.plot_note("彼が$maryたちを助け出してくれる"),
            w.plot_note("しかし警戒する$maryと$lime"),
            w.plot_note("ただ$maryはそのホームレスにどこか懐かしい匂いを感じる"),
            w.plot_note("彼は「$sherlockは生きている」と言い残して去っていった"),
            w.plot_note("家に戻ると$wilsonがいて、ひどい怪我を負っていたが、無事に逃げ出したと言う"),
            w.plot_note("$maryは自分たちを助けた男が$sherlockの生存を言っていたと伝える"),
            w.plot_note("$wilsonはそのホームレスのことを教えてくれと頼む"),
            w.plot_note("$maryたちにここで休むようにいい、$wilsonは$sherlockを探しに出ていった"),
            w.plot_note("そこに$wilsonが指名手配されたと$restradeがやってくる"),
            )


def truth(w: World):
    return w.episode("真実",
            w.plot_note("$maryたちは$ignesたち少年探偵団に連れられて彼らの隠れ家を訪れる"),
            w.plot_note("そこは$sherlockがもしものために彼らに準備させていた場所だった"),
            w.plot_note("多くの資料が集まり、武器なども収納されている"),
            w.plot_note("そこに$sherlockはいた。大怪我を負っていたが大丈夫だと言う"),
            w.plot_note("そこで$sherlockは自分がこの半年ほどの間にどうしていたのかを語る"),
            w.plot_note("そして$wilsonが偽物で、すべての黒幕だと教えた"),
            w.plot_note("そこに警察から連絡が入る"),
            w.plot_note("$sherlockの指示で監視していた施設が突如爆発したらしい"),
            w.plot_note("$sherlockとともに宗教団体の施設を探す"),
            w.plot_note("その地下で儀式が行われた跡を発見する"),
            w.plot_note("儀式が失敗したことはわかったが、$wilsonはいなかった"),
            )


def strange_end(w: World):
    return w.episode("奇妙な結末",
            w.plot_note("$sherlockは$maryたちに偽$wilsonが$bossの復活のために全てを準備していたのだと語る"),
            w.plot_note("そして儀式に不可欠だったのが$heroの心臓であり、それを探してずっと$heroの血縁の人間を殺しまわっていたと"),
            w.plot_note("どの心臓も合わなかったらしく、最後に白羽の矢がたったのが$sherlockで、ダミーの$morianoにより誘い出して殺そうとしたと"),
            w.plot_note("しかし全てが失敗に終わり、$stoneは粉々になって発見された"),
            w.plot_note("$wilsonは機会を伺って潜伏しているだろうが、また自分を殺しにくると伝える"),
            w.plot_note("だが警察は$wilsonの遺体を空き家で見つける"),
            w.plot_note("同じ手法だったが、それは遠隔操作$gunによる自殺だった"),
            w.plot_note("その後、警察の捜査により$sherlockが調べ上げた偽$wilsonが協力をしたと思われる人物リストを全て調査したが、全員失踪あるいは自殺、事故死していた"),
            w.plot_note("$sherlockは$wilsonの住居から何か情報がないかと探す"),
            w.plot_note("しかし偽$wilsonは何もかも綺麗に処分をしていた"),
            w.plot_note("ただ一つだけ、この世界のものとは思えないものを発見する"),
            w.plot_note("それは$wilsonが愛用していた謎の端末だった"),
            w.plot_note("$sherlockは確信するのだ。まだ偽$wilsonは生きていると"),
            )


# Chapter
def main(w: World):
    return w.chapter(TITLES[7],
            w.plot_setup("$maryたちは$sherlockが生きていると信じて捜索を続けていた"),
            w.plot_turnpoint("$sherlockに似た人を空き家で見かけたという情報が入る"),
            w.plot_develop("空き家の調査を行い、そこで身元不明の遺体を発見する"),
            w.plot_turnpoint("空き家の遺体の犯人が$sherlockとして指名手配される"),
            w.plot_develop("$sherlockから$maryたちに秘密の連絡がある"),
            w.plot_turnpoint("$sherlock（偽物）に捕まえられ、$maryたちは監禁される"),
            w.plot_develop("$maryたちは暗闇に閉じ込められ、同じ手法で殺されそうになる"),
            w.plot_turnpoint("刑事の一人が改造$gunを使って殺そうとしたところを逮捕される"),
            w.plot_develop("助け出された$maryたちは$sherlockが生きていると$restradeから知らされる"),
            w.plot_turnpoint("$wilsonが指名手配される"),
            w.plot_develop("$sherlockと再会し、全ての事情を聞く"),
            w.plot_turnpoint("$wilsonが偽物だと$sherlockが教える"),
            w.plot_resolve("偽$wilsonが遺体となって発見された"),
            #
            lookfor_sherlock(w),
            empty_house(w),
            fake_reunion(w),
            his_alive(w),
            truth(w),
            strange_end(w),
            )


