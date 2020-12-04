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
    rest = w.get("restrade")
    return w.scene("教団施設",
            w.change_camera("sherlock"),
            w.change_stage(TEMPLE),
            w.change_time("afternoon"),
            w.plot_note("$sherlockとともに宗教団体の施設を探す"),
            shal.come("閉鎖中の$MinsterTempleにやってくる"),
            mary.come(),
            lime.come(),
            )


def basement_hall(w: World):
    shal, mary, lime = w.get("sherlock"), w.get("mary"), w.get("lime")
    rest = w.get("restrade")
    return w.scene("地下のホールで",
            w.plot_note("その地下で儀式が行われた跡を発見する"),
            w.plot_note("儀式が失敗したことはわかったが、$wilsonはいなかった"),
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
