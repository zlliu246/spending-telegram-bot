def route(update, context):
    text = update.message.text
    
    month, *lines = text.split("\n")
    out = f"Month: {month}\n"

    d = {}
    for line in lines:
        day, *expenses = [i.strip() for i in line.split(",")]
        daytotal = 0
        for expense in expenses:
            try:
                daytotal += float(expense.split(" ")[-1])
                day = int(day)
            except:
                pass
        d[day] = daytotal

    totalspent = sum(list(d.values()))
    averagespent = totalspent / max(d.keys())

    out += f"Total Spent: ${totalspent:.2f}\nAverage Spent Per Day: ${averagespent:.2f}\n\n"

    for day,spent in d.items():
        out += f"day: {day}, spent: ${spent:.2f}\n"

    # telegram bot replies 
    update.message.reply_text(out.strip())
