# @Time : 2020/12/9 下午4:30 
# @Author : tongyue

import re

# 正则如何避免换行等问题
listStr = '''
<head>
    <meta charset="utf-8">
    <meta name="referrer" content="always">
    <title>IT新闻 - 博客园</title>
    <meta name="keywords" content="IT新闻,it news,互联网新闻,业界新闻,IT资讯,IT业界,新闻频道">
    <meta name="description">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <link id="rsslink" title="rss" type="application/rss+xml" rel="alternate" href="http://feed.cnblogs.com/news/rss">
    <link rel="shortcut icon" href="//common.cnblogs.com/favicon.ico">
    <link rel="stylesheet" href="/Content/bundles/news.css?v=UGqTWlsVUep3QvYAgaz2LPgMvc7Ik0wuEfwfZJ-5tZM">
    <link rel="stylesheet" type="text/css" href="//mention.cnblogs.com/css/mention-simple.css?id=20160613">
    <link id="smallScreen" rel="stylesheet" type="text/css" media="screen and (max-width:768px)" href="/Content/smallScreen.css?v=ZscfE6XKOKclm8eBNhYn5QbFrhnJcbmiXBucBroqRIs">
    <script type="text/javascript" src="/Scripts/jquery.min.js"></script>
    <script type="text/javascript" src="/Scripts/bundles/news.js?v=NWzOaUGAd-DmDHBEBJ-MPL3eLK8Vpc26nS6ubbAaS3o"></script>
    <script async="async" src="https://www.googletagservices.com/tag/js/gpt.js"></script>
    <script>
        var googletag = googletag || {};
        googletag.cmd = googletag.cmd || [];
    </script>
    <script>
        googletag.cmd.push(function () {
            googletag.defineSlot('/1090369/news_E1', [728, 90], 'div-gpt-ad-1533633736227-0').addService(googletag.pubads());
            googletag.defineSlot('/1090369/news_E2', [300, 250], 'div-gpt-ad-1533633736227-1').addService(googletag.pubads());
            googletag.defineSlot('/1090369/news_E3', [300, 250], 'div-gpt-ad-1533633736227-2').addService(googletag.pubads());
            googletag.defineSlot('/1090369/news_E4', [468, 60], 'div-gpt-ad-1533633736227-3').addService(googletag.pubads());
            googletag.pubads().enableSingleRequest();
            googletag.enableServices();
        });
    </script>
</head>
<body>
    <a name="top"></a>
    <div id="wrap">
        <div id="header">
            <a name="top"></a>
            <div id="wrapper_top_block">
                <div id="login_area">
                </div>
                <div id="top_mini_nav_block">« <a href="//www.cnblogs.com" class="dark_gray" title="程序员的网上家园">网站首页</a> <a href="http://zzk.cnblogs.com/" class="dark_gray">找找看</a></div>
                <div class="clear"></div>
            </div>
        </div>
    </div>
    <div id="main_wrapper">
        <div id="main_header">
            <div class="header_div">
                <div class="logo">
                    <a href="//www.cnblogs.com">
                        <img src="/Images/logo.gif" alt="logo">
                    </a>
                </div>
                <div class="banner">
                    <div id="clubHeader_panelNews">
                        <div id="e1"></div>
                    </div>
                </div>
            </div>
            <div class="mainmenu">
                <div class="feedback_block">
                    <a href="//group.cnblogs.com/forum/public/">反馈问题或建议</a>
                </div>
                <ul id="navlist_main">
                    <li style="margin-left:20px;">
                        <a href="//www.cnblogs.com">首页</a>
                    </li>
                    <li>
                        <a href="//home.cnblogs.com">园子</a>
                    </li>
                    <li>
                    </li>
                    <li id="clubHeader_liNews">
                        <a id="clubHeader_lnkNews" title="IT新闻" class="current" href="/">新 闻</a>
                    </li>
                    <li>
                        <a id="clubHeader_lkQuestionMenu" href="//q.cnblogs.com/">博问</a>
                    </li>
                    <li>
                    </li>
                    <li>
                        <a id="clubHeader_lkIngMenu" href="//ing.cnblogs.com/">闪存</a>
                    </li>
                    <li>
                        <a id="clubHeader_lnkWz" href="//wz.cnblogs.com/">收藏</a>
                    </li>
                    <li>
                        <a href="https://brands.cnblogs.com/">专区</a>
                    </li>
                    <li>
                        <a href="//kb.cnblogs.com">知识库</a>
                    </li>
                    <li id="clubHeader_liMyMessage">
                    </li>
                </ul>
            </div>
            <script type="text/javascript">
                if (typeof (jQuery) != 'undefined') {
                    GetUserInfo();
                }
            </script>
        </div>
        <div id="sideleft">
    <div id="guide" style="display:none;">
        <h3>
            <a href="//www.cnblogs.com" title="程序员的网上家园">博客园</a> » <a href="/" title="IT新闻">新闻</a><span id="lbMobileAuditTips" style="display:none;"></span>
        </h3>
    </div>
    <div id="navcontainer" class="floatright" style="padding-top: 1px;">
        <ul id="navlist">
            <li>
                <a href="/" class="current">最新发布</a>
            </li>
            <li>
                <a href="/n/recommend">推荐新闻</a>
            </li>
            <li>
                <a href="/n/digg">热门新闻</a>
            </li>
            <li>
                <a href="/n/comment">新闻评论</a>
            </li>
        </ul>
    </div>
    <div class="clear">
    </div>
    <div id="news_list">
            <div class="news_block" id="entry_685430">
                <div class="action">
                    <div class="diggit" onclick="VoteNews(685430,'agree')">
                        <span id="digg_num_685430" class="diggnum">0</span>
                    </div>
                    <div class="clear"></div>
                    <div id="digg_tip_685430" class="digg-tip"></div>
                </div>
                <!--end: action -->
                <div class="content">
                    <h2 class="news_entry">
                        <a href="/n/685430/" target="_blank">历时21个月！FDA终于发布首个医疗AI行动计划，一切要归功于这个人</a>
                    </h2>
                    <div class="entry_summary" style="display: block;">
                        <a href="/n/topic_1268.htm"><img src="https://images2018.cnblogs.com/news_topic/20180820083250783-2011194759.png" class="topic_img" alt=""></a>
                        1 月 12 日，FDA 正式发布了该机构的第一个人工智能/机器学习（AI / ML）的 SaMD（Software as a Medical Device，医疗设备独立软件）行动计划。 （关注公众号医健 AI 掘金志，对话框回复“FDA”，即可获取计划文件） 这个行动计划提出了一种多管齐下的方法，
                    </div>
                    <div class="entry_footer">
                        <a href="//home.cnblogs.com/u/itwriter/" class="gray" target="_blank">
                            itwriter
                        </a>投递 
                        <span class="comment">
                            <a href="/n/685430#comment" class="gray" target="_blank">评论(0)</a>
                        </span><span class="view">0 人浏览</span>
                        <span class="tag"> <a href="/n/tag/FDA/" class="gray">FDA</a> <a href="/n/tag/AI/" class="gray">AI</a> </span>
                        发布于 <span class="gray">2021-01-17 20:13</span>
                    </div>
                    <!--end: entry_footer -->
                </div>
                <!--end: content -->
                <div class="clear">
                </div>
            </div>
            <!--end: news_block -->
            <div class="clear">
            </div>
            <div class="news_block" id="entry_685429">
                <div class="action">
                    <div class="diggit" onclick="VoteNews(685429,'agree')">
                        <span id="digg_num_685429" class="diggnum">0</span>
                    </div>
                    <div class="clear"></div>
                    <div id="digg_tip_685429" class="digg-tip"></div>
                </div>
                <!--end: action -->
                <div class="content">
                    <h2 class="news_entry">
                        <a href="/n/685429/" target="_blank">关于自动驾驶， Mobileye的14个最新观点</a>
                    </h2>
                    <div class="entry_summary" style="display: block;">
                        <a href="/n/topic_132.htm"><img src="//images0.cnblogs.com/news_topic/ITblog.jpg" class="topic_img" alt=""></a>
                        为了在 2025 年实现消费级别的自动驾驶，Mobileye 都做了什么？ Mobileye 近日在 CES 2021 展会上进一步分享了其在 ADAS 及全自动驾驶领域的战略规划，并详细介绍了 Mobileye 为实现消费级别的全自动驾驶和“挽救生命”愿景所研发的几项技术，其中涵盖了芯片、雷达、地
                    </div>
                    <div class="entry_footer">
                        <a href="//home.cnblogs.com/u/itwriter/" class="gray" target="_blank">
                            itwriter
                        </a>投递 
                        <span class="comment">
                            <a href="/n/685429#comment" class="gray" target="_blank">评论(0)</a>
                        </span><span class="view">0 人浏览</span>
                        <span class="tag"> <a href="/n/tag/Mobileye/" class="gray">Mobileye</a> </span>
                        发布于 <span class="gray">2021-01-17 20:10</span>
                    </div>
                    <!--end: entry_footer -->
                </div>
                <!--end: content -->
                <div class="clear">
                </div>
            </div>
            <!--end: news_block -->
            <div class="clear">
            </div>
            <div class="news_block" id="entry_685428">
                <div class="action">
                    <div class="diggit" onclick="VoteNews(685428,'agree')">
                        <span id="digg_num_685428" class="diggnum">0</span>
                    </div>
                    <div class="clear"></div>
                    <div id="digg_tip_685428" class="digg-tip"></div>
                </div>
                <!--end: action -->
                <div class="content">
                    <h2 class="news_entry">
                        <a href="/n/685428/" target="_blank">全球首款RISC-V AI单板计算机推出，值得花119美元拥抱开源？</a>
                    </h2>
                    <div class="entry_summary" style="display: block;">
                        <a href="/n/topic_116.htm"><img src="//images0.cnblogs.com/news_topic/opensource.jpg" class="topic_img" alt=""></a>
                        2021 开年，RISC-V 的生态建设又就有了新动态。本周，赛昉科技发布了全球首款基于 RISC-V 的 AI 单板计算机星光（BeagleV），具备当今台式机的所有可扩展性功能，面积只有 85mm x 70mm，4GB 内存版本售价 119 美元，8GB 内存版本售价 149 美元。 首款 RI
                    </div>
                    <div class="entry_footer">
                        <a href="//home.cnblogs.com/u/itwriter/" class="gray" target="_blank">
                            itwriter
                        </a>投递 
                        <span class="comment">
                            <a href="/n/685428#comment" class="gray" target="_blank">评论(0)</a>
                        </span><span class="view">0 人浏览</span>
                        <span class="tag"> <a href="/n/tag/RISC-V%20AI/" class="gray">RISC-V AI</a> </span>
                        发布于 <span class="gray">2021-01-17 20:00</span>
                    </div>
                    <!--end: entry_footer -->
                </div>
                <!--end: content -->
                <div class="clear">
                </div>
            </div>
            <!--end: news_block -->
            <div class="clear">
            </div>
            <div class="news_block" id="entry_685427">
                <div class="action">
                    <div class="diggit" onclick="VoteNews(685427,'agree')">
                        <span id="digg_num_685427" class="diggnum">0</span>
                    </div>
                    <div class="clear"></div>
                    <div id="digg_tip_685427" class="digg-tip"></div>
                </div>
                <!--end: action -->
                <div class="content">
                    <h2 class="news_entry">
                        <a href="/n/685427/" target="_blank">谷歌将于3月15日起限制在第三方浏览器上使用的Chrome数据同步API</a>
                    </h2>
                    <div class="entry_summary" style="display: block;">
                        <a href="/n/topic_145.htm"><img src="https://img2018.cnblogs.com/news_topic/20191025104913585-6919525.png" class="topic_img" alt=""></a>
                        谷歌刚刚宣布，经过慎重的调查和考虑，其将于 2021 年 3 月 15 日起，限制第三方浏览器对于 Chrome 数据同步 API 的调用。据悉，尽管包括新版 Microsoft Edge、Opera、Vivaldi、Brave 等在内的第三方浏览器，都是基于开源的 Chromium 内核而构建，但
                    </div>
                    <div class="entry_footer">
                        <a href="//home.cnblogs.com/u/itwriter/" class="gray" target="_blank">
                            itwriter
                        </a>投递 
                        <span class="comment">
                            <a href="/n/685427#comment" class="gray" target="_blank">评论(0)</a>
                        </span><span class="view">18 人浏览</span>
                        <span class="tag"> <a href="/n/tag/Google/" class="gray">Google</a> <a href="/n/tag/Chrome/" class="gray">Chrome</a> </span>
                        发布于 <span class="gray">2021-01-17 19:56</span>
                    </div>
                    <!--end: entry_footer -->
                </div>
                <!--end: content -->
                <div class="clear">
                </div>
            </div>
            <!--end: news_block -->
            <div class="clear">
            </div>
            <div class="news_block" id="entry_685426">
                <div class="action">
                    <div class="diggit" onclick="VoteNews(685426,'agree')">
                        <span id="digg_num_685426" class="diggnum">0</span>
                    </div>
                    <div class="clear"></div>
                    <div id="digg_tip_685426" class="digg-tip"></div>
                </div>
                <!--end: action -->
                <div class="content">
                    <h2 class="news_entry">
                        <a href="/n/685426/" target="_blank">MIT生物学家揭秘：为什么癌细胞会浪费这么多能量</a>
                    </h2>
                    <div class="entry_summary" style="display: block;">
                        <a href="/n/topic_319.htm"><img src="https://img2018.cnblogs.com/news_topic/20181019121101783-952728829.gif" class="topic_img" alt=""></a>
                        早在 20 世纪 20 年代，德国化学家奥托-沃伯格发现，癌细胞对糖的代谢方式与健康细胞通常的代谢方式不同。从那时起，科学家们就试图弄清楚为什么癌细胞会使用这种效率低得多的替代途径。麻省理工学院的生物学家现在已经找到了这个长期存在的问题的可能答案。 在发表在《分子细胞》上的一项研究中，他们阐明，这种
                    </div>
                    <div class="entry_footer">
                        <a href="//home.cnblogs.com/u/itwriter/" class="gray" target="_blank">
                            itwriter
                        </a>投递 
                        <span class="comment">
                            <a href="/n/685426#comment" class="gray" target="_blank">评论(0)</a>
                        </span><span class="view">167 人浏览</span>
                        <span class="tag"> <a href="/n/tag/Mit/" class="gray">Mit</a> </span>
                        发布于 <span class="gray">2021-01-17 14:56</span>
                    </div>
                    <!--end: entry_footer -->
                </div>
                <!--end: content -->
                <div class="clear">
                </div>
            </div>
            <!--end: news_block -->
            <div class="clear">
            </div>
            <div class="news_block" id="entry_685425">
                <div class="action">
                    <div class="diggit" onclick="VoteNews(685425,'agree')">
                        <span id="digg_num_685425" class="diggnum">0</span>
                    </div>
                    <div class="clear"></div>
                    <div id="digg_tip_685425" class="digg-tip"></div>
                </div>
                <!--end: action -->
                <div class="content">
                    <h2 class="news_entry">
                        <a href="/n/685425/" target="_blank">YouTube网站增加了用于搜索和控制的语音指令</a>
                    </h2>
                    <div class="entry_summary" style="display: block;">
                        <a href="/n/topic_22.htm"><img src="//images0.cnblogs.com/news_topic/youtube.gif" class="topic_img" alt=""></a>
                        YouTube 已经在其网站上增加了播放和搜索的语音控制功能。新功能的推出非常低调，没有从谷歌的线上新闻稿看到的官方通知。用户可以通过点击搜索栏右侧的麦克风图标，开始发出语音指令搜索视频。一旦用户允许访问电脑上的麦克风，就会出现一个方框，里面显示"Listening"字样，之前任何视频播放都会暂停。
                    </div>
                    <div class="entry_footer">
                        <a href="//home.cnblogs.com/u/itwriter/" class="gray" target="_blank">
                            itwriter
                        </a>投递 
                        <span class="comment">
                            <a href="/n/685425#comment" class="gray" target="_blank">评论(0)</a>
                        </span><span class="view">35 人浏览</span>
                        <span class="tag"> <a href="/n/tag/YouTube/" class="gray">YouTube</a> </span>
                        发布于 <span class="gray">2021-01-17 14:51</span>
                    </div>
                    <!--end: entry_footer -->
                </div>
                <!--end: content -->
                <div class="clear">
                </div>
            </div>
            <!--end: news_block -->
            <div class="clear">
            </div>
            <div class="news_block" id="entry_685424">
                <div class="action">
                    <div class="diggit" onclick="VoteNews(685424,'agree')">
                        <span id="digg_num_685424" class="diggnum">0</span>
                    </div>
                    <div class="clear"></div>
                    <div id="digg_tip_685424" class="digg-tip"></div>
                </div>
                <!--end: action -->
                <div class="content">
                    <h2 class="news_entry">
                        <a href="/n/685424/" target="_blank">首批随心飞用户“毕业” 9成不想继续“保研”</a>
                    </h2>
                    <div class="entry_summary" style="display: block;">
                        <a href="/n/topic_132.htm"><img src="//images0.cnblogs.com/news_topic/ITblog.jpg" class="topic_img" alt=""></a>
                        2020 年，“随心飞”产品成为航空业和旅游业的一个亮点，引发了关注和抢购，也引发了不少争议。首创“随心飞”的东航在年度总结中写道：“恭喜随心飞首届飞友，毕业快乐。”第一批“随心飞”用户的体验如何，会不会买新版“随心飞”？想买更便宜“随心飞”的用户，能等到期待的优惠吗？ 飞行 21 次，节省 115
                    </div>
                    <div class="entry_footer">
                        <a href="//home.cnblogs.com/u/itwriter/" class="gray" target="_blank">
                            itwriter
                        </a>投递 
                        <span class="comment">
                            <a href="/n/685424#comment" class="gray" target="_blank">评论(0)</a>
                        </span><span class="view">128 人浏览</span>
                        
                        发布于 <span class="gray">2021-01-17 14:45</span>
                    </div>
                    <!--end: entry_footer -->
                </div>
                <!--end: content -->
                <div class="clear">
                </div>
            </div>
            <!--end: news_block -->
            <div class="clear">
            </div>
            <div class="news_block" id="entry_685423">
                <div class="action">
                    <div class="diggit" onclick="VoteNews(685423,'agree')">
                        <span id="digg_num_685423" class="diggnum">0</span>
                    </div>
                    <div class="clear"></div>
                    <div id="digg_tip_685423" class="digg-tip"></div>
                </div>
                <!--end: action -->
                <div class="content">
                    <h2 class="news_entry">
                        <a href="/n/685423/" target="_blank">DICE开发者称微软还有很多未公布的Xbox独占游戏</a>
                    </h2>
                    <div class="entry_summary" style="display: block;">
                        <a href="/n/topic_299.htm"><img src="//images0.cnblogs.com/news_topic/xbox.jpg" class="topic_img" alt=""></a>
                        一名 EA DICE 开发者爆料，微软仍然有很多未公布的 Xbox 独占游戏（这里指的是主机版独占），今年发售。昨天微软在官网 Xbox Wire 发布了一个新的博客，详细介绍了即将在 2021 年加入到 Xbox 大家庭的独占游戏，包括《光环：无限》，《灵媒》，《蔑视》，《Lake》，《最后一站》
                    </div>
                    <div class="entry_footer">
                        <a href="//home.cnblogs.com/u/itwriter/" class="gray" target="_blank">
                            itwriter
                        </a>投递 
                        <span class="comment">
                            <a href="/n/685423#comment" class="gray" target="_blank">评论(0)</a>
                        </span><span class="view">35 人浏览</span>
                        <span class="tag"> <a href="/n/tag/Xbox/" class="gray">Xbox</a> </span>
                        发布于 <span class="gray">2021-01-17 14:35</span>
                    </div>
                    <!--end: entry_footer -->
                </div>
                <!--end: content -->
                <div class="clear">
                </div>
            </div>
            <!--end: news_block -->
            <div class="clear">
            </div>
            <div class="news_block" id="entry_685422">
                <div class="action">
                    <div class="diggit" onclick="VoteNews(685422,'agree')">
                        <span id="digg_num_685422" class="diggnum">0</span>
                    </div>
                    <div class="clear"></div>
                    <div id="digg_tip_685422" class="digg-tip"></div>
                </div>
                <!--end: action -->
                <div class="content">
                    <h2 class="news_entry">
                        <a href="/n/685422/" target="_blank">西安 - 东京全货运航线开通 由顺丰航空执飞</a>
                    </h2>
                    <div class="entry_summary" style="display: block;">
                        <a href="/n/topic_528.htm"><img src="//images0.cnblogs.com/news_topic/20150323122850630.png" class="topic_img" alt=""></a>
                        1 月 16 日上午，O37159 航班从西安咸阳国际机场起飞飞往东京，标志着西安—东京全货运航线正式开通，这也是今年陕西开通的首条国际全货运航线。 该航线由顺丰航空执飞，机型为 B767-300，每周一班，主要运输三星电子产品，预计全年运输货邮 2000 余吨。 据悉，西部机场集团航空物流公司成立
                    </div>
                    <div class="entry_footer">
                        <a href="//home.cnblogs.com/u/itwriter/" class="gray" target="_blank">
                            itwriter
                        </a>投递 
                        <span class="comment">
                            <a href="/n/685422#comment" class="gray" target="_blank">评论(0)</a>
                        </span><span class="view">49 人浏览</span>
                        <span class="tag"> <a href="/n/tag/%E9%A1%BA%E4%B8%B0/" class="gray">顺丰</a> </span>
                        发布于 <span class="gray">2021-01-17 14:30</span>
                    </div>
                    <!--end: entry_footer -->
                </div>
                <!--end: content -->
                <div class="clear">
                </div>
            </div>
            <!--end: news_block -->
            <div class="clear">
            </div>
            <div class="news_block" id="entry_685421">
                <div class="action">
                    <div class="diggit" onclick="VoteNews(685421,'agree')">
                        <span id="digg_num_685421" class="diggnum">0</span>
                    </div>
                    <div class="clear"></div>
                    <div id="digg_tip_685421" class="digg-tip"></div>
                </div>
                <!--end: action -->
                <div class="content">
                    <h2 class="news_entry">
                        <a href="/n/685421/" target="_blank">微软提供新的设置选项 客户可对其语音数据施加更多的控制</a>
                    </h2>
                    <div class="entry_summary" style="display: block;">
                        <a href="/n/topic_2.htm"><img src="https://img2018.cnblogs.com/news_topic/20200115105457739-1483150216.png" class="topic_img" alt=""></a>
                        微软昨天宣布，公司正在更新要求客户允许使用语音数据的方式，以改进使用其语音识别技术的微软产品。因此，微软现在提供了新的设置，让用户对他们的语音数据有更多的控制。 以下是官方提供的变化摘要： 在您的允许下，您的语音片段--您使用语音与 Microsoft 产品和服务进行交互时所说的话的音频记录--会偶
                    </div>
                    <div class="entry_footer">
                        <a href="//home.cnblogs.com/u/itwriter/" class="gray" target="_blank">
                            itwriter
                        </a>投递 
                        <span class="comment">
                            <a href="/n/685421#comment" class="gray" target="_blank">评论(0)</a>
                        </span><span class="view">24 人浏览</span>
                        <span class="tag"> <a href="/n/tag/%E5%BE%AE%E8%BD%AF/" class="gray">微软</a> </span>
                        发布于 <span class="gray">2021-01-17 14:22</span>
                    </div>
                    <!--end: entry_footer -->
                </div>
                <!--end: content -->
                <div class="clear">
                </div>
            </div>
            <!--end: news_block -->
            <div class="clear">
            </div>
            <div class="news_block" id="entry_685420">
                <div class="action">
                    <div class="diggit" onclick="VoteNews(685420,'agree')">
                        <span id="digg_num_685420" class="diggnum">0</span>
                    </div>
                    <div class="clear"></div>
                    <div id="digg_tip_685420" class="digg-tip"></div>
                </div>
                <!--end: action -->
                <div class="content">
                    <h2 class="news_entry">
                        <a href="/n/685420/" target="_blank">控评的大众点评 正在失去年轻人</a>
                    </h2>
                    <div class="entry_summary" style="display: block;">
                        <a href="/n/topic_330.htm"><img src="//images0.cnblogs.com/news_topic/dianping.gif" class="topic_img" alt=""></a>
                        “周末去的网红店又踩雷了，这是探店还是玩扫雷？”每个城市，大概都有那么几家让当地年轻人深恶痛绝的热门餐厅。这些店铺往往品质未见多好，门口排号人数却不少，怒而差评后仍旧源源不断的客流量仿佛在提醒你，它存在的意义就是被拔草。 刷单控评的大众点评，糊弄不了年轻人了。/《武林外传》 快用大众点评，随时随地发
                    </div>
                    <div class="entry_footer">
                        <a href="//home.cnblogs.com/u/itwriter/" class="gray" target="_blank">
                            itwriter
                        </a>投递 
                        <span class="comment">
                            <a href="/n/685420#comment" class="gray" target="_blank">评论(0)</a>
                        </span><span class="view">91 人浏览</span>
                        <span class="tag"> <a href="/n/tag/%E5%A4%A7%E4%BC%97%E7%82%B9%E8%AF%84/" class="gray">大众点评</a> </span>
                        发布于 <span class="gray">2021-01-17 14:18</span>
                    </div>
                    <!--end: entry_footer -->
                </div>
                <!--end: content -->
                <div class="clear">
                </div>
            </div>
            <!--end: news_block -->
            <div class="clear">
            </div>
            <div class="news_block" id="entry_685419">
                <div class="action">
                    <div class="diggit" onclick="VoteNews(685419,'agree')">
                        <span id="digg_num_685419" class="diggnum">0</span>
                    </div>
                    <div class="clear"></div>
                    <div id="digg_tip_685419" class="digg-tip"></div>
                </div>
                <!--end: action -->
                <div class="content">
                    <h2 class="news_entry">
                        <a href="/n/685419/" target="_blank">Bumble IPO文件发警告：苹果隐私新政可能会损害其利益</a>
                    </h2>
                    <div class="entry_summary" style="display: block;">
                        <a href="/n/topic_82.htm"><img src="https://img2018.cnblogs.com/news_topic/20190822140314801-1842879152.png" class="topic_img" alt=""></a>
                        据外媒报道，约会应用 Bumble 于当地时间周五在其 IPO 文件中向投资者发出警告，苹果持续改善用户隐私的努力可能会损害到其长期利润。周五，Bumble 向美国证券交易委员会(SEC)提交了 IPO 申请。SEC 则在向公众出售股票之前公开这家公司的计划。 据悉，Bumble 在文件中提到了苹果
                    </div>
                    <div class="entry_footer">
                        <a href="//home.cnblogs.com/u/itwriter/" class="gray" target="_blank">
                            itwriter
                        </a>投递 
                        <span class="comment">
                            <a href="/n/685419#comment" class="gray" target="_blank">评论(0)</a>
                        </span><span class="view">25 人浏览</span>
                        <span class="tag"> <a href="/n/tag/%E8%8B%B9%E6%9E%9C/" class="gray">苹果</a> </span>
                        发布于 <span class="gray">2021-01-17 14:10</span>
                    </div>
                    <!--end: entry_footer -->
                </div>
                <!--end: content -->
                <div class="clear">
                </div>
            </div>
            <!--end: news_block -->
            <div class="clear">
            </div>
            <div class="news_block" id="entry_685418">
                <div class="action">
                    <div class="diggit" onclick="VoteNews(685418,'agree')">
                        <span id="digg_num_685418" class="diggnum">0</span>
                    </div>
                    <div class="clear"></div>
                    <div id="digg_tip_685418" class="digg-tip"></div>
                </div>
                <!--end: action -->
                <div class="content">
                    <h2 class="news_entry">
                        <a href="/n/685418/" target="_blank">三星“掌门”李在镕行贿案重审结果将于18日宣判</a>
                    </h2>
                    <div class="entry_summary" style="display: block;">
                        <a href="/n/topic_251.htm"><img src="https://img2018.cnblogs.com/news_topic/20190906161325617-1698330440.png" class="topic_img" alt=""></a>
                        据韩媒报道，韩国首尔高等法院将于当地时间 18 日下午，就三星电子会长李在镕行贿案的重审进行宣判。据报道，重审期间，独立检察组和李在镕方面就如何评价三星守法监视委员会围绕量刑问题进行了辩论。李在镕最终获判实刑还是缓刑备受关注。 据此前报道，李在镕卷入韩国前总统朴槿惠的“亲信干政”丑闻，涉嫌为继承三星
                    </div>
                    <div class="entry_footer">
                        <a href="//home.cnblogs.com/u/itwriter/" class="gray" target="_blank">
                            itwriter
                        </a>投递 
                        <span class="comment">
                            <a href="/n/685418#comment" class="gray" target="_blank">评论(0)</a>
                        </span><span class="view">29 人浏览</span>
                        <span class="tag"> <a href="/n/tag/%E4%B8%89%E6%98%9F/" class="gray">三星</a> </span>
                        发布于 <span class="gray">2021-01-17 14:07</span>
                    </div>
                    <!--end: entry_footer -->
                </div>
                <!--end: content -->
                <div class="clear">
                </div>
            </div>
            <!--end: news_block -->
            <div class="clear">
            </div>
            <div class="news_block" id="entry_685417">
                <div class="action">
                    <div class="diggit" onclick="VoteNews(685417,'agree')">
                        <span id="digg_num_685417" class="diggnum">0</span>
                    </div>
                    <div class="clear"></div>
                    <div id="digg_tip_685417" class="digg-tip"></div>
                </div>
                <!--end: action -->
                <div class="content">
                    <h2 class="news_entry">
                        <a href="/n/685417/" target="_blank">游族老板疑被毒杀后，29亿遗产继承漏了一个小孩？</a>
                    </h2>
                    <div class="entry_summary" style="display: block;">
                        <a href="/n/topic_2728.htm"><img src="https://img2020.cnblogs.com/news_topic/20201224071851351-259780996.png" class="topic_img" alt=""></a>
                        游族网络原控股股东林奇去世后，风波未止。近日，有网友发文直指林奇的遗产分配有问题，“隐瞒林奇还有小儿子的消息是何居心？”“忽略他的小儿子有合法继承权的事实？ 游族网络 15 日公告截图。 15 日，游族网络发布公告称，公司原控股股东林奇名下的公司部分股份被司法冻结。该消息再次将游族网络推上舆论的风口
                    </div>
                    <div class="entry_footer">
                        <a href="//home.cnblogs.com/u/itwriter/" class="gray" target="_blank">
                            itwriter
                        </a>投递 
                        <span class="comment">
                            <a href="/n/685417#comment" class="gray" target="_blank">评论(0)</a>
                        </span><span class="view">102 人浏览</span>
                        <span class="tag"> <a href="/n/tag/%E6%B8%B8%E6%97%8F/" class="gray">游族</a> </span>
                        发布于 <span class="gray">2021-01-17 14:00</span>
                    </div>
                    <!--end: entry_footer -->
                </div>
                <!--end: content -->
                <div class="clear">
                </div>
            </div>
            <!--end: news_block -->
            <div class="clear">
            </div>
            <div class="news_block" id="entry_685416">
                <div class="action">
                    <div class="diggit" onclick="VoteNews(685416,'agree')">
                        <span id="digg_num_685416" class="diggnum">8</span>
                    </div>
                    <div class="clear"></div>
                    <div id="digg_tip_685416" class="digg-tip"></div>
                </div>
                <!--end: action -->
                <div class="content">
                    <h2 class="news_entry">
                        <a href="/n/685416/" target="_blank">自焚的饿了么骑手：工资被扣5000元 多次讨要未果而轻生</a>
                    </h2>
                    <div class="entry_summary" style="display: block;">
                        <a href="/n/topic_505.htm"><img src="https://img2020.cnblogs.com/news_topic/20200909152956315-1601830473.png" class="topic_img" alt=""></a>
                        北青深一度 记者/韩谦实习记者/李彤王焕熔 编辑/杨宝璐 刘进在医院等待清创手术 1 月 11 日上午 10 点左右，47 岁的饿了么外卖员刘进站在他工作的江苏泰州一配送站门口，将汽油淋到了自己身上，引火自焚。他身后的配送站招牌上，蓝底白字写着“即时配送，美好生活”。 周边的商家赶紧用灭火器把他救下
                    </div>
                    <div class="entry_footer">
                        <a href="//home.cnblogs.com/u/itwriter/" class="gray" target="_blank">
                            itwriter
                        </a>投递 
                        <span class="comment">
                            <a href="/n/685416#comment" class="gray" target="_blank">评论(4)</a>
                        </span><span class="view">867 人浏览</span>
                        <span class="tag"> <a href="/n/tag/%E9%A5%BF%E4%BA%86%E4%B9%88/" class="gray">饿了么</a> </span>
                        发布于 <span class="gray">2021-01-17 10:57</span>
                    </div>
                    <!--end: entry_footer -->
                </div>
                <!--end: content -->
                <div class="clear">
                </div>
            </div>
            <!--end: news_block -->
            <div class="clear">
            </div>
            <div class="news_block" id="entry_685415">
                <div class="action">
                    <div class="diggit" onclick="VoteNews(685415,'agree')">
                        <span id="digg_num_685415" class="diggnum">0</span>
                    </div>
                    <div class="clear"></div>
                    <div id="digg_tip_685415" class="digg-tip"></div>
                </div>
                <!--end: action -->
                <div class="content">
                    <h2 class="news_entry">
                        <a href="/n/685415/" target="_blank">百度造车AB面：市值起伏间为何重迎市场关注？</a>
                    </h2>
                    <div class="entry_summary" style="display: block;">
                        <a href="/n/topic_5.htm"><img src="//images0.cnblogs.com/news_topic/baidu.jpg" class="topic_img" alt=""></a>
                        文/周文猛 来源：InfoQ（ID:infoqchina） 2018 年，在追赶移动互联网的过程中，百度将搜索引擎打造成了移动端 App，用户搜索体验得以显著提升，市值也开始扶摇直上，一度高达 910.56 亿美元。 但在此之后，由于百度积极布局的 AI 、信息流等业务并没有带来太多实质性的营收增长
                    </div>
                    <div class="entry_footer">
                        <a href="//home.cnblogs.com/u/itwriter/" class="gray" target="_blank">
                            itwriter
                        </a>投递 
                        <span class="comment">
                            <a href="/n/685415#comment" class="gray" target="_blank">评论(0)</a>
                        </span><span class="view">77 人浏览</span>
                        <span class="tag"> <a href="/n/tag/%E7%99%BE%E5%BA%A6/" class="gray">百度</a> </span>
                        发布于 <span class="gray">2021-01-17 10:57</span>
                    </div>
                    <!--end: entry_footer -->
                </div>
                <!--end: content -->
                <div class="clear">
                </div>
            </div>
            <!--end: news_block -->
            <div class="clear">
            </div>
            <div class="news_block" id="entry_685414">
                <div class="action">
                    <div class="diggit" onclick="VoteNews(685414,'agree')">
                        <span id="digg_num_685414" class="diggnum">0</span>
                    </div>
                    <div class="clear"></div>
                    <div id="digg_tip_685414" class="digg-tip"></div>
                </div>
                <!--end: action -->
                <div class="content">
                    <h2 class="news_entry">
                        <a href="/n/685414/" target="_blank">担心遭到特朗普支持者报复：Twitter职工将个人账号改为私人状态</a>
                    </h2>
                    <div class="entry_summary" style="display: block;">
                        <a href="/n/topic_111.htm"><img src="https://img2018.cnblogs.com/news_topic/20191025154240816-905588526.png" class="topic_img" alt=""></a>
                        据《纽约时报》报道，由于担心成为特朗普支持者的攻击目标，一些 Twitter 员工将自己的账号设置为私人账号并删除了自己的在线传记。此外，Twitter 的一些高管则被分配了个人安全任务。当地时间 1 月 8 日，特朗普的@realDonaldTrump 账号遭到 Twitter 永久封号，“因为存
                    </div>
                    <div class="entry_footer">
                        <a href="//home.cnblogs.com/u/itwriter/" class="gray" target="_blank">
                            itwriter
                        </a>投递 
                        <span class="comment">
                            <a href="/n/685414#comment" class="gray" target="_blank">评论(0)</a>
                        </span><span class="view">67 人浏览</span>
                        <span class="tag"> <a href="/n/tag/Twitter/" class="gray">Twitter</a> </span>
                        发布于 <span class="gray">2021-01-17 10:51</span>
                    </div>
                    <!--end: entry_footer -->
                </div>
                <!--end: content -->
                <div class="clear">
                </div>
            </div>
            <!--end: news_block -->
            <div class="clear">
            </div>
            <div class="news_block" id="entry_685413">
                <div class="action">
                    <div class="diggit" onclick="VoteNews(685413,'agree')">
                        <span id="digg_num_685413" class="diggnum">0</span>
                    </div>
                    <div class="clear"></div>
                    <div id="digg_tip_685413" class="digg-tip"></div>
                </div>
                <!--end: action -->
                <div class="content">
                    <h2 class="news_entry">
                        <a href="/n/685413/" target="_blank">亏了20亿 王思聪要回万达子承父业了？</a>
                    </h2>
                    <div class="entry_summary" style="display: block;">
                        <a href="/n/topic_1020.htm"><img src="//images2017.cnblogs.com/news_topic/20170917105740719-684705229.png" class="topic_img" alt=""></a>
                        文/王慧莹 来源：Tech 星球(ID:tech618) 这几天，“富二代”们都有点忙。前有任正非的二女儿姚安娜，在 1 月 14 日生日当天高调宣布出道，进军娱乐圈；后有“国民老公”王思聪和父亲王健林一起成立新的投资公司。 Tech 星球 1 月 15 日获悉，根据天眼查 App 显示，万达产业投
                    </div>
                    <div class="entry_footer">
                        <a href="//home.cnblogs.com/u/itwriter/" class="gray" target="_blank">
                            itwriter
                        </a>投递 
                        <span class="comment">
                            <a href="/n/685413#comment" class="gray" target="_blank">评论(0)</a>
                        </span><span class="view">166 人浏览</span>
                        <span class="tag"> <a href="/n/tag/%E7%8E%8B%E6%80%9D%E8%81%AA/" class="gray">王思聪</a> </span>
                        发布于 <span class="gray">2021-01-17 10:45</span>
                    </div>
                    <!--end: entry_footer -->
                </div>
                <!--end: content -->
                <div class="clear">
                </div>
            </div>
            <!--end: news_block -->
            <div class="clear">
            </div>
            <div class="news_block" id="entry_685412">
                <div class="action">
                    <div class="diggit" onclick="VoteNews(685412,'agree')">
                        <span id="digg_num_685412" class="diggnum">0</span>
                    </div>
                    <div class="clear"></div>
                    <div id="digg_tip_685412" class="digg-tip"></div>
                </div>
                <!--end: action -->
                <div class="content">
                    <h2 class="news_entry">
                        <a href="/n/685412/" target="_blank">国产车也能做高端 理想创始人李想：中国会出现世界顶级品牌</a>
                    </h2>
                    <div class="entry_summary" style="display: block;">
                        <a href="/n/topic_2658.htm"><img src="https://img2020.cnblogs.com/news_topic/20200519081225487-510553435.png" class="topic_img" alt=""></a>
                        在汽车领域，BBA 为代表的高端品牌纵横全球数十年，国产车多年来大都只能做中低端市场。 未来国产车能不能做到全球顶级品牌？理想创始人李想对这个问题是肯定的。 在日前的第七届中国电动汽车百人会论坛上，李想表示他在做智能电动车之前做了超过 10 年的汽车网站“汽车之家“，跟很多汽车品牌负责人在聊，很多话
                    </div>
                    <div class="entry_footer">
                        <a href="//home.cnblogs.com/u/itwriter/" class="gray" target="_blank">
                            itwriter
                        </a>投递 
                        <span class="comment">
                            <a href="/n/685412#comment" class="gray" target="_blank">评论(0)</a>
                        </span><span class="view">79 人浏览</span>
                        <span class="tag"> <a href="/n/tag/%E7%90%86%E6%83%B3%E6%B1%BD%E8%BD%A6/" class="gray">理想汽车</a> </span>
                        发布于 <span class="gray">2021-01-17 10:33</span>
                    </div>
                    <!--end: entry_footer -->
                </div>
                <!--end: content -->
                <div class="clear">
                </div>
            </div>
            <!--end: news_block -->
            <div class="clear">
            </div>
            <div class="news_block" id="entry_685411">
                <div class="action">
                    <div class="diggit" onclick="VoteNews(685411,'agree')">
                        <span id="digg_num_685411" class="diggnum">0</span>
                    </div>
                    <div class="clear"></div>
                    <div id="digg_tip_685411" class="digg-tip"></div>
                </div>
                <!--end: action -->
                <div class="content">
                    <h2 class="news_entry">
                        <a href="/n/685411/" target="_blank">特斯拉Model 3撞上高架隔离桩 前脸完全损毁</a>
                    </h2>
                    <div class="entry_summary" style="display: block;">
                        <a href="/n/topic_429.htm"><img src="https://img2020.cnblogs.com/news_topic/20200919095456914-256019808.png" class="topic_img" alt=""></a>
                        前段时间，因为频频被车主之一“失控”，特斯拉也被推到了舆论的风口浪尖之上。只不过，早已经历过这么多全球车主质疑“失控”的风风雨雨，特斯拉早已“出师”，回应几乎都是“车辆没有任何问题，驾驶员误操作”。 同时，特斯拉的销量并没有受到太大影响，仍是一马领先，成为国内高端纯电动车的销冠品牌。只不过，特斯拉的
                    </div>
                    <div class="entry_footer">
                        <a href="//home.cnblogs.com/u/itwriter/" class="gray" target="_blank">
                            itwriter
                        </a>投递 
                        <span class="comment">
                            <a href="/n/685411#comment" class="gray" target="_blank">评论(0)</a>
                        </span><span class="view">104 人浏览</span>
                        <span class="tag"> <a href="/n/tag/Tesla/" class="gray">Tesla</a> </span>
                        发布于 <span class="gray">2021-01-17 10:25</span>
                    </div>
                    <!--end: entry_footer -->
                </div>
                <!--end: content -->
                <div class="clear">
                </div>
            </div>
            <!--end: news_block -->
            <div class="clear">
            </div>
            <div class="news_block" id="entry_685410">
                <div class="action">
                    <div class="diggit" onclick="VoteNews(685410,'agree')">
                        <span id="digg_num_685410" class="diggnum">0</span>
                    </div>
                    <div class="clear"></div>
                    <div id="digg_tip_685410" class="digg-tip"></div>
                </div>
                <!--end: action -->
                <div class="content">
                    <h2 class="news_entry">
                        <a href="/n/685410/" target="_blank">程序员大意扔掉7500枚比特币硬盘：欲花费7000万美元挖垃圾场被拒</a>
                    </h2>
                    <div class="entry_summary" style="display: block;">
                        <a href="/n/topic_424.htm"><img src="https://img2020.cnblogs.com/news_topic/20201127175718159-1044964558.png" class="topic_img" alt=""></a>
                        近日，比特币价格长势喜人，但英国一位拥有 7500 枚比特币的男子却怎么也高兴不起来。 据外媒报道，英国 IT 工程师詹姆斯·豪威尔斯（James Howells）曾不小心将藏有 7500 枚比特币私钥的硬盘当垃圾扔掉，向政府申请挖掘垃圾填埋场以寻找这个硬盘，但是被拒绝了。 据悉，这名来自威尔士纽波
                    </div>
                    <div class="entry_footer">
                        <a href="//home.cnblogs.com/u/itwriter/" class="gray" target="_blank">
                            itwriter
                        </a>投递 
                        <span class="comment">
                            <a href="/n/685410#comment" class="gray" target="_blank">评论(1)</a>
                        </span><span class="view">146 人浏览</span>
                        <span class="tag"> <a href="/n/tag/%E6%AF%94%E7%89%B9%E5%B8%81/" class="gray">比特币</a> </span>
                        发布于 <span class="gray">2021-01-17 10:21</span>
                    </div>
                    <!--end: entry_footer -->
                </div>
                <!--end: content -->
                <div class="clear">
                </div>
            </div>
            <!--end: news_block -->
            <div class="clear">
            </div>
            <div class="news_block" id="entry_685409">
                <div class="action">
                    <div class="diggit" onclick="VoteNews(685409,'agree')">
                        <span id="digg_num_685409" class="diggnum">0</span>
                    </div>
                    <div class="clear"></div>
                    <div id="digg_tip_685409" class="digg-tip"></div>
                </div>
                <!--end: action -->
                <div class="content">
                    <h2 class="news_entry">
                        <a href="/n/685409/" target="_blank">字节跳动的第一场败仗：烧光20亿 悟空问答终落幕</a>
                    </h2>
                    <div class="entry_summary" style="display: block;">
                        <a href="/n/topic_1365.htm"><img src="https://img2018.cnblogs.com/news_topic/20190903110342690-1278481212.png" class="topic_img" alt=""></a>
                        2021 年伊始，字节跳动旗下两款产品接连宣布停止运营。1 月 5 日，知识付费平台好好学习宣布将于 1 月 20 日停止运营。1 月 13 日，问答社区悟空问答发布公告称将于 1 月 20 日从各大应用市场下架，并将于 2 月 3 日正式停止运营，关闭服务。 作为一款相当受重视的产品，悟空问答也曾
                    </div>
                    <div class="entry_footer">
                        <a href="//home.cnblogs.com/u/itwriter/" class="gray" target="_blank">
                            itwriter
                        </a>投递 
                        <span class="comment">
                            <a href="/n/685409#comment" class="gray" target="_blank">评论(0)</a>
                        </span><span class="view">109 人浏览</span>
                        <span class="tag"> <a href="/n/tag/%E5%AD%97%E8%8A%82%E8%B7%B3%E5%8A%A8/" class="gray">字节跳动</a> </span>
                        发布于 <span class="gray">2021-01-17 10:17</span>
                    </div>
                    <!--end: entry_footer -->
                </div>
                <!--end: content -->
                <div class="clear">
                </div>
            </div>
            <!--end: news_block -->
            <div class="clear">
            </div>
            <div class="news_block" id="entry_685408">
                <div class="action">
                    <div class="diggit" onclick="VoteNews(685408,'agree')">
                        <span id="digg_num_685408" class="diggnum">0</span>
                    </div>
                    <div class="clear"></div>
                    <div id="digg_tip_685408" class="digg-tip"></div>
                </div>
                <!--end: action -->
                <div class="content">
                    <h2 class="news_entry">
                        <a href="/n/685408/" target="_blank">滴滴发公告：北京超10万滴滴司机预约接种疫苗</a>
                    </h2>
                    <div class="entry_summary" style="display: block;">
                        <a href="/n/topic_473.htm"><img src="https://img2020.cnblogs.com/news_topic/20200916090549924-327187345.png" class="topic_img" alt=""></a>
                        1 月 16 日消息，滴滴发布公告，表示将有序组织司机接种疫苗。 滴滴方面指出，滴滴在防疫部门和交通主管部门的指导和帮助下，正有序组织滴滴和花小猪网约车司机、滴滴代驾司机、青桔单车运维师傅、司机服务经理、防疫消杀站工作人员等交通从业者的疫苗接种工作，保障用户出行安全。 从 1 月 13 日起，北京滴
                    </div>
                    <div class="entry_footer">
                        <a href="//home.cnblogs.com/u/itwriter/" class="gray" target="_blank">
                            itwriter
                        </a>投递 
                        <span class="comment">
                            <a href="/n/685408#comment" class="gray" target="_blank">评论(0)</a>
                        </span><span class="view">28 人浏览</span>
                        <span class="tag"> <a href="/n/tag/%E6%BB%B4%E6%BB%B4/" class="gray">滴滴</a> </span>
                        发布于 <span class="gray">2021-01-17 10:11</span>
                    </div>
                    <!--end: entry_footer -->
                </div>
                <!--end: content -->
                <div class="clear">
                </div>
            </div>
            <!--end: news_block -->
            <div class="clear">
            </div>
            <div class="news_block" id="entry_685407">
                <div class="action">
                    <div class="diggit" onclick="VoteNews(685407,'agree')">
                        <span id="digg_num_685407" class="diggnum">0</span>
                    </div>
                    <div class="clear"></div>
                    <div id="digg_tip_685407" class="digg-tip"></div>
                </div>
                <!--end: action -->
                <div class="content">
                    <h2 class="news_entry">
                        <a href="/n/685407/" target="_blank">北京现代销量连续4年下滑！经销商无奈转让场地给特斯拉</a>
                    </h2>
                    <div class="entry_summary" style="display: block;">
                        <a href="/n/topic_787.htm"><img src="//images2015.cnblogs.com/news_topic/20161221142641557-922206159.png" class="topic_img" alt=""></a>
                        日前，有媒体报道称，北京朝阳区的一家北京现代 4S 店，经销商将展厅的大部分租给特斯拉。而原先的北京现代搬到了旁边，那里曾经是售后服务的区域。 该北京现代 4S 店销售人员表示，这两家店面原本都属于北京现代，但因为“各种原因”，展厅的大部分出租给了特斯拉，而北京现代店面则搬到了西侧，这里此前是北京现
                    </div>
                    <div class="entry_footer">
                        <a href="//home.cnblogs.com/u/itwriter/" class="gray" target="_blank">
                            itwriter
                        </a>投递 
                        <span class="comment">
                            <a href="/n/685407#comment" class="gray" target="_blank">评论(0)</a>
                        </span><span class="view">50 人浏览</span>
                        <span class="tag"> <a href="/n/tag/Tesla/" class="gray">Tesla</a> <a href="/n/tag/%E7%8E%B0%E4%BB%A3/" class="gray">现代</a> </span>
                        发布于 <span class="gray">2021-01-17 10:06</span>
                    </div>
                    <!--end: entry_footer -->
                </div>
                <!--end: content -->
                <div class="clear">
                </div>
            </div>
            <!--end: news_block -->
            <div class="clear">
            </div>
            <div class="news_block" id="entry_685406">
                <div class="action">
                    <div class="diggit" onclick="VoteNews(685406,'agree')">
                        <span id="digg_num_685406" class="diggnum">0</span>
                    </div>
                    <div class="clear"></div>
                    <div id="digg_tip_685406" class="digg-tip"></div>
                </div>
                <!--end: action -->
                <div class="content">
                    <h2 class="news_entry">
                        <a href="/n/685406/" target="_blank">微软承认Win10存在严重NTFS漏洞：解压缩包等会损坏硬盘</a>
                    </h2>
                    <div class="entry_summary" style="display: block;">
                        <a href="/n/topic_2.htm"><img src="https://img2018.cnblogs.com/news_topic/20200115105457739-1483150216.png" class="topic_img" alt=""></a>
                        昨天我们报道称，某个组成文件系统路径的短字符串，可能导致 Windows 10 用户的硬盘驱动器损坏。 现在微软证实了这个消息，并且表示，会在后续的更新中修复上述漏洞。 据悉，微软正努力修复存在于 Windows 10 系统中的关键 NTFS 漏洞。当用户打开 HTML 文件、Windows 快捷方
                    </div>
                    <div class="entry_footer">
                        <a href="//home.cnblogs.com/u/itwriter/" class="gray" target="_blank">
                            itwriter
                        </a>投递 
                        <span class="comment">
                            <a href="/n/685406#comment" class="gray" target="_blank">评论(0)</a>
                        </span><span class="view">71 人浏览</span>
                        <span class="tag"> <a href="/n/tag/%E5%BE%AE%E8%BD%AF/" class="gray">微软</a> </span>
                        发布于 <span class="gray">2021-01-17 10:00</span>
                    </div>
                    <!--end: entry_footer -->
                </div>
                <!--end: content -->
                <div class="clear">
                </div>
            </div>
            <!--end: news_block -->
            <div class="clear">
            </div>
            <div class="news_block" id="entry_685405">
                <div class="action">
                    <div class="diggit" onclick="VoteNews(685405,'agree')">
                        <span id="digg_num_685405" class="diggnum">0</span>
                    </div>
                    <div class="clear"></div>
                    <div id="digg_tip_685405" class="digg-tip"></div>
                </div>
                <!--end: action -->
                <div class="content">
                    <h2 class="news_entry">
                        <a href="/n/685405/" target="_blank">英伟达收购ARM的交易可能被一国或多国监管机构拒绝</a>
                    </h2>
                    <div class="entry_summary" style="display: block;">
                        <a href="/n/topic_217.htm"><img src="https://img2018.cnblogs.com/news_topic/20190801102552535-795219988.png" class="topic_img" alt=""></a>
                        去年 9 月，英伟达宣布将以 400 亿美元收购 ARM，如果这笔交易达成，将创下半导体行业单笔并购交易金额的记录。不过，这一交易从宣布之初就备受关注和争议。 英伟达创始人兼首席执行官黄仁勋说收购 ARM 是一生仅有一次的机会。ARM 联合创始人 Hermann Hauser 却说这笔收购会是一场灾
                    </div>
                    <div class="entry_footer">
                        <a href="//home.cnblogs.com/u/itwriter/" class="gray" target="_blank">
                            itwriter
                        </a>投递 
                        <span class="comment">
                            <a href="/n/685405#comment" class="gray" target="_blank">评论(0)</a>
                        </span><span class="view">41 人浏览</span>
                        <span class="tag"> <a href="/n/tag/%E8%8B%B1%E4%BC%9F%E8%BE%BE/" class="gray">英伟达</a> <a href="/n/tag/ARM/" class="gray">ARM</a> </span>
                        发布于 <span class="gray">2021-01-17 09:53</span>
                    </div>
                    <!--end: entry_footer -->
                </div>
                <!--end: content -->
                <div class="clear">
                </div>
            </div>
            <!--end: news_block -->
            <div class="clear">
            </div>
            <div class="news_block" id="entry_685404">
                <div class="action">
                    <div class="diggit" onclick="VoteNews(685404,'agree')">
                        <span id="digg_num_685404" class="diggnum">0</span>
                    </div>
                    <div class="clear"></div>
                    <div id="digg_tip_685404" class="digg-tip"></div>
                </div>
                <!--end: action -->
                <div class="content">
                    <h2 class="news_entry">
                        <a href="/n/685404/" target="_blank">电竞算不算体育！爱奇艺体育说了不算</a>
                    </h2>
                    <div class="entry_summary" style="display: block;">
                        <a href="/n/topic_132.htm"><img src="//images0.cnblogs.com/news_topic/ITblog.jpg" class="topic_img" alt=""></a>
                        近日，爱奇艺体育 CEO 发表了一则“暴论”——“从游戏演变而来的电子竞技，我坚决反对它是体育！” 先不说该大佬单方面将电竞这个国家体育总局承认，且入选亚运会的项目逐出体育范畴的行为，是多么的中二热血，单说其对电竞起源的偏见，就让人有点摸不着头脑。 我们不妨先看看目前世界上主流体育项目最原始的样子：
                    </div>
                    <div class="entry_footer">
                        <a href="//home.cnblogs.com/u/itwriter/" class="gray" target="_blank">
                            itwriter
                        </a>投递 
                        <span class="comment">
                            <a href="/n/685404#comment" class="gray" target="_blank">评论(1)</a>
                        </span><span class="view">48 人浏览</span>
                        <span class="tag"> <a href="/n/tag/%E7%88%B1%E5%A5%87%E8%89%BA%E4%BD%93%E8%82%B2/" class="gray">爱奇艺体育</a> </span>
                        发布于 <span class="gray">2021-01-17 09:45</span>
                    </div>
                    <!--end: entry_footer -->
                </div>
                <!--end: content -->
                <div class="clear">
                </div>
            </div>
            <!--end: news_block -->
            <div class="clear">
            </div>
            <div class="news_block" id="entry_685403">
                <div class="action">
                    <div class="diggit" onclick="VoteNews(685403,'agree')">
                        <span id="digg_num_685403" class="diggnum">0</span>
                    </div>
                    <div class="clear"></div>
                    <div id="digg_tip_685403" class="digg-tip"></div>
                </div>
                <!--end: action -->
                <div class="content">
                    <h2 class="news_entry">
                        <a href="/n/685403/" target="_blank">对标苹果M1：曝高通正在研发8cx升级版处理器</a>
                    </h2>
                    <div class="entry_summary" style="display: block;">
                        <a href="/n/topic_258.htm"><img src="//images0.cnblogs.com/news_topic/qualcomm.gif" class="topic_img" alt=""></a>
                        1 月 16 日消息，自从苹果推出了首款自研 M1 芯片，便受到业界人士的持续关注，同时，为了能与 M1 有一战之力，主流芯片厂商纷纷加快自家旗舰级芯片研发的速度。 近日，据媒体 winfuture 消息，在一份进出口数据库报告中，出现了一款代号 SC8280 的处理器。 报道称，这款骁龙 SC82
                    </div>
                    <div class="entry_footer">
                        <a href="//home.cnblogs.com/u/itwriter/" class="gray" target="_blank">
                            itwriter
                        </a>投递 
                        <span class="comment">
                            <a href="/n/685403#comment" class="gray" target="_blank">评论(0)</a>
                        </span><span class="view">69 人浏览</span>
                        <span class="tag"> <a href="/n/tag/%E9%AB%98%E9%80%9A/" class="gray">高通</a> </span>
                        发布于 <span class="gray">2021-01-17 09:40</span>
                    </div>
                    <!--end: entry_footer -->
                </div>
                <!--end: content -->
                <div class="clear">
                </div>
            </div>
            <!--end: news_block -->
            <div class="clear">
            </div>
            <div class="news_block" id="entry_685402">
                <div class="action">
                    <div class="diggit" onclick="VoteNews(685402,'agree')">
                        <span id="digg_num_685402" class="diggnum">0</span>
                    </div>
                    <div class="clear"></div>
                    <div id="digg_tip_685402" class="digg-tip"></div>
                </div>
                <!--end: action -->
                <div class="content">
                    <h2 class="news_entry">
                        <a href="/n/685402/" target="_blank">北京组织外卖小哥、快递小哥接种新冠疫苗</a>
                    </h2>
                    <div class="entry_summary" style="display: block;">
                        
                        1 月 17 日，北青-北京头条记者了解到，近日，北京市疫苗接种工作组会同市商务、邮政等部门，协调美团、京东等平台，组织“外卖小哥”、“快递小哥”开展新冠疫苗接种工作，在前期完成 5 万人接种的基础上，1 月 18 日前，将继续完成约 3 万人疫苗接种。另据了解，本市从 2021 年 1 月 1 日
                    </div>
                    <div class="entry_footer">
                        <a href="//home.cnblogs.com/u/itwriter/" class="gray" target="_blank">
                            itwriter
                        </a>投递 
                        <span class="comment">
                            <a href="/n/685402#comment" class="gray" target="_blank">评论(0)</a>
                        </span><span class="view">22 人浏览</span>
                        
                        发布于 <span class="gray">2021-01-17 09:40</span>
                    </div>
                    <!--end: entry_footer -->
                </div>
                <!--end: content -->
                <div class="clear">
                </div>
            </div>
            <!--end: news_block -->
            <div class="clear">
            </div>
            <div class="news_block" id="entry_685401">
                <div class="action">
                    <div class="diggit" onclick="VoteNews(685401,'agree')">
                        <span id="digg_num_685401" class="diggnum">0</span>
                    </div>
                    <div class="clear"></div>
                    <div id="digg_tip_685401" class="digg-tip"></div>
                </div>
                <!--end: action -->
                <div class="content">
                    <h2 class="news_entry">
                        <a href="/n/685401/" target="_blank">上汽集团王晓秋：五菱宏光MINI购买者中"90后"超50%</a>
                    </h2>
                    <div class="entry_summary" style="display: block;">
                        <a href="/n/topic_2702.htm"><img src="https://img2020.cnblogs.com/news_topic/20201015085823646-279798419.png" class="topic_img" alt=""></a>
                        21 财经 APP 宋豆豆广州报道 “得益于我国经济和整体车市的快速反弹，全年中国新能源车销量重回增长轨道。分析销量结构特征，增量主要来自于两类产品：一类是高端电动车产品，另一类是以五菱宏光 MINI 为代表的经济型代步产品。”1 月 16 日，上海汽车集团股份有限公司总裁王晓秋在中国电动汽车百人会
                    </div>
                    <div class="entry_footer">
                        <a href="//home.cnblogs.com/u/itwriter/" class="gray" target="_blank">
                            itwriter
                        </a>投递 
                        <span class="comment">
                            <a href="/n/685401#comment" class="gray" target="_blank">评论(0)</a>
                        </span><span class="view">67 人浏览</span>
                        <span class="tag"> <a href="/n/tag/%E4%BA%94%E8%8F%B1%E5%AE%8F%E5%85%89/" class="gray">五菱宏光</a> </span>
                        发布于 <span class="gray">2021-01-17 09:35</span>
                    </div>
                    <!--end: entry_footer -->
                </div>
                <!--end: content -->
                <div class="clear">
                </div>
            </div>
            <!--end: news_block -->
            <div class="clear">
            </div>
    </div>
    <div class="pager"><a href="/" class="p_1 current">1</a><a href="/n/page/2/" class="p_2 middle">2</a><a href="/n/page/3/" class="p_3 middle">3</a><a href="/n/page/4/" class="p_4 middle">4</a><a href="/n/page/5/" class="p_5 middle">5</a><a href="/n/page/6/" class="p_6 middle">6</a><a href="/n/page/7/" class="p_7 middle">7</a><a href="/n/page/8/" class="p_8 middle">8</a><a href="/n/page/9/" class="p_9 middle">9</a><span class="ellipsis">···</span><a href="/n/page/100/" class="p_100 last">100</a><a href="/n/page/2/">Next &gt;</a></div>
</div>


<script type="text/javascript">
    $(function () {
        LoadNewsCategory("NewsCategoryId",11,0);
        //新闻列表-右侧编辑推荐新闻
        CommonLoadNews("/NewsAjax/GetRecommendNews", "RecommendNewsId", 7);
        //新闻列表-右侧今日新闻排行
        CommonLoadNews("/NewsAjax/GetHotNews", "HotNewsId", 10);
        //新闻列表-右侧24小时推荐排行
        CommonLoadNews("/NewsAjax/GetHotByDiggCount", "HotByDiggCountId", 7);
        //新闻列表-右侧热门IT新闻
        CommonLoadNews("/NewsAjax/GetRecentHotNews", "RecentHotNewsId", 10);
        //新闻列表-右侧最新评论
        LoadSideComments("NewsIndexCommentsId", 15);
        CheckAudit();
        LoadIndexSideInfo();
    });
</script>
        <div id="sideright">
            
    <div style="margin-top:25px;">
        <span id="lbAuditTips" style="display:none;"></span>
        <div class="news_home_navlink">
            <div id="rss_sub_top" class="rss_sub">
                <a href="http://feed.cnblogs.com/news/rss" title="博客园IT新闻RSS订阅">
                    <img src="//common.cnblogs.com/images/icon_rss.gif" alt="RSS订阅">
                </a>
            </div>
            <div style="line-height:30px;">
                &gt; <a href="https://www.cnblogs.com/news/" class="big">新闻栏目</a><br>
                &gt; <a href="/n/date/" class="big">新闻日历</a><br>
                &gt; <a href="/n/topiclist/" class="big">新闻主题</a><br>
            </div>
        </div>
        <div class="clear">
        </div>
        <br>
        <div id="side_right_search">
            <input type="text" id="google_search_q" size="27" class="side_right_search_q" onkeydown="return google_search_enter(event);">
            <input type="submit" name="sa" value="搜索新闻" class="side_right_search_sa" onclick="return google_search();">
        </div>
<div class="side_block">
    <div class="a4content" id="e2">
        <div id="div-gpt-ad-1533633736227-1" style="height:250px; width:300px;">
            <script>
                googletag.cmd.push(function () { googletag.display('div-gpt-ad-1533633736227-1'); });
            </script>
        </div>
    </div>
</div>        <div class="side_block" id="cate_news">
            <h3 class="title_yellow">
                新闻类别
            </h3>
            <div class="indent" id="NewsCategoryId">
            </div>
        </div>
        <div id="HotNews1_panelToday">
            <div class="side_block" id="last_news">
                <h3 class="title_blue">
                    今日新闻排行
                </h3>
                <ul class="topnews block_list bt" id="HotNewsId">
                </ul>
            </div>
        </div>
        <div class="side_block">
            <h3 class="title_yellow">
                编辑推荐新闻
            </h3>
            <ul class="topnews block_list bt" id="RecommendNewsId">
            </ul>
        </div>
        <div id="HotNews1_panelDiggTop">
            <div class="side_block" id="Div1">
                <h3 class="title_green">
                    24小时推荐排行
                </h3>
                <ul class="topnews block_list bt" id="HotByDiggCountId">
                </ul>
            </div>
        </div>
        <div class="side_block" id="hot_news">
            <h3 class="title_red">
                热门IT新闻
            </h3>
            <ul class="topnews block_list bt" id="RecentHotNewsId">
            </ul>
        </div>
<div class="side_block">
    <div id="e3">
        <div id="div-gpt-ad-1533633736227-2" style="height:250px; width:300px;">
            <script>
                googletag.cmd.push(function () { googletag.display('div-gpt-ad-1533633736227-2'); });
            </script>
        </div>
    </div>
</div>        <div class="side_block">
            <h3 class="title_green">
                最新评论
            </h3>
            <ul class="block_list" id="NewsIndexCommentsId">
            </ul>
            <a href="/Comment">
                <img src="/Images/more_comment.gif" title="更多最新评论" style="float: right; margin: 7px;" alt="">
            </a>
            <div style="clear: both;">
            </div>
        </div>
        <a name="more"></a>
        <div id="rss_sub_bottom" class="rss_sub">
            <a href="http://feed.cnblogs.com/news/rss" title="博客园IT新闻RSS订阅">
                <img src="//common.cnblogs.com/images/icon_rss_news.gif" alt="RSS订阅">
            </a>
            <a href="//news.cnblogs.com/m" rel="nofollow" title="博客园新闻频道手机版">
                <img src="/Images/ico_ing_cellphone.gif" alt="手机版">
            </a>
        </div>
    </div>

        </div>
        <div class="clear">
        </div>
        <div id="footer">
            <div id="foot">
                <a href="//www.cnblogs.com/AboutUS.aspx">关于博客园</a>
                <a href="//www.cnblogs.com/ContactUs.aspx">联系我们</a>
                <a href="//www.cnblogs.com/ad.aspx">广告服务</a>
                <a href="https://beian.miit.gov.cn" target="_blank">沪ICP备09004260号</a>
                <span>©2004-2021</span>
                <a href="//www.cnblogs.com">博客园</a>
                <span id="powered_by">Powered by .NET on Kubernetes</span>
            </div>
            <div id="footMobile" style="display:none;">
                <span>©2004-2021</span> <a href="//www.cnblogs.com">博客园</a>
            </div>
        </div>
        <script type="text/javascript">
            var _gaq = _gaq || [];
            _gaq.push(['_setAccount', 'UA-476124-8']);
            _gaq.push(['_trackPageview']);
            (function () {
                var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
                ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
                var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
            })();
        </script>
    </div>
</body>
</html>
'''

'''
字符有换行时， 有些换行符带着 (.*?)匹配不到 就和很蛋疼
后来认识了\s 和\S
是完全通配的意思，\s是指空白，包括空格、换行、tab缩进等所有的空白，而\S刚好相反
这样一正一反下来，就表示所有的字符，完全的，一字不漏的。
'''

#此处href前面没有加?号，因为要贪婪匹配，右侧先匹配到Next,Next左侧找到最近的href
regex_str = '[\s\S]*href="(.*)">Next[\s\S]*?'
# <a href="/n/page/2/">Next &gt;</a></div>
result = re.match(regex_str,listStr)
print(result.group(1))

