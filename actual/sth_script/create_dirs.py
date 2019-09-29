import os


class CreateDirs:
    def create(self):
        path = 'D:\\bpz\\python\\actual\\launch_logo\\mipmap'
        os.makedirs(path, 0, True)
        print("mkdirs")


if __name__ == '__main__':
    download = CreateDirs()
    download.create()
