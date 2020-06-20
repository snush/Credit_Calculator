import math
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--principal', type=int)
parser.add_argument('--payment', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
args = parser.parse_args()

if args.interest is not None and len(sys.argv) == 5:
    interest = args.interest / (12 * 100)
    if args.type == "annuity":
        if args.periods is None:
            count_of_periods = math.log((args.payment / (args.payment - interest * args.principal)), 1 + interest)
            years, months = math.ceil(count_of_periods) // 12, math.ceil(count_of_periods) % 12
            if years == 0:
                print('You need {} months to repay this credit!'.format(months))
            elif months == 0:
                print('You need {} years to repay this credit!'.format(years))
            else:
                print('You need {} years and {} months to repay this credit!'.format(years, months))
            print('Overpayment = {}'.format(args.payment * math.ceil(count_of_periods) - args.principal))
        elif args.principal is None:
            credit_principal = args.payment / ((interest * (1 + interest) ** args.periods) /
                                                   ((1 + interest) ** args.periods - 1))
            print('Your credit principal = {}'.format(math.ceil(credit_principal)))
            print('Overpayment = {}'.format(args.payment * args.periods - math.ceil(credit_principal)))
        else:
            monthly_payment = args.principal * ((interest * (1 + interest) ** args.periods) /
                                                ((1 + interest) ** args.periods - 1))
            print('Your annuity payment = {}!'.format(math.ceil(monthly_payment)))
            print('Overpayment = {}'.format(math.ceil(monthly_payment) * args.periods - args.principal))
    elif args.type == "diff":
        overpayment = 0
        for m in range(1, args.periods + 1):
            monthly_payment = args.principal / args.periods + interest\
                              * (args.principal - (args.principal * (m - 1)) / args.periods)
            overpayment += math.ceil(monthly_payment)
            print('Month {}: paid out {}'.format(m, math.ceil(monthly_payment)))
        print('Overpayment = {}'.format(overpayment - args.principal))
    else:
        print('Incorrect parameters')
else:
    print('Incorrect parameters')

