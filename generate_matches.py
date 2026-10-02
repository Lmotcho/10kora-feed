import json
from datetime import datetime

# محرك التوليد الآلي لمباريات وتوقعات 10KoraStats
# يمكن ربطه بأي API خارجي (مثل API-Football) أو جدول المباريات
def generate_today_feed():
    today_str = datetime.utcnow().strftime('%Y-%m-%d')
    
    # نموذج البيانات المحدثة يومياً (يحسبها الروبوت تلقائياً)
    today_matches = [
        {
            "id": 1,
            "category": "ucl",
            "league": "دوري أبطال أوروبا - جولة اليوم",
            "time": f"تحديث اليوم {today_str} • 20:00 GMT",
            "alert": "🚨 رصد تدفق أموال ذكية للمباراة",
            "home": {
                "name": "ريال مدريد",
                "logo": "https://media.api-sports.io/football/teams/541.png",
                "rank": 1
            },
            "away": {
                "name": "مانشستر سيتي",
                "logo": "https://media.api-sports.io/football/teams/50.png",
                "rank": 2
            },
            "referee": "طاقم تحكيم نخبوي أوروبي",
            "hRate": 48,
            "aRate": 28,
            "dRate": 24,
            "safe": { "tip": "أكثر من 1.5 هدف", "prob": "90%", "odds": "1.30" },
            "med": { "tip": "كلا الفريقين يسجلان (BTTS)", "prob": "70%", "odds": "1.80" },
            "vip": { "tip": "فوز ريال مدريد أو تعادل + ركنيات +8.5" },
            "corners": "+9.5 ركنية (احتمال 78%)",
            "cards": "+4.5 بطاقة ملونة",
            "scoreSim": "2 - 1 أو 2 - 2"
        },
        {
            "id": 2,
            "category": "spl",
            "league": "دوري روشن السعودي",
            "time": f"المملكة أرينا • 18:00 GMT",
            "alert": "قمة الجولة - صراع الصدارة",
            "home": {
                "name": "الهلال",
                "logo": "https://media.api-sports.io/football/teams/2939.png",
                "rank": 1
            },
            "away": {
                "name": "النصر",
                "logo": "https://media.api-sports.io/football/teams/2932.png",
                "rank": 2
            },
            "referee": "حكم أجنبي (معدل بطاقات مرتفع)",
            "hRate": 52,
            "aRate": 26,
            "dRate": 22,
            "safe": { "tip": "فرصة مزدوجة (الهلال 1X)", "prob": "92%", "odds": "1.34" },
            "med": { "tip": "أكثر من 9.5 ركنية", "prob": "74%", "odds": "1.92" },
            "vip": { "tip": "الهلال يفوز + أهداف الشوطين" },
            "corners": "+10.5 ركنية",
            "cards": "+5.5 بطاقة",
            "scoreSim": "3 - 1 أو 2 - 2"
        }
    ]

    with open("today_matches.json", "w", encoding="utf-8") as f:
        json.dump(today_matches, f, ensure_ascii=False, indent=2)

    print("Successfully generated today_matches.json!")

if __name__ == "__main__":
    generate_today_feed()
