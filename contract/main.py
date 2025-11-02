# main.py
import argparse
from reader import read_pdf
from summary import summarize_contract
from classifier import risk_score, detect_contract_type

def main(file_path):
    contract_text = read_pdf(file_path)

    contract_type = detect_contract_type(contract_text)
    print(f"Contract Type: {contract_type}")

    score, triggers = risk_score(contract_text)
    print(f"Risk Score: {score}/10 | Triggers: {', '.join(triggers)}")

    summary = summarize_contract(contract_text)
    print("\nSummary:\n", summary)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Path to contract PDF")
    args = parser.parse_args()
    main(args.file)