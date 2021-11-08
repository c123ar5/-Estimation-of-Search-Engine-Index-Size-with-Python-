# -*- coding: utf-8 -*-

import string
import random
import os


keywords=["列","紅","武","響","雖","推","勢","參","希","古","眾","構","房","節","半","土","投","某","案","維","黑","革","劃","敵","致","陳","律","足","態","護","興","七","派","驗","孩","責","營","星","夠","章","音","跟","志","底","站","嚴","巴","例","防","族","供","效","續","施","留","講","型","料","終","答","黃","緊","絕","奇","察","母","京","段","依","批","項","群","故","按","河","米","圍","江","織","雙","害","鬥","境","客","紀","采","舉","殺","攻","父","蘇","密","低","朝","友","訴","止","細","願","千","值","仍","錢","男","破","網","熱","助","倒","育","屬","坐","帝","限","船","臉","職","速","刻","樂","否","剛","威","毛","狀","率","甚","獨","球","般","普","怕","彈","校","苦","創","假","久","錯","承","印","晚","蘭","試","股","拿","腦","預","誰","陽","益","若","哪","微","尼","繼","送","急","血","藥","驚","傷","素","適","波","夜","省","初","衛","喜","源","食","險","待","述","陸","習","置","居","勞","財","環","排","福","納","歡","雷","警","獲","模","充","負","雲","停","木","遊","龍","樹","疑","層","冷","洲","沖","射","略","範","竟","句","室","異","激","漢","村","哈","策","演","簡","卡","罪","判","擔","州","靜","退","既","衣","您","餘","宗","積","痛","檢","差","富","靈","協","角","占","配","征","修","皮","揮","勝","降","階","審","沉","堅","善","媽","劉","讀","啊","超","免","壓","銀","養","買","皇","伊","懷","執","副","亂","抗","犯","追","幫","宣","佛","歲","航","優","怪","香","田","鐵","控","稅","左","右","份","穿","藝","背","陣","草","腳","概","惡","塊","頓","敢","守","酒","島","央","托","戶","烈","洋","哥","索","胡","款","靠","評","版","寶","座","釋","顧","景","弟","登","貨","互","付","伯","慢","歐","換","聞","危","忙","核","暗","姐","介","討","壞","麗","良","臨","序","升","監","亮","露","永","呼","味","野","架","域","沙","掉","括","艦","魚","雜","誤","灣","吉","減","編","楚","肯","測","敗","屋","跑","夢","散","溫","困","劍","漸","封","救","貴","槍","缺","樓","縣","尚","毫","移","娘","朋","畫","班","智","亦","耳","恩","短","掌","恐","遺","謝","固","席","松","秘","魯","遇","康","慮","幸","均","銷","鐘","詩","藏","趕","劇","票","損","忽","巨","炮","舊","端","探","湖","錄","葉","鄉","春","附","吸","予","禮","港","雨","呀","板","庭","婦","歸","飯","睛","額","含","補","順","輸","搖","招","婚","脫","謂","督","毒","油","療","旅","澤","材","滅","逐","筆","莫","亡","鮮","詞","聖","擇","尋","廠","睡","博","勒","煙","授","諾","倫","岸","奧","唐","賣","俄","炸","載","洛","健","堂","旁","宮","陰","喝","借","君","禁","園","謀","宋","避","抓","榮","姑","孫","逃","牙","束","頂","跳","玉","鎮","練","雪","午","迫","爺","篇","肉","嘴","館","遍","凡","礎","洞","卷","坦","牛","紙","寧","諸","訓","私","莊","祖","絲","翻","暴","森","塔","默","握","戲","隱","熟","骨","訪","弱","夥","蒙","歌","軟","店","鬼","典","欲","薩","遭","盤","爸","蓋","擴","弄","雄","穩","忘","億","刺","擁","徒","姆","楊","齊","賽","趣","曲","刀","床","虛","迎","冰","玩","析","窗","醒","妻","透","購","替","塞","努","休","虎","揚","途","侵","刑","綠","兄","迅","套","貿","畢","穀","唯","輪","跡","庫","尤","競","街","促","延","震","棄","甲","偉","麻","川","申","緩","針","潛","閃","售","燈","哲","絡","抵","朱","埃","抱","鼓","植","純","夏","頁","忍","傑","築","折","貝","鄭","尊","吳","秀","混","臣","雅","振","染","盛","怒","舞","圓","搞","狂","措","姓","秋","殘","培","猛","迷","誠","寬","宇","擺","梅","毀","伸","摩","盟","末","乃","悲","拍","丁","趙","硬","麥","蔣","操","耶","阻","訂","彩","抽","贊","魔","紛","沿","喊","違","妹","浪","匯","幣","豐","藍","殊","獻","桌","啦","瓦","萊","援","譯","奪","汽","燒","距","裁","偏","符","勇","觸","課","敬","哭","懂","襲","牆","召","罰","俠","廳","拜","巧","側","韓","冒","債","曼","融","慣","享","戴","童","猶","紹","乘","掛","獎","厚","縱","障","訊","涉","徹","刊","丈","爆","烏","鏡","役","描","洗","瑪","患","妙","唱","煩","簽","仙","彼","弗","症","仿","傾","牌","陷","鳥","轟","閉","咱","菜","奮","慶","撤","淚","茶","疾","緣","播","朗","杜","奶","季","丹","狗","尾","儀","偷","奔","蟲","珠","駐","孔","宜","艾","橋","淡","翼","恨","繁","寒","伴","歎","旦","縮","愈","潮","糧","罷","聚","徑","恰","挑","袋","灰","捕","徐","珍","幕","映","裂","泰","隔","啟","尖","忠","累","炎","暫","估","泛","荒","償","橫","拒","瑞","憶","孤","鼻","鬧","羊","呆","厲","衡","胞","窮","零","舍","碼","赫","婆","魂","災","膽","洪","腿","辯","津","俗","胸","曉","勁","貧","仁","偶","輯","邦","賴","恢","圈","摸","仰","潤","堆","碰","艇","稍","遲","輛","廢","淨","凶","署","禦","壁","奉","旋","礦","冬","抬","蛋","晨","雞","伏","吹","糊","倍","秦","盾","杯","診","租","騎","乏","隆","奴","攝","喪","汙","渡","旗","甘","耐","憑","紮","搶","緒","粗","肩","梁","幻","菲","皆","碎","宙","叔","岩","綜","蕩","爬","荷","悉","蒂","返","井","壯","薄","悄","掃","礙","敏","詳","殖","迪","矛","霍","允","幅","撒","剩","顆","凱","罵","賞","液","番","箱","貼","漫","酸","郎","腰","舒","眉","憂","浮","辛","戀","餐","嚇","挺","勵","鍵","辭","艘","伍","峰","尺","昨","黎","輩","貫","偵","滑","券","崇","擾","憲","趨","繞","慈","喬","閱","汗","枝","拖","墨","脅","插","箭","臘","泥","粉","氏","彭","拔","騙","鳳","慧","媒","佩","憤","撲","齡","驅","惜","掩","豪","兼","躍","屍","肅","帕","駛","堡","屆","欣","惠","冊","儲","飄","桑","閑","慘","潔","蹤","勃","頻","賓","仇","磨","遞","邪","滾","撞","擬","奏","顏","巡","貢","劑","績","瘋","坡","瞧","截","燃","焦","殿","偽","柳","鎖","逼","頗","昏","勸","飲","呈","搜","勤","戒","駕","漂","曹","朵","仔","柔","倆","孟","腐","幼","踐","籍","牧","涼","牲","佳","娜","濃","芳","稿","竹","脈","腹","跌","邏","垂","遵","貌","柏","獄","猜","憐","惑","陶","獸","帳","飾","貸","昌","敘","鋼","躺","溝","寄","扶","詢","鋪","鄧","壽","懼","湯","盜","肥","嘗","匆","輝","奈","扣","廷","澳","嘛","董","遷","凝","慰","厭","髒","騰","幽","怨","鞋","丟","埋","泉","湧","轄","躲","晉","紫","艱","魏","吾","慌","祝","郵","吐","狠","鑒","曰","械","咬","鄰","赤","擠","椅","彎","陪","割","揭","韋","悟","聰","霧","鋒","貓","梯","闊","祥","譽","籌","叢","鳴","牽","沈","閣","穆","屈","旨","袖","獵","臂","蛇","賀","柱","拋","鼠","瑟","戈","牢","遜","邁","欺","噸","琴","衰","瓶","惱","燕","誘","仲","狼","池","疼","盧","仗","冠","粒","遙","呂","玄","塵","馮","撫","淺","敦","鑽","糾","豈","晶","蒼","峽","噴","耗","淩","敲","菌","賠","塗","粹","扁","虧","寂","煤","熊","恭","濕","循","暖","糖","賦","抑","秩","帽","哀","宿","踏","爛","袁","侯","抖","夾","昆","肝","豬","擦","煉","恒","慎","搬","紐","紋","玻","漁","磁","齒","銅","跨","押","怖","漠","疲","叛","茲","遣","祭","腫","醉","拳","彌","斜","檔","膚","稀","捷","疫","豆","削","崗","晃","吞","宏","癌","隸","肚","履","漲","耀","扭","壇","沃","撥","繪","伐","堪","僕","郭","呵","犧","殲","墓","雇","廉","契","拼","懲","捉","覆","刷","劫","嫌","瓜","歇","雕","悶","乳","串","蓮","贏","娃","繳","喚","桃","霸","妥","瘦","搭","赴","嶽","艙","嘉","俊","址","銳","龐","耕","縫","悔","邀","玲","惟","斥","宅","添","挖","訟","氧","浩","羽","斤","禍","酷","掠","貪","妖","侍","乙","妨","掙","汪","尿","莉","軌","懸","鹽","唇","翰","倉","枚","覽","傅","帥","廟","芬","屏","寺","胖","璃","愚","滴","疏","蕭","腸","姿","顫","醜","劣","柯","溜","寸","扔","盯","辱","匹","俱","辨","餓","鬱","蜂","哦","謹","腔","潰","糟","葛","苗","忌","鴻","爵","鵬","鷹","籠","丘","桂","滋","聊","擋","綱","肌","茨","殼","痕","碗","穴","膀","臥","賢","卓","膜","毅","錦","欠","哩","函","茫","昂","薛","皺","誇","豫","胃","舌","剝","傲","拾","窩","睜","攜","陵","哼","棉","鈴","晴","飼","填","吻","渴","扮","逆","脆","喘","罩","蔔","爐","柴","愉","繩","胎","蓄","眠","竭","喂","傻","慕","渾","奸","扇","櫃","悅","攔","誕","飽","乾","賊","泡","亭","夕","爹","酬","儒","姻","卵","氛","泄","杆","挨","僧","蜜","吟","猩","遂","狹","肖","甜","霞","駁","裕","頑","摘","矮","秒","卿","畜","咽","輔","披","勾","盆","疆","賭","塑","畏","吵","囊","嗯","泊","驟","肺","纏","岡","羞","瞪","賈","吊","漏","斑","濤","悠","鹿","俘","錫","卑","葬","銘","灘","嫁","催","璿","翅","蠻","盒","矣","潘","歧","賜","鍋","鮑","廊","拆","灌","勉","盲","宰","佐","脹","啥","扯","禧","遼","抹","筒","棋","褲","唉","樸","咐","孕","誓","喉","妄","鏈","拘","馳","纖","逝","欄","竊","豔","頸","臭","璣","棵","趁","匠","盈","翁","愁","瞬","嬰","孝","倘","浙","諒","蔽","暢","贈","妮","莎","尉","凍","跪","闖","葡","鴨","廚","顛","遮","誼","圳","籲","侖","辟","瘤","陀","嫂","框","譚","亨","欽","庸","歉","芝","吼","甫","衫","宴","攤","囑","衷","嬌","陝","浦","矩","訝","聳","膠","裸","碧","摧","薪","淋","恥","屠","鵝","饑","盼","脖","虹","翠","崩","賬","萍","逢","賺","撐","綿","翔","倡","枯","猴","巫","昭","怔","淵","湊","溪","蠢","禪","闡","旺","寓","藤","匪","傘","碑","挪","瓊","脂","謊","慨","菩","萄","獅","脊","掘","抄","嶺","暈","砍","逮","掏","狄","晰","罕","挽","脾","舟","癡","蔡","剪","弓","懶","叉","拐","喃","僚","捐","姊","騷","拓","歪","粘","柄","坑","陌","窄","湘","兆","崖","驕","刹","鞭","芒","筋","鉤","聘","棍","嚷","腺","弦","焰","耍","俯","厘","愣","廈","懇","饒","釘","寡","憾","摔","疊","惹","譜","喻","愧","煌","徽","溶","墜","煞","巾","濫","灑","堵","瓷","咒","姨","棒","郡","浴","媚","穌","淮","哎","屁","漆","淫","巢","吩","撰","滯","嘯","玫","碩","釣","蝶","膝","姚","軀","茂","吏","猿","寨","壟","恕","渠","戚","辰","頒","舶","惶","狐","諷","笨","袍","嘲","腎","啡","潑","銜","倦","涵","雀","旬","僵","撕","肢","夷","逸","茅","僑","輿","窯","涅","蒲","謙","杭","噢","弊","勳","刮","郊","淒","捧","浸","磚","諮","鼎","籃","餅","蒸","畝","貞","陡","爪","兔","殷","薦","啞","炭","墳","眨","搏","咳","攏","舅","昧","擅","爽","咖","擱","祿","雌","哨","鞏","絹","螺","裹","昔","軒","謬","薑","諜","龜","媳","瞎","冤","鴉","蓬","巷","琳","栽","詐","沾","齋","瞞","彪","厄","紡","劈","罐","桶","壤","頌","糕","膨","諧","壘","咕","隙","辣","綁","寵","黴","嘿","兌","挫","輻","稽","紗","乞","裙","嘻","哇","繡","杖","塘","衍","軸","攀","膊","譬","斌","祈","踢","轎","肆","坎","泣","棚","屢","躁","邱","凰","溢","椎","簾","砸","趟","帆","竄","棲","販","丸","斬","堤","塌","廂","掀","喀","乖","謎","閻","捏","蘋","虜","蘆","濱","匙","卸","沼","禱","鑰","株","剖","熙","怯","嘩","棠","胳","樁","瑰","娛","娶","沫","嗓","蹲","淘","焚","韻","嫩","豎","匈","襯","鈞","峻","豹","撈","菊","鄙","魄","兜","哄","蟻","穎","鎊","屑","壺","禿","怡","滲","鹹","迦","旱","喲","焉","宛","譴","稻","鑄","鍛","伽","詹","斃","恍","貶","燭","駭","芯","汁","桓","坊","驢","朽","靖","傭","汝","碌","迄","冀","荊","崔","雁","紳","珊","榜","誦","傍","彥","醇","笛","禽","勿","娟","瞄","幢","寇","賄","睹","踩","霆","嗚","拱","妃","蔑","諭","縛","詭","淹","篷","腕","煮","倩","卒","勘","馨","逗","甸","賤","炒","墊","燦","敞","蠟","囚","栗","辜","妒","魁","謠","寞","甩","蜀","枕","涯","丐","泳","奎","泌","逾","叮","黛","燥","擲","憎","樞","藉","鯨","弘","倚","侮","藩","拂","鶴","蝕","芙","漿","垃","烤","曬","霜","剿","蘊","圾","綢","嶼","氫","駝","妝","捆","鉛","逛","淑","榴","丙","癢","鈔","蹄","犬","躬","晝","藻","蛛","褐","頰","奠","募","耽","蹈","陋","侶","魅","嵐","侄","虐","墮","陛","瑩","蔭","狡","閥","莖","絞","垮","膏","緬","喇","絨","攪","凳","梭","丫","姬","鈕","詔","棺","締","耿","懈","嫉","鴿","灶","勻","嗣","澡","鑿","緯","沸","刃","疇","遏","爍","嗅","叭","熬","瞥","骸","奢","拙","棟","毯","桐","砂","莽","瀉","坪","梳","杉","晤","稚","蔬","蠅","頃","搗","麽","尷","詫","鏢","尬","硫","羨","嚼","淪","滬","曠","彬","芽","冥","狸","碳","咧","惕","蘿","暑","咯","洶","腥","窺","俺","潭","崎","麟","撿","拯","厥","澄","哉","萎","渦","滔","暇","溯","釀","鱗","茵","愕","瞅","暮","衙","誡","斧","兮","煥","棕","佑","嘶","妓","喧","蓉","刪","櫻","伺","嗡","娥","梢","蠶","壩","敷","瀾","杏","綏","冶","庇","撓","摟","倏","聶","婉","噪","稼","鰭","菱","盞","匿","吱","寢","髓","攬","秉","矢","哺","啪","幟","膩","邵","挾","嗽","缸","揉","馴","纜","貯","晌","癱","覓","朦","隋","僻","蔓","咋","嵌","虔","畔","瑣","碟","澀","朧","嘟","蹦","塚","瀏","蝦","裔","襟","叨","訣","旭","簿","啤","擒","棗","嘎","苑","牟","嘔","駱","凸","熄","兀","喔","裳","凹","贖","屯","膛","澆","灼","裘","砰","棘","聾","橡","堿","姥","瑜","糞","毋","婭","沮","俏","萌","黯","粟","撇","尹","苟","螞","癲","禹","廖","儉","帖","竇","縷","煎","簇","矯","棱","叩","呐","瑤","墅","鶯","蔥","蛙","燙","歹","伶","哮","眩","諱","坤","廓","啼","乍","瓣","枉","跋","梗","廁","琢","譏","釉","窟","斂","軾","廬","胚","呻","綽","扼","懿","炯","竿","慷","虞","錘","栓","槳","蚊","磅","孽","慚","稟","戳","鄂","饋","顱","垣","鈣","咚","濺","礁","彰","眯","豁","雯","磷","墟","迂","瞻","琉","悼","蝴","揀","渺","眷","憫","汰","懾","嬸","斐","噓","鑲","炕","宦","繃","趴","窘","襄","珀","囂","拚","酌","毓","濁","嗜","撼","翹","扛","峭","磕","槽","柵","淌","頹","瑛","熏","頤","竅","忖","牡","綴","徊","梨","肪","涕","摹","憊","踱","肘","熔","摯","氯","凜","繹","庶","脯","迭","睦","粥","庵","滄","沁","奕","怠","嚨","氨","矗","盔","拇","沛","榻","揣","嶄","鞘","鞠","墾","洽","唾","櫥","仕","蜘","襪","痰","峙","蟬","柬","蟹","諫","擎","鵑","皓","朕","疤","鈍","鏟","禺","酶","匣","氓","弧","錐","峨","揪","杠","吭","崛","誣","冉","抒","庚","悍","靡","晦","鋸","醋","夭","壕","咦","侈","婢","猾","徘","硝","煽","皂","舵","嗦","狽","靴","捂","郝","瘡","苛","穢","茜","搓","簷","芸","賃","醬","鈾","餉","蕉","苔","緞","赦","舷","筷","朔","婪","紊","廝","婿","寥","兢","糙","卦","槐","扒","裴","祀","埔","絮","芭","屜","瘓","霄","綻","邑","宵","霖","岔","韌","餌","茄","琪","鄒","瑚","殆","憋","嚕","忒","忿","釁","淳","悖","髦","粵","孜","隘","瀕","錚","驀","畸","籬","剔","塢","澱","唬","汀","趾","鑼","緝","嫦","斟","鞍","扳","拴","詛","謨","呃","懦","犁","逞","懺","擰","叱","亥","佟","舜","絆","龔","腮","邸","椒","蔚","狩","湛","眶","棧","薇","阪","肮","瀑","渣","褂","嘰","臀","妞","巍","唔","疚","戎","鯉","肇","篤","嫻","轍","阮","劄","懊","燾","恤","疹","瀟","鋁","滌","恃","嘍","砌","楞","遁","窪","阱","咎","炳","葦","噬","磯","拷","楓","哆","矽","翩","窒","儂","胰","靶","蕪","妾","嚎","辮","幌","踉","佃","葫","拽","皖","濾","睬","匕","俞","嗤","謗","捍","孵","倪","癮","匡","敝","綾","磋","淆","堯","蕊","烘","璋","亢","軋","賂","榆","蝗","誅","駿","勺","梵","頜","笠","熾","閘","狒","樊","鎔","繆","垢","瘟","菇","琦","剃","炫","迸","溺","惚","嗨","隕","羈","贓","嘀","臻","膳","贛","殉","躊","桔","瞿","閩","豚","沌","摻","喳","惰","橢","咪","霎","侃","猝","窖","戮","祠","矚","菁","佬","躇","肋","咄","忡","雍","忱","蕾","蹌","伎","炊","釗","蝠","諦","屎","拭","褪","丞","卉","隧","茸","鉗","伢","啃","舔","閨","蹬","眺","攣","袱","隴","柿","毆","梧","惺","弛","琛","僥","捅","膿","醞","薯","曳","澈","鏽","稠","眸","咆","簧","瘍","鷗","騾","瀆","汲","嬉","穗","巳","邢","拎","檻","廿","篩","攙","曙","樵","隅","謁","倭","痹","猖","佯","呱","肛","奚","抨","甭","蛾","嘮","嵩","熒","詰","漱","酋","攘","篡","睿","噩","悵","盎","徙","鞅","祟","漓","攸","睫","翎","嗆","筐","塹","檀","寅","惘","馭","磊","吠","馱","瑙","炬","痙","愷","曝","螢","胺","敕","箏","幡","竺","霹","鳩","毗","烙","埠","蒜","阜","筍","嘈","鼇","乒","帷","闕","啄","氈","褥","搔","冕","韶","骼","獰","藹","烹","奄","嫖","沐","詠","噗","岑","蛟","詣","弩","擄","孚","圃","撚","悴","鈉","祁","捶","襖","澎","恪","氮","雛","彷","堰","撮","鸚","暉","犀","沽","腑","橄","掐","褻","齲","嗒","咀","錨","祺","貽","匾","乓","萃","揖","覷","吝","憔","羌","誨","礫","蠕","肴","撩","坍","酥","嫋","黝","俾","嫣","穹","鵲","秧","妊","溉","聿","疙","蘑","輾","睾","鋅","楷","茹","酵","滇","纂","圭","幔","褒","揍","倔","誹","腓","頡","鋤","嗔","磺","攢","瘩","靂","吆","悚","墩","彝","輒","囪","逍","桅","儼","綸","殃","悸","幀","俐","綺","籽","袒","孰","贅","愫","拌","缽","暨","橙","敖","抉","頊","剌","娼","淤","葵","噥","酣","麓","琅","簸","禾","銖","璧","娠","彗","惋","腋","螂","劾","掣","粱","嚓","瀝","醯","憚","氖","謔","捎","羔","俟","渲","欖","繭","霓","胥","鵡","琶","撬","橘","拈","笆","亟","痊","渭","狙","珂","蛻","刨","諺","饅","憧","瞟","拗","帚","釵","哧","喋","簫","刁","繚","怦","迥","湄","閔","渝","磐","冗","噶","黏","蕃","餃","驛","弼","淄","踞","韜","婷","唆","蜒","偎","榨","漉","皈","矜","碉","笈","鯊","枷","躡","瀚","酪","癖","炙","揩","蜷","燼","侏","凋","漪","悻","訕","蹋","詮","搐","碘","帛","碾","擂","苯","訶","鐸","戊","荀","駒","攫","憬","哽","踵","蟒","漾","嘖","吮","氟","楠","慫","叼","偕","竣","漩","翌","蹭","撾","臆","崽","絢","糜","瘢","闌","跤","恬","豢","汶","蹺","蝸","琵","憨","螅","惴","戟","匱","恙","箋","抿","楨","飭","蛤","瞳","衹","瓢","芹","秤","跺","潦","噠","栩","曦","骷","鬢","丕","鹵","嫡","梓","嗖","浚","惦","哢","荃","藐","唧","璽","髏","汛","銬","皿","渤","箍","餡","戍","汾","痔","褶","聆","汞","涎","奐","疣","漬","巔","逵","儺","耆","蟋","鱷","訛","膺","鉀","躥","沂","釜","筏","坯","巒","茬","摒","蟀","攆","飆","滸","繽","嵋","瓏","苞","瑾","泵","曖","賡","遝","鐮","叟","佚","臍","撂","晏","甥","璐","蠱","漳","癟","閹","蹂","璉","鰓","湃","轆","僭","鼾","躪","懵","寐","褚","攥","澗","蝙","禎","驥","轅","杞","渙","煜","傣","噯","酉","捺","秸","瑕","鑫","饞","窿","胱","楔","荔","軻","蟆","鐲","屹","湍","遐","韁","鋇","樺","燉","緋","羚","嗇","詡","籙","掖","涸","塾","鴛","呸","掄","熹","擻","坷","亙","跛","嗟","筵","甕","汕","鯰","歟","壑","潁","踴","姍","溥","梟","跚","暄","稷","笙","漣","瀛","滕","踝","瞼","貳","瞰","惻","嚏","迢","獗","縈","邯","珥","贍","酮","璞","羹","緘","俸","晾","媲","鸞","恿","蜿","諛","扈","訥","蜈","犢","戌","翟","蓓","鋆","藕","鍍","謾","蠍","卯","岐","諳","荼","椰","甄","蹊","蟾","螃","濘","擼","薔","檬","猓","羲","瘸","蘸","蔗","鏘","傀","蚌","錮","恚","遽","邃","皚","簌","睞","鱉","昊","焙","鸛","誥","睽","劊","唄","噎","寰","唷","殯","恣","淖","詼","鴦","嬋","櫚","氦","蛹","靳","繕","愜","蹙","眈","罡","胤","皋","蛀","絳","偌","疵","葆","顎","喙","黔","齦","佼","烽","儡","斕","嬪","諡","盅","娓","町","簍","芥","瘠","蹣","挎","啜","閡","橇","薈","垛","淇","瓚","虱","躋","髯","龕","諄","瞠","癇","掂","潼","鎂","騁","灸","腆","筱","壬","茗","椋","蛔","潺","扉","耘","檳","甬","雹","淞","蚪","燎","蕙","蜻","軼","鄲","猙","楣","捋","涓","蓀","婁","麝","蚤","薰","醮","搪","湮","瞌","輟","謐","鰨","茉","梆","樟","嶇","臼","穡","癬","玷","饃","呷","萼","嫵","佇","彤","岬","莓","媛","惆","啾","蜓","囔","孺","徇","徵","岱","昵","焊","卅","邙","隼","痞","恫","桀","愴","鍬","綬","襠","盂","檜","蚓","嗷","摳","槌","芮","蚣","痘","痢","閂","鏗","颶","皰","蝌","莢","蚯","撅","窠","斡","耷","硯","牒","煦","賑","囁","耙","榕","韃","稈","袤","諶","醺","徨","翡","櫓","纓","嵇","圪","髻","諂","痣","輜","娩","蛐","鷂","翱","靦","庖","鰻","籟","蓿","瘧","頷","瘀","嚅","黜","黠","餒","瀨","忐","洵","忑","砥","閭","咂","罹","糠","匝","偃","淙","紉","祛","喏","蟄","閏","澇","曜","洄","疽","廄","煊","汐","鉻","璜","蘚","渥","靼","苓","酗","噤","咫","鯽","椿","錠","罔","鍾","匍","祗","錳","脛","岌","鑾","畹","熠","糯","醃","鐳","沅","旌","棣","饈","孢","豌","盹","熵","駙","鎬","骰","嚶","癩","虯","韭","裨","瞑","闔","雋","宕","戾","鐫","溟","牘","婊","鵠","拄","埂","媧","萱","啵","蠡","芋","胭","褸","豺","啻","蛆","掰","檸","蕁","篆","葷","颼","倌","蛭","嚀","紜","莞","澹","謖","潞","郅","鐧","弋","螳","胄","蟑","宓","猥","曇","蟠","柑","匐","烯","濮","蟮","仄","祐","偈","蜃","粼","箴","嗥","襤","蕨","鈦","圩","薊","諉","杳","孿","魘","鏤","簪","氳","摞","颯","夙","舀","槁","臧","貂","蒿","蜥","蹩","靄","鈈","皙","濂","鎧","獾","鱸","叵","霾","泯","碴","鴕","飩","邇","峪","饕","紂","輳","瘁","睢","鬃","夔","佘","垠","榭","鮭","娑","隍","篝","洌","浜","榔","汩","浣","舐","諤","忻","瞭","詒","咻","唑","鶉","皎","懋","麾","氐","冽","箕","俚","汴","宸","芍","捱","摺","擯","簦","箔","噝","孀","怏","吒","諞","砧","耄","漕","罌","饢","鷲","烷","榘","灃","欒","沱","俑","榷","縝","螄","泗","剽","衢","紓","臊","瘴","怵","晁","酚","齧","孛","煬","憩","掬","欏","鐐","畿","撣","驍","侗","椽","泓","蚱","酯","癜","藎","灤","癸","蚜","捫","歆","廡","蝮","蹶","弈","蠣","庋","喟","滂","啕","翊","獺","齪","莘","鄴","燮","剁","覲","鐺","臃","鎳","讒","蝟","墒","曄","燔","涿","嘭","籮","鷺","睨","鄱","坳","砷","諍","唏","伲","歿","蚩","琥","縹","涇","芻","殮","鰍","芷","舫","逅","氰","詆","嶙","唰","囈","茁","媯","饉","驤","峋","苷","袂","擢","懣","蓑","祉","淶","踹","飪","綹","沏","掇","誑","餑","噫","逕","飧","鍘","樅","熨","葒","鋈","戛","賒","儔","么","湎","芪","凇","觶","齷","苻","嘁","嬴","撻","韉","鈺","肽","慟","迨","儆","齜","訖","覦","媾","滓","僮","杈","赳","疸","胯","斛","涮","觥","綰","卞","慍","庠","拮","燁","龢","窈","菠","緲","罄","弁","囤","咣","奘","腴","繅","郟","鑣","柚","喵","遛","潢","荻","琨","藜","臏","雉","橐","艮","蛉","駢","詵","柩","搽","寮","濡","佗","啷","僂","夯","闈","枸","虻","筠","諼","臾","埽","笞","婀","钜","珞","粑","顴","殞","綣","嶗","覬","昱","嗑","榛","蜴","鱔","淼","噙","囿","硼","礬","泅","邂","蠹","堊","乩","淦","嗝","樽","誚","啐","淅","揆","櫸","馗","魷","暹","騖","轡","苫","竦","詈","獠","獷","篙","諢","峒","蜚","鉸","餛","瀅","琬","靚","狻","璨","蟎","鸕","芩","蜇","嘹","錕","洹","櫛","釷","儷","瑁","鍁","竑","壹","痿","粕","犄","瘙","衲","摶","餞","踮","齙","訃","愎","馥","鄺","梏","艿","趺","鱘","鶚","剜","笥","縐","罅","衩","姣","斫","爻","晗","窕","鎩","獼","仨","崴","酢","搡","孑","佞","璀","檄","蓯","舛","岷","邕","闓","閾","鉑","霽","鍔","犒","麋","餾","麒","妍","宥","涔","摁","鋌","惲","嗲","麂","胛","贗","哂","呶","桎","噘","懍","擷","櫟","霰","饗","娣","揄","噔","賁","臚","忝","薏","鵪","迤","嗵","鍪","瀘","刈","咿","僖","蔫","銓","嗪","岫","茯","軲","嶸","懟","蘢","昕","咩","郢","髡","澧","餿","苣","盥","濯","囡","礪","弑","楂","翦","讖","鍥","怩","楹","霏","蠼","謳","胝","砭","慵","杵","樾","濰","銑","幗","碣","胴","啶","徠","裟","鈷","謅","楫","銥","赭","驊","酊","磧","醛","魑","陂","剮","畦","閌","鬮","祚","鶻","泱","趄","陲","騫","呤","倜","鄖","鉉","燧","粲","骶","忸","峁","淥","戡","髭","袞","莧","蜊","鋥","鎢","譎","蒞","戕","幄","虢","闥","驪","詬","妲","絀","袈","椏","燴","鎗","儻","肓","杲","撳","藪","厝","氤","縉","硒","旖","紇","唁","硎","裱","嬗","顰","煨","鏖","礴","靨","羿","笏","蟈","鋰","蠔","湟","煒","煲","筧","銼","鼐","甑","軛","頦","弭","喑","嫗","嶂","潯","苡","孳","醴","絛","渚","鷸","饌","邛","覃","耦","膘","褡","癆","屙","篾","兗","爰","痂","艄","遨","耨","鬩","昶","秣","焓","漚","邋","俎","窣","榫","蟪","鳶","烴","氬","稗","謇","鍇","齬","磣","肱","俁","笫","痤","嬤","芨","砣","莆","菏","闋","鼴","竽","舸","猷","誆","鏨","姘","悌","婕","淬","隗","槭","邈","稹","歙","蹴","豕","砒","羯","魴","鎦","癰","蔦","匭","笤","蓖","詿","浹","烊","崢","徭","謄","蚨","趔","褓","窸","縊","翳","酆","鴣","仃","炔","勖","蚴","葺","賾","瀧","蠐","媸","俳","祜","砦","逡","孱","蹕","諏","伉","屐","蛞","溴","鎘","圻","矸","崆","庾","掮","蒯","緙","鴇","橛","蛩","餳","蠖","囀","劭","杼","哐","崧","遑","螫","齟","顥","饔","欞","顳","腱","繈","牝","蛄","愾","鮃","濠","頎","嗄","灝","輦","轂","疥","苜","砝","嘣","夤","蕎","忤","旎","遢","瘛","魎","氚","娌","涫","碇","滎","臁","瓤","吡","毖","瑋","羥","壅","縟","珈","虼","佝","玨","祇","郛","翕","遴","玖","逋","詁","粽","氅","蹇","岢","聒","髁","芾","淝","閎","黍","鞣","瀠","鱟","髖","鶩","汨","胍","鈐","戩","銨","閼","鬈","枰","衾","崮","檣","膾","蹼","劬","囫","咭","洱","紺","鯀","刎","芏","琊","碚","鱈","芎","恂","嘧","槿","謫","鰱","闃","浠","跏","潸","噱","酈","抻","臬","琰","萇","矍","鶿","齠","鈿","饜","呔","芄","雒","觴","讜","舂","釩","飫","槎","鴆","阡","妗","蚧","莒","萸","稔","穰","餼","菸","葩","踔","薌","譙","鎰","佻","倨","釧","嘌","厴","蠓","黷","鴰","恁","殫","鎏","藿","纈","訌","囟","呋","旃","婺","酩","緔","鄣","甌","鍶","訐","逶","懨","縵","聵","菟","媼","鄔","殤","濉","螟","鮫","簣","醪","闐","肼","芡","嫠","嶠","鄯","峴","愆","摜","燜","黿","卟","姒","杷","砉","挈","蚋","笳","袢","菖","靛","蓧","黽","踽","萵","閿","挲","笪","郯","誄","鳧","儈","韙","钁","趿","菅","嵊","箸","褳","旯","涪","莠","圜","齎","曷","柞","圇","巽","跎","嗍","榧","裰","簟","籩","蕘","枋","逖","絝","詎","魃","餮","騅","乜","瑭","踅","鄢","閽","菬","蟛","饊","鱒","縞","氘","忪","姹","桉","紕","氪","藺","躒","旮","汊","紆","郃","娉","傈","艫","庥","堋","笮","槊","緇","魍","髂","櫪","鶘","齶","鈸","枳","蜍","搿","醚","鏊","禳","鷓","珩","蒺","蜢","鬻","閬","卮","苄","苕","埡","菀","袷","瘺","騔","驃","躚","鶇","鹼","缶","笸","磬","鷙","躉","芰","紈","砩","琮","鄆","犛","鋃","錒","蘄","蠲","妯","舢","駟","鷯","芫","笊","嗉","蠊","枇","浯","焱","飴","閫","蕕","鈧","柢","鉚","擤","醢","帙","呲","堀","崾","硪","雱","碓","漵","牖","瀦","鵒","鬣","鑷","疝","桁","郴","詘","蛺","僳","獐","箝","冪","鰥","賅","贄","呦","囹","茴","脲","揶","嗌","螈","腖","痼","膈","銻","鯿","鍤","苤","雎","嶧","橈","鮒","鞫","鼬","苧","緡","鮁","昀","痍","獯","蟊","癤","韝","鱧","乇","炷","梔","硐","熗","裾","槲","儕","羸","鸝","臒","佰","牯","旆","掾","琺","僦","嗶","縯","鯡","仟","圮","芟","崍","笱","跗","廩","擘","圄","匏","彀","嗾","卣","玳","浞","涑","畛","赧","湣","粳","摑","顓","刖","湫","椴","貉","篋","擀","鯪","邐","鑠","緗","朐","畈","訇","茱","啖","愀","蛘","慳","鷚","氹","佶","苴","晟","匚","佤","厙","徉","氡","洙","胗","鋯","鞽","鉞","勰","繇","螭","鴟","肟","邨","肫","軫","嵬","癭","蠆","仞","宄","睇","跆","鉬","奩","樗","熳","螻","鯫","轤","錈","磽","誒","餜","薜","襇","櫬","鏵","讕","帑","虺","矬","碡","寤","慪","糅","蹚","讎","鑭","礱","糴","鼉","钅","悒","啁","硌","蛑","塤","犍","艉","驁","齏","噅","筮","肄","艏","糝","釙","蜮","勱","齔","黢","畚","鬯","稞","耪","觳","鵓","鯤","鱺","柘","捌","菔","嬈","魨","獬","篪","蓴","鯁","狎","倀","孬","聃","閆","鄄","遒","綦","磔","誶","灩","泠","釹","硨","蔻","鐙","罘","胂","菹","僉","煆","煸","嶝","螯","躅","鷥","坨","哞","洳","盍","徜","菽","萘","慊","羰","澠","褫","縻","躑","灞","緄","怛","芤","俅","洮","胼","隳","羆","鏞","縋","芊","啉","焐","噌","嬙","膻","蜆","亓","倮","葎","嘞","鏌","蘅","荏","唳","傖","骱","澍","熲","檁","韞","蘖","髕","怙","垡","焯","腚","羧"]
keywords_n=""
i=0


random.shuffle(keywords)

for i in range(120):
    r=keywords[i]
    if r not in keywords_n:
        if i == 0:
            keywords_n=keywords_n + str(r) 
        if i != 0:
            keywords_n=keywords_n +","
            keywords_n+= str(r)

print (keywords_n)