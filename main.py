from customtkinter import *
from PIL import Image




class AuthWindow(CTk):
    def __init__(self):
        super().__init__()


        self.title("Вхід")
        self.geometry("700x400")
        self.resizable(False, False)


        self.left_frame = CTkFrame(self)
        self.left_frame.pack(side="left", fill="both")


        ctk_img = CTkImage(Image.open("bg.png"), size=(450, 400))
        self.img_label = CTkLabel(
            self.left_frame,
            image=ctk_img,
            text="Welcome",
            font=("Helvetica", 60, "bold"),
        )
        self.img_label.pack()


        main_font = ("Helvetica", 20, "bold")
        self.right_frame = CTkFrame(self, fg_color="white")
        self.right_frame.pack_propagate(False)
        self.right_frame.pack(side="right", fill="both", expand="True")


        CTkLabel(
            self.right_frame, text="LogiTalk", font=main_font, text_color="#6753cc"
        ).pack(pady=60)


        self.name_entry = CTkEntry(
            self.right_frame,
            placeholder_text="ім'я",
            height=45,
            font=main_font,
            corner_radius=25,
            fg_color="#eae6ff",
            border_color="#eae6ff",
            text_color="#6753cc",
            placeholder_text_color="#6753cc",
        )
        self.name_entry.pack(fill="x", padx=10)


        self.settings_button = CTkButton(
            self.right_frame,
            text="Налаштування",
            height=45,
            corner_radius=25,
            fg_color="#eae6ff",
            font=main_font,
            text_color="#6753cc",
            image=CTkImage(Image.open("setting.png"), size=(20, 20)),
            compound='left'
        )
        self.settings_button.pack(fill="x", padx=10, pady=5)


        self.connect_button = CTkButton(
            self.right_frame,
            text="УВІЙТИ",
            height=45,
            corner_radius=25,
            fg_color="#230f94",
            font=main_font,
            text_color="white"
        )
        self.connect_button.pack(fill="x", padx=50, pady=10)




window = AuthWindow()
window.mainloop()


