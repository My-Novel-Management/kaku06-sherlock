# -*- coding: utf-8 -*-
'''
Stage: "孤島"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   魔獣の伝説の残る孤島
#   王国の東側の海にあり、一番近い港まで半日かかる


## scenes
def legendary_island(w: World):
    return w.scene("伝説の残る孤島",
            w.plot_note("観光協会の男に案内され、怪奇事件の謎を解くイベントに連れて行かれる"),
            )


def copse_of_murder(w: World):
    return w.scene("殺人のあった雑木林",
            w.plot_note("男からこの島にはかつて五十名ほどの住人がいたが、魔獣の伝説のせいでみんな逃げ出してしまい、今では城主だけが残っていると"),
            )


def walk_slope_for_castle(w: World):
    return w.scene("古城に続く坂道",
            )


def research_first_murder_case(w: World):
    return w.scene("最初の事件があった場所を調べる",
            w.plot_note("$sherlockは最初の事件があった場所に、$mochに案内してもらった"),
            w.plot_note("そこは城から離れた雑木林"),
            w.plot_note("看板が建てられ、そこが最初の殺害現場だと示されている"),
            w.plot_note("観光資源にしようとしている$mochたち"),
            )


def second_dead(w: World):
    return w.scene("$mochの遺体",
            w.plot_note("しかし$mochは最初の殺害現場で同じように猟奇的に殺害されていた"),
            w.plot_note("$sherlockはそこで$mochの遺体に付着しているあるものを拾う"),
            )


def call_rescue(w: World):
    return w.scene("助けを呼びに",
            w.plot_note("天候が回復し、船舶操作に慣れた男が警察を呼んでくると何人か連れて島を離れる"),
            w.plot_note("その間に$sherlockは$cherryにもう一度城を探させてほしいとお願いする"),
            )
