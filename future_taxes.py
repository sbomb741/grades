







class tax_scenario:

    def __init__(self, 
                 gross_household_income=90000, 
                 retirement_pct=0,
                 hsa_monthly_amt=0,
                 hsa_yearly_amt=0,
                 real_hsa=True,
                 insurance_monthly_amt=0,
                 insurance_yearly_amt=0,
                 married_deduction = 30000):
        
        # Declare self variables 
        self.gross_household_income = gross_household_income
        self.retirement_pct = retirement_pct
        self.hsa_monthly_amt = hsa_monthly_amt
        self.hsa_yearly_amt = hsa_yearly_amt
        self.real_hsa = real_hsa
        self.insurance_monthly_amt = insurance_monthly_amt
        self.insurance_yearly_amt = insurance_yearly_amt
        self.married_deduction = married_deduction

        # Amount to decrease gross amount by due to retirement/healthcare
        self.adjusted_gross_income = gross_household_income
        self.net_income = gross_household_income

        self.retirement = 0
        self.hsa = 0
        self.insurance = 0

        self.total_tax = 0


    # ADJUSTED GROSS INCOME (AGI) FUNCTIONS
    def adjust_gross_income(self):
        self.deductRetirement(self.retirement_pct)
        self.deductHSA(self.hsa_monthly_amt, self.hsa_yearly_amt)
        self.deductInsurance(self.insurance_monthly_amt, self.insurance_yearly_amt)


    def deductRetirement(self, yearly_percentage):
        self.retirement = self.gross_household_income * (yearly_percentage * .01)
        self.adjusted_gross_income = self.adjusted_gross_income - self.retirement
    

    def deductHSA(self, monthly_amount=0, yearly_amount=0):
        if yearly_amount == 0:
            yearly_amount = monthly_amount*12
        
        self.hsa = yearly_amount

        if self.real_hsa:
            self.adjusted_gross_income = self.adjusted_gross_income - self.hsa

        self.updateNetIncome()


    def deductInsurance(self, monthly_amount=0, yearly_amount=0):
        if yearly_amount == 0:
            yearly_amount = monthly_amount*12

        self.insurance+=yearly_amount

        if self.real_hsa:
            self.adjusted_gross_income = self.adjusted_gross_income - self.insurance

        self.updateNetIncome()


    # TAXES FUNCTIONS
    def deductTaxes(self):
        self.deductFederalIncomeTax()
        self.deductStateIncomeTax()
        self.deductMedicareSSNTax()


    def deductFederalIncomeTax(self):
        # Calculate federal taxes based on AGI minus deduction
        new_taxable_income = self.adjusted_gross_income - self.married_deduction
        total_tax = 0
        bottom_range = 0

        # Tax brackets 2025
        married_joint_tax_bracket_thresholds = [23850, 96950, 206700, 394600]
        tax_rates = [.10, .12, .22, .24]
        
        # Calculate taxes based on the brackets
        for i in range(len(married_joint_tax_bracket_thresholds)):
            bracket_threshold = married_joint_tax_bracket_thresholds[i]
            tax_rate = tax_rates[i]

            if new_taxable_income > bracket_threshold:
                total_tax += tax_rate * (bracket_threshold - bottom_range)
                bottom_range = bracket_threshold

            else:
                taxable_range = new_taxable_income - bottom_range
                total_tax += tax_rate * taxable_range

                # update the class total tax amount, and update the net income
                self.total_tax = total_tax
                self.updateNetIncome()
                break

        
    def deductStateIncomeTax(self):
        self.updateNetIncome()
        return


    def deductMedicareSSNTax(self):
        """[Real] HSA contributions deduct FICA taxes; insurance and retirement do not"""
        # Tax percentages
        if self.real_hsa:
            hsa_amount = self.hsa
        else:
            hsa_amount = 0
        
        social_security_tax = (self.gross_household_income-hsa_amount) * 0.062
        medicare_tax = (self.gross_household_income-hsa_amount) * 0.0145
        FICA_taxes = social_security_tax + medicare_tax

        # update the class total tax amount and update net income
        self.total_tax += FICA_taxes
        self.updateNetIncome()

    
    # Net income helper function
    def updateNetIncome(self):
        if self.real_hsa:
            self.net_income = self.adjusted_gross_income - self.total_tax 
        else:
            self.net_income = self.adjusted_gross_income - self.total_tax - self.hsa - self.insurance 



# Individual + Spouse (2024)
m_silverPPO = tax_scenario(hsa_yearly_amt=5500,
                           real_hsa=True,
                           insurance_monthly_amt=1000)
m_goldPOS = tax_scenario(hsa_yearly_amt=7000,
                         real_hsa=True,
                         insurance_monthly_amt=800)

# Individual (2024)
s_silverPPO = tax_scenario(hsa_yearly_amt=2750,
                           real_hsa=True,
                           insurance_monthly_amt=500)
s_goldPOS = tax_scenario(hsa_yearly_amt=3500,
                         real_hsa=True,
                         insurance_monthly_amt=300)


# Medishare (2024)
no_insurance = tax_scenario(hsa_yearly_amt=0,
                            insurance_monthly_amt=0)

no_insurance.adjust_gross_income()
no_insurance.deductTaxes()

s6k = tax_scenario(hsa_yearly_amt=6000,
                   real_hsa=False,
                   insurance_monthly_amt=236)
s6k.adjust_gross_income()
s6k.deductTaxes()

print(s6k.net_income+s6k.hsa+s6k.insurance)
s_3k = 3000+311*12
s_6k = 6000+236*12
s_9k = 9000+191*12
s_12k = 12000+141*12

m_3k = 3000+526*12
m_6k = 6000+393*12
m_9k = 9000+312*12
m_12k = 12000+221*12


insurance_list = [m_silverPPO, m_goldPOS, s_silverPPO, s_goldPOS, no_insurance]
for option in insurance_list:
    option.adjust_gross_income()
    option.deductTaxes()

medishare_list = [s_3k, s_6k, s_9k, s_12k, m_3k, m_6k, m_9k, m_12k]
medishare_slist = [s_3k, s_6k, s_9k, s_12k]
medishare_mlist = [m_3k, m_6k, m_9k, m_12k]
med_net = no_insurance.net_income

print(med_net)


# Print statements
print (f"\nNo insurance net income: {med_net}\n\n")

# Individual and Spouse Coverage Comparison
print(f"m_silverPPO: {m_silverPPO.net_income}")
print(f"m_goldPOS: {m_goldPOS.net_income}\n")

print("Take home pay after FULL medishare deductable amounts 3k, 6k, 9k, 12k are met")
for amt in medishare_mlist:
    print (med_net - amt)
print("\n")

print("Take home pay after NO medishare deductable 3k, 6k, 9k, 12k amounts are met")
i = 3000
for amt in medishare_mlist:
    print (med_net - amt + i)
    i+=3000
print("\n")

# Individual Coverage Comparison
print(f"s_silverPPO: {s_silverPPO.net_income}")
print(f"s_goldPOS: {s_goldPOS.net_income}")

print("Take home pay after FULL medishare deductable amounts 3k, 6k, 9k, 12k are met")
for amt in medishare_slist:
    print (med_net - amt)
print("\n")

print("Take home pay after NO medishare deductable amounts 3k, 6k, 9k, 12k are met")
i = 3000
for amt in medishare_slist:
    print (med_net - amt + i)
    i+=3000
print("\n")