import random

class Game:
    def __init__(self):
        self.rooms = {
            1: {
                "description": '''Вы находитесь в подвальном помещении замка, освещаемом небольшими окнами, перекрытыми стальными решётками.
В конце помещения можно заметить дверь.
Выберите одно из 3-х действий:''',
                "actions": {
                    "осмотреться": self.look_around_room_1,
                    "подойти к двери": self.approach_door,
                    "выбить дверь": self.break_door
                }
            },
            2: {
                "description": '''Небольшое, пустое помещение, освещаемое одним факелом. В центре стоит стол с железным ящиком. В конце помещения видна дверь.
Выберите одно из 5-х действий:''',
                "actions": {
                    "осмотреть стол": self.inspect_table,
                    "осмотреться": self.look_around_room_2,
                    "осмотреть лист": self.inspect_paper,
                    "открыть дверь": self.open_door,
                    "открыть инвентарь": self.show_inventory
                },
                "key_found": False
            },
            3: {
                "description": '''Неестественно тёмное помещение с кругами призыва на полу.''',
                "actions": {
                    "осмотреться": self.look_around_room_3,
                    "начать бой": self.start_battle_3,
                    "открыть инвентарь": self.show_inventory
                }
            }
        }
        self.current_room = 1
        self.inventory = {'меч', 'ключ от кладовой'}
        self.has_key = False
        self.health = 100
        self.zombies = 2
        self.alive = True

    def start(self):
        print("Пре-альфа тест. Добро пожаловать в подвал!")
        while True:
            self.describe_current_room()
            self.show_actions()
            action = input("Выберите одно из действий: ").strip().lower()
            if action in self.rooms[self.current_room]["actions"]:
                self.rooms[self.current_room]["actions"][action]()
            else:
                print("Неверное действие. Попробуйте снова.")

    def show_actions(self):
        print("Доступные действия:")
        for action in self.rooms[self.current_room]["actions"]:
            print(f"- {action}")

    def perform_action(self, action):
        if action == "осмотреться":
            self.look_around()
        elif action == "подойти к двери":
            self.approach_door()
        elif action == "выбить дверь":
            self.break_door()
        elif action == "осмотреть стол":
            self.inspect_table()
        elif action == "осмотреть лист":
            self.inspect_paper()
        elif action == "открыть дверь":
            self.open_door()
        elif action == "открыть инвентарь":
            self.show_inventory()
        elif action == "начать бой":
            self.start_battle_3()
        else:
            print("Неверное действие. Попробуйте снова.")

    def describe_current_room(self):
        print(self.rooms[self.current_room]["description"])

    def look_around_room_1(self):
        print('''Вы находитесь в подвальном помещении замка освещаемом небольшими оконцами перекрытыми стальными решётками.  
Хотя, вам в любом случае не удалось бы пролезть через них. 
Сам подвал ничего интересного из себя не представляет. 
Маленькое, пустое помещение, в котором нет ничего кроме двери и люка в потолке, который вас сюда и привёл.''')

    def approach_door(self):
        print('''Вы подходите к двери. 
Дверь выполнена из старого дерева.
Похоже, время её не пожалело.''')

    def break_door(self):
        print('''Вы  делаете несколько шагов назад и разбегаетесь прямиком в дверь. 
            Она удивительно легко слетает с петель и вы по инерции оказываетесь в новом для вас помещении.''')
        self.current_room = 2

    def open_door(self):
        if self.has_key:
            print('''
Подойдя к двери вы почувствовали странную ауру, словно она затягивает воздух в себя. 
Приготовив к мечь к бою, вы вставляете ключ в замок и прокручиваете его до характерного щелчка. 
Отворив дверь, вы видите лишь тьму. Однако, вы не решаетесь зайти в неё. 
Лучше взять факел - с этими словами вы снимаете факел и, держа его перед собой, входите во тьму.''')
            self.current_room = 3
        else:
            print("Дверь заперта. Видимо, нужен ключ.")

    def inspect_table(self):
        print('''
Простой, грубо выполненный стол, на котором лежит железная коробка со странным узором. 
На ней лежит лист бумаги, на котором что-то написано. 
Сама коробка закрыта на замок, требующий ввести 3 цифры.''')
        if not self.rooms[2]["key_found"]:
            self.solve_puzzle()

    def look_around_room_2(self):
        print("Маленькое пустое помещение, освещаемое одним факелом. В дальнем конце видна дверь.")

    def inspect_paper(self):
        print("На листе написано:\nЗдесь цифры загаданы, попробуй найти,\nОни все идут по порядку в пути.\nПервая — это сколько лап у кота,\nВторая — сколько всего колёс у карет?.\nТретья — число глаз, что смотрят на свет?")

    def solve_puzzle(self):
        answer = input("Введите 3 цифры: ")
        if answer == "442":
            print('''Открыв коробку, вы видите ключ. 
Возможно, он подойдёт к двери?''')
            self.has_key = True
            self.inventory.add("ключ от двери")

    def show_inventory(self):
        print("Ваш инвентарь содержит:")
        for item in self.inventory:
            print(f"- {item}")

    def look_around_room_3(self):
        print('''
Вы осматриваетесь в тёмной комнате, чувствуя нарастающее напряжение...
Странные рисунки на полу, похожие круги призыва или пентаграммы. Сильный холод несмотря на лето. 
Даже в предыдущих двух помещениях не было так холодно. Здесь явно проводили какой-то ритуал, но что же произошло? 
Местные говорили, что замок в один момент опустел, а те немногие смельчаки, что решались в него зайти больше, не возвращались. 
Внезапно, ваши рассуждения прервал дверной проём и 2 силуэта, что неподвижно стояли во тьме напротив.
Вытянув факел вперёд, вы пытаетесь их разглядеть. 
Перед вами, охраняя лестницу, стояло два человека, больше походящих на трупы. 
Были ли они действительно таковыми или их просто кто-то оживил, вас уже не интересует.
Они неторопливо приближалются к вам.
Расправиться с ними не должно составить труда, но надо быть на настороже. Даже 1 укус может быть смертелен.''')

    def start_battle_3(self):
        print("На вас наступают два противника!")
        while self.alive and self.zombies > 0:
            action = input(
'''Выберите действие: 
выжидать 
обезглавить 
поджечь 
бить в голову 
убежать''').strip().lower()

            if action == "выжидать":
                self.wait()
            elif action == "обезглавить":
                self.decapitate()
            elif action == "поджечь":
                self.burn()
            elif action == "бить в голову":
                self.hit_head()
            elif action == "убежать":
                self.run_away()
                break
            else:
                print("Неверное действие. Попробуйте снова.")

        if not self.alive:
            print("Поражение. Попробуйте снова.")
            self.reset_battle()
        elif self.zombies == 0:
            print('''Поднявшись по лестнице, вы прислонились к стене перед дверью с осознанием, что вам повезло. 
                    Вытирая пот со лба, вы подходте к двери и открываете её.....''')
            self.end_battle()

    def wait(self):
        print("Вы подпускаете противника поближе, выжидая шанс для атаки.")

    def decapitate(self):
        print('''
Не дожидаясь, пока ваш противник примет оборонительную стойку, вы наносите точный удар по его шее. 
Старый, уже давно не сиявший клинок встретился с гниющей на глазах плотью мертвеца, 
и его кромка прошла сквозь кожу, мускулы и кости противника с визгливым воем, 
эхом раздавшимся по тёмной комнате, освещаемой лишь вашим факелом''')
        self.zombies -= 1
        self.check_remaining_zombies()

    def burn(self):
        print("Аккуратно поднеся факел к мертвецу, вы поджигаете его одежду!")
        if random.choice([True, False]):
            print("Не ожидая этого, мертвец, окутанный пламенем, делает несколько шагов назад.")
            self.zombies -= 1
            self.check_remaining_zombies()
        else:
            self.health -= 50
            print("Вы получили удар! Ваша здоровье:", self.health)
            self.check_health()

    def hit_head(self):
        print("Вы проводите точный, колющий удар в голову.")
        if random.choice([True, False]):
            self.zombies -= 1
            print("Лезвие нашло свою цель, поразив её насмерть.")
        else:
            self.health -= 50
            print("Вы получили ответный удар! Ваша здоровье:", self.health)
            self.check_health()

    def run_away(self):
        print("Вы решили убежать!")
        if self.zombies > 1:
            print("Вы пытаетесь проскочить между ними к лестнице и подняться наверх.")
            if random.choice([True, False]):
                print("Успешно обойдя обоих противников, пытавшихся вас остановить, вы начали подъём по лестнице.")
            else:
                self.health -= 50
                print("Вы получили удар при попытке убежать. Ваша здоровье:", self.health)
                self.check_health()
        self.alive = False

    def check_remaining_zombies(self):
        if self.zombies > 0:
            print(f"Осталось противников: {self.zombies}")
        else:
            print("Все противники были повержены! Лестница теперь свободна.")

    def check_health(self):
        if self.health <= 0:
            self.alive = False
            print("Вы погибли в бою. Это конец.")

    def end_battle(self):
        print('''Спасибо за игру! Возможно я её доработаю, а может и нет:)
                В Любом случае, хорошего дня и счастья вам.''')
        exit()  

# Запуск игры
game = Game()
game.start()