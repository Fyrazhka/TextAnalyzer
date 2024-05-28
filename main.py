from TextAnalyzer import TextAnalyzer


def main():
    given_string="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."
    analyzed = TextAnalyzer(given_string)
    print("Formatted Text:", analyzed.text)
    freq_map = analyzed.freq_all()
    print(freq_map)
    word = "lorem"
    frequency = analyzed.freq_of(word)
    print("The word", word, "appears", frequency, "times.")


if __name__ == '__main__':
    main()
