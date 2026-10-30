import os
import discord
from discord.ext import commands
from google import genai

# إعداد مفتاح الـ API الخاص بـ Gemini
client = genai.Client(api_key="AQ.Ab8RN6L2u4zQjuwEA6bmApqZnCE_YPgbqqfh2K0dYDNNdXQdWg")

# إعدادات البوت وصلاحيات القراءة
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# آي دي الروم المخصص للأسئلة والمشاكل
TARGET_CHANNEL_ID = 1565703105264484515

@bot.event
async def on_ready():
    print(f"تم تسجيل الدخول بنجاح باسم: {bot.user}")
    print("البوت جاهز للعمل 24/7 وفي الروم المخصص!")

@bot.event
async def on_message(message):
    # تجاهل رسائل البوت نفسه لكي لا يحدث تداخل أو ردود لا نهائية
    if message.author == bot.user:
        return

    # التحقق من أن الرسالة أُرسلت في الروم المخصص فقط
    if message.channel.id == TARGET_CHANNEL_ID:
        user_msg = message.content.strip().lower()

        # 1. الرد الثابت عند السؤال عن الاسم (V AI)
        if any(word in user_msg for word in ["اسمك", "وش اسمك", "إيش اسمك", "مين أنت", "من أنت"]):
            await message.reply("اسمـي **V AI**.")
            return

        # 2. الرد الثابت عند السؤال عن فائدة أو تعريف السيرفر
        if any(word in user_msg for word in ["فائدة السيرفر", "وش السيرفر", "ايش السيرفر", "عن ايش السيرفر", "ايش فائدة السيرفر", "وش تسوون هنا", "ايش هذا السيرفر", "وش هذا السيرفر"]):
            await message.reply("هذا السيرفر هو **V Family Community**، مجتمع متكامل نلعب فيه ألعاب مختلفة ونجتمع مع الأصدقاء لأجواء ممتعة ورائعة!")
            return

        # 3. الرد الثابت عند السؤال عن القوانين (القوانين التي أرسلتها كاملة)
        if any(word in user_msg for word in ["قوانين", "الشروط", "القوانين", "النظام"]):
            rules_text = (
                "📜 **قوانين سيرفر V Family Community:**\n\n"
                "🔹 **القواعد الأساسية:**\n"
                "• **الاحترام:** ممنوع الشتم، الإهانة، أو العنصرية بكافة أنواعها.\n"
                "• **المحتوى:** ممنوع نشر المحتوى الحساس، الإباحي، أو العنيف.\n"
                "• **الأسماء والصور:** ممنوع منعاً باتاً استخدام الأسماء المخفية (الفارغة) أو الصور المخفية.\n"
                "• **الإعلانات:** ممنوع الترويج أو نشر الروابط (بالعام أو الخاص).\n"
                "• **الإزعاج:** ممنوع السبام، التكرار، والمنشن العشوائي للأعضاء والإدارة.\n"
                "• **الصوت والتذاكر:** ممنوع الأصوات المزعجة، التسجيل بدون إذن، أو فتح تذكرة بلا سبب واضح.\n\n"
                "⏱️ **أسباب التايم أوت (Timeout):**\n"
                "• السبام وتكرار الرسائل أو المنشن المزعج.\n"
                "• افتعال المشاكل والجدال في المحادثات العامة.\n"
                "• استخدام أصوات مزعجة في الرومات الصوتية.\n\n"
                "🚫 **أسباب الباند (Ban):**\n"
                "• السب والألفاظ الشديدة أو القذف.\n"
                "• الترويج للسيرفرات أو الحسابات الأخرى.\n"
                "• نشر محتوى إباحي، عنيف، أو مخالف للآداب.\n"
                "• تسريب معلومات، صور، أو محادثات خاصة.\n"
                "• شتم الإدارة أو الاعتداء على سياسة السيرفر."
            )
            await message.reply(rules_text)
            return

        # 4. الذكاء الاصطناعي الحقيقي الخاص بالسيرفر
        async with message.channel.typing():
            try:
                prompt = f"""أنت ذكاء اصطناعي رسمي وخاص بسيرفر دسكورد يسمى "V Family Community". 
مهمتك التحدث بذكاء واحترافية عالية وبنفس قوة ومستوى نموذج Gemini، لمساعدة الأعضاء والإجابة على أي أسئلة أو استفسارات عامة أو تقنية يطرحونها في السيرفر باللغة العربية بأسلوب ودود ولائق.

سؤال أو رسالة العضو: {message.content}"""
                
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                )
                
                reply_text = response.text

                if len(reply_text) > 2000:
                    chunks = [reply_text[i:i+1990] for i in range(0, len(reply_text), 1990)]
                    for chunk in chunks:
                        await message.reply(chunk)
                else:
                    await message.reply(reply_text)

            except Exception as e:
                await message.reply("عذراً، حدث خطأ مع نظام الذكاء الاصطناعي. يرجى المحاولة لاحقاً.")
                print(f"Error: {e}")

    await bot.process_commands(message)

# تشغيل البوت باستخدام الـ Token الخاص بك
bot.run("MTU2NTcwMDQ0NTk4MzIxMTYzMA.GalAH3.hjmN7VzBX0hYfy2JN81Tzk7zjoEBPDml8sZyuc")