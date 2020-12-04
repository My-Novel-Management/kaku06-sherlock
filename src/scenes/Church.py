# -*- coding: utf-8 -*-
'''
Stage: "教会"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   教会については、こちらを利用する


TEMPLE = "WestminsterTemple"
HALL = "WestminsterTempleHall"
SUBWAY = "WestminsterTempleSubway"
RITUAL = "WestminsterTempleRitualRoom"


# Scenes


def mystery_cult(w: World):
    return w.scene("神秘教団",
            w.plot_note("$sherlockは彼女に接触しその技法を教えた$cultXのことをマークした"),
            w.plot_note("そこに情報がもたらされる"),
            )


## in EmptyHouse
def cult_facility(w: World):
    shal, mary, lime = w.get("sherlock"), w.get("mary"), w.get("lime")
    pat = w.get("patson")
    return w.scene("教団施設",
            w.change_camera("sherlock"),
            w.change_stage(TEMPLE),
            w.change_time("afternoon"),
            w.plot_note("$sherlockとともに宗教団体の施設を探す"),
            shal.come("閉鎖中の$MinsterTempleにやってくる"),
            mary.come(),
            lime.come(),
            pat.be(),
            pat.talk("こっちです！"),
            pat.do("$sherlockの指示で先に到着していた$Sが手をあげて合図する"),
            shal.do("$patsonの他にも数名の警官がいて、管理者に脇のドアを開けてもらい中に入っていく"),
            )


def lookfor_ritual_place(w: World):
    shal, mary, lime = w.get("sherlock"), w.get("mary"), w.get("lime")
    pat = w.get("patson")
    return w.scene("儀式の場所を探せ",
            w.change_stage(HALL),
            shal.be(),
            mary.be(),
            lime.be(),
            pat.be(),
            mary.do("初めて入った聖堂の大ホールの天井いっぱいのステンドグラスに驚く$S"),
            mary.talk("すごーい"),
            shal.talk("今改装中で、覆いがされているところは修繕中だ",
                "ここが建てられたのは八百年ほど前になるからね。ずいぶん古い"),
            shal.talk("知っていると思うが、ここは歴代の王や王族、大司教たちの墓が作られていて、目に見える箱は全て彼らの墓なんだ"),
            shal.do("沢山の横長の机と椅子、それに前にはパイプオルガンも準備されている"),
            shal.do("$Sはどこかで$boss復活の儀式を行うはずだという"),
            shal.do("その場所は光（日光）が届かない場所が相応しいことから、必ず地下室を選ぶはずだと"),
            shal.do("みんなで手分けして地下への入り口を探す"),
            mary.do("$Sが一番後ろにマークがつけられている墓を見つける"),
            shal.talk("それは$cultXのマークだね"),
            shal.talk("名前は……そうか。これは$bossのアナグラムになっている"),
            shal.do("墓を開けて調べる$S"),
            pat.do("驚いてやめさせようとするが、$sherlockはきかない"),
            shal.talk("あった"),
            shal.do("墓を動かすとその下に隠しはしごが現れた"),
            )


def goto_ritual_room(w: World):
    shal, mary, lime = w.get("sherlock"), w.get("mary"), w.get("lime")
    pat = w.get("patson")
    return w.scene("儀式の間に向かう",
            w.change_stage(SUBWAY),
            shal.come(),
            shal.do("はしごを降りて、地下道に出る"),
            shal.do("かなり昔に整備されたものらしく、ランプが置けるようになっている"),
            shal.do("ライターを明かりにしながら先に進む"),
            mary.come(),
            mary.do("$Sは怖がりながらも夜目がきくからと、先に歩いていく"),
            shal.talk("気をつけるんだ"),
            shal.talk("ただまだ儀式は終わっていないはずだ",
                "もし終わっていれば世界は闇に閉ざされてしまっている"),
            shal.talk("文献で見た話だけれどね"),
            mary.do("うん、と答えて歩いていく"),
            lime.come(),
            lime.do("$Sが後ろから$maryの肩に手をおいて、自分が守ると意思表示をする"),
            mary.talk("あっ"),
            mary.do("薄い光が見える", "行くての先にドアがあって、少しだけ開いているのだ"),
            )


def basement_hall(w: World):
    shal, mary, lime = w.get("sherlock"), w.get("mary"), w.get("lime")
    pat = w.get("patson")
    rest = w.get("restrade")
    return w.scene("儀式の間",
            w.change_stage(RITUAL),
            w.plot_note("その地下で儀式が行われた跡を発見する"),
            w.plot_note("儀式が失敗したことはわかったが、$wilsonはいなかった"),
            shal.come(),
            mary.come(),
            lime.come(),
            pat.come(),
            mary.do("扉をあけて中に入る$S"),
            shal.do("$Sも続く"),
            mary.talk("ここって"),
            shal.do("地下には広大な部屋が広がっていた"),
            shal.do("中央に祭壇が作られ、そこには台座と、それを取り囲むようにして何かを捧げるための器が置かれている"),
            shal.do("ただ何がおこったのか、台座を中心としてあたり一面に血が飛び散っていて、むわっと不思議な臭気が漂っている"),
            shal.do("やってきた警官たちも口や鼻を押さえて動けない"),
            shal.talk("失敗したのか"),
            shal.talk("$Sはその光景を見て悟った"),
            shal.do("一人だけ先に台座に向かう"),
            pat.talk("$sherlockさん！"),
            pat.do("$Sもあとを追う"),
            shal.do("$Sは$patsonに状況説明を行う"),
            pat.talk("これは？"),
            shal.talk("儀式が失敗したんだ", "$meの心臓を手に入れ残ったやつらは別の心臓、本物の$ailyの心臓を使い、儀式を敢行した",
                "けれど彼女には$heroの資格がなかったんだろうね"),
            shal.talk("$bossを復活させるために必要なものは四つの$stoneと純粋な$heroの血と心臓だ",
                "ただ彼らには彼女が本当に$heroの純血の血筋であるかどうかを知らなかったんだ"),
            shal.talk("これを見てほしい"),
            shal.do("$Sは$jackからもらった$ailyの出生証明書を見せる"),
            shal.do("そこには父親側こそ王室の人間だったが、母親は無名といってもいい、水商売の女と書かれていた"),
            shal.talk("かわいそうなことに、彼女は最後まで自分を直系の$heroだと信じたまま、彼らに殺されたんだ"),
            shal.talk("$heroの血は引いているから$compassに反応は出ただろうが、純度まではわからない"),
            )


def betray_man(w: World):
    shal, mary, lime = w.get("sherlock"), w.get("mary"), w.get("lime")
    pat = w.get("patson")
    rest = w.get("restrade")
    return w.scene("裏切りの男",
            shal.do("$Sはここにはもう何もないと思って立ち去ろうとしたが"),
            pat.do("$Sが$gunを取り出して、それで警官を撃つ"),
            pat.do("$Sが$maryを人質に取る"),
            pat.talk("動かないでもらおうか"),
            pat.do("今までに見せた表情とは違った顔を見せる$S"),
            mary.talk("なんで？　$k_pat何してるん？"),
            pat.talk("お嬢ちゃんでは"),
            # TODO
            )


def unexpected_end(w: World):
    shal, mary, lime = w.get("sherlock"), w.get("mary"), w.get("lime")
    rest = w.get("restrade")
    return w.scene("意外な最後",
            w.change_camera("mary"),
            w.change_stage(TEMPLE),
            w.plot_note("$sherlockは$maryたちに偽$wilsonが$bossの復活のために全てを準備していたのだと語る"),
            w.plot_note("そして儀式に不可欠だったのが$heroの心臓であり、それを探してずっと$heroの血縁の人間を殺しまわっていたと"),
            w.plot_note("どの心臓も合わなかったらしく、最後に白羽の矢がたったのが$sherlockで、ダミーの$morianoにより誘い出して殺そうとしたと"),
            w.plot_note("しかし全てが失敗に終わり、$stoneは粉々になって発見された"),
            w.plot_note("$wilsonは機会を伺って潜伏しているだろうが、また自分を殺しにくると伝える"),
            w.plot_note("だが警察は$wilsonの遺体を空き家で見つける"),
            shal.come("$Sとともに教会にやってくる"),
            mary.come(),
            lime.come(),
            rest.be(),
            shal.do("$Xeno教徒の中央教会にやってきたが、そこの隣に建っている倉庫のような場所"),
            shal.do("$Sはこの施設の下に儀式の場所が作られているという"),
            shal.do("$restradeと合流し、警察とともにそこに突入する"),
            shal.do("階段があり、降りていく"),
            shal.do("そこは五十人ほどが収容できる空間が作られていた"),
            shal.do("祭壇が作られ、その中心に失踪した大司教の死体が置かれていた"),
            shal.do("$Sは$gunによる殺人だと見抜く"),
            shal.do("そこには４つの$stoneと一つの心臓を捧げるための祭壇の設備があったが、$stoneは砕け、心臓を捧げるはずの場所には血だまりがあっただけ"),
            shal.do("他にも多くの使者たちの死体が転がっていた"),
            shal.do("それを見て$sherlockは$wilsonがいないことに気づく"),
            )
