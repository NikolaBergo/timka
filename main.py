from urllib.request import urlopen
from lxml import etree
from lxml import html

class abitur:
    def __init__(self, id):
        self.id = id
        self.specToSum = {}
        self.specToRating = {}
        self.specToPriority = {}
        self.specToPassed = {}
        self.docsStatus = ''
    def addSpecializationSum(self, spec, sum, priority):
        self.specToSum[spec] = sum
        self.specToPriority[spec] = priority
    def addDocsStatus(self, status):
        self.docsStatus = status
    def addRating(self, spec, place, passed):
        self.specToRating[spec] = place
        self.specToPassed[spec] = passed
    def passedSomewhereElse(self, spec):
        for item in self.specToPriority:
            if item == spec:
                continue
            if self.specToPriority[item] < self.specToPriority[spec]:
                if self.specToPassed[item] == True:
                    return True
        return False

    def print(self):
        print("Unique ID = ", self.id, ", docs status = ", self.docsStatus)
        print("{:36} {:10} {:10} {:10} {:10}".format("Специализация",
                                                    "баллы",
                                                    "приоритет",
                                                    "рейтинг",
                                                    "проход"))
        for item in self.specToSum:
            print("{:30} {:10} {:10} {:10} {:10}".format(item, self.specToSum[item],
                  self.specToPriority[item],
                  self.specToRating[item],
                  self.specToPassed[item]))

class specialization:
    def __init__(self, name, capacity, url):
        self.name = name
        self.capacity = capacity
        self.url = url
        self.abiturList = []
    def addAbitur(self, abitur):
        self.abiturList.append(abitur)
    def formRating(self):
        sorted(self.abiturList, key=lambda abitur : abitur.specToSum[self.name])
        for i in range(0, len(self.abiturList)):
            if i < self.capacity:
                self.abiturList[i].addRating(self.name, i + 1, True)
            else:
                self.abiturList[i].addRating(self.name, i + 1, False)
    def printRealRating(self):
        j = 1
        for item in self.abiturList:
            if item.specToPriority[self.name] == 1:
                print("{:5}/{} {:10} {:40}".format(j, self.capacity, item.specToSum[self.name], item.id))
                j += 1
            elif item.passedSomewhereElse(self.name):
                print("{:8} {:10} {:40}".format("---", item.specToSum[self.name], item.id))
            else:
                print("{:5}/{} {:10} {:40}".format(j, self.capacity, item.specToSum[self.name], item.id))
                j += 1
            
            

specializationList = []
idToAbiturMap = {}

specializationList.append(specialization('Гидрометеорология', 16, 'https://www.timacad.ru/abitur/prikaz/spiski/000000001_05.03.04_OFO_OO_2023_B.html'))
specializationList.append(specialization('Биология', 55, "https://www.timacad.ru/abitur/prikaz/spiski/000000001_06.03.01_OFO_OO_2023_B.html"))
specializationList.append(specialization('Строительство', 51, 'https://www.timacad.ru/abitur/prikaz/spiski/000000001_08.03.01_OFO_OO_2023_B.html'))
specializationList.append(specialization('Информационные системы', 58, 'https://www.timacad.ru/abitur/prikaz/spiski/000000001_09.03.02_OFO_OO_2023_B.html'))
specializationList.append(specialization('Прикладная информатика', 63, 'https://www.timacad.ru/abitur/prikaz/spiski/000000001_09.03.03_OFO_OO_2023_B.html'))
specializationList.append(specialization('Теплоэнергетика', 18, 'https://www.timacad.ru/abitur/prikaz/spiski/000000001_13.03.01_OFO_OO_2023_B.html'))
specializationList.append(specialization('Электроэнергетика', 36, 'https://www.timacad.ru/abitur/prikaz/spiski/000000001_13.03.02_OFO_OO_2023_B.html'))
specializationList.append(specialization('Технологические машины', 16, 'https://www.timacad.ru/abitur/prikaz/spiski/000000001_15.03.02_OFO_OO_2023_B.html'))
specializationList.append(specialization('Биотехнология', 63, 'https://www.timacad.ru/abitur/prikaz/spiski/000000001_19.03.01_OFO_OO_2023_B.html'))
specializationList.append(specialization('Продукты питания растительные', 21, 'https://www.timacad.ru/abitur/prikaz/spiski/000000001_19.03.02_OFO_OO_2023_B.html'))
specializationList.append(specialization('Продукты питания животные', 21, 'https://www.timacad.ru/abitur/prikaz/spiski/000000001_19.03.03_OFO_OO_2023_B.html'))
specializationList.append(specialization('Техносферная безопасность', 35, 'https://www.timacad.ru/abitur/prikaz/spiski/000000001_20.03.01_OFO_OO_2023_B.html'))
specializationList.append(specialization('Природообустройство и вода', 35, 'https://www.timacad.ru/abitur/prikaz/spiski/000000001_20.03.02_OFO_OO_2023_B.html'))
specializationList.append(specialization('Землеустройство и кадастры', 16, 'https://www.timacad.ru/abitur/prikaz/spiski/000000001_21.03.02_OFO_OO_2023_B.html'))
specializationList.append(specialization('Технология транспортных процессов', 16, 'https://www.timacad.ru/abitur/prikaz/spiski/000000001_23.03.01_OFO_OO_2023_B.html'))
specializationList.append(specialization('Эксплуатация ... машин', 42, 'https://www.timacad.ru/abitur/prikaz/spiski/000000001_23.03.03_OFO_OO_2023_B.html'))
specializationList.append(specialization('Лесное дело', 15, 'https://www.timacad.ru/abitur/prikaz/spiski/000000001_35.03.01_OFO_OO_2023_B.html'))
specializationList.append(specialization('Агрохимия и агропочвоведение', 32, 'https://www.timacad.ru/abitur/prikaz/spiski/000000001_35.03.03_OFO_OO_2023_B.html'))
specializationList.append(specialization('Агрономия', 74, 'https://www.timacad.ru/abitur/prikaz/spiski/000000001_35.03.04_OFO_OO_2023_B.html'))
specializationList.append(specialization('Садоводство', 70, 'https://www.timacad.ru/abitur/prikaz/spiski/000000001_35.03.05_OFO_OO_2023_B.html'))
specializationList.append(specialization('Агроинженерия', 82, 'https://www.timacad.ru/abitur/prikaz/spiski/000000001_35.03.06_OFO_OO_2023_B.html'))
specializationList.append(specialization('Технология пр-ва сх продукции', 39, 'https://www.timacad.ru/abitur/prikaz/spiski/000000001_35.03.07_OFO_OO_2023_B.html'))
specializationList.append(specialization('Ландшафтная архитектура', 70, 'https://www.timacad.ru/abitur/prikaz/spiski/000000001_35.03.10_OFO_OO_2023_B.html'))
specializationList.append(specialization('Гидромелиорация', 13, 'https://www.timacad.ru/abitur/prikaz/spiski/000000001_35.03.11_OFO_OO_2023_B.html'))
specializationList.append(specialization('Ветеринарная экспертиза', 30, 'https://www.timacad.ru/abitur/prikaz/spiski/000000001_36.03.01_OFO_OO_2023_B.html'))
specializationList.append(specialization('Зоотехния', 32, 'https://www.timacad.ru/abitur/prikaz/spiski/000000001_36.03.02_OFO_OO_2023_B.html'))
specializationList.append(specialization('Туризм', 16, 'https://www.timacad.ru/abitur/prikaz/spiski/000000001_43.03.02_OFO_OO_2023_B.html'))
specializationList.append(specialization('Профессиональное обучение', 44, 'https://www.timacad.ru/abitur/prikaz/spiski/000000001_44.03.04_OFO_OO_2023_B.html'))

# you can implement your analogue here
def parseAbiturs():
    return 0

# bergo version
for curSpec in specializationList:
    response = urlopen(curSpec.url)
    webContent = response.read().decode('UTF-8')

    tree = html.fromstring(webContent)
    table = tree.xpath('//table/tr/td/text()')
    i = 0
    width = 0

    while i < len(table):
        if table[i] == 'Уникальный код':
            width += 2
            i += 1
            while table[i] != 'Состояние':
                width += 1
                i += 1
            width += 1
            i += 1
            break
        i += 1

    # 10 is quantity of permanent fields
    numOfSubjects = width - 10
    idNum = 1
    while i < len(table):
        if str(idNum) != table[i]:
            break
        i += 1
        new_id = table[i]
        i += 1
        sum = int(table[i])
        if sum < 200 and sum > 10:
            break

        # now i points to 'Оригинал' or 'Копия'
        i += (numOfSubjects + 3)

        # Fucking BVI has 0 to 10 points
        if idNum < 50 and sum >= 0 and sum <= 10:
            sum = 310
            i -= numOfSubjects

        if idToAbiturMap.get(new_id) == None:
            idToAbiturMap[new_id] = abitur(new_id)

        if table[i] == 'Оригинал' or table[i] == 'Копия':
            idToAbiturMap[new_id].addDocsStatus(table[i])
            i += 1
        else:
            idToAbiturMap[new_id].addDocsStatus('Неизвестно')

        priority = int(table[i])
        idToAbiturMap[new_id].addSpecializationSum(curSpec.name, sum, int(priority))
        curSpec.addAbitur(idToAbiturMap[new_id])

        idNum += 1
        i += 1
        while table[i] != str(idNum) and i < len(table): 
            i += 1

# Sort ratings
for curSpec in specializationList:
    curSpec.formRating()

# Print each specializatioon rating
for curSpec in specializationList:
    print('==================================')
    print('           ', curSpec.name)
    print('\n')
    curSpec.printRealRating()

# Print each abitur info
for item in idToAbiturMap:
    idToAbiturMap[item].print()
    print('-----------------------------')