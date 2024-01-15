import tkinter
from PIL import ImageTk, Image


class Card:
    def __init__(self, name, image_path, description):
        self.name = name
        self.image_path = image_path
        self.description = description


class CardGameApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Card Game")

        self.card1 = Card("Card 1", "images/card1.png", "가즈아")
        self.card2 = Card("Card 2", "images/card2.png", "고고싱")

        self.current_card = self.card1

        # 이미지 로드 및 크기 조절
        self.original_image = Image.open(self.current_card.image_path)
        self.resized_image = self.original_image.resize((300, 300), Image.LANCZOS)
        self.card_image = ImageTk.PhotoImage(self.resized_image)

        self.canvas = tkinter.Canvas(self.master, width=300, height=400)
        self.canvas.pack()

        self.canvas.create_image(150, 150, anchor=tkinter.CENTER, image=self.card_image)

        self.label_description = tkinter.Label(self.master, text=self.current_card.description, wraplength=250)
        self.label_description.pack()

        self.button_next_card = tkinter.Button(self.master, text="다음 카드", command=self.next_card)
        self.button_next_card.pack()

    def next_card(self):
        if self.current_card == self.card1:
            self.current_card = self.card2
        else:
            self.current_card = self.card1

        # 이미지 업데이트
        self.original_image = Image.open(self.current_card.image_path)
        self.resized_image = self.original_image.resize((300, 300), Image.LANCZOS)
        self.card_image = ImageTk.PhotoImage(self.resized_image)
        self.canvas.itemconfig(self.canvas.find_all()[0], image=self.card_image)

        self.label_description.config(text=self.current_card.description)


if __name__ == "__main__":
    root = tkinter.Tk()
    app = CardGameApp(root)
    root.mainloop()