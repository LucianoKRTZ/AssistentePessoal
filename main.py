from tools import Tools

class Main:
    def __init__(self):
        self.tools = Tools()

    def runListenner(self):
        data = self.tools.listen()
        print(f"Final recognized status: {data['status']}")
        print(f"Final recognized text: {data['text']}")

if __name__ == "__main__":
    main = Main()
    main.runListenner()
