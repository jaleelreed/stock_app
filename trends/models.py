from django.db import models

# Create your models here.

class StockApp(models.Model):
    id = models.BigIntegerField(primary_key=True, null=False)
    symbol = models.TextField(db_column='Symbol', blank=True, null=True)  # Field name made lowercase.
    dates = models.TextField(blank=True, null=True)
    consolidated_income = models.BigIntegerField(db_column='Consolidated Income', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cost_of_revenue = models.BigIntegerField(db_column='Cost of Revenue', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dividend_per_share = models.BigIntegerField(db_column='Dividend per Share', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ebit = models.BigIntegerField(db_column='EBIT', blank=True, null=True)  # Field name made lowercase.
    ebit_margin = models.BigIntegerField(db_column='EBIT Margin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ebitda = models.BigIntegerField(db_column='EBITDA', blank=True, null=True)  # Field name made lowercase.
    ebitda_margin = models.BigIntegerField(db_column='EBITDA Margin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    eps = models.BigIntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    eps_diluted = models.BigIntegerField(db_column='EPS Diluted', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    earnings_before_tax_margin = models.BigIntegerField(db_column='Earnings Before Tax Margin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    earnings_before_tax = models.BigIntegerField(db_column='Earnings before Tax', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    free_cash_flow_margin = models.BigIntegerField(db_column='Free Cash Flow margin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gross_margin = models.BigIntegerField(db_column='Gross Margin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gross_profit = models.BigIntegerField(db_column='Gross Profit', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    income_tax_expense = models.BigIntegerField(db_column='Income Tax Expense', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    interest_expense = models.BigIntegerField(db_column='Interest Expense', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    net_income = models.BigIntegerField(db_column='Net Income', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    net_income_discontinued_ops = models.BigIntegerField(db_column='Net Income - Discontinued ops', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    net_income_non_controlling_int = models.BigIntegerField(db_column='Net Income - Non-Controlling int', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    net_income_com = models.BigIntegerField(db_column='Net Income Com', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    net_profit_margin = models.BigIntegerField(db_column='Net Profit Margin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    operating_expenses = models.BigIntegerField(db_column='Operating Expenses', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    operating_income = models.BigIntegerField(db_column='Operating Income', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    preferred_dividends = models.BigIntegerField(db_column='Preferred Dividends', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    profit_margin = models.BigIntegerField(db_column='Profit Margin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    r_d_expenses = models.BigIntegerField(db_column='R&D Expenses', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    revenue = models.BigIntegerField(db_column='Revenue', blank=True, null=True)  # Field name made lowercase.
    revenue_growth = models.BigIntegerField(db_column='Revenue Growth', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sg_a_expense = models.BigIntegerField(db_column='SG&A Expense', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    weighted_avg_shs_out = models.BigIntegerField(db_column='Weighted Avg Shs Out', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    weighted_average_shs_out_dil = models.BigIntegerField(db_column='Weighted Average Shs Out_Dil', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'financials_data'

def __str__(self):
   return "{}:{}..".format(self.id, self.paragraph[:10])