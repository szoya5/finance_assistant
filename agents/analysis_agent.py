def get_aum_change(today_pct, yesterday_pct):
    return round(today_pct - yesterday_pct, 2)

def earnings_summary(results):
    summary = []
    for company, change in results.items():
        verdict = "beat estimates" if change > 0 else "missed estimates"
        summary.append(f"{company} {verdict} by {abs(change):.1f}%")
    return ", ".join(summary) 
