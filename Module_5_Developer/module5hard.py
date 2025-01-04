import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'{self.nickname}'


class Video:
    def __init__(self, title: str, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users: list[User] = []
        self.videos: list[Video] = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and user.password == hash(password):
                self.current_user = user

    def register(self, nickname, password, age):
        list_nicknames = []
        for user in self.users:
            list_nicknames.append(user.nickname)
        if nickname not in list_nicknames:
            user = User(nickname, password, age)
            self.users.append(user)
            self.log_in(nickname, password)
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None

    def add(self, *videos: Video):
         list_title = []
         for video in self.videos:
             list_title.append(video.title)
         for video in videos:
             if video.title not in list_title:
                 self.videos.append(video)

    def get_videos(self, search_word):
        list_video = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                list_video.append(video.title)
        return list_video

    def watch_video(self, title_video):
        if self.current_user is None:
            print("Войдите в аккаунт, что бы смотреть видео")
            return
        for video in self.videos:
            if video.title == title_video:
                if video.adult_mode and self.current_user.age >= 18:
                    for second in range(1, video.duration + 1):
                        print(second, end=' ')
                        video.time_now += 1
                        time.sleep(1)
                    video.time_now = 0
                    print('Конец видео')
                else:
                    print("Вам нет 18 лет, пожалуйста покинте страницу")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')