def format_prepare(
    event,
    area,
    fundamental
):

    buy_low, buy_high = (
        area["buy_area"]
    )

    sell_low, sell_high = (
        area["sell_area"]
    )

    return f"""
🚨 <b>HIGH IMPACT NEWS PREPARE</b>

⏰ <b>30 MENIT MENUJU NEWS</b>

🇺🇸 <b>{event.title}</b>

🔥 Impact: <b>{event.impact}</b>

━━━━━━━━━━━━━━━━━━

🧠 <b>POTENSI DAMPAK XAUUSD</b>

Bias fundamental:
<b>{fundamental["bias"]}</b>

Fundamental Score:
<b>{fundamental["score"]}/100</b>

━━━━━━━━━━━━━━━━━━

🎯 <b>AREA HARGA</b>

🟢 BUY AREA
<code>{buy_low:.2f} - {buy_high:.2f}</code>

🔴 SELL AREA
<code>{sell_low:.2f} - {sell_high:.2f}</code>

📌 Support:
<code>{area["support"]:.2f}</code>

📌 Resistance:
<code>{area["resistance"]:.2f}</code>

━━━━━━━━━━━━━━━━━━

📊 <b>DATA EKONOMI</b>

Forecast:
<code>{event.forecast}</code>

Previous:
<code>{event.previous}</code>

━━━━━━━━━━━━━━━━━━

⚠️ High Impact News berpotensi
menyebabkan volatilitas tinggi.

Hindari entry terlalu dekat dengan
waktu rilis jika belum ada konfirmasi.

━━━━━━━━━━━━━━━━━━

🔗 <b>SUMBER RESMI</b>

<a href="{event.source_url}">
{event.source_name}
</a>

━━━━━━━━━━━━━━━━━━

🤖 <b>XAU AI FUNDAMENTAL</b>
"""


def format_result(
    event,
    area,
    fundamental
):

    buy_low, buy_high = (
        area["buy_area"]
    )

    sell_low, sell_high = (
        area["sell_area"]
    )

    return f"""
🚨 <b>HIGH IMPACT NEWS RESULT</b>

🇺🇸 <b>{event.title}</b>

━━━━━━━━━━━━━━━━━━

📊 <b>ACTUAL</b>
<code>{event.actual}</code>

📊 <b>FORECAST</b>
<code>{event.forecast}</code>

📊 <b>PREVIOUS</b>
<code>{event.previous}</code>

━━━━━━━━━━━━━━━━━━

🧠 <b>FUNDAMENTAL IMPACT</b>

Bias:
<b>{fundamental["bias"]}</b>

Score:
<b>{fundamental["score"]}/100</b>

━━━━━━━━━━━━━━━━━━

🎯 <b>UPDATED XAUUSD AREA</b>

🟢 BUY AREA
<code>{buy_low:.2f} - {buy_high:.2f}</code>

🔴 SELL AREA
<code>{sell_low:.2f} - {sell_high:.2f}</code>

📌 Support:
<code>{area["support"]:.2f}</code>

📌 Resistance:
<code>{area["resistance"]:.2f}</code>

━━━━━━━━━━━━━━━━━━

⚠️ Tunggu volatilitas awal mereda
sebelum mengambil posisi.

━━━━━━━━━━━━━━━━━━

🔗 <b>SUMBER RESMI</b>

<a href="{event.source_url}">
{event.source_name}
</a>

━━━━━━━━━━━━━━━━━━

🤖 <b>XAU AI FUNDAMENTAL</b>
"""
