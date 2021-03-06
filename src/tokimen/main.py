# -*- coding: utf-8 -*-
"""Chapter: 時らーめん
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## local files


## define alias
W = Writer
_ = W.getWho()

## scenes
def sc_makura(w: World):
    teller = W(w.teller)
    return w.scene("枕として",
            teller.do("日本人というのは昔も今も麺類に目がないって言いますね",
                "でも麺類のめを抜いたら”んるい”って、何だか訳わかんねえ言葉になってしまいます"),
            _.do("え？　$meは誰だって？",
                "江戸っこはこまけぇこたぁ気にしないもんですぜ？",
                "はあ、あなたは江戸っこじゃない？",
                "まあまあ、ここはまず白湯でも飲んで落ち着いてくだせえ"),
            _.do("ああ、$meは蕎麦湯です",
                "こう言っちゃなんですが$me、蕎麦派なんですよ",
                "でも今日の昼はラーメンにしましたよ",
                "何たってこれからラーメンの話をするんですからね",
                "ここでスパゲティやハンバーグ定食くってたんじゃ話になりません"),
            _.do("そういや蕎麦や饂飩が今みたいに麺の形状になったのは何でも江戸時代あたりらしいですね",
                "落語にも時そばとか時うどんとか出てきますが、当時から安くてうまい麺類は庶民の味方だった訳です",
                "ただこの時そばや時うどんって落語では、時間の数え方をうまく使って店主を騙す訳ですが、現代では今なん時だい？　って尋ねられてすぐに答えられる店主なんざいませんから、酢豚のパイナップルくらい使えない噺なんですよ"),
            _.do("え？　酢豚のパイナップルうまいじゃねえかって？　そりゃあトンでもねえ意見だよ、旦那――酢ブタだけにってね"),
            _.do("何か今日は寒いみたいなんで、ここらで温かいラーメンでも食べますかね、お客さん"),
            camera=w.teller,
            area=w.Tokyo,
            stage=w.on_street,
            day=w.in_current, time=w.at_afternoon,
            )

def sc_at_ramenshop(w: World):
    ani, hati = W(w.aniki), W(w.hati)
    sh = W(w.shopper)
    return w.scene("ラーメン店にて",
            w.symbol("　　　　◆"),
            ani.be(),
            hati.be(),
            ani.explain("昼下がりのラーメン屋の店内、奥のキッチンで丼を片付ける音が響く",
                "そこに麺をすすり上げる音を重ねる二人の若い衆はカウンターに横並びで座り、それぞれ額に汗をかいていた", "&"),
            ani.do("細面の男はふうふうとやりながら、湯気を上げる中華麺を口に運ぶ",
                "割り箸の使い方は手慣れたもので、一旦レンゲに乗せた麺は綺麗に口に吸い込まれた"),
            hati.talk("兄貴兄貴！"),
            hati.do("その右側に座るでっぷりとした腹を揺らして喜んでいる男は、口周りにナルトを付けたままで喋りかける"),
            hati.talk("このラーメンめちゃくちゃうまいっスよ！"),
            ani.talk("おうよハチ",
                "食べロウが激安だって紹介してたからな！"),
            hati.talk("ただ兄貴、さっきからこう口のあたりがヒリヒリするんスけど"),
            ani.talk("激辛食堂だからな"),
            ani.do("壁の並ぶメニューにはやたら『激辛』の赤字が目立つ"),
            ani.talk("どうだお前も追い七味？　七味はいくら入れてもタダだ。どんどん入れろ"),
            ani.do("そう言って兄貴は目の前の赤い缶を手に取り、既に赤く染まっているスープの上に更に赤い粉を浮かべた"),
            hati.talk("い、いや、流石に七味はもういいっス。オリーブオイルじゃねえし"),
            ani.talk("おいハチ。お前いつからオリーブオイルなんてセレブなもん使ってんだよ。金持ちになったらなら俺に奢れ"),
            hati.talk("何言ってんスか。今の手持ちは三十二円しかないッス"),
            ani.talk("お前それじゃあブラックサンダーも買えないだろ？"),
            hati.talk("え！？　いつのまに三十二円じゃなくなったんスか！"),
            ani.talk("ハチ", "お前はいつの時代を生きてんだ？", "昭和か？", "平成か？"),
            hati.talk("れ、令和っス"),
            ani.do("兄貴が睨むと「すんません」と$hatiは頭を下げた"),
            ani.talk("しっかし$hatiよ、世間は何とかミクスで景気よさげなことを言ってた癖に、俺たちはずっと不景気なままだと思わねえか？"),
            hati.talk("ミックスケーキをデザートでお願いします！"),
            ani.talk("おいハチ。何勝手に頼んでんだよ！"),
            hati.talk("あれ？　兄貴が欲しかったんじゃないんスか？"),
            ani.talk("俺はケーキよりまんじゅうの方が恐いんだよ！"),
            hati.talk("恐いならケーキでいいッスよね？　あ、ケーキもう一つ追加で"),
            ani.talk("お前はほんとにトンチキチンな野郎だ。まんじゅうが恐いっつったら、普通はまんじゅう食わせようとするだろうが？　それが江戸っこの常識だ"),
            hati.talk("へえ。ところで兄貴はいつから江戸っこに？　確か秋田の生まれじゃ"),
            ani.talk("おめ何いっでんだ！　おらがいつ秋田さ方言話しただ！"),
            hati.talk("あー、姉ちゃんそのケーキこっちね。それとあんみつも追加で"),
            ani.do("$hatiは目の前の空っぽにした丼をポニーテールの店員に渡しながら追加注文し、水のお替りを貰っている"),
            ani.talk("はあ。あのよ、ハチ"),
            hati.talk("なんスか？"),
            ani.talk("そのケーキとあんみつの代金、誰が支払うんでい？"),
            hati.talk("兄貴です"),
            ani.talk("ちょっとよく聴こえなかったんだがもういっぺん言ってみれくれるか？"),
            hati.talk("兄貴で"),
            ani.do("即座に同じ返答を口にした$hatiに右の拳を振り上げて見せる"),
            hati.talk("だってぇ"),
            ani.talk("おめえはあいかわらずドテスカテンだなあ"),
            hati.talk("兄貴ぃー。おら、いつだって兄貴だけを頼って生きてんスから"),
            ani.talk("だから金を出せ、と？"),
            hati.talk("へえ"),
            hati.do("$Sは満面の笑みでそう言った"),
            ani.talk("へえ、じゃねえよ！　こんちきしょう。俺もお前に奢ってやりたいのは山々なんだが、あいにくとな……手持ちがねえ。ほら"),
            hati.talk("ひぃ、ふぅ、みぃ……兄貴。おらがこんだけ出しますから"),
            ani.talk("ハチよ、おめえ……三十二円じゃ何も食えんだろが！"),
            hati.talk("で、兄貴はいくら持ってんです？"),
            ani.talk("百円玉で千四百円……だな"),
            hati.talk("レシートはっと……千五百四十円。兄貴。ここは必殺の土下座で何とかこらえてもらいやしょう"),
            ani.talk("そうだな……いや、ハチ。ここは俺に考えがある"),
            ani.explain("そう言って兄貴はレシートを持ってレジに向かった"),
            ani.talk("お勘定を"),
            sh.be("カウンターの奥で作業をしていたスキンヘッドの店主は低い声で「はいよ」と答えると、", "&"),
            sh.do("二人を一瞥してからレジに立つ"),
            sh.talk("ありがとうございました。こちら、お預かりします、ね？"),
            sh.do("確認するように$anikiたちを見やり、それから領収書を手に取って逞しい指で器用にレジを打ち込む"),
            ani.talk("おう。なかなかうまかったな。特に最後に食べたあのスウィーツな"),
            sh.talk("あん、みつ……でございますか？"),
            hati.talk("兄貴兄貴", "&"),
            hati.talk("ぜってぇこの店主人何人かやってますって"),
            ani.do("足を蹴飛ばして後ろの$hatiを黙らせる"),
            ani.talk("とにかく美味かったよ", "ごちそうさま"),
            sh.talk("いえいえ。お会計ですが、合計で……千五百四十円でございます"),
            ani.do("店主の方は特に気にした素振りもなく金額を伝えるが、",
                    "その丁寧な口調が彼の強面の怖さをより引き立てている",
                    "$Sはここが勝負だとばかりに気合を入れると、汗ばむ手を懐で拭ってこう切り出した"),
            ani.talk("えらく安いな。おし、ちょっと細かいからよーく数えてくれよ"),
            ani.do("へえ、と返事をした店主の前で財布から小銭を取り出して見せる"),
            ani.talk("まずは一、二、三、四十円"),
            sh.talk("はい"),
            ani.talk("続いて百円玉だ。こまけぇけど数えてくれよ"),
            sh.talk("合点です"),
            ani.talk("えー……いくぞ"),
            sh.talk("ほいきた"),
            hati.talk("兄貴。えらく威勢のいい店主ですね"),
            ani.talk("だからお前は黙ってやがれ。それじゃあ、いきますね"),
            sh.talk("いつでもどうぞ"),
            ani.talk("一つ、二つ、三つ、四つ……ふぅ……五つ、六つ、七つ、八つ……ところで今なんどきだい？"),
            sh.talk("九つで"),
            ani.talk("十、十一、十二、十三、十四、十五。それじゃあな"),
            ani.do("兄貴たち颯爽と外に出ていく"),
            ani.talk("もうこんなことごめんだぞ。おい"),
            hati.talk("しかしあの店主。よく今がなんどきか答えられたよな。$meには無理だ"),
            ani.talk("おめえはバカだからな"),
            hati.talk("それって褒めてんスか？　あははは"),
            ani.do("二人は安堵の笑顔を向け合ったが、$Sは軽くなった財布を仕舞うと明日から真面目に仕事を探そうと心に誓ったのだった"),
            camera=w.aniki,
            stage=w.on_ramen,
            )

def sc_at_foot_stall(w: World):
    hati = W(w.hati)
    god = W(w.god)
    return w.scene("屋台にて",
            w.symbol("　　　　◆"),
            hati.be(),
            god.be(),
            hati.explain("それから数日後、兄貴は行方不明になった"),
            hati.do("スマホに今日も連絡がないことに溜息をつきながら、$Sは薄暗い路地を歩いていた"),
            hati.talk("はぁ……。兄貴、どこいっちまったんだろう。仕事はないし、金は落ちてないし、腹はすくしで大変だよ"),
            hati.do("その暗がりで赤い提灯が一つだけ目に入る"),
            hati.talk("お、こんなとこに新しい店が出来てるな。地獄ラーメン？　こいつぁうまそうだ"),
            hati.do("$Sは空腹の虫を聞いて一つ思案する",
                "前に兄貴がしたみたいに、うまくちょろまかせれば安く食べられるんじゃないか、と思いつき、意気揚々と暖簾を潜った"),
            hati.talk("おうごめんよ……なんだ、店員も客もいないッスよ？　おーい。おーいおいおいおーい……って、なんだかオラが泣いてるみてえッスね"),
            hati.do("電気も点いてない店内で、蝋燭の火が灯されたテーブルの上に一枚だけメモが置いてある"),
            hati.talk("何だこりゃ。何か書いてあるぞ……ふむふむ。まずは靴を脱いで奥の間へお進み下さい。ほお。こりゃこりゃ丁寧なこったな"),
            hati.do("座敷に上がるにはその方がいいだろうと、$Sは靴を脱いで、注意深く畳に足を乗せた"),
            hati.talk("奥ってのはあっちか？"),
            hati.do("薄明かりが障子越しに見える", "&"),
            hati.do("けれど戸を開けた先はまた真っ暗だ", "部屋の隅に蝋燭が一本だけ立てられ、そこの壁には『上着をお脱ぎ下さい』と書かれていた"),
            hati.talk("このハンガーに掛けりゃいいのかな"),
            hati.do("上着をハンガーで吊るすと、$Sは壁伝いに奥へと進む"),
            hati.talk("お次はっと……お、今度はシャツとズボンを脱いで、お風呂が用意してありますって？　食べる前に風呂まで用意してくれるなんて、えらく気が効いたラーメン屋ッスねえ、こりゃこりゃ"),
            hati.do("相変わらず部屋は薄暗いが、それでも今までよりは随分とマシだ",
                "$Sはシャツとズボンを脱いで、かけ流しのその湯船へと足先を入れた"),
            hati.talk("随分とあったけえが、$meも江戸っ子だ"),
            hati.do("用意されていた手ぬぐいを額に乗せると、勢いよく肩まで浸かる"),
            hati.talk("あぁー、こりゃあいい湯加減だ。五臓六腑に染み渡るって感じッスかねえ、兄貴。ああ、兄貴はいねえんだった。兄貴も一緒だったらなあ……"),
            hati.do("そこに何かが落ちてくる"),
            hati.talk("おいおい何ッスか？　ラーメン？"),
            hati.do("指で掬ってみるとどうやら黄色い玉子麺のように見える"),
            hati.talk("これ、食ってもいいんスかね？　箸、箸、箸っと……箸は置いてねえなあ。まあ仕方ねえから手で食うか"),
            hati.do("自分の湯船に落ちてきたことも気にせず、$Sは思い切りずずいと吸い込んだ"),
            hati.talk("熱っ！　こりゃ熱くて茹でたの麺だなあ", "しかしなかなかうまいぞ。こうシコシコっとしてて。またダシがよく効いてらあ。塩味がちょっと濃いけど、それがよく麺に合って……うめえうめえ。ははは。こりゃあいい"),
            hati.do("けれど食べても食べても麺はなくならず、それどころか食べる度にわんこ蕎麦さながらに麺が投入されていく"),
            hati.talk("も、もうさすがに食えねえッス……ああ。そろそろお勘定。そうだそうだ。お勘定で兄貴のあれ、やんなきゃな"),
            hati.do("と、どこからともなく声が響いてきた"),
            hati.talk("ん？　何だい？　えーっと……"),
            god.voice("一つ、二つ、三つ……今何どきだい？"),
            hati.talk("んだって？　ああ、えー、五つでさあ"),
            hati.do("声はまだだな、と続く"),
            hati.talk("あのー。お勘定をー。すみませーん。お勘定"),
            hati.do("するとまた声が聴こえてきた"),
            god.voice("一つ、二つ、三つ……今なんどきだい？"),
            hati.talk("えー……四つ、いや五つかな"),
            hati.do("声はもう少しだな、と続く"),
            hati.talk("ふぅ、ふぅ……あー、も、もうオラ頭がぼーっとしてダメだ"),
            hati.do("するとまた声が聴こえてきた"),
            god.voice("一つ、二つ、三つ……今なんどきだい？"),
            hati.talk("八つ……いや九つ？　あれ、今いつなんだろう"),
            god.voice("そろそろいいだろう"),
            hati.do("それを合図にぞろぞろと大きな図体の赤や青の鬼どもが姿を現した",
                "けれど既に$Sは前後不覚で目を回し、とても自分が鬼に囲まれているとは気づけない"),
            god.talk("うんうん。いい塩梅に茹だったようだな。じゃあ、食うか"),
            w.br(),
            hati.do("ここは地獄の一丁目。嘘つきは地獄行きになるそうだ。旦那方、くれぐれもご注意を"),
            w.symbol("（了）"),
            camera=w.hati,
            stage=w.on_shop1,
            )

## episode
def ep_makura(w: World):
    return w.episode("話の枕",
            sc_makura(w),
            )

def ep_aniki(w: World):
    return w.episode("兄貴の場合",
            sc_at_ramenshop(w),
            note="ハチにラーメンを奢ることになった兄貴だったが持ち合わせが足りず、思案する")

def ep_hachi(w: World):
    return w.episode("ハチの場合",
            sc_at_foot_stall(w),
            note="ハチは兄貴のやり方をまねて安くすませようとしたが")

## chapter
def ch_tokimen(w: World):
    return w.chapter("時らーめん",
            ep_makura(w),
            ep_aniki(w),
            ep_hachi(w),
            note="金を持っていなかった兄貴はハチに奢ると約束した手前、何とかしようと思案し、妙案を出して乗り切る。ハチはそれを利用しようとするが")
