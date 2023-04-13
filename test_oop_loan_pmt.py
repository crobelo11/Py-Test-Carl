import pytest
from oop_loan_pmt import Loan, collectLoanDetails, main

# Test data
loan_amount = 100000
years = 30
interest = 0.06
monthly_payment = 599.55

# Unit tests
def test_Loan():
    loan = Loan(loan_amount, years, interest)
    assert loan.loanAmount == loan_amount
    assert loan.annualRate == interest
    assert loan.numberOfPmts == years * 12
    assert loan.periodicIntRate == interest / 12
    assert loan.discountFactor == 0.0
    assert loan.loanPmt == 0

def test_calculateDiscountFactor():
    loan = Loan(loan_amount, years, interest)
    loan.calculateDiscountFactor()
    assert loan.discountFactor == pytest.approx(166.7916, rel=1e-4)

def test_calculateLoanPmt():
    loan = Loan(loan_amount, years, interest)
    loan.calculateLoanPmt()
    assert loan.loanPmt == pytest.approx(monthly_payment, rel=1e-2)

def test_collectLoanDetails(monkeypatch):
    inputs = [loan_amount, years, interest]
    monkeypatch.setattr('builtins.input', lambda _: str(inputs.pop(0)))
    loan = collectLoanDetails()
    assert loan.loanAmount == loan_amount
    assert loan.annualRate == interest
    assert loan.numberOfPmts == years * 12

# Functional tests
def test_main(capfd, monkeypatch):
    inputs = [loan_amount, years, interest]
    monkeypatch.setattr('builtins.input', lambda _: str(inputs.pop(0)))
    main()
    captured = capfd.readouterr()
    assert captured.out.strip() == "Your monthly payment is: $599.55"
