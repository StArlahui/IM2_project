def convert_currency(dollar):
    peso = dollar * 57.17
    yen = dollar * 146.67
    return peso, yen 

dollar_input = input("Enter currency in ($): ")
dollars = [float(x) for x in dollar_input.split(",")]
print(f"\n{'Dollar($)':<12}{'Phil Peso(P)':<15}{'Jpn Yen(Y)':<15}")
for d in dollars:
    peso, yen = convert_currency(d)
    print(f"{d:<12.2f}{peso:<15.2f}{yen:<15.2f}")