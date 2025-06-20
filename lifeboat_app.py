def lifeboat_calculator(DS, CD, R, S, HR, W):
    Sp = DS * CD
    Sp_wk = Sp / W
    Gross = (R + Sp + S) / 0.88
    H = Gross / HR
    HW = H / W
    WD = (H * 5) / HW
    CD_calculated = (WD / 5) * 7
    
    return {
        "Spending": Sp,
        "Weekly Spending": Sp_wk,
        "Gross Income Needed": Gross,
        "Total Hours Needed": H,
        "Hours per Week": HW,
        "Work Days": WD,
        "Calendar Days": CD_calculated
    }
