if __name__ == "__main__":
    from Api import Api_sample_1
    from Performance_analyzer import Analyzer_sample_1

    analyzer = Analyzer_sample_1()
    api = Api_sample_1(analyzer)

    analyzer2 = Analyzer_sample_1()
    api2 = Api_sample_1(analyzer2)

    for i in range(4): api.service()
    for j in range(10): api2.service()

    print(analyzer.result2json())
    print(analyzer2.result2json())
    