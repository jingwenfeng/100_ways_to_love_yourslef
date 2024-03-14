from flask import Flask, render_template_string, jsonify
import random

app = Flask(__name__)

# 假设我们有500个活动，这里只演示部分
activities_en = [
    "Make a new recipe",
    "Learn a new language",
    "Engage in home fitness",
    "Try meditating for 5 minutes",
    "Read a book and share key points",
    "Boston handicraft workshop",
    "Make handicrafts",
    "Eat delicious snacks",
    "Learn a new musical instrument",
    "Shoot a daily Vlog",
    "Boston Conference",
    "Boston specialty restaurant tour",
    "Try new photography techniques",
    "Write a personal diary",
    "Go for an outdoor hike",
    "Boston historical novel writing",
    "Have a snack",
    "Explore the local market",
    "Try indoor gardening",
    "Learn programming basics",
    "Make DIY home decor",
    "Try being vegetarian for a day",
    "Make your own skincare products",
    "Shoot a dance video",
    "Practice yoga",
    "Learn how to make cocktails",
    "Make a personal cookbook",
    "Try digital painting",
    "Learn calligraphy",
    "Create a personal podcast",
    "Shoot a short film",
    "Learn fashion design",
    "Bookstore tour",
    "Try making ceramics",
    "Organize an online book club",
    "Make your own music",
    "Learn magic tricks",
    "Undertake a personal branding design",
    "Create a personal travel guide",
    "Learn pet training skills",
    "Take an online education course",
    "Make a simple game",
    "Try outdoor rock climbing",
    "Campus walk",
    "Engage in cultural exchange",
    "Learn gardening skills",
    "Explore Boston's food market",
    "Make handmade soap",
    "Take a series of fashion photos",
    "Learn home woodworking crafts",
    "Create a personal website",
    "Learn first aid skills",
    "Try different art styles",
    "Create an online course",
    "Learn electronic music production",
    "Try watercolor painting",
    "Conduct a science experiment",
    "Learn antique restoration",
    "Make a micro-movie",
    "Organize a family movie night",
    "Undergo personal time management training",
    "Try outdoor camping",
    "Learn to make candles",
    "Create a personal fashion magazine",
    "Learn basic photography courses",
    "Try making your own hair accessories",
    "Learn how to make video games",
    "Try baking bread",
    "Learn basic woodworking skills",
    "Create and maintain a personal financial budget",
    "Learn Go or chess",
    "Try garden design",
    "Learn how to knit sweaters",
    "Create your own e-magazine",
    "Learn how to use a 3D printer",
    "Try making handmade paper",
    "Learn basic car maintenance",
    "Make a family emergency kit",
    "Learn how to do home maintenance",
    "Try making home decorations",
    "Learn how to pack luggage efficiently",
    "Create a personal fitness plan",
    "Learn how to make homemade jam",
    "Try learning calligraphy",
    "Learn how to make handmade soap",
    "Create a personal development plan",
    "Learn how to do home care",
    "Try learning embroidery",
    "Learn how to make handmade skincare products",
    "Create a personal travel guide",
    "Learn how to make handmade chocolates",
    "Practice public speaking",
    "Learn how to make homemade facial masks",
    "Create a home accounting system",
    "Learn how to cook foreign dishes",
    "Try learning to dance",
    "Learn how to make handmade jewelry",
    "Create a set of personal efficiency tools",
    "Learn how to cook vegetarian dishes",
    "Try learning painting",
    "Learn how to make homemade shampoo",
    "Make a home safety inspection list",
    "Learn how to cook healthy desserts",
    "Try learning sculpture",
    "Learn how to make homemade candies",
    "Create a personal brand logo",
    "Learn how to cook low-calorie foods",
    "Try learning programming",
    "Learn how to make homemade soap",
    "Make a personal health plan",
    "Learn how to cook festive meals",
    "Try learning digital drawing",
    "Learn how to make homemade facial cleanser",
    "Make a personal learning plan",
    "Learn how to cook traditional dishes",
    "Try learning illustration",
    "Learn how to make homemade hand cream",
    "Make a home maintenance list",
    "Learn how to cook seasonal foods",
    "Try learning UI/UX design",
    "Learn how to make homemade facial cleanser",
    "Make a home renovation plan",
    "Learn how to cook quick simple meals",
    "Try learning graphic design",
    "Learn how to make homemade conditioner",
    "Make a home energy-saving plan",
    "Learn how to cook healthy snacks",
    "Try learning architectural design",
    "Learn how to make homemade shower gel",
    "Make a home disaster preparedness plan",
    "Learn how to cook late-night gourmet food",
    "Try learning landscape design",
    "Learn how to make homemade lip scrub",
    "Make a personal life guide",
    "Learn how to cook healthy staple food",
    "Try learning interior design",
    "Learn how to make homemade skincare oil",
    "Make a home activity plan",
    "Learn how to cook home-cooked dishes",
    "Try learning fashion design",
    "Learn how to make homemade body lotion",
    "Make a personal time management tool",
    "Learn how to cook creative desserts",
    "Try learning jewelry design",
    "Learn how to make homemade foot soak",
    "Make a personal morning routine",
    "Learn how to cook healthy soups",
    "Try learning product design",
    "Learn how to make homemade massage oil",
    "Make a home entertainment plan",
    "Learn how to cook quick breakfasts",
    "Try learning furniture design",
    "Learn how to make homemade exfoliating scrub",
    "Make a personal nighttime routine",
    "Learn how to cook simple lunches",
    "Try learning lighting design",
    "Learn how to make homemade lip exfoliator",
    "Make a home health plan",
    "Learn how to cook nutritious dinners",
    "Try learning gardening design",
    "Learn how to make homemade body scrub",
    "Make a personal health goal list",
    "Learn how to cook for one",
    "Try learning pet design",
    "Learn how to make homemade hand sanitizer",
    "Make a family celebration activity plan",
    "Learn how to cook nutritious drinks",
    "Try learning food design",
    "Learn how to make homemade bathroom cleaner",
    "Make a personal life goal list",
    "Learn how to cook fast food dinners",
    "Try learning car design",
    "Learn how to make homemade kitchen cleaner",
    "Make a family fire safety drill plan",
    "Learn how to cook healthy drinks",
    "Try learning ship design",
    "Learn how to make homemade glass cleaner",
    "Make a personal development goal list",
    "Learn how to cook five-minute snacks",
    "Try learning airplane design",
    "Learn how to make homemade floor cleaner",
    "Make a family emergency contact plan",
    "Learn how to cook ten-minute fast food",
    "Try learning rocket design",
    "Learn how to make homemade furniture polish",
    "Make a personal financial plan",
    "Learn how to cook healthy lunchboxes",
    "Try learning bicycle design",
    "Learn how to make homemade leather care balm",
    "Make a family fire safety plan"
]

activities_zh = [
    "做一道新菜谱",
    "学习一门新语言",
    "进行家庭健身",
    "尝试冥想5分钟",
    "读一本书并分享要点",
    "波士顿手工艺品制作课",
    "制作手工艺品",
    "吃美味的点心",
    "学习新的乐器",
    "拍摄日常Vlog",
    "波士顿 Conference",
    "波士顿特色餐厅之旅",
    "尝试新的摄影技巧",
    "编写个人日记",
    "进行户外徒步",
    "波士顿历史小说创作",
    "吃一份小吃",
    "探索本地市场",
    "尝试室内园艺",
    "学习编程基础",
    "制作DIY家居装饰",
    "尝试素食一天",
    "制作自己的护肤品",
    "拍摄一段舞蹈视频",
    "练习瑜伽",
    "学习如何做鸡尾酒",
    "制作一本个人食谱",
    "尝试数字绘画",
    "学习手写书法",
    "创建个人播客",
    "拍摄一部短片",
    "学习服装设计",
    "书店之旅",
    "尝试制作陶瓷",
    "组织一次线上读书会",
    "制作自己的音乐",
    "学习魔术技巧",
    "进行一次自我品牌设计",
    "制作个人旅行指南",
    "学习宠物训练技巧",
    "进行一次在线教育课程",
    "制作一款简单的游戏",
    "尝试户外攀岩",
    "校园漫步"
    "进行一次文化交流",
    "学习园艺技能",
    "波士顿食品市场探索",
    "制作手工皂",
    "拍摄一系列时尚照片",
    "学习家庭木工工艺",
    "制作一个个人网站",
    "学习急救技能",
    "尝试不同的艺术风格",
    "制作一个在线课程",
    "学习电子音乐制作",
    "尝试水彩画",
    "进行科学实验",
    "学习古董修复",
    "制作微电影",
    "组织家庭电影之夜",
    "进行个人时间管理培训",
    "尝试户外露营",
    "学习自制蜡烛",
    "制作个人时尚杂志",
    "学习基础摄影课程",
    "尝试做自己的发饰",
    "学习如何制作视频游戏",
    "尝试烘焙面包",
    "学习基础的木工技能",
    "制作和维护个人财务预算",
    "学习围棋或国际象棋",
    "尝试园艺设计",
    "学习怎样编织毛衣",
    "制作一个自己的电子杂志",
    "学习怎样使用3D打印机",
    "尝试制作手工纸",
    "学习基本的汽车维修",
    "制作一个家庭应急准备包",
    "学习如何做家庭保养",
    "尝试做家庭装饰品",
    "学习怎样有效地打包行李",
    "制作一个个人健身计划",
    "学习怎样自制果酱",
    "尝试学习书法",
    "学习怎样制作手工香皂",
    "制作一个个人发展计划",
    "学习怎样做家庭护理",
    "尝试学习刺绣",
    "学习怎样制作手工护肤品",
    "制作一份个人旅游指南",
    "学习怎样做手工巧克力",
    "尝试练习公共演讲",
    "学习怎样制作自制面膜",
    "制作一个家庭记账系统",
    "学习怎样烹饪外国菜肴",
    "尝试学习舞蹈",
    "学习怎样制作手工饰品",
    "制作一套个人效率工具",
    "学习怎样烹饪素食料理",
    "尝试学习绘画",
    "学习怎样制作自制洗发水",
    "制作一份家庭安全检查单",
    "学习怎样烹饪健康甜点",
    "尝试学习雕塑",
    "学习怎样制作自制糖果",
    "制作一个个人品牌标志",
    "学习怎样烹饪低卡路里食物",
    "尝试学习编程",
    "学习怎样制作自制肥皂",
    "制作一份个人健康计划",
    "学习怎样烹饪节日大餐",
    "尝试学习数字绘图",
    "学习怎样制作自制洗面奶",
    "制作一份个人学习计划",
    "学习怎样烹饪传统菜肴",
    "尝试学习插画",
    "学习怎样制作自制护手霜",
    "制作一份家庭维修清单",
    "学习怎样烹饪节气食物",
    "尝试学习UI/UX设计",
    "学习怎样制作自制洁面乳",
    "制作一个家庭装修计划",
    "学习怎样烹饪快速简餐",
    "尝试学习平面设计",
    "学习怎样制作自制护发素",
    "制作一份家庭节能计划",
    "学习怎样烹饪健康零食",
    "尝试学习建筑设计",
    "学习怎样制作自制沐浴露",
    "制作一份家庭防灾计划",
    "学习怎样烹饪宵夜美食",
    "尝试学习景观设计",
    "学习怎样制作自制润唇膏",
    "制作一份个人生活指南",
    "学习怎样烹饪健康主食",
    "尝试学习室内设计",
    "学习怎样制作自制护肤油",
    "制作一份家庭活动计划",
    "学习怎样烹饪家常菜",
    "尝试学习服装设计",
    "学习怎样制作自制身体乳",
    "制作一个个人时间管理器",
    "学习怎样烹饪创意甜品",
    "尝试学习珠宝设计",
    "学习怎样制作自制足浴盐",
    "制作一份个人早晨例行公事",
    "学习怎样烹饪健康汤品",
    "尝试学习产品设计",
    "学习怎样制作自制按摩油",
    "制作一个家庭娱乐计划",
    "学习怎样烹饪快手早餐",
    "尝试学习家具设计",
    "学习怎样制作自制去角质膏",
    "制作一份个人夜间例行公事",
    "学习怎样烹饪简易午餐",
    "尝试学习照明设计",
    "学习怎样制作自制唇部磨砂膏",
    "制作一个家庭健康计划",
    "学习怎样烹饪营养晚餐",
    "尝试学习园艺设计",
    "学习怎样制作自制身体磨砂膏",
    "制作一个个人健康目标清单",
    "学习怎样烹饪一人食",
    "尝试学习宠物设计",
    "学习怎样制作自制洗手液",
    "制作一份家庭庆祝活动计划",
    "学习怎样烹饪营养饮品",
    "尝试学习食品设计",
    "学习怎样制作自制浴室清洁剂",
    "制作一个个人生活目标清单",
    "学习怎样烹饪速食晚餐",
    "尝试学习汽车设计",
    "学习怎样制作自制厨房清洁剂",
    "制作一份家庭安全演练计划",
    "学习怎样烹饪健康饮品",
    "尝试学习船舶设计",
    "学习怎样制作自制玻璃清洁剂",
    "制作一个个人发展目标清单",
    "学习怎样烹饪五分钟小吃",
    "尝试学习飞机设计",
    "学习怎样制作自制地板清洁剂",
    "制作一份家庭紧急联络计划",
    "学习怎样烹饪十分钟快餐",
    "尝试学习火箭设计",
    "学习怎样制作自制家具护理油",
    "制作一个个人理财计划",
    "学习怎样烹饪健康便当",
    "尝试学习自行车设计",
    "学习怎样制作自制皮革护理膏",
    "制作一份家庭消防安全计划"
]


html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Daily Activity Selector | 每日活动选择器</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 20px;
        }
        #activity {
            font-size: 24px;
            font-weight: bold;
            color: #333;
            margin: 20px;
        }
        button {
            margin-top: 20px;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div id="activity">Click the button to randomly select an activity! | 点击按钮随机选择一个活动！</div>
    <button onclick="getActivity()">Randomly Select | 随机选择</button>

    <script>
        function getActivity() {
            fetch('/get_activity')
            .then(response => response.json())
            .then(data => {
                document.getElementById('activity').innerHTML = data.activity_en + " | " + data.activity_zh;
            });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template)

@app.route('/get_activity')
def get_activity():
    random_index = random.randint(0, len(activities_zh) - 1)
    selected_activity_en = activities_en[random_index]
    selected_activity_zh = activities_zh[random_index]
    return jsonify(activity_en=selected_activity_en, activity_zh=selected_activity_zh)

if __name__ == '__main__':
    app.run(debug=True)
