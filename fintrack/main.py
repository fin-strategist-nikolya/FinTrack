# main.py

import argparse
from fintrack.portfolio_analyzer import PortfolioAnalyzer
from fintrack.risk_modeling import RiskModeling

def main():
    parser = argparse.ArgumentParser(description="FinTrack: Portfolio Performance Analyzer and Risk Modeler.")
    
    parser.add_argument('--analyze', action='store_true', help="Analyze portfolio performance")
    parser.add_argument('--risk', action='store_true', help="Run risk simulations")
    
    args = parser.parse_args()
    
    if args.analyze:
        # Example: Portfolio Analyzer with sample data
        analyzer = PortfolioAnalyzer()
        analyzer.analyze_portfolio()

    if args.risk:
        # Example: Risk modeling using Monte Carlo simulations
        modeler = RiskModeling()
        modeler.run_simulation()

if __name__ == '__main__':
    main()
