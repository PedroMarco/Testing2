__author__ = 'acpb859'

EmployeeName=(str(input('Enter employee\'s name: ')))
HoursWeek=(eval(input('Enter number of hours worked in a week: ')))
HourlyPay=(eval(input('Enter hourly pay rate: ')))
TaxMain=(eval(input('Enter tax withholding rate: ')))
TaxRest=(eval(input('Enter Other tax withholding rate: ')))
GrossPay=HoursWeek*HourlyPay

print('Employee Name: ', EmployeeName)
print('Hours Worked: ', str(HoursWeek))
print('Pay Rate: ', str(HourlyPay))
print('Gross Pay: ', str(GrossPay))
print('Deductions:')
print('Tax Withholding (',str(TaxMain*100),'%): ',str(TaxMain*(HourlyPay*HoursWeek)))
print('Other Tax Withholding (',str(TaxRest*100),'%): ',str(TaxRest*(HourlyPay*HoursWeek)))
print('Total Deduction :',str((TaxMain*(HourlyPay*HoursWeek))+(TaxRest*(HourlyPay*HoursWeek))))
print()
print('Net Pay :',str(GrossPay-(((TaxMain*(HourlyPay*HoursWeek))+(TaxRest*(HourlyPay*HoursWeek))))))
